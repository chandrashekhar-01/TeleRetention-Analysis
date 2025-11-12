from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
import joblib

# Load the trained model, scaler, and label encoder
model = joblib.load('catboost_model.pkl')
scaler = joblib.load('scaler.pkl')
label_encoder = joblib.load('label_encoder.pkl')

# Initialize Flask app
app = Flask(__name__)

# Define home route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse input data
        data = request.json if request.is_json else request.form.to_dict()
        
        # Extract required features
        features = ['MonthlyCharges', 'tenure', 'TotalCharges']
        input_data = np.array([[float(data[feature]) for feature in features]])

        # Scale the input data
        scaled_data = scaler.transform(input_data)

        # Predict churn
        prediction = model.predict(scaled_data)[0]
        probability = model.predict_proba(scaled_data)[0][1]

        # Decode prediction
        prediction_label = label_encoder.inverse_transform([int(prediction)])[0]

        # Return result as JSON
        return jsonify({
            'prediction': prediction_label,  # Yes or No
            'probability': round(probability * 100, 2)  # Probability in percentage
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
