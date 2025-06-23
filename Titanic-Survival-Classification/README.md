# 🛳️ Titanic Survival Classification

A focused project on preprocessing mixed‐type features and building binary classifiers to predict which passengers survived the Titanic disaster.

---

## 🌍 Task Overview

Predict the `survived` label (0 = No, 1 = Yes) using passenger attributes such as class, age, family relationships and more. You’ll handle missing data, create new features, and compare decision trees vs. k-nearest neighbors, tuning each for best performance.

---

## 📊 Data

- **data.csv** – training set with `survived` and these features:  
  - `Pclass` (1/2/3), `Name`, `Sex`, `Age`  
  - `SibSp`, `Parch`, `Ticket`, `Fare`, `Cabin`  
  - `Embarked` (C/Q/S), `Home.Dest`
- **evaluation.csv** – test set (no `survived`); generate predictions here.

---

## 🔍 Methodology

1. **Split** into train / validation / test subsets.  
2. **Preprocess & Feature Engineering**  
   - Encode categories (`Sex`, `Embarked`)  
   - Impute missing ages, fares, cabins, etc.  
   - Derive new features (e.g. name length, family size)  
3. **Modeling**  
   - **Decision Tree**: interpretability vs. overfitting  
   - **KNN**: distance-based classification  
4. **Hyperparameter Tuning**  
   - Optimize tree depth, leaf size; tune `k` in KNN  
   - Evaluate by F1 score on validation  
5. **Evaluation**  
   - Compute F1, plot ROC curve & calculate AUC  
   - Document methodological choices and pitfalls  
6. **Final Selection & Prediction**  
   - Choose best model (≥75% expected accuracy)  
   - Predict on `evaluation.csv` → save `results.csv` with `ID, survived`

