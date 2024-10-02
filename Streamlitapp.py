import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

import pickle
# Load the trained model

# Load the trained model
try:
    with open('model11.pkl', 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    print("Error loading the model:", e)

# Title of the app
st.title("Car Price Prediction")

html_temp="""
<img style="display: block;-webkit-user-select: none;margin: auto;cursor: zoom-in;background-color: hsl(0, 0%, 90%);transition: background-color 300ms;" src="https://dutchuncles.in/wp-content/uploads/2021/06/CarDekho-Feature.jpg" width="804" height="314">"""

st.markdown(html_temp, unsafe_allow_html=True)


# User input fields
st.header("Input Car Details")

# Input fields for car features

Kms_driven = st.sidebar.number_input("Kms Driven:",min_value=0, max_value=5500000, value=10000, step=5000)
No_of_owners=st.sidebar.number_input("No of previous owners",min_value=0,max_value=5,step=1)
Mileage = st.sidebar.number_input("Mileage:",min_value=7, max_value=140, value=10, step=10)
Engine = st.sidebar.number_input("Engine Capcity in CC:",min_value=50, max_value=5000, value=100, step=300)
Max_power = st.sidebar.number_input("Max power in BHP:",min_value=0, max_value=850000, value=10, step=10)
Seating_capacity = st.sidebar.number_input("Seating Capacity", min_value=1, max_value=10, value=5)
Vehicle_age = st.sidebar.number_input("Age of the Vehicle:",min_value=1, max_value=29, value=1, step=1)
Car_type = st.sidebar.selectbox("Car Body type", ('Hatchback', 'SUV','Sedan','MUV', 'Coupe', 'Minivans', 'Pickup Trucks'
 'Convertibles','Hybrids','Wagon'))
Fuel_type = st.sidebar.selectbox("Fuel Type", ("Petrol", "Diesel", "LPG", "CNG", "Electric"))
Insurance_type = st.sidebar.selectbox("Insurance Type", ("Third Party", "Comprehensive", "Zero Depo", "Others", "Not Available"))
Transmission=st.sidebar.selectbox("Transmission", ("Manual", "Automatic"))

expected_features = ['Kms_driven', 'No_of_owners', 'Mileage', 'Engine',
       'Max_power', 'Seating_capacity', 'Vehicle_age', 'Car_type_Convertibles',
       'Car_type_Coupe', 'Car_type_Hatchback', 'Car_type_Hybrids',
       'Car_type_MUV', 'Car_type_Minivans', 'Car_type_Pickup Trucks',
       'Car_type_SUV', 'Car_type_Sedan', 'Car_type_Wagon', 'Fuel_type_CNG',
       'Fuel_type_Diesel', 'Fuel_type_Electric', 'Fuel_type_LPG',
       'Fuel_type_Petrol', 'Insurance_type_Comprehensive',
       'Insurance_type_Not Available', 'Insurance_type_Others',
       'Insurance_type_Third Party', 'Insurance_type_Zero Dep',
       'Transmission_Automatic', 'Transmission_Manual']


# Create a DataFrame for the input data
input_data = pd.DataFrame({
    'Kms_driven':[Kms_driven],
    'No_of_owners':[No_of_owners],
    'Mileage':[Mileage],
    'Engine':[Engine],
    'Max_power':[Max_power],
    'Seating_capacity': [Seating_capacity],
    'Vehicle_age':[Vehicle_age],
    'Car_type_Convertibles': [1 if Car_type == 'Convertibles' else 0],
    'Car_type_Coupe': [1 if Car_type == 'Coupe' else 0],
    'Car_type_Hatchback': [1 if Car_type == 'Hatchback' else 0],
    'Car_type_Hybrids': [1 if Car_type == 'Hybrids' else 0],
    'Car_type_MUV': [1 if Car_type == 'MUV' else 0],
    'Car_type_Minivans': [1 if Car_type == 'Minivans' else 0],
    'Car_type_Pickup Trucks': [1 if Car_type == 'Pickup Trucks' else 0],
    'Car_type_SUV': [1 if Car_type == 'SUV' else 0],
    'Car_type_Sedan': [1 if Car_type == 'Sedan' else 0],
    'Car_type_Wagon':[1 if Car_type == 'Wagon' else 0],
    'Fuel_type_CNG': [1 if Fuel_type == 'CNG' else 0],
    'Fuel_type_Diesel': [1 if Fuel_type == 'Diesel' else 0],
    'Fuel_type_Electric': [1 if Fuel_type == 'Electric' else 0],
    'Fuel_type_LPG': [1 if Fuel_type == 'LPG' else 0],
    'Fuel_type_Petrol': [1 if Fuel_type == 'Petrol' else 0],
    'Insurance_type_Comprehensive': [1 if Insurance_type == 'Comprehensive' else 0],
    'Insurance_type_Not Available':[1 if Insurance_type == 'Not Available' else 0],
    'Insurance_type_Others': [1 if Insurance_type == 'Others' else 0],
    'Insurance_type_Third Party': [1 if Insurance_type == 'Third Party' else 0],
    'Insurance_type_Zero Dep': [1 if Insurance_type == 'Zero Dep' else 0],
    'Transmission_Automatic': [1 if Transmission == 'Automatic' else 0],
    'Transmission_Manual': [1 if Transmission == 'Manual' else 0]
})


# Make prediction
if st.button("Predict Price"):
    prediction = model.predict(input_data)
    
    # Convert prediction from numeric to lakhs
    price_in_lakh =prediction[0]# Assuming the prediction is in the original currency
    st.success(f"The predicted car price is: Rs {price_in_lakh:,.2f} Lakh")

