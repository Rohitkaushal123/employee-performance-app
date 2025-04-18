import streamlit as st
import pickle
import numpy as np


model = pickle.load(open('model.pkl', 'rb'))



age = st.number_input('Age', 18,65,30)
experience = st.slider("Years of Experience", 0, 40, 5)
hours = st.slider("Work Hours Per Week", 20, 80, 40)
certs = st.slider("Certifications", 0, 10, 2)
mentor = st.radio('Has mentor',['yes', 'No'])
mentor_val = 1 if mentor == 'yes' else 0

education = st.selectbox("Education Level", ["high_school", "master", "phd"])
edu_vals = {'high_school':[1,0,0], 'master':[0,1,0], 'phd':[0,0,1]}
edu_encoded = edu_vals[education]

dept = st.selectbox("Department", ["Finance", "HR", "Marketing", "Sales"])
dept_vals = {"Finance": [1, 0, 0, 0], "HR": [0, 1, 0, 0], "Marketing": [0, 0, 1, 0], "Sales": [0, 0, 0, 1]}
dept_encoded = dept_vals[dept]

input_data = np.array([[age, experience, hours, certs, mentor_val] + edu_encoded + dept_encoded])

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    st.success(f"🎯 Predicted Performance Score: {round(prediction, 2)}")
