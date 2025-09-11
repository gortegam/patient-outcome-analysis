import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("data/hospital_data.csv")

# Target and features
df["Readmission"] = df["Readmission"].str.strip().str.capitalize()
y = df["Readmission"].map({"No": 0, "Yes": 1})
X = df[["Age", "Gender", "Diagnosis", "Length_of_Stay", "Treatment", "Outcome"]]

# Preprocessing
categorical_features = ["Gender", "Diagnosis", "Treatment", "Outcome"]
numeric_features = ["Age", "Length_of_Stay"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ("num", "passthrough", numeric_features)
    ]
)

# Model
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000))
])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
model.fit(X_train, y_train)

# Streamlit UI
st.title("🏥 Patient Readmission Risk Dashboard")
st.markdown("Use the sidebar to simulate patient info and predict readmission risk.")

st.sidebar.header("Patient Information")
age = st.sidebar.slider("Age", 0, 100, 50)
gender = st.sidebar.selectbox("Gender", df["Gender"].unique())
diagnosis = st.sidebar.selectbox("Diagnosis", df["Diagnosis"].unique())
treatment = st.sidebar.selectbox("Treatment", df["Treatment"].unique())
length = st.sidebar.slider("Length of Stay", 1, 60, 5)

# Make prediction
input_df = pd.DataFrame([{
    "Age": age,
    "Gender": gender,
    "Diagnosis": diagnosis,
    "Treatment": treatment,
    "Length_of_Stay": length,
    "Outcome": "Recovered"
}])

prob = model.predict_proba(input_df)[:, 1][0]
pred = "Yes" if prob >= 0.5 else "No"

st.subheader("Prediction Result")
st.write(f"**Predicted Readmission:** {pred}")
st.write(f"**Probability:** {prob:.2%}")
