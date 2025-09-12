# 🏥 Patient Outcome Analysis

## 📌 Objective
This project analyzes hospital patient data to uncover patterns in length of stay, discharge status, and readmission. The goal is to derive actionable insights that could help healthcare administrators improve efficiency and patient care.

## 🧰 Tools Used
- Python
- Pandas
- Matplotlib / Seaborn
- Jupyter Notebook

## 🚀 Live Demo
Try the app here: [Patient Readmission Dashboard](https://gortegam-patient-outcome-analysis.streamlit.app)


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

## 🤖 Machine Learning

To extend the analysis, we built a predictive model to estimate **hospital readmission risk** based on patient demographics, diagnoses, and treatment details.

- **Model:** Logistic Regression with one-hot encoding for categorical features  
- **Target Variable:** `Readmission` (Yes/No → 1/0)  
- **Features:** Age, Gender, Diagnosis, Treatment, Length of Stay, Outcome  
- **Pipeline:** Preprocessing (categorical encoding + passthrough numerics) → Logistic Regression


### 🔎 Evaluation
- Metrics include **Accuracy, Precision, Recall, F1-score, and ROC-AUC**  
- Confusion matrix visualization for classification performance  
- ROC-AUC provides insight into separability of the model

### 📊 Insights
This model provides a baseline for predicting readmission.  
Future improvements may include:
- Using ensemble methods (Random Forest, XGBoost)  
- Hyperparameter tuning with cross-validation  
- Feature importance analysis for interpretability  

The complete implementation is available in [`notebooks/readmission_model.ipynb`](notebooks/readmission_model.ipynb).

### ML Models Update

This project includes two predictive models for **hospital readmission risk**:

- **Logistic Regression** – a baseline model chosen for simplicity and interpretability.  
- **Random Forest** – a more powerful model that captures non-linear relationships and provides feature importance insights.  

Both models are implemented as Jupyter notebooks in the `notebooks/` directory.



## 📁 Data

- The primary dataset used for this project is synthetic and modeled after typical hospital patient records. It has the following fields:  
  `Patient_ID`, `Age`, `Gender`, `Diagnosis`, `Treatment`, `Length_of_Stay`, `Outcome`, `Readmission`.

- For those interested in exploring similar real-oriented datasets, here are some useful references:
  - [Synthetic Hospital Data](https://www.kaggle.com/datasets/amulyas/synthetic-hospital-data) — includes demographic information, diagnoses, and stay length. 
  - [Hospital Patient Records Dataset](https://www.kaggle.com/datasets/blueblushed/hospital-dataset-for-practice) — about 1,000 patient records with outcomes and treatment data.
  - [Hospital Readmission Prediction (Synthetic)](https://www.kaggle.com/datasets/siddharth0935/hospital-readmission-predictionsynthetic-dataset) — structured for exploring readmission risk. 

- Note: No personally identifiable information is included in the dataset. All records are synthetic or anonymized.

## 🩺 Why It Matters
Hospitals are constantly seeking ways to reduce costs and improve patient outcomes. This project provides exploratory insights that can inform resource allocation and policy decisions in a healthcare setting.

## 🚀 Next Steps
- Add ML model to predict readmission risk
- Deploy dashboard using Streamlit or Power BI

## 📜 License
MIT License – feel free to use or modify the code.
