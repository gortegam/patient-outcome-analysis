import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model.pkl")

# Title
st.title("🏥 Patient Readmission Risk Dashboard")

st.markdown("Use the form below to simulate patient characteristics and predict readmission risk.")

# Sidebar inputs
st.sidebar.header("Patient Information")
age = st.sidebar.slider("Age", 0, 100, 50)
gender = st.sidebar.selectbox("Gender", ["M", "F"])
diagnosis = st.sidebar.selectbox("Diagnosis", ["Heart Failure", "Pneumonia", "Diabetes", "Stroke", "Fracture", "Cancer"])
treatment = st.sidebar.selectbox("Treatment", ["Medication", "Antibiotics", "Insulin", "Surgery", "Cast", "Chemo"])
length = st.sidebar.slider("Length of Stay", 1, 60, 5)

# Make prediction
input_df = pd.DataFrame([{
    "Age": age,
    "Gender": gender,
    "Diagnosis": diagnosis,
    "Treatment": treatment,
    "Length_of_Stay": length,
    "Outcome": "Recovered"  # placeholder to match preprocessing
}])

prob = model.predict_proba(input_df)[:, 1][0]
pred = "Yes" if prob >= 0.5 else "No"

# Results
st.subheader("Prediction Result")
st.write(f"**Predicted Readmission:** {pred}")
st.write(f"**Probability:** {prob:.2%}")
