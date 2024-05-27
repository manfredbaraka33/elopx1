import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Function to load machine learning models
def load_models():
    diabetes_model = pickle.load(open("diabetes_model.sav", 'rb'))
    heart_disease_model = pickle.load(open("heart.sav", 'rb'))
    parkinsons_model = pickle.load(open("parkinson.sav", 'rb'))
    return diabetes_model, heart_disease_model, parkinsons_model

# Function to define custom Streamlit theme
def set_custom_theme():
    custom_theme = """
    [theme]
    primaryColor="#007bff"  # Blue primary color
    backgroundColor="#ffffff"
    secondaryBackgroundColor="#f0f2f6"
    textColor="#262730"
    font="sans serif"
    """
    st.markdown(f'<style>{custom_theme}</style>', unsafe_allow_html=True)

# Function to display home page content
def display_home_page():
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
    if not all([Pregnancies, SkinThickness, DiabetesPedigreeFunction, Glucose, Insulin, Age, BloodPressure, BMI]):
        st.warning("Please fill out all input fields.")
    else:
        try:
            # Code for prediction
            diab_diagnosis = ''
            # Button
            if st.button("Diabetes prediction result"):
                input_data = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
                diab_diagnosis = diabetes_model.predict(input_data)
                diab_diagnosis = 'The person is diabetic' if diab_diagnosis[0] == 1 else 'The person is not diabetic'
            st.success(diab_diagnosis)
        except Exception as e:
            st.error("An error occurred during prediction. Please check your input and try again.")

# Function to display heart disease prediction page
def display_heart_disease_prediction(heart_disease_model):
    st.title('Heart disease prediction')
    st.markdown('<style>div.block-container{padding-top:2rem}</style>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')

    # Rest of the input fields and prediction logic goes here...

# Function to display Parkinson's disease prediction page
def display_parkinsons_disease_prediction(parkinsons_model):
    st.title('Parkinson`s disease prediction')
    st.markdown('<style>div.block-container{padding-top:2rem}</style>', unsafe_allow_html=True)
   
    # Input fields and prediction logic goes here...

# Main function
def main():
    st.set_page_config(page_title="Elopyx-Medics", layout='wide', page_icon=":pill:")
    set_custom_theme()

    # Load models
    diabetes_model, heart_disease_model, parkinsons_model = load_models()

    # Sidebar navigation
    with st.sidebar:
        selected = option_menu('Elopyx-Medics',
                              ['Home', 'Diabetes prediction', 'Heart disease prediction', 'Parkinson`s disease pediction'],
                              icons=['house', 'droplet-fill', 'activity', 'person-walking'],
                              default_index=0)

    # Page selection and rendering
    if selected == 'Home':
        display_home_page()
    elif selected == 'Diabetes prediction':
        display_diabetes_prediction(diabetes_model)
    elif selected == 'Heart disease prediction':
        display_heart_disease_prediction(heart_disease_model)
    elif selected == 'Parkinson`s disease pediction':
        display_parkinsons_disease_prediction(parkinsons_model)

if __name__ == "__main__":
    main()
