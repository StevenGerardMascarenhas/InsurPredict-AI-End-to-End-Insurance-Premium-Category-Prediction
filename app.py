from fastapi import FastAPI
from fastapi.responses import JSONResponse

from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse
from model.predict import predict_output,model, MODEL_VERSION



app = FastAPI() #create FastAPI instance








#adding routes hime and health check
@app.get('/')
def home():
    return {"message": "Welcome to the Health Insurance Premium Prediction API"}


#machine readable
@app.get('/health')
def health_check():
    return {
        "status": 'OK',
        'version': MODEL_VERSION,
        'model_loaded': model is True
        }

@app.post('/predict',response_model=PredictionResponse)
def predict_premium(data: UserInput):
    # Ensure pd.DataFrame is called correctly as a function
    user_input = { 
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:
        # Now model.predict will receive a valid DataFrame object
        prediction = predict_output(user_input)

        # Convert prediction to a standard Python type (e.g., int or float) 
        # so JSONResponse can serialize it easily
        return JSONResponse(status_code=200, content={'response': prediction})
  
    except Exception as e:
        return JSONResponse(status_code=500, content= str(e))