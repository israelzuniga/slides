from utils.data import pima_data
import pandas as pd
import numpy as np

cols_list = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']

def test_pima_data():
    data = pima_data()
    assert all(data.columns == cols_list)
