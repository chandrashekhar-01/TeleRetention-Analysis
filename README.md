# TeleRetention-Analysis

## Overview

This project focuses on customer retention analysis in the telecom sector by leveraging **Machine learning (ML)** models and **Power BI** for data visualization. The aim is to predict **Customer Churn**, estimate **Customer Lifetime Value (CLV)**, and provide actionable insights through interactive dashboards. By employing advanced ML techniques and Data Visualization, the project enables stakeholders to make informed decisions and implement proactive retention strategies.

---

## Features

- **Churn Prediction**:  
   Utilized algorithms like **Random Forest**, **CatBoost**, and **Recurrent Neural Networks (RNN)** to predict churn with high accuracy.
- **CLV Estimation**:  
   Modeled **Customer Lifetime Value** to understand revenue contribution and focus retention efforts on high-value customers.
- **Interactive Dashboards**:  
   Power BI visualizations provided real-time insights into churn rates, CLV distribution, and customer segmentation.
- **Data Balancing**:  
   Applied techniques like **SMOTE** and **SMOTE-ENN** to handle class imbalance for reliable model performance.

---

## Project Structure

### Data Preprocessing
- Includes handling missing values, encoding categorical data, and scaling features.

### ML Models
- **Random Forest**: Achieved 92% accuracy with SMOTE-ENN for balancing.
- **CatBoost**: Delivered the highest accuracy at 96%.
- **Recurrent Neural Networks (RNN)**: Used to capture temporal dependencies in customer data.

### Visualization
- Power BI dashboards provide dynamic insights into customer behavior, retention strategies, and key KPIs.

---

## Results

- **Churn Prediction**:  
   CatBoost achieved the highest accuracy (96%) with excellent F1-scores on imbalanced data.
- **CLV Estimation**:  
   Calculated using customer tenure and monthly charges to identify high-value customers.
- **Dashboards**:  
   Customer Demographics, Churn Analysis, and CLV Distribution dashboards.

---

## Tools and Technologies

- **Programming**: Python (`Pandas`, `NumPy`, `Scikit-learn`, `CatBoost`, `TensorFlow`)
- **Visualization**: Power BI
- **Data Processing**: SMOTE, SMOTE-ENN
- **Other Tools**: Jupyter Notebook

---

## Future Enhancements

- **Cloud Deployment**:  
   Deploy models on platforms like AWS or Azure for real-time processing.

- **Advanced Features**:  
   Incorporate sentiment analysis and unstructured data insights.

- **API Integration**:  
   Build APIs for seamless integration with CRM tools.

- **Enhanced Dashboards**:  
   Add more drill-down features for deeper insights.
