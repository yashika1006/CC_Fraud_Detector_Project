import { spawn } from "child_process";

export const predictFraud = (req, res) => {
  const inputData = req.body;

  // call Python script
  const python = spawn("python", [
    "../CreditCardFraudDetector/predict_fraud.py",
    JSON.stringify(inputData),
  ]);

  let dataToSend = "";

  python.stdout.on("data", (data) => {
    dataToSend += data.toString();
  });

  python.stderr.on("data", (data) => {
    console.error(`stderr: ${data}`);
  });

  python.on("close", (code) => {
    console.log(`Python script exited with code ${code}`);
    try {
      res.json(JSON.parse(dataToSend));
    } catch {
      res.status(500).json({ error: "Failed to parse model output" });
    }
  });
};
