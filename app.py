import streamlit as st

st.title("Welcome to My Second Streamlit")
st.write("This is your  first Streamlit App!")
st.write("it's a simple app that demonstrates how to use Streamlit.")
st.write("You can add text, images, and other elements to your app.")

st.markdown("<h1 style='color:red;'>This is Red</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:green;'>This is Green</p>", unsafe_allow_html=True)
st.markdown("<p style='color:blue;'>This is Blue</p>", unsafe_allow_html=True)
st.markdown("<h3 style='color:yellew;'>This is yellow</h3>", unsafe_allow_html=True)

if st.button("Click Me"):
    st.write("You clicked the button!🥰")

name = st.text_input("Enter your name")
if name:
    st.write(f"Hello, {name}! Welcome to my Streamlit app.")

Marks = st.number_input("Enter your marks", min_value=0, max_value=100)
if Marks >= 50:
    st.success("You have passed the exam! 🎉")
else:
    st.error("You have failed the exam. Please try again. 😢")

s = st.slider("Select a range of values", 0, 100)
st.write(f"Selected range: {s}")
birthday = st.date_input("Select a Birthday")
st.write(f"Your birthday is: {birthday}")

st.selectbox("Select your favorite color", ["Red", "Green", "Blue"])   


# My first app
#Here's our first attempt at using data to create a table:


import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'Name': ['Krishna','Radha', 'Dhiraj','Akram'],
  'Marks': [100, 200, 300, 400]
})

df

    # -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 18:41:46 2025

@author: Akram Hussain
@title: Data Analysis using Python and Streamlit
"""
import streamlit as st
import pandas as pd
#Title and Subtitle
st.title("Data Analysis")
st.subheader("Data analysis using Python and Streamlit")

#Upload Dataset
#We will create a upload varibale
upload = st.file_uploader("Upload your dataset(In CSV format)")
if upload is not None:
    data= pd.read_csv(upload)
   

#Show Dataset
if upload is not None:
    if st.checkbox("Previous Uploaded file"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())
    
#Check Datatype of Each Columns
if upload is not None:
    if st.checkbox("Datatype of Each Columns"):
        st.text("Datatype")
        st.write(data.dtypes)
    
    
#Check for the Shape of your data 
if upload is not None:
    data_shape = st.radio("Do you want to check the Number of ",("Rows","Columns"))
    if data_shape == "Rows":
        st.text("Number of Rows")
        st.write(data.shape[0])
    if data_shape == "Columns":
        st.text("Number of Columns")
        st.write(data.shape[1])
        
        
#Check Null Values in the dataset
if upload is not None:
    test = data.isnull().values.any()
    if test == True:
       if st.checkbox("Null Values in your Dataset"):
        sns.heatmap(data.isnull())
        st.pyplot()
    else:
        st.success("Congratulations No Null values in your Dataset")
                 
                 
##Find Duplicates in the Dataset
if upload is not None:
    test = data.duplicated().any()
    if test == True:
        st.warning("Your data has duplicates")
        dup = st.selectbox("Do you want to remove duplicates", ("Select One", "Yes", "No"))
        if dup == "Yes":
            data = data.drop_duplicates()
            st.write("All Duplicates removed")
        if dup == "No":
            st.text("No Issue, Duplicates kept")
            
#Get Overall Statistics
if upload is not None:
    if st.checkbox("Summary of the Dataset"):
        st.write(data.describe(include= "all"))

#About Section
if st.button("About App"):
    st.text("Built using Streamlit")
    st.text("Thank to Streamlit")
    
#Created By
if st.button("Created by"):
    st.success("Created by Akram Hussain, Thank you for using the Web App")
    
           

