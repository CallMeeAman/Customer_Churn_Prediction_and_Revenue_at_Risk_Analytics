import streamlit as st

st.set_page_config(
    page_title="Customer Churn & Revenue-at-Risk Analytics",
    page_icon="📊",
    layout="wide"
)

# Sidebar
st.sidebar.success("Select what you want to perform")

# Title
st.title("📊 Customer Churn Prediction & Revenue-at-Risk Analytics")
st.subheader("A Machine Learning & Business Intelligence Project")

st.write("""
Welcome to my Customer Churn Prediction & Revenue-at-Risk Analytics project!

This project uses machine learning to identify customers who are likely
to leave a company's services. It also estimates the monthly revenue
associated with customers at risk of churning.

By combining predictive analytics, revenue analysis, and interactive
visualizations, the project aims to help businesses understand customer
churn and make data-driven customer retention decisions.
""")

st.divider()

# About the Project
st.header("📌 About the Project")

st.write("""
Customer churn occurs when a customer stops using a company's products
or services. For subscription-based businesses, losing customers can
directly affect recurring revenue and long-term business growth.

However, identifying customers who may leave is only part of the problem.
Businesses also need to understand the potential financial impact of
customer churn.

This project addresses both challenges by building a machine learning
model to predict customer churn and analyzing the monthly revenue
associated with customers identified as being at risk.

The project uses the Telco Customer Churn dataset to explore customer
behavior, identify churn patterns, and estimate potential monthly
revenue exposure.
""")

st.divider()

# Project Objectives
st.header("🎯 Project Objectives")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔮 Customer Churn Prediction")

    st.write("""
    - Predict whether a customer is likely to churn.
    - Identify customers who may be at risk of leaving.
    - Analyze the factors associated with customer churn.
    - Evaluate the performance of the machine learning model.
    """)

with col2:
    st.subheader("💰 Revenue-at-Risk Analytics")

    st.write("""
    - Estimate the monthly revenue associated with at-risk customers.
    - Calculate total monthly revenue at risk.
    - Analyze revenue exposure across customer segments.
    - Identify high-revenue customers who may require retention efforts.
    """)

st.divider()

# Revenue-at-Risk Explanation
st.header("💰 What Is Revenue at Risk?")

st.write("""
Revenue at risk represents the monthly recurring revenue associated
with customers who are predicted to churn.

Instead of looking only at the number of customers who may leave,
this project also considers their monthly charges to estimate the
potential financial impact of customer churn.
""")

st.info("""
**Example:**

Suppose a model identifies 100 customers as being at risk of churning.
If their combined monthly charges are ₹50,000, the estimated monthly
revenue at risk is ₹50,000.

This represents the monthly revenue associated with those customers,
not a guaranteed financial loss. The actual impact depends on which
customers ultimately churn and whether the business retains them.
""")

st.write("""
The dashboard will help answer questions such as:
""")

st.markdown("""
- **How many customers are at risk of churning?**
- **What percentage of customers are predicted to churn?**
- **What is the total monthly revenue at risk?**
- **What is the average monthly charge of at-risk customers?**
- **Which customer segments contribute the most revenue at risk?**
- **Which customers have both a high churn risk and high monthly charges?**
""")

st.divider()

# Dashboard Overview
st.header("📈 Revenue-at-Risk Dashboard")

st.write("""
The interactive dashboard will present key business metrics and
visualizations to help users understand the potential impact of
customer churn.
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Key Performance Indicators")

    st.markdown("""
    - Total customers analyzed
    - Customers predicted to churn
    - Predicted churn rate
    - Total monthly revenue at risk
    - Average monthly charges of at-risk customers
    - Percentage of total monthly revenue at risk
    """)

with col2:
    st.subheader("📉 Business Insights")

    st.markdown("""
    - Churn distribution across customers
    - Monthly revenue at risk by contract type
    - Revenue exposure by payment method
    - Churn patterns across tenure groups
    - High-risk, high-revenue customer segments
    - Comparison of revenue at risk across customer groups
    """)

st.caption("""
Note: The metrics and visualizations will be calculated from the dataset
and model predictions. The figures shown in the dashboard will depend
on the data being analyzed.
""")

st.divider()

# How It Works
st.header("⚙️ How Does It Work?")

st.write("""
The project follows a complete machine learning and analytics workflow:
""")

st.markdown("""
1. **Data Collection:** Load the Telco Customer Churn dataset.
2. **Data Cleaning:** Handle missing values, correct data types, and
   prepare the dataset for analysis.
3. **Exploratory Data Analysis:** Investigate customer behavior,
   churn patterns, and relationships between variables.
4. **Feature Engineering:** Prepare relevant customer attributes for
   machine learning.
5. **Model Training:** Train and evaluate classification models to
   predict customer churn.
6. **Churn Prediction:** Identify customers predicted to be at risk.
7. **Revenue-at-Risk Calculation:** Sum the monthly charges associated
   with predicted at-risk customers.
8. **Dashboard Development:** Present business metrics and interactive
   visualizations to explore customer churn and revenue exposure.
""")

st.divider()

# Technologies Used
st.header("🛠️ Technologies Used")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("🐍 Python")
    st.write("Programming language")

with col2:
    st.subheader("🤖 Scikit-learn")
    st.write("Machine learning and model evaluation")

with col3:
    st.subheader("🐼 Pandas")
    st.write("Data cleaning and analysis")

with col4:
    st.subheader("🌐 Streamlit")
    st.write("Interactive web application")

st.divider()

# Expected Business Impact
st.header("💡 Expected Business Impact")

st.write("""
The goal is to turn customer churn predictions into actionable business
insights.

By combining churn prediction with revenue-at-risk analysis, the project
can help businesses:
""")

st.markdown("""
- Prioritize customers who are both likely to churn and contribute
  significant monthly revenue.
- Understand which customer segments have the greatest revenue exposure.
- Explore customer retention strategies based on data-driven insights.
- Monitor potential recurring revenue exposure through an interactive
  dashboard.
- Make better-informed decisions about customer retention efforts.
""")

st.warning("""
Revenue at risk is an estimate of monthly charges associated with
predicted at-risk customers. It is not a prediction of exact financial
loss, profit loss, or annual revenue loss.
""")

st.divider()

# Footer
st.caption(
    "Customer Churn Prediction & Revenue-at-Risk Analytics "
    "| Built with Python, Scikit-learn, Pandas, and Streamlit"
)

