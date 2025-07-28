from pydantic import BaseModel, Field

class PredictionResponse(BaseModel):
    predicted_medical_charge: float = Field(...,description="Predicted medical charge based on user input")

    