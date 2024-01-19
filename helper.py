import pandas as pd
import numpy as np

SKEWED_COLUMNS = ['Pregnancies', 'SkinThickness', 'Insulin', 'DiabetesPedigreeFunction', 'Age']

def preprocess(df, scaler):
    # impute data with 0 value with median from training set
    df['Glucose'] = df['Glucose'].replace(0, 117.0)
    df['BloodPressure'] = df['BloodPressure'].replace(0, 72.0)
    df['SkinThickness'] = df['SkinThickness'].replace(0, 23.0)
    df['Insulin'] = df['Insulin'].replace(0, 30.5)
    df['BMI'] = df['BMI'].replace(0, 32.0)
    
    df[SKEWED_COLUMNS] = np.log(df[SKEWED_COLUMNS]+1)
    df = scaler.transform(df)

    return df