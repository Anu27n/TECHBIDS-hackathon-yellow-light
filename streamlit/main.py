import numpy as np
import pickle

loaded_model =pickle.load(open('C:/Users/jaswa/Downloads/streamlit/trained_model.sav','rb'))
loaded_model2=pickle.load(open('C:/Users/jaswa/Downloads/streamlit/trained_model2.sav','rb'))
input_data = [(39.760016,  0.248224,  40.255363,  0.136816)]

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)



