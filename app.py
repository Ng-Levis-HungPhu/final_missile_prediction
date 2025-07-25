from flask import Flask, request, jsonify
from flask_cors import CORS

from tensorflow import keras
import tensorflow as tf

import numpy as np
import os

import pickle

from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)
CORS(app)

MODEL_DIR = "1. SAVING MODELS"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        mode = data.get("mode", "").strip()

        mach = float(data["mach"])
        aoa = float(data["aoa"])
        ln = float(data["ln"])
        swept = float(data["swept"])
        lln = float(data["lln"])

        if mode == "NASA":
            warning_msg = ""

            if not (-4 <= aoa <= 25):
                return jsonify({"error": "Góc tấn (Angle of Attack) phải nằm trong khoảng từ -4 đến 25)"}),400
            elif -4 <= aoa < -2.5:
                warning_msg = "Kết quả dự đoán CL và CD có thể có sai số lên tới lần lượt là: 32.22% và 19.18%"

            if mach < 1.2 :
                return jsonify({"error": "Giá trị Mach phải lớn hơn hoặc bằng 1.2"}), 400
            elif 1.2 <= mach <= 1.6:
                warning_msg = "Kết quả dự đoán CL và CD có thể có sai số lên tới lần lượt là: 18.74% và 15.28%"            
            elif mach >= 3.2:
                warning_msg = "Kết quả dự đoán CL và CD có thể có sai số lên tới 40%"


            if not (3 <= ln <= 20.32):
                return jsonify({"error": "Chiều dài mũi (Ln) phải nằm trong khoảng từ 3 đến 20.32"}), 400
            elif 3 <= ln < 6:
                warning_msg ="Kết quả dự đoán CD có thể có sai số lên tới 19.60%"

            if not (5 <= swept <= 70):
                return jsonify({"error": "Góc swept (Swept Angle) phải nằm trong khoảng từ 5 đến 70)"}),400

            model_cl_path = os.path.join(MODEL_DIR, "NASA_cl.h5")
            model_cd_path = os.path.join(MODEL_DIR, "NASA_cd.h5")
            scaler_path = os.path.join(MODEL_DIR, "NASA.pkl")
            
            model_cl = tf.keras.models.load_model(model_cl_path)
            model_cd = tf.keras.models.load_model(model_cd_path)

            with open(scaler_path,'rb') as f:
                scaler = pickle.load(f)

            input_data = np.array([[lln,ln,swept,mach,aoa]])
            input_data_scaled = scaler.transform(input_data)
        
        elif mode == "Von-Karman Nose":
            if not (-2 <= aoa <= 20):
                return jsonify({"error": "Góc tấn (Angle of Attack) phải nằm trong khoảng từ -2 đến 20)"}),400
            else:
                warning_msg = ""

            if not (1.7 <= mach <= 2.86):
                return jsonify({"error": "Giá trị Mach phải nằm trong khoảng từ 1.7 đến 2.86"}), 400
            else:
                warning_msg = ""

            model_cl_path = os.path.join(MODEL_DIR, "Von-Karman Nose_cl.h5")
            model_cd_path = os.path.join(MODEL_DIR, "Von-Karman Nose_cd.h5")
            scaler_path = os.path.join(MODEL_DIR, "Von-Karman Nose.pkl")

            model_cl = tf.keras.models.load_model(model_cl_path)
            model_cd = tf.keras.models.load_model(model_cd_path)

            with open(scaler_path,'rb') as f:
                scaler = pickle.load(f)

            input_data = np.array([[mach,aoa]])
            input_data_scaled = scaler.transform(input_data)
        
        elif mode == "Missile Shape 1":
            if not (-2 <= aoa <= 20):
                return jsonify({"error": "Góc tấn (Angle of Attack) phải nằm trong khoảng từ -2 đến 20)"}),400
            else:
                warning_msg = ""

            if not (1.7 <= mach <= 3.2):
                return jsonify({"error": "Giá trị Mach phải nằm trong khoảng từ 1.7 đến 3.2"}), 400
            else:
                warning_msg = ""

            model_cl_path = os.path.join(MODEL_DIR, "Missile Shape 1_cl.h5")
            model_cd_path = os.path.join(MODEL_DIR, "Missile Shape 1_cd.h5")
            scaler_path = os.path.join(MODEL_DIR, "Missile Shape 1.pkl")

            model_cl = tf.keras.models.load_model(model_cl_path)
            model_cd = tf.keras.models.load_model(model_cd_path)

            with open(scaler_path,'rb') as f:
                scaler = pickle.load(f)

            input_data = np.array([[mach,aoa]])
            input_data_scaled = scaler.transform(input_data)

        elif mode == "Missile Shape 2":
            if not (-2 <= aoa <= 20):
                return jsonify({"error": "Góc tấn (Angle of Attack) phải nằm trong khoảng từ -2 đến 20)"}),400
            else:
                warning_msg = ""

            if not (0.5 <= mach <= 0.8):
                return jsonify({"error": "Giá trị Mach phải nằm trong khoảng từ 0.5 đến 0.8"}), 400
            else:
                warning_msg = ""

            model_cl_path = os.path.join(MODEL_DIR, "Missile Shape 2_cl.h5")
            model_cd_path = os.path.join(MODEL_DIR, "Missile Shape 2_cd.h5")
            scaler_path = os.path.join(MODEL_DIR, "Missile Shape 2.pkl")

            model_cl = tf.keras.models.load_model(model_cl_path)
            model_cd = tf.keras.models.load_model(model_cd_path)

            with open(scaler_path,'rb') as f:
                scaler = pickle.load(f)
            input_data = np.array([[mach,aoa]])
            input_data_scaled = scaler.transform(input_data)

        elif mode == "Missile Shape 3":
            if not (-2 <= aoa <= 20):
                return jsonify({"error": "Góc tấn (Angle of Attack) phải nằm trong khoảng từ -2 đến 20)"}),400
            else:
                warning_msg = ""

            if not (0.5 <= mach <= 0.8):
                return jsonify({"error": "Giá trị Mach phải nằm trong khoảng từ 0.5 đến 0.8"}), 400
            else:
                warning_msg = ""
    
            model_cl_path = os.path.join(MODEL_DIR, "Missile Shape 3_cl.h5")
            model_cd_path = os.path.join(MODEL_DIR, "Missile Shape 3_cd.h5")
            scaler_path = os.path.join(MODEL_DIR, "Missile Shape 3.pkl")
            
            model_cl = tf.keras.models.load_model(model_cl_path)
            model_cd = tf.keras.models.load_model(model_cd_path)

            with open(scaler_path,'rb') as f:
                scaler = pickle.load(f)

            input_data = np.array([[mach,aoa]])
            input_data_scaled = scaler.transform(input_data)
        else: 
            return jsonify({"error": f"Unsupported mode: {mode}"}), 400


        cl_pred = float(model_cl.predict(input_data_scaled)[0][0])
        cd_pred = float(model_cd.predict(input_data_scaled)[0][0])

        return jsonify({
            "cl": round(cl_pred, 5),
            "cd": round(cd_pred, 5),
            "warning": warning_msg
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# 1. SỬ DỤNG KHI BUILD LIVE SERVER
# if __name__ == "__main__":
#     app.run(debug=True)
    
# 2. SỬ DỤNG KHI BUILD BACKEND
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
