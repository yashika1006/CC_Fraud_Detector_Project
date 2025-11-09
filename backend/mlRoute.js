import express from "express";
import { spawn } from "child_process";

const router = express.Router();

router.post("/predict", (req, res) => {
  const inputData = req.body;

  // spawn Python process
  const python = spawn("python3", ["ml/predict_api.py", JSON.stringify(inputData)]);


  let result = "";
  python.stdout.on("data", (data) => {
    result += data.toString();
  });

  python.stderr.on("data", (data) => {
    console.error(`Error: ${data}`);
  });

  python.on("close", (code) => {
    try {
      const output = JSON.parse(result);
      res.json(output);
    } catch {
      res.status(500).json({ error: "Invalid response from Python script" });
    }
  });
});

export default router;
