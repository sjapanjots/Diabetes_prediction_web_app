# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 04:10:38 2023

@author: Japanjot Singh
"""

import numpy as np 
import pickle 
import streamlit as st

#loading the saveds model 
loaded_model = pickle.load(open('C:/Users/Japanjot Singh/Desktop/Diabetic Model/diabetes_model.sav' , 'rb'))

# Creating a function 

def diabetes_prediction(input_data):
    
    
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
    
def main():
    
    
    # giving a title 
    st.title('Diabetes Prediction Web App')
    
    # getting the input data from the user 
    Pregnancies = st.text_input('Number of Pregnancies ')
    Glucose = st.text_input('Enter glucose level ')
    BloodPressure = st.text_input('Blood pressure level ')
    SkinThickness =st.text_input('Skin Thickness level')
    Insulin = st.text_input('Insulin level')
    BMI = st.text_input('Enter BMI ')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value ')
    Age = st.text_input('enter the Age')
    
    
    # code for prediction 
    diagnosis = ''
    
    # creating a button for prediction 
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose , BloodPressure, SkinThickness, Insulin , BMI , DiabetesPedigreeFunction, Age])
        
        
    st.success(diagnosis)
        
        
        
        
        
        
if __name__ =='__main__':
    main()
        
        
        
        
        
        
        
        