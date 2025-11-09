import joblib
import pandas as pd

# === Load trained model ===
model = joblib.load('ml/kaggle_fraud_model.pkl')
print("✅ Model loaded successfully!")

# === Create test transaction (only the features model expects) ===
new_transaction = pd.DataFrame([{
    'amt': 154.75,
    'category': 'shopping_pos'
}])

# === Encode category if necessary ===
# If your model was trained with label encoding for 'category',
# manually map unseen categories to 0 or handle using try/except
try:
    # If category is string but model expects numeric
    new_transaction['category'] = pd.factorize(new_transaction['category'])[0]
except Exception as e:
    print("⚠️ Encoding warning:", e)

# === Predict ===
try:
    prediction = model.predict(new_transaction)[0]
    proba = model.predict_proba(new_transaction)[0][1] if hasattr(model, "predict_proba") else None

    print(f"\n🚨 Prediction: {'FRAUD' if prediction == 1 else 'NOT FRAUD'}")
    if proba is not None:
        print(f"🧠 Fraud Probability: {proba:.4f}\n")
except Exception as e:
    print("⚠️ Prediction failed:", e)
