import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# 🧩 Example synthetic dataset
# Replace this with your actual dataset later
data = pd.DataFrame({
    'amt': [10, 200, 500, 1500, 75, 1000, 120, 50],
    'category': [0, 1, 1, 0, 0, 1, 1, 0],
    'is_fraud': [0, 1, 1, 0, 0, 1, 1, 0]
})

X = data[['amt', 'category']]
y = data['is_fraud']

# 🧠 Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 🌲 Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 💾 Save the trained model
joblib.dump(model, 'ml/kaggle_fraud_model.pkl')

print("✅ Model trained and saved as kaggle_fraud_model.pkl")
