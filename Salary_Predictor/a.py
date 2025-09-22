import pandas as pd
import numpy as np
import pickle
import streamlit as st

rf = pickle.load(open("model.pkl",'rb'))

df = pd.read_csv('Salary_data.csv')

st.header('Salary Predicter')

Age = float(st.slider("Employee Age", 20.0, 60.0, 23.0, format="%.1f"))
exp = st.slider("Experience (in years)", 0, 30, 0)
Education_level = ["High School","Bachelor's", "Master's", "PhD"]
opt = st.selectbox('Education Level', Education_level)

# Convert Education Level to numerical values
if opt == "High School":
    education_level = "Education Level_High School"
elif opt == "Bachelor's":
    education_level = "Education Level_Bachelor's"
elif opt == "Master's":
    education_level = "Education Level_Master's"
elif opt == "PhD":
    education_level = "Education Level_PhD"

inputs = {"Age": Age, "Years of Experience": exp, 
          "Education Level_Bachelor's": 0, "Education Level_High School": 0, 
          "Education Level_Master's": 0, "Education Level_PhD": 0}

inputs[education_level] = 1

t = pd.DataFrame(data=inputs, index=[0])

pre = rf.predict(t)
if st.button('Predict Salary'):
    st.write(f"Predicted Salary:${pre[0]:.2f}")