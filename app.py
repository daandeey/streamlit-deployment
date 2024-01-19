import streamlit as st
import pandas as pd
import numpy as np
from helper import preprocess
import pickle

# Load the model
# model = joblib.load('your_model.pkl')  # Replace with the path to your saved model
model = pickle.load(open('model/random_forest.sav', 'rb'))
scaler = pickle.load(open('model/standard_scaler.sav', 'rb'))

# Define the Streamlit app
st.title('Diabetes Prediction')

feature_list = dict()

# Add input widgets for user input
feature_list['Pregnancies'] = st.text_input('Enter Pregnancies:')
feature_list['Glucose'] = st.text_input('Enter Glucose:')
feature_list['BloodPressure'] = st.text_input('Enter Blood Pressure:')
feature_list['SkinThickness'] = st.text_input('Enter Skin Thickness:')
feature_list['Insulin'] = st.text_input('Enter Insulin:')
feature_list['BMI'] = st.text_input('Enter BMI:')
feature_list['DiabetesPedigreeFunction'] = st.text_input('Enter Diabetes Pedigree Function:')
feature_list['Age'] = st.text_input('Enter Age:')

# Add a button to make predictions
if st.button('Predict'):
    # Perform predictions
    df_feature_list = pd.DataFrame(data=np.array(list(feature_list.values())).reshape(1,-1), columns=feature_list.keys())
    df_feature_list = df_feature_list.astype(float)
    final_features = preprocess(df_feature_list, scaler)

    prediction = model.predict(final_features)
    output = int(prediction[0])
    if output == 1:
        text = "Diabetes"
        st.error(f'Prediction: {text}')
    else:
        text = "Healthy"
        st.success(f'Prediction: {text}')
    