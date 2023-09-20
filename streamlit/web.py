import numpy as np
import pickle
import streamlit as st
import os
import pickle

# Get the current directory of your Python script
current_directory = os.path.dirname(os.path.realpath(__file__))

# Construct the absolute file path using forward slashes
model_file_path = os.path.join(current_directory, 'trained_model.sav')
model_file_path2 = os.path.join(current_directory, 'trained_model2.sav')
# Load the model
loaded_model = pickle.load(open(model_file_path, 'rb'))
loaded_model2 = pickle.load(open(model_file_path2, 'rb'))

# Load your first trained model
#loaded_model = pickle.load(open('C:/Users/jaswa/OneDrive/Documents/tam hack complete/streamlit/trained_model.sav', 'rb'))

# Load your second trained model
#loaded_model2 = pickle.load(open('C:/Users/jaswa/OneDrive/Documents/tam hack complete/streamlit/trained_model2.sav', 'rb'))

def predict_model(input_data, model):
    # Convert input_data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    # Make predictions using the specified model
    prediction = model.predict(input_data_reshaped)
    return prediction

def main():
    st.title('pipeline infrastructure monitoring project')

    # Input values
    p1 = st.text_input('Enter pressure at starting of the pipe')
    q1 = st.text_input('Enter flow at starting point of the pipe')
    p2 = st.text_input('Enter pressure at ending of the pipe')
    q2 = st.text_input('Enter flow at ending of the pipe')

    result_model1 = 0.0
    result_model2 = 0.0

    if st.button('Predict if there is a leak in the pipeline'):
        input_data_model1 = [float(p1), float(q1), float(p2), float(q2)]
        result_model1 = predict_model(input_data_model1, loaded_model)
        input_data_model2 = [float(p1), float(q1), float(p2), float(q2)]
        result_model2 = predict_model(input_data_model2, loaded_model2)
        st.success(f'There is a possible leak at {result_model2[0]:.4f} meters from the starting of the pipe which is of diameter {result_model1[0]:.4f} meters')



if __name__ == '__main__':
    main()
