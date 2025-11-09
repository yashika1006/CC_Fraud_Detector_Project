import sys
import json
import joblib
import pandas as pd
from datetime import datetime

# === Load model ===
data = joblib.load('kaggle_fraud_model.pkl')
model = data['model']
scaler = data['scaler']
label_encoders = data['label_encoders']
feature_columns = data['feature_columns']

# === Read JSON input from Node ===
input_json = sys.argv[1]
input_data = json.loads(input_json)

# Example: ensure required keys exist
transaction = pd.DataFrame([input_data])

# Encode categorical columns
for col, le in label_encoders.items():
    if col in transaction.columns:
        try:
            transaction[col] = le.transform(transaction[col])
        except ValueError:
            transaction[col] = [0]

# Scale numeric data
transaction_scaled = scaler.transform(transaction[feature_columns])

# Predict
prediction = model.predict(transaction_scaled)[0]
probability = model.predict_proba(transaction_scaled)[0][1]

# Return JSON to Node
output = {
    "prediction": "FRAUD" if prediction == 1 else "NOT FRAUD",
    "probability": round(float(probability), 4)
}

print(json.dumps(output))
