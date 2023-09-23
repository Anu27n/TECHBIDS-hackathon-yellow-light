import numpy as np
import pickle
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Load the models
model_file_path = 'trained_model.sav'
model_file_path2 = 'trained_model2.sav'
loaded_model = pickle.load(open(model_file_path, 'rb'))
loaded_model2 = pickle.load(open(model_file_path2, 'rb'))


# Define a function to predict using the loaded models
def predict_model(input_data, model):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = model.predict(input_data_reshaped)
    return prediction
@app.get("/")
async def hello_world():
    return {"message" :"hello"}


@app.post("/predict/")
async def predict(p1: float, q1: float, p2: float, q2: float):
    input_data_model1 = [p1, q1, p2, q2]
    input_data_model2 = [p1, q1, p2, q2]
    result_model1 = predict_model(input_data_model1, loaded_model)
    result_model2 = predict_model(input_data_model2, loaded_model2)

    return {
        "result_model1": result_model1[0],
        "result_model2": result_model2[0]
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)


