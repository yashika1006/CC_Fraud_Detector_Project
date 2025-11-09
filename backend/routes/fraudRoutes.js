import express from "express";
import { predictFraud } from "../controllers/fraudController.js";

const router = express.Router();

// POST /api/predict
router.post("/predict", predictFraud);

export default router;
