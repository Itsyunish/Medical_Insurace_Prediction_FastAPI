# 🩺 Medical Insurance Charge Prediction API

This is a **FastAPI-based RESTful API** that predicts medical insurance charges based on user demographic and health data using a trained machine learning model.

---

## 🚀 Features

- Predict insurance charges via `/predict` endpoint
- Health check endpoint `/health` to monitor API status
- Input data validation with Pydantic
- BMI category auto-calculated from BMI value
- Clean and production-ready structure

---

## 🧠 Model Details

- Model type: Pickle-based trained pipeline (`pipeline.pkl`)
- Input features:
  - Age
  - Sex
  - BMI
  - Children
  - Smoker status
  - Region
  - Derived feature: BMI category

---


