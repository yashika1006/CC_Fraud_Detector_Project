import express from "express";
import cors from "cors";
import { spawn } from "child_process";

const app = express();
const PORT = 5001;

app.use(cors());
app.use(express.json());

// ✅ Root route
app.get("/", (req, res) => {
  res.status(200).send("✅ Backend server connected to ML model!");
});

// ✅ Predict route — calls Python script
app.post("/api/predict", (req, res) => {
  const inputData = req.body;

  const python = spawn("/usr/local/bin/python3", ["ml/predict_fraud.py"], {
    cwd: process.cwd(),
  });

  let result = "";
  python.stdout.on("data", (data) => {
    result += data.toString();
  });

  let error = "";
  python.stderr.on("data", (data) => {
    error += data.toString();
  });

  python.on("close", (code) => {
    if (error) {
      console.error("❌ Python error:", error);
      return res.status(500).json({ error: "Python execution failed" });
    }
    console.log("✅ Python output:", result);
    res.json({ result });
  });
});

// Start server
app.listen(PORT, "0.0.0.0", () => {
  console.log(`🚀 Server running at http://localhost:${PORT}`);
});
