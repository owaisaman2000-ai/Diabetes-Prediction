# Import Packages
import streamlit as st
import pandas as pd
import numpy as np
import joblib
# Load the saved model
saved = joblib.load('diabetes_model.pkl')
model = saved['model']
imputer = saved['imputer']
scaler = saved['scaler']
# App Title
st.title('Diabetes Prediction System')
st.write('Enter your details below to predict diabetes.')
# Input Fields
pregnancies = st.number_input('Pregnancies', min_value=0)
glucose = st.number_input('Glucose', min_value=0)
bp = st.number_input('Blood Pressure', min_value=0)
skin = st.number_input('Skin Thickness', min_value=0)
insulin = st.number_input('Insulin', min_value=0)
bmi = st.number_input('BMI', min_value=0.0)
dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0)
age = st.number_input('Age', min_value=0)
# Prediction Button
if st.button('Predict'):
    data= pd.DataFrame([[pregnancies, glucose, bp, skin,insulin, bmi, dpf, age]],columns=['Pregnancies', 'Glucose', 'BloodPressure',
        'SkinThickness', 'Insulin', 'BMI',
        'DiabetesPedigreeFunction', 'Age'])
    # Replace invalid zeros
    cols= ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    data[cols]= data[cols].replace(0, np.nan)
    # Fill missing values
    data = imputer.transform(data)
     # Scale input data
    data=  scaler.transform(data)
    # Make prediction
    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]
    # Display prediction
    if prediction == 1:
        st.error('Diabetes Prediction: Positive')
    else:
        st.success('Diabetes Prediction: Negative')
    #Display probability
    st.write("Diabetes Probability:", round(probability * 100, 2), "%")
st.caption("For educational purposes only. Not a medical diagnosis.")
