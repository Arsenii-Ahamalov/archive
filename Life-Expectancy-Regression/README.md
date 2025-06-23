# 📈 Life Expectancy Regression Analysis

A comprehensive exploration into predicting average life expectancy across countries and years using a diverse set of demographic, health and socioeconomic indicators. This project not only builds predictive models but also uncovers which factors most strongly influence lifespan, offering potential insights for policy and public health planning.

---

## 🌍 Motivation

Life expectancy is a key summary measure of a population’s overall health and wellbeing. By understanding the drivers of longevity, governments and organizations can better allocate resources toward interventions—whether that’s strengthening immunization programs, reducing adult mortality, or investing in education and economic development.

---

## 📊 Data Overview

We work with historical country-year records, each row containing:
- **Target**: Life expectancy (years)
- **Demographics**: Adult mortality, infant and under-five mortality
- **Health metrics**: Vaccination rates (Hepatitis B, Polio, Diphtheria, Measles), HIV/AIDS mortality
- **Lifestyle**: Alcohol consumption, average BMI, thinness in children
- **Socioeconomics**: GDP per capita, government health expenditure, schooling years, “Income composition of resources”
- **Country status**: Developed vs. developing
- **Missing values** are present in several fields and require thoughtful imputation.

---

## 🔍 Methodology

1. **Data Cleaning & Imputation**  
   Handle missing entries and encode categorical fields to prepare for modeling.
2. **Feature Engineering**  
   Normalize, transform or bucketize select variables to capture nonlinear effects.
3. **Model Comparison**  
   - **Custom Random Forest**: Built from scratch to illustrate decision-tree ensembles  
   - **Linear & Ridge Regression**: Baseline statistical approaches  
   - **Advanced Learner**: e.g. Support Vector Regression or XGBoost for boosted performance  
4. **Hyperparameter Tuning & Evaluation**  
   Use RMSE and MAE on validation splits to select optimal model configurations.

---

## 📈 Key Insights

- **Top Predictors**: Adult mortality, GDP per capita and schooling emerged as the strongest drivers of life expectancy.  
- **Model Performance**: Random Forest and XGBoost notably outperformed linear models, capturing complex interactions and nonlinearities.  
- **Feature Effects**: Diminishing returns in GDP and schooling highlight where additional investment yields smaller lifespan gains.

---

## 🎯 Deliverables

- **`results.csv`**: Final predictions on held-out evaluation data, formatted with `Country, Year, Life expectancy`.  
- **Jupyter Notebook**: Step-by-step narrative of data exploration, model development, and result interpretation.  
- **Source Code**: Modular Python scripts for preprocessing, model implementation, training and evaluation.

---

By combining rigorous data work with multiple modeling approaches, this project demonstrates both predictive accuracy and interpretability—providing a solid foundation for evidence-based policy recommendations.  
