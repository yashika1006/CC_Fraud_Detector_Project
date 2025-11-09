# 💳 Credit Card Fraud Detector

A machine learning web application that detects fraudulent credit card transactions in real-time.  
Built with **React**, **Tailwind CSS**, and a backend model trained to identify fraud patterns.


## 🚀 Features

- 🔍 Predicts whether a transaction is fraudulent or legitimate  
- 📊 Clean, responsive frontend interface  
- ⚙️ Machine learning model integrated for prediction  
- 🌐 Deployed-ready setup with API endpoint and form input  
- 📁 Modular project structure for easy updates


## 🧠 Tech Stack

**Frontend:** React.js, Tailwind CSS  
**Backend (optional if included):** Flask / FastAPI  
**ML Model:** Scikit-learn (Logistic Regression / Random Forest, etc.)  
**Version Control:** Git & GitHub  


## 📂 Folder Structure

CC_Fraud_Detector_Project/
│
├── CC_fraud_detector/ # Frontend (React app)
├── model/ # ML model files 
├── requirements.txt # Python dependencies
├── package.json # Node dependencies (frontend)
└── README.md # Project documentation


## ⚡ How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yashika1006/CC_Fraud_Detector_Project.git
cd CC_Fraud_Detector_Project
2️⃣ Install dependencies
If using a virtual environment (Python backend):
pip install -r requirements.txt

For frontend:
cd CC_fraud_detector
npm install

3️⃣ Run the app
Frontend:
npm run dev
Backend (if included):
python app.py
Then open your browser at http://localhost:5173 or your shown dev URL.

🧾 Model Overview
The ML model is trained on a dataset containing anonymized credit card transactions.
It detects fraud based on transaction amount, frequency, and hidden feature patterns.

Author
Yashika Malik
📧 yashika1006@github.com

🛡️ License
This project is open-source and available under the MIT License.

Hi! This is a small project I built to detect fraudulent credit card transactions. The idea is simple: feed in the transaction details, and the system will tell you whether it looks suspicious or not. I wanted to combine web development with machine learning, so the result is a nice little interactive app.
