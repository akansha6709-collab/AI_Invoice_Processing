# Vendor Invoice Intelligence System

### Freight Cost Prediction & Invoice Risk Flagging

An end-to-end Machine Learning project designed to help finance and procurement teams analyze vendor invoices, predict freight costs, and identify invoices that may require manual review.

---

## 📌 Project Overview

Vendor invoice data contains financial, purchasing, freight, and operational information.

This project uses SQL, Python, Pandas, Scikit-learn, and Machine Learning to build two predictive solutions:

1. **Freight Cost Prediction** – Regression problem
2. **Invoice Risk Flagging** – Classification problem

The goal is to help finance teams improve cost estimation and identify potentially abnormal invoices for further review.

---

## 🎯 Business Objectives

### 1. Freight Cost Prediction

**Objective:**

Predict the expected freight cost for a vendor invoice using invoice and purchasing information.

**Why it matters:**

- Helps estimate landed costs
- Supports procurement planning
- Helps identify unusual freight charges
- Can support vendor cost analysis
- Improves financial forecasting

### 2. Invoice Risk Flagging

**Objective:**

Identify invoices that may require manual review based on abnormal invoice amounts, purchasing values, and operational patterns.

**Why it matters:**

- Reduces manual invoice screening
- Helps prioritize invoices for review
- Supports financial controls
- Helps identify potentially unusual transactions

> Note: The invoice risk labels in this project are created using predefined business rules for learning and demonstration purposes. They are not confirmed fraud labels.

---

## 📂 Data Source

The project uses a SQLite database:

`Data/inventory.db`

The database contains the following tables:

- `vendor_invoice` – Vendor invoice information
- `purchases` – Purchase and item-level information
- `purchase_prices` – Purchase price reference data
- `begin_inventory` – Beginning inventory information
- `end_inventory` – Ending inventory information

SQL queries and aggregations are used to create meaningful invoice-level features for Machine Learning.

---

## 🔍 Exploratory Data Analysis

EDA was performed to understand relationships between invoice, purchasing, and freight-related variables.

Key business questions include:

- Does freight cost increase with quantity?
- Does invoice value have a relationship with freight cost?
- Do flagged invoices have different financial characteristics?
- Are there unusual values or outliers?
- Which variables are most useful for prediction?

Statistical analysis, correlation analysis, and visualization were used during the analysis.

---

## 🤖 Machine Learning Models

### Freight Cost Prediction – Regression

The following models were evaluated:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

### Invoice Risk Flagging – Classification

The following models were used/evaluated:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

Random Forest classification uses `GridSearchCV` for hyperparameter tuning.

F1-score is used during model selection because it provides a better balance between precision and recall when dealing with potentially imbalanced classes.

---

## 📊 Model Evaluation

### Freight Cost Prediction

The regression models are evaluated using:

- MAE – Mean Absolute Error
- RMSE – Root Mean Squared Error
- R² Score

### Invoice Risk Flagging

The classification model is evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Classification Report
- Feature Importance

---

## 📈 Freight Prediction Results

The following results were obtained during model evaluation:

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 24.11 | 124.72 | 96.99% |
| Decision Tree Regressor | 32.97 | 150.31 | 95.63% |
| Random Forest Regressor | 26.13 | 134.79 | 96.48% |

### Best Performing Model

**Linear Regression**

- MAE: **24.11**
- RMSE: **124.72**
- R²: **96.99%**

The trained model is saved as:

`models/predict_freight_model.pkl`

---

## 🧠 Feature Engineering

The project uses SQL-based aggregation and feature engineering to transform raw transactional data into ML-ready features.

Examples include:

- Invoice quantity
- Invoice dollars
- Freight
- Total item quantity
- Total item dollars
- Total brands
- Average receiving delay
- Days from PO to invoice
- Days from invoice to payment

These features help capture both financial and operational characteristics of vendor invoices.

---

## 🛠️ Technologies Used

### Programming

- Python
- SQL

### Data Analysis

- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Machine Learning

- Scikit-learn

### Database

- SQLite

### Model Persistence

- Joblib

### Application

- Streamlit

---

## 📁 Project Structure

```text
Vendor_Invoice_Intelligence/
│
├── Data/
│   └── inventory.db
│
├── models/
│   ├── predict_freight_model.pkl
│   ├── scaler.pkl
│   └── predict_flag_invoice.pkl
│
├── notebooks/
│
├── data_preprocessing.py
├── data_preprocessing2.py
│
├── modeling_evaluation.py
├── modeling_evaluation2.py
│
├── train.py
├── train2.py
│
├── invoice_flagging.py
│
└── README.md