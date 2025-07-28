from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import predict_output, MODEL_VERSION, pipeline
from schema.prediction_response import PredictionResponse

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Welcome to the Medical Insurance Prediction API'}


@app.get('/health')
def health_check():
    return {
        'status': 'OK',
        'version': MODEL_VERSION,
        'model_loaded': pipeline is not None
    }


@app.post('/predict', response_model=PredictionResponse)
def predict_charges(data: UserInput):

    user_input = {
        'age': data.age,
        'sex': data.sex,
        'bmi': data.bmi,
        'children': data.children,
        'smoker': data.smoker,
        'region': data.region,
        'bmi_category': data.bmi_category
    }

    try :
        
      prediction = predict_output(user_input)
      return JSONResponse(status_code=200, content={'predicted_medical_charge': prediction})
  
    except Exception as e:
        
        return JSONResponse(status_code=500, content={'error': str(e)})







