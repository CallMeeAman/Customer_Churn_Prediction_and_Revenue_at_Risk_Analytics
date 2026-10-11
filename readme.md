# 📊 Customer Churn Prediction & Revenue-at-Risk Analytics

A machine learning and business analytics project that predicts customer churn and estimates the monthly recurring revenue associated with customers at risk of leaving a company's services.

The project combines **machine learning, exploratory data analysis, and an interactive Streamlit dashboard** to turn customer data into actionable business insights.

## 📌 Project Overview

Customer churn is a major challenge for subscription-based businesses. Losing customers can reduce recurring revenue and negatively affect long-term business growth.

However, knowing how many customers might leave is not enough. Businesses also need to understand the potential financial impact of losing those customers.

This project addresses both challenges by:

* Predicting which customers are likely to churn using machine learning.
* Estimating the monthly revenue associated with predicted at-risk customers.
* Exploring customer behavior and churn patterns through data visualizations.
* Providing an interactive dashboard to analyze customer churn and revenue exposure.

The project uses the **Telco Customer Churn dataset**.

## 🎯 Project Objectives

* Build and evaluate machine learning models for customer churn prediction.
* Identify customers predicted to be at risk of leaving.
* Calculate total monthly revenue at risk.
* Analyze churn patterns across different customer segments.
* Identify customers with both high churn risk and high monthly charges.
* Present key business metrics and insights through an interactive dashboard.

## 💰 Revenue-at-Risk Analytics

One of the main features of this project is its focus on the financial impact of customer churn.

Instead of focusing only on the number of customers who may leave, the project estimates the monthly revenue associated with those customers.

### Key Metrics

| Metric                                       | Description                                                       |
| -------------------------------------------- | ----------------------------------------------------------------- |
| Total Customers                              | Total number of customers analyzed.                               |
| Predicted Churn Customers                    | Number of customers predicted to churn.                           |
| Predicted Churn Rate                         | Percentage of analyzed customers predicted to churn.              |
| Total Monthly Revenue at Risk                | Sum of monthly charges for customers predicted to churn.          |
| Average Monthly Charges of At-Risk Customers | Average monthly charges among predicted at-risk customers.        |
| Percentage of Monthly Revenue at Risk        | At-risk monthly charges as a percentage of total monthly charges. |

### Revenue-at-Risk Calculation

**Total Monthly Revenue at Risk**

Sum of the `MonthlyCharges` values for customers predicted to churn.

**Percentage of Monthly Revenue at Risk**

(Total Monthly Revenue at Risk / Total Monthly Charges) × 100

These metrics estimate revenue exposure based on model predictions. They do not represent guaranteed financial losses because some predicted customers may remain with the company.

## 📈 Dashboard Features

The Streamlit dashboard is designed to provide an overview of customer churn and its potential financial impact.

### Key Performance Indicators

* Total customers analyzed
* Predicted churn customers
* Predicted churn rate
* Total monthly revenue at risk
* Average monthly charges of at-risk customers
* Percentage of monthly revenue at risk

### Data Visualizations

* Customer churn distribution
* Revenue at risk by contract type
* Revenue at risk by payment method
* Churn patterns across customer tenure groups
* Comparison of customer segments
* Identification of high-risk, high-revenue customers

*Dashboard metrics and visualizations will depend on the implemented features, dataset, and model predictions.*

## ⚙️ Machine Learning Workflow

The project follows a structured data science workflow:

1. **Data Collection** — Load the Telco Customer Churn dataset.
2. **Data Cleaning** — Handle missing values, correct data types, and prepare the data.
3. **Exploratory Data Analysis (EDA)** — Investigate customer characteristics and churn patterns.
4. **Feature Engineering** — Prepare relevant features for model training.
5. **Data Preprocessing** — Encode categorical variables and handle numerical features.
6. **Model Training** — Train machine learning classification models.
7. **Model Evaluation** — Evaluate predictive performance using appropriate classification metrics.
8. **Churn Prediction** — Predict which customers are at risk of churning.
9. **Revenue-at-Risk Calculation** — Calculate the monthly charges associated with predicted at-risk customers.
10. **Dashboard Development** — Present metrics and visualizations through Streamlit.

## 🛠️ Technologies Used

| Technology       | Purpose                                                 |
| ---------------- | ------------------------------------------------------- |
| Python           | Programming and data analysis                           |
| Pandas           | Data manipulation and cleaning                          |
| NumPy            | Numerical computations                                  |
| Matplotlib       | Data visualization                                      |
| Seaborn          | Exploratory data analysis and statistical visualization |
| Scikit-learn     | Data preprocessing, model training, and evaluation      |
| Streamlit        | Interactive web application                             |
| Jupyter Notebook | Data exploration and model experimentation              |







## 🚀 Getting Started

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository's actual URL.

### 2. Navigate to the Project Directory

```bash
cd Customer-Churn-Prediction
```

### 3. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment.

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📊 Dataset

This project uses the Telco Customer Churn dataset, which contains customer information, service subscriptions, account details, monthly charges, and churn status.

Important features may include:

| Feature        | Description                                               |
| -------------- | --------------------------------------------------------- |
| CustomerID     | Unique customer identifier                                |
| Tenure         | Number of months the customer has stayed with the company |
| Contract       | Customer's contract type                                  |
| PaymentMethod  | Method used to pay for the service                        |
| MonthlyCharges | Monthly amount charged to the customer                    |
| TotalCharges   | Total amount charged over the customer's tenure           |
| Churn          | Whether the customer left the company                     |


## 📏 Model Evaluation

The classification models should be evaluated using suitable metrics, such as:

* **Accuracy:** Overall proportion of correct predictions.
* **Precision:** Proportion of predicted churners who actually churned.
* **Recall:** Proportion of actual churners correctly identified.
* **F1-Score:** Balance between precision and recall.
* **Confusion Matrix:** Breakdown of correct and incorrect predictions.
* **ROC-AUC:** Ability to distinguish between churners and non-churners across classification thresholds.

For customer churn prediction, recall and precision are particularly important because businesses need to identify potential churners while avoiding excessive false alarms.

We got 82% Recall score here.

## 💡 Potential Business Value

The project demonstrates how machine learning predictions can support business decision-making.

Potential applications include:

* Prioritizing customers for retention campaigns.
* Identifying customer segments with greater revenue exposure.
* Understanding patterns associated with customer churn.
* Supporting data-driven customer retention strategies.
* Monitoring estimated recurring revenue at risk.

The dashboard is intended to support analysis and decision-making, not to guarantee that customers will churn or that a specific amount of revenue will be lost.



## 👨‍💻 Author

**Aman Sharma**

BCA Graduate | MCA (Data Science) Student

Interested in Data Science, Machine Learning, and Data Analytics.

---

⭐ If you find this project interesting, feel free to explore the repository and its implementation.
