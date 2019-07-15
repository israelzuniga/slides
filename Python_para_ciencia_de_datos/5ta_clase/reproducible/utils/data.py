'''
utils/data.py

'''
import os
from urllib.request import urlretrieve

import pandas as pd

PIMA_URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data'


def pima_data(filename='diabetes.csv', url=PIMA_URL,
                     force_download=False):
    """
    """
    list_cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv(filename, names =  list_cols)
    return data

