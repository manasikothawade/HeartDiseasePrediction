import numpy as np
import streamlit as st
import pandas as pd
import pickle

# Dummy credentials
dummy_username = "user"
dummy_password = "pass"

# Load the trained model
model_filename = r"C:\Users\ritvi\Downloads\model.pkl"

with open(model_filename, 'rb') as file:
    loaded_model = pickle.load(file)

def heart_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data).astype(float)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    return prediction[0]

def display_diagnosis(prediction):
    if prediction == 0:
        return 'The person does not have Heart Disease'
    else:
        return 'The person has Heart Disease'

def signup():
    st.subheader("Sign Up")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Sign Up"):
        # Dummy validation for signup
        if username == dummy_username and password == dummy_password:
            st.success("You have successfully signed up!")
            st.info("Please go to the login page to login.")
        else:
            st.error("Invalid credentials. Please try again.")

def login():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        # Dummy validation for login
        if username == dummy_username and password == dummy_password:
            st.session_state.logged_in = True  # Set login status to True
            st.success("Login successful!")
            st.info("You are now logged in.")
        else:
            st.error("Invalid username or password. Please try again.")

def heart():
    st.title('Heart Disease Prediction')
    age = st.slider('Age', 18, 100, 50)
    sex_options = ['Male', 'Female']
    sex = st.selectbox('Sex', sex_options)
    sex_num = 1 if sex == 'Male' else 0 
    cp_options = ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic']
    cp = st.selectbox('Chest Pain Type', cp_options)
    cp_num = cp_options.index(cp)
    trestbps = st.slider('Resting Blood Pressure', 90, 200, 120)
    chol = st.slider('Cholesterol', 100, 600, 250)
    fbs_options = ['False', 'True']
    fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', fbs_options)
    fbs_num = fbs_options.index(fbs)
    restecg_options = ['Normal', 'ST-T Abnormality', 'Left Ventricular Hypertrophy']
    restecg = st.selectbox('Resting Electrocardiographic Results', restecg_options)
    restecg_num = restecg_options.index(restecg)
    thalach = st.slider('Maximum Heart Rate Achieved', 70, 220, 150)
    exang_options = ['No', 'Yes']
    exang = st.selectbox('Exercise Induced Angina', exang_options)
    exang_num = exang_options.index(exang)
    oldpeak = st.slider('ST Depression Induced by Exercise Relative to Rest', 0.0, 6.2, 1.0)
    slope_options = ['Upsloping', 'Flat', 'Downsloping']
    slope = st.selectbox('Slope of the Peak Exercise ST Segment', slope_options)
    slope_num = slope_options.index(slope)
    ca = st.slider('Number of Major Vessels Colored by Fluoroscopy', 0, 4, 1)
    thal_options = ['Normal', 'Fixed Defect', 'Reversible Defect']
    thal = st.selectbox('Thalassemia', thal_options)
    thal_num = thal_options.index(thal)

    if st.button('Predict'):
        user_input = pd.DataFrame(data={
            'age': [age],
            'sex': [sex_num],  
            'cp': [cp_num],
            'trestbps': [trestbps],
            'chol': [chol],
            'fbs': [fbs_num],
            'restecg': [restecg_num],
            'thalach': [thalach],
            'exang': [exang_num],
            'oldpeak': [oldpeak],
            'slope': [slope_num],
            'ca': [ca],
            'thal': [thal_num]
        })
        prediction = loaded_model.predict(user_input)
        prediction_proba = loaded_model.predict_proba(user_input)

        if prediction[0] == 1:
            bg_color = '#FF474D'
            prediction_result = 'Positive'
        else:
            bg_color = 'green'
            prediction_result = 'Negative'
        
        confidence = prediction_proba[0][1] if prediction[0] == 1 else prediction_proba[0][0]

        st.markdown(f"<div style='text-align: center;'><p style='background-color:{bg_color}; color:white; padding:10px;'>Prediction: {prediction_result}<br>Confidence: {((confidence*10000)//1)/100}%</p></div>", unsafe_allow_html=True)

def main():
    st.title("EASY DIAGNOSE")
  
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False  # Initialize login status in session state

    nav_choice = st.sidebar.selectbox("Navigation", ["Home", "Heart Disease Predictor"])

    if nav_choice == "Home":
        st.header("Welcome to Easy Diagnose!")
        st.write("We predict heart disease and this project is made for SEM VI MINI PROJECT")
        signup()  # Show signup form on the home page
    elif nav_choice == "Heart Disease Predictor":
        login()  # Check login status
        heart()  # Call heart function here

if __name__ == "__main__":
    main()
