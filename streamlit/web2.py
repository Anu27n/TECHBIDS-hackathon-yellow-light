import numpy as np
import pickle
import streamlit as st

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


def yellow_light_section():
    st.title('MACHINE LEARNING MODEL ')
    # Input values
    p1 = st.text_input('Enter pressure at the start of the pipe', key='p1')
    q1 = st.text_input('Enter flow at the starting point of the pipe', key='q1')
    p2 = st.text_input('Enter pressure at the end of the pipe', key='p2')
    q2 = st.text_input('Enter flow at the end of the pipe', key='q2')

    # Modify CSS to remove colors for text inputs
    st.markdown(
        """
        <style>
        div.stTextInput {
            background-color: transparent !important;
            border: 1px solid transparent !important;
            border-radius: 0 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    result_model1 = 0.0
    result_model2 = 0.0

    if st.button('Predict if there is a leak in the pipeline'):
        input_data_model1 = [float(p1), float(q1), float(p2), float(q2)]
        result_model1 = predict_model(input_data_model1, loaded_model)
        input_data_model2 = [float(p1), float(q1), float(p2), float(q2)]
        result_model2 = predict_model(input_data_model2, loaded_model2)
        st.success(
            f'There is a possible leak at {result_model2[0]:.4f} meters from the start of the pipe which has a diameter of {result_model1[0]:.4f} meters')


def main():
    st.sidebar.title("PIPELINE LEAKAGE MONITORING SYSTEM")

    # Add custom CSS for navigation bar style
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            font-size: 135% !important;
            font-family: 'Quattrocento', sans-serif !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Add the Google Fonts link for Quattrocento
    st.markdown(
        """
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Quattrocento&display=swap">
        """,
        unsafe_allow_html=True,
    )

    navigation_choice = st.sidebar.radio("Go to", ["Description", "Working Prototype"])

    if navigation_choice == "Description":
        st.title("DESCRIPTION OF THE PROJECT")

        # Add an image with description
        st.image("WhatsApp Image 2023-09-23 at 00.07.05.jpg", caption="Pipeline Monitoring", use_column_width=True)

        # Add a project description
        st.write("Welcome to the Pipeline Infrastructure Monitoring Project. "
                 "This project uses machine learning models to predict possible leaks in pipelines based on pressure and flow data. "
                 "You can use the 'Yellow Light' tab to input data and get predictions.")

        st.image("WhatsApp Image 2023-09-23 at 13.35.53.jpg", caption="sdg", use_column_width=True)
        st.write(
            "Our project is deeply aligned with the United Nations Sustainable Development Goals, particularly focusing on Goals 6, 9, and 11."
            " These goals underscore ourcommitment to creating a positive impact on the world and advancing the well-being of humanity. "
            "Goal 6, 'Clean Water and Sanitation,' is at the core of our project's mission. By effectively managing and preventing pipeline leakages"

            "Goal 9, 'Industry, Innovation, and Infrastructure,' underscores the importance of technological advancements and infrastructure development."
            "Our innovative pipeline leakage system represents a pioneering step in infrastructure management."
            "Goal 11, 'Sustainable Cities and Communities,' highlights the significance of creating inclusive, resilient, and sustainable urban environments."
            "Our project plays a pivotal role in this by minimizing water wastage and environmental damage caused by pipeline leakages")

        st.image("WhatsApp Image 2023-09-23 at 14.15.21.jpg", caption="pipe diagram", use_column_width=True)
        st.write("The illustrated diagram above provides a comprehensive and detailed depiction"
                 " of the functioning of each individual pipeline within the entire system. It offers an insightful overview of how each pipeline operates,"
                 "showcasing its unique features and operations in a concise yet comprehensive manner. This visual representation serves as an informative guide"
                 "to better understand the inner workings of the entire pipeline system, making it an invaluable resource for anyone seeking a comprehensive"
                 "understanding of the system's functionality.")
        st.image("WhatsApp Image 2023-09-23 at 14.16.01.jpg", caption="sensor diagram", use_column_width=True)
        st.write(
            "The diagram depicted above serves as a visual representation of the sensor employed within our cutting-edge pipeline leakage detection system."
            " This sensor lies at the heart of our technology, playing a pivotal role in the accurate and reliable identification of leaks in the pipeline network"
            " Its design and functionality are critical components of our system's success, making it an essential element in safeguarding the integrity and efficiency"
            " of our pipeline infrastructure")
        st.write(
            "The pressure sensors, P₁ and P₂, had a full-scale rror of 1.5% and could measure pressures between 0 and 5 bar. The flow sensor measuring the leak QL could"
            " measure flow between 1 and 251/min with an error raging up to 3%. The flow sensor measuring the flow Q₁ at the inlet could measure flow ranging between 1 and 120 l/min"
            " with and error ranging up to 2%. Measurements were taken at 10000 Hz.")

        # Copyright, About, and Contact buttons
        st.sidebar.markdown(
            """
            [Copyright](#) | [About](#) | [Contact](#)
            """
        )
        # Reference to University of Pretoria
        st.sidebar.write("Reference: University of Pretoria")
        st.sidebar.write("Team: Yellow Light")

    elif navigation_choice == "Working Prototype":
        yellow_light_section()


if __name__ == '__main__':
    main()