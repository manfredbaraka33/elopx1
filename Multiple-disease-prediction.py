# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 15:55:57 2024
@author: Elopy
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load machine learning models
diabetes_model = pickle.load(open("diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open("heart.sav", 'rb'))
parkinsons_model = pickle.load(open("parkinson.sav", 'rb'))

# Define a custom theme with a blue primary color
custom_theme = """
[theme]
primaryColor="#007bff"  # Blue primary color
backgroundColor="#ffffff"
secondaryBackgroundColor="#f0f2f6"
textColor="#262730"
font="sans serif"
"""

# Apply the custom theme
st.markdown(f'<style>{custom_theme}</style>', unsafe_allow_html=True)

# Function to display diabetes prediction page
def display_diabetes_prediction(diabetes_model):
    st.title('Diabetes prediction')
    st.markdown('<style>div.block-container{padding-top:2rem}</style>', unsafe_allow_html=True)
    
    # Getting user input
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of pregnancies')
        SkinThickness = st.text_input('Skin thickness value')
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
    with col2:
        Glucose = st.text_input('Glucose level')
        Insulin = st.text_input('Insulin level')
        Age = st.text_input('Age of a person')
    with col3:
        BloodPressure = st.text_input('Blood pressure value') 
        BMI = st.text_input('Body Mass Index')
        
    # Check if any input field is empty
    if not Pregnancies or not SkinThickness or not DiabetesPedigreeFunction or not Glucose or not Insulin or not Age or not BloodPressure or not BMI:
        st.warning("Please fill out all input fields.")
        return
    
    # Code for prediction
    diab_diagnosis = ''
    
    # Prediction button
    if st.button("Diabetes prediction result"):
        diab_diagnosis = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if diab_diagnosis[0] == 0:
            diab_diagnosis = 'The person is not diabetic'
        else:
            diab_diagnosis = 'The person is diabetic'
    
    st.success(diab_diagnosis)

# Function to display heart disease prediction page
def display_heart_disease_prediction(heart_disease_model):
    st.title('Heart disease prediction')
    st.markdown('<style>div.block-container{padding-top:2rem}</style>', unsafe_allow_html=True)
    
    # Getting user input
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
        trestbps = st.text_input('Resting Blood Pressure')
        restecg = st.text_input('Resting Electrocardiographic results')
        oldpeak = st.text_input('ST depression induced by exercise')
        ca = st.text_input('Number of major vessels colored by flourosopy')
    with col2:
        sex = st.text_input('Sex')
        chol = st.text_input('Serum Cholestoral in mg/dl')
        thalach = st.text_input('Maximum Heart Rate achieved')
        slope = st.text_input('Slope of the peak exercise ST segment')
        thal = st.text_input('Thalassemia')
    with col3:
        cp = st.text_input('Chest Pain type')
        fbs = st.text_input('Fasting Blood Sugar')
        exang = st.text_input('Exercise Induced Angina')
    
    # Check if any input field is empty
    if not age or not sex or not cp or not trestbps or not chol or not fbs or not restecg or not thalach or not exang or not oldpeak or not slope or not ca or not thal:
        st.warning("Please fill out all input fields.")
        return
    
    # Code for prediction
    heart_diagnosis = ''
    
    # Prediction button
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
    
    st.success(heart_diagnosis)

# Function to display Parkinson's disease prediction page
def display_parkinsons_prediction(parkinsons_model):
    st.title('Parkinson`s disease prediction')
    st.markdown('<style>div.block-container{padding-top:2rem}</style>', unsafe_allow_html=True)
    
    # Getting user input
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        fo = st.text_input('MDVP-Fo(Hz)')
        RAP = st.text_input('MDVP-RAP')
        APQ3 = st.text_input('Shimmer-APQ3')
        DDA = st.text_input('Shimmer-DDA')
        NHR = st.text_input('NHR')
        RPDE = st.text_input('RPDE')
        spread1 = st.text_input('spread1')
        D2 = st.text_input('D2')
    with col2:
        fhi = st.text_input('MDVP-Fhi(Hz)')
        PPQ = st.text_input('MDVP-PPQ')
        APQ5 = st.text_input('Shimmer-APQ5')
        Shimmer = st.text_input('MDVP-Shimmer')
        HNR = st.text_input('HNR')
        DFA = st.text_input('DFA')
        spread2 = st.text_input('spread2')
        PPE = st.text_input('PPE')
    with col3:
        flo = st.text_input('MDVP-Flo(Hz)')
        DDP = st.text_input('Jitter-DDP')
        APQ = st.text_input('MDVP-APQ')
        MDVP_Shimmer_dB = st.text_input('MDVP-Shimmer(dB)')
        RPDE = st.text_input('RPDE')
    with col4:
        Jitter_percent = st.text_input('MDVP-Jitter(%)')
        Shimmer_dB = st.text_input('MDVP-Shimmer(dB)')
        DDA = st.text_input('Shimmer-DDA')
        spread1 = st.text_input('spread1')
        D2 = st.text_input('D2')
    with col5:
        Jitter_Abs = st.text_input('MDVP-Jitter(Abs)')
        APQ3 = st.text_input('Shimmer-APQ3')
        DDA = st.text_input('Shimmer-DDA')
        NHR = st.text_input('NHR')
        spread2 = st.text_input('spread2')
        PPE = st.text_input('PPE')
        Thal = st.text_input('Thalassemia')
    
    # Check if any input field is empty
    if not fo or not fhi or not flo or not Jitter_percent or not Jitter_Abs or not RAP or not PPQ or not DDP or not Shimmer or not MDVP_Shimmer_dB or not APQ3 or not APQ5 or not APQ or not DDA or not NHR or not HNR or not RPDE or not DFA or not spread1 or not spread2 or not D2 or not PPE or not Thal:
        st.warning("Please fill out all input fields.")
        return
    
    # Code for Prediction
    parkinsons_diagnosis = ''
    
    # Prediction button
    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, MDVP_Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE, Thal]
        user_input = [float(x) for x in user_input]
        parkinsons_prediction = parkinsons_model.predict([user_input])
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
    
    st.success(parkinsons_diagnosis)

# Main code
st.set_page_config(page_title="Elopyx-Medics", layout='wide', page_icon=":pill:")

# Sidebar navigation
with st.sidebar:
    selected = option_menu('Elopyx-Medics',
                           ['Home', 'Diabetes prediction', 'Heart disease prediction', 'Parkinson`s disease pediction'],
                           icons=['house', 'droplet-fill', 'activity', 'person-walking'],
                           default_index=0)

# Pages
if selected == 'Home':
    st.title("Welcome to Elopyx-Medics!")
    st.write("Elopyx-Medics is an application for predicting health conditions using machine learning.")
    st.write("Please select an option from the sidebar to make predictions.")
    
    st.header("Instructions:")
    st.write("1. Select one of the options from the sidebar navigation.")
    st.write("2. Fill in the required information on the prediction page.")
    st.write("3. Click the button to get the prediction result.")
    st.write("4. View the prediction result on the same page.")
    
    st.header("About the Models:")
    st.write("The models used in this application are trained machine learning models that predict health conditions based on input features.")
    st.write("These models have been trained on labeled datasets and are capable of making predictions with a certain level of accuracy.")
    
    st.header("Disclaimer:")
    st.write("The predictions provided by this application are for informational purposes only.")
    st.write("They should not be considered as medical advice, and users are advised to consult with a healthcare professional for any medical concerns.")

elif selected == 'Diabetes prediction':
    display_diabetes_prediction(diabetes_model)

elif selected == 'Heart disease prediction':
    display_heart_disease_prediction(heart_disease_model)

elif selected == 'Parkinson`s disease pediction':
    display_parkinsons_prediction(parkinsons_model)
