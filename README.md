# Early Projects Archive

This repository collects my first coursework and learning experiments in Data Science and Machine Learning. Each folder contains a standalone project with its own `README.md` and notebook, demonstrating the specific tasks and techniques required by the assignment.

> **Note:**  
> For my current, portfolio-ready projects, please see the main repositories on my GitHub profile.

---

## Contents

- Animal-Shelter-Analysis  
- Gym-Fitness-Data-Analysis-Visualization  
- Titanic-Survival-Classification  
- Life-Expectancy-Regression  
- Fashion-MNIST-Neural-Networks  

---

### Animal-Shelter-Analysis

Exploratory analysis of animal shelter intake and outcome records in Texas (2013–2024).  
- Load and clean the raw data  
- Handle missing values and transform categorical fields  
- Visualize intake/outcome trends and breakdown by species  
- Build an interactive Streamlit dashboard to explore key metrics  

---

### Gym-Fitness-Data-Analysis-Visualization

Analysis of personal fitness tracker data (heart rate, calories burned, BMI).  
- Preprocess and explore time-series measurements  
- Visualize distributions and correlations (histograms, scatter plots)  
- Train a Logistic Regression model to predict user gender  
- Deploy a Streamlit app to demonstrate data insights and model predictions  

---

### Titanic-Survival-Classification

Binary classification of Titanic passenger survival.  
- Load `data.csv`, split into training/validation/test subsets  
- Preprocess features: encode categoricals, impute missing values, derive new features (e.g. name length)  
- Train and tune Decision Tree and k-Nearest Neighbors classifiers via grid search  
- Compute F1-score, plot ROC curves and report AUC for each model  
- Select final model, estimate expected performance on unseen data  
- Generate `results.csv` with columns `ID` and `survived` for `evaluation.csv`  

---

### Life-Expectancy-Regression

Regression of country life expectancy from socioeconomic indicators.  
- Load `data.csv`, split into training/validation/test subsets  
- Encode categorical variables, impute missing values, optionally engineer new features  
- Implement a custom Random Forest from provided skeleton  
- Compare three models: custom RF, linear (or ridge) regression, plus one additional regressor  
- Tune hyperparameters by RMSE, report RMSE and MAE on validation set  
- Select final model, estimate expected RMSE on unseen data  
- Produce `results.csv` with columns `Country`, `Year`, and `Life expectancy` for `evaluation.csv`  

---

### Fashion-MNIST-Neural-Networks

Feed-forward and convolutional neural networks for Fashion-MNIST variants.  
- Load `train.csv` (32×32 images), split into train/validation/test; display example images  
- Build several feed-forward network variants: vary depth, layer sizes, normalization/standardization, optimizers, regularization  
- Build several convolutional network variants: vary number and size of conv/dense layers, apply normalization and regularization  
- For each model, report training behavior and validation accuracy  
- Select final network and estimate expected accuracy on unseen data  
- Output `results.csv` with columns `ID` and `label` for `evaluate.csv`  
