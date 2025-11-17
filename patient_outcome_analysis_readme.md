# 🏥 Patient Outcome Analysis
**Data-Driven Insights for Length of Stay, Discharge Patterns, and Readmission Risk**

## 📌 Objective
This project analyzes synthetic hospital patient data to uncover patterns in **length of stay**, **discharge outcomes**, and **readmission risk**.  
The goal is to produce actionable insights for hospital administrators.

## 🧠 Business Impact
- Reduce avoidable readmissions  
- Identify high-risk groups  
- Optimize length of stay  
- Improve discharge practices  
- Support leadership dashboards  

## 🧰 Tools Used
- Python, Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  
- Streamlit  
- Jupyter Notebooks  

## 🚀 Live Demo
[Patient Readmission Dashboard](https://gortegam-patient-outcome-analysis.streamlit.app)

## 🗂️ Project Structure
```
patient-outcome-analysis/
├── data/
├── notebooks/
├── scripts/
├── requirements.txt
└── README.md
```

## 📊 Key Questions
- What is LOS by diagnosis and demographics?  
- Which diagnoses predict readmission?  
- How do treatments affect outcomes?  

## 📈 Sample Insights
- Cancer patients: ~14-day stays  
- Readmission risk increases sharply age 50+  
- Fractures: shortest LOS (~2.3 days)

## 🤖 Machine Learning
Two models built:

### Logistic Regression
- Interpretable baseline  
- One-hot encoding + numeric passthrough  

### Random Forest
- Captures non-linear patterns  
- Feature importance  

## 🧪 Model Performance (Fill after running)
| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|------|----------|-----------|--------|----|---------|
| Logistic Regression | _X.XX_ | _X.XX_ | _X.XX_ | _X.XX_ | _X.XX_ |
| Random Forest | _X.XX_ | _X.XX_ | _X.XX_ | _X.XX_ | _X.XX_ |

## 📸 Visualizations (Add screenshots)
- LOS by Diagnosis  
- Readmission by Age  
- Feature Importance  
- Streamlit Dashboard Preview  

## 📁 Data
Synthetic dataset fields:  
`Patient_ID`, `Age`, `Gender`, `Diagnosis`, `Treatment`, `Length_of_Stay`, `Outcome`, `Readmission`

## 🏥 Real Hospital Use Cases
- Monthly readmission reports  
- LOS dashboards for bed management  
- Root cause analysis  
- Case management flagging  
- Predictive modeling workflow  

## 🚀 Next Steps
- Add calibration curves  
- Expand dashboard  
- Add cost estimator for readmissions  
- Hyperparameter tuning  
- Optional API for predictions
