import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline
model = joblib.load('model.pkl')

st.set_page_config(page_title="Health Cost Predictor")

st.title("💡 Health Insurance Cost Predictor")
st.write("Fill in your information to estimate your insurance charges.")

# Input fields
age = st.slider("Age", 18, 64, 30)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Children", 0, 5, 0)
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

if st.button("Predict Insurance Cost"):
    input_df = pd.DataFrame([{
        'age': age,
        'bmi': bmi,
        'children': children,
        'sex': sex,
        'smoker': smoker,
        'region': region
    }])
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Insurance Cost: ${prediction:,.2f}")
