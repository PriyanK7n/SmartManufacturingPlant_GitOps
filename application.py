from flask import Flask, render_template, request
import joblib
import numpy as np


app = Flask(__name__)

MODEL_PATH = "artefacts/models/model.pkl"
SCALER_PATH = "artefacts/processed/scaler.pkl"

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# Independent Features Below according to which we'll be predicting Efficiency
FEATURES = [
                'Operation_Mode', 'Temperature_C', 'Vibration_Hz',
                'Power_Consumption_kW', 'Network_Latency_ms', 'Packet_Loss_%',
                'Quality_Control_Defect_Rate_%', 'Production_Speed_units_per_hr',
                'Predictive_Maintenance_Score', 'Error_Rate_%','Year', 'Month', 'Day', 'Hour'
            ]


# As we're classifying Efficiency whose numerical mappings can be grabbed from Efficiency_Target and Efficiency_Status in the data:  
LABELS = {
    0 : "High",
    1 : "Low",
    2 : "Medium"
}


@app.route("/" , methods=["GET" , "POST"])
def index():
    prediction = None

    if request.method =="POST":
        try:
            input_data = [float(request.form[feature]) for feature in FEATURES]
            input_array = np.array(input_data).reshape(1,-1)

            scaled_array = scaler.transform(input_array)

            pred = model.predict(scaled_array)[0]
            
            prediction = LABELS.get(pred , "Unknown")

        except Exception as e:
            prediction = f"Error : {e}"

    # Sends prediction and features variables from (application.py) to index.html via Jinja2 template rendering (acts as a bridge)
    
    return render_template("index.html", prediction = prediction, features = FEATURES)

# For Testing Purposes Only
if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 5000)