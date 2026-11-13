# Diabetes Prediction System

## Project Overview
The Diabetes Prediction System is a machine learning-based web application that predicts whether a person is likely to have diabetes based on medical input parameters.

The application uses Logistic Regression to generate predictions and displays the prediction probability.

## Project Objectives
- Build a machine learning model for diabetes prediction.
- Develop an interactive web application using Streamlit.
- Allow users to enter medical parameters and receive predictions.
- Display prediction results and probability percentages.

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

## Machine Learning Algorithm
**Logistic Regression**

The trained model is saved as `diabetes_model.pkl` and loaded by the Streamlit application to generate predictions.

## Input Features
1. Pregnancies
2. Glucose
3. Blood Pressure
4. Skin Thickness
5. Insulin
6. BMI
7. Diabetes Pedigree Function
8. Age

## Project Files
- `app.py` – Streamlit application code.
- `diabetes_model.pkl` – Trained machine learning model.
- `requirements.txt` – Required Python libraries.
- `runtime.txt` – Python runtime configuration.

## How to Run the Project Locally

1. Clone the repository.
2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
streamlit run app.py
```

## Live Application

[Diabetes Prediction System](https://diabetes-prediction-owais.streamlit.app/)

## Disclaimer
This application is developed for educational purposes only. Its predictions are not a substitute for professional medical advice or diagnosis.
