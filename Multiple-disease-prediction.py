# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 15:55:57 2024

@author: Elopy
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Elopyx-Medics", layout='wide',page_icon=":pill:")
# loading the models
diabetes_model = pickle.load(open("diabetes_model.sav",'rb'))
heart_disease_model = pickle.load(open("heart.sav",'rb'))
parkinsons_model = pickle.load(open("parkinson.sav",'rb'))


# the side bar for navigation




with st.sidebar:
    # Custom CSS for styling the sidebar
    st.markdown("""
    <style>
        /* Change background color of selected sidebar section */
        .element-container.sidebar .sidebar-content .stSelectbox div[data-baseweb="menu"] div:last-child {
            background-color: #28a745 !important; /* Change the color to Bootstrap success color */
        }
    </style>
   """, unsafe_allow_html=True)
    selected =option_menu('Elopyx-Medics',
                          [  'Home',
                            'Diabetes prediction',
                           'Heart disease prediction',
                           'Parkinson`s disease pediction'
                           ],
                          icons=['house','droplet-fill','activity','person-walking'],
                          default_index=0
                          )


    
    
# diabetes prediction page
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
    # title 
    st.title('Diabetes prediction')
    st.markdown('<style>div.block-container{padding-top:2rem}</style>',unsafe_allow_html=True)
    #getting user input
    col1,col2,col3 = st.columns(3)
    
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
    
 
    # code for prediction
    diab_diagnosis = ''
    # button
    if st.button("Diabetes prediction result"):
        diab_diagnosis = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if (diab_diagnosis[0] == 0):
          diab_diagnosis = 'The person is not diabetic'
        else:
          diab_diagnosis = 'The person is diabetic'
    st.success(diab_diagnosis)
elif selected == 'Heart disease prediction':
    
    #title
   st.title('Heart disease prediction')
   st.markdown('<style>div.block-container{padding-top:2rem}</style>',unsafe_allow_html=True)

   col1, col2, col3 = st.columns(3)

   with col1:
       age = st.text_input('Age')

   with col2:
       sex = st.text_input('Sex: 0=Male; 1=Female')

   with col3:
       cp = st.text_input('Chest Pain type: 0=Typical angina; 1=Atypical angina; 2=Non-anginal; 3=Asymptomatic')

   with col1:
       trestbps = st.text_input('Resting Blood Pressure')

   with col2:
       chol = st.text_input('Serum Cholestoral in mg/dl')

   with col3:
       fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl(0=Yes; 1=No )')

   with col1:
       restecg = st.text_input('Resting Electrocardiographic results: 0=Normal; 1=STT abnormality; 2=LV hypertrophy')

   with col2:
       thalach = st.text_input('Maximum Heart Rate achieved')

   with col3:
       exang = st.text_input('Exercise Induced Angina: 0=TRUE; 1=FALSE')

   with col1:
       oldpeak = st.text_input('ST depression induced by exercise(old peak)')

   with col2:
       slope = st.text_input('Slope of the peak exercise ST segment')

   with col3:
       ca = st.text_input('Number of major vessels colored by flourosopy:eg; 0,1,2......')

   with col1:
       thal = st.text_input('Thalassemia: 0 = normal; 1 = fixed defect; 2 = reversable defect')

   # code for Prediction
   heart_diagnosis = ''

   # creating a button for Prediction

   if st.button('Heart Disease Test Result'):

       user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

       user_input = [float(x) for x in user_input]

       heart_prediction = heart_disease_model.predict([user_input])

       if heart_prediction[0] == 1:
           heart_diagnosis = 'The person is having heart disease'
       else:
           heart_diagnosis = 'The person does not have any heart disease'

   st.success(heart_diagnosis)

    
elif selected ==  'Parkinson`s disease pediction':
    #title
    st.title('Parkinson`s disease prediction')
    st.markdown('<style>div.block-container{padding-top:2rem}</style>',unsafe_allow_html=True)
   
    with st.expander('Expand this for more clarity on the attributes used in this prediction'):
        st.subheader('Attribute Information',divider='green')
        st.text('MDVP:Fo(Hz) - Average vocal fundamental frequency')
        st.text('MDVP:Fhi(Hz) - Maximum vocal fundamental frequency')
        st.text('MDVP:Flo(Hz) - Minimum vocal fundamental frequency')
        st.text('MDVP:Jitter(%), MDVP:Jitter(Abs), MDVP:RAP, MDVP:PPQ, Jitter:DDP - Several measures of variation in fundamental frequency')
        st.text('MDVP:Shimmer,MDVP:Shimmer(dB),Shimmer:APQ3,Shimmer:APQ5,MDVP:APQ,Shimmer:DDA - Several measures of variation in amplitude')  
        st.text("NHR, HNR - Two measures of the ratio of noise to tonal components in the voice status - The health status of the subject (one) - Parkinson's, (zero) - healthy")
        st.text(" RPDE, D2 - Two nonlinear dynamical complexity measures ")
        st.text(" DFA - Signal fractal scaling exponent ")
        st.text(" spread1,spread2,PPE - Three nonlinear measures of fundamental frequency variation ")
        
    col1, col2, col3, col4, col5 = st.columns(5)
 
    with col1:
        fo = st.text_input('MDVP-Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP-Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP-Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP-Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP-Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP-RAP')

    with col2:
        PPQ = st.text_input('MDVP-PPQ')

    with col3:
        DDP = st.text_input('Jitter-DDP')

    with col4:
        Shimmer = st.text_input('MDVP-Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP-Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer-APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer-APQ5')

    with col3:
        APQ = st.text_input('MDVP-APQ')

    with col4:
        DDA = st.text_input('Shimmer-DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)

else:
    pass

    
    
    
    
