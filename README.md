# 🏥 Patient Outcome Analysis

## 📌 Objective
This project analyzes hospital patient data to uncover patterns in length of stay, discharge status, and readmission. The goal is to derive actionable insights that could help healthcare administrators improve efficiency and patient care.

## 🧰 Tools Used
- Python
- Pandas
- Matplotlib / Seaborn
- Jupyter Notebook

## 🗂️ Project Structure
- `data/` – Contains the raw or sample datasets used for analysis.
- `notebooks/` – Jupyter Notebooks with all the data exploration and visualizations.
- `src/` – (Optional) Python scripts or helper functions.
- `requirements.txt` – List of Python libraries needed to run the notebooks.
- `.gitignore` – Prevents unnecessary files (e.g., cache, checkpoints) from being tracked.
- `README.md` – Overview of the project.

## 📊 Key Questions Explored
- What is the average length of stay by diagnosis or age group?
- Are certain diagnoses more likely to result in readmission?
- Are there patterns in discharge status across patient types?

## 📈 Sample Insights
- Patients with cancer have significantly longer stays(14.0 days on average).
- Readmission risk increases with age above 49(33% below vs 54.5% at/above).
- Fractures are most associated with early discharge(2.3 days on average).

*(This section will be updated as analysis progresses.)*

## 📁 Data

- The primary dataset used for this project is synthetic and modeled after typical hospital patient records. It has the following fields:  
  `Patient_ID`, `Age`, `Gender`, `Diagnosis`, `Treatment`, `Length_of_Stay`, `Outcome`, `Readmission`.

- For those interested in exploring similar real-oriented datasets, here are some useful references:
  - [Synthetic Hospital Data](https://www.kaggle.com/datasets/amulyas/synthetic-hospital-data) — includes demographic information, diagnoses, and stay length. :contentReference[oaicite:3]{index=3}  
  - [Hospital Patient Records Dataset](https://www.kaggle.com/datasets/blueblushed/hospital-dataset-for-practice) — about 1,000 patient records with outcomes and treatment data. :contentReference[oaicite:4]{index=4}  
  - [Hospital Readmission Prediction (Synthetic)](https://www.kaggle.com/datasets/siddharth0935/hospital-readmission-predictionsynthetic-dataset) — structured for exploring readmission risk. :contentReference[oaicite:5]{index=5}

- Note: No personally identifiable information is included in the dataset. All records are synthetic or anonymized.

## 🩺 Why It Matters
Hospitals are constantly seeking ways to reduce costs and improve patient outcomes. This project provides exploratory insights that can inform resource allocation and policy decisions in a healthcare setting.

## 🚀 Next Steps
- Add ML model to predict readmission risk
- Deploy dashboard using Streamlit or Power BI

## 📜 License
MIT License – feel free to use or modify the code.
