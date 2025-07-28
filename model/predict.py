import pickle
import pandas as pd

with open('model/pipeline.pkl', 'rb') as f:
    pipeline = pickle.load(f)
    
MODEL_VERSION = '1.0.0'

def predict_output(user_input: dict):
    
    input_df = pd.DataFrame([user_input])
    
    output = pipeline.predict(input_df)[0]
    
    return output