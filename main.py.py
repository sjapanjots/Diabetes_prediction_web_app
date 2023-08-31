# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 03:03:34 2023

@author: Japanjot Singh
"""

import numpy as np 
import pickle
import streamlit as st

# loadinf the saved model 
loaded_model = pickle.load(open(r"C:/Users/Japanjot Singh/Downloads/deploy model/trained_model.sav" , 'rb'))

#creating a function for prediciton 

def diabetes_prediction(input_data):
    
    # changing the input data to numpy array 
    input_data_as_numpy_array = np.asaaray(input_data)
    
    # reshape the arrasy as we are predicting for one instance 
    input_data_reshaped = input_data_as_numpy_array.reshape(-1,1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if (prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return 'the person in diabetic'
        
        
        
    
def main():
    
    # giving a title 
    st.title('Diabetes Prediciton Web App')
    
    # getting the input data from the users 
    
    
    Pregnancies = st.text_input('Enter the number of pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure Level')
    SkinThickness = st.text_input('Skin Thickness Level ')
    Insulin = st.text('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value ')
    Age = st.text_input('Age of the person')
    
    # code for predsiciton 
    diagnosis = ''
    
    # creating a button for prediction 
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies ,Glucose ,BloodPressure ,SkinThickness ,Insulin ,BMI ,DiabetesPedigreeFunction , Age  ])
    
    
    st.success(diagnosis)
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
