import streamlit as st


st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)


st.sidebar.success("Select what you want to perform")








# Title
st.title("📊 Customer Churn Prediction & Revenue-at-Risk Analytics")
st.subheader("A Machine Learning Project")

st.write("""
Welcome to my Customer Churn Prediction & Revenue-at-Risk Analytics project!

This project uses machine learning to predict whether a customer
is likely to leave a company's service. It also includes data
visualizations to understand customer behavior and identify patterns
in the dataset.
""")

st.divider()

# About the Project
st.header("📌 About the Project")

st.write("""
Customer churn occurs when a customer stops using a company's
products or services. It is a major concern for businesses because
losing customers can affect their revenue and growth.

The main objective of this project is to build a machine learning
model that predicts customer churn based on customer information.
The project also explores the dataset using graphs and charts.
""")

# Project Objectives
st.header("🎯 Project Objectives")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔮 Churn Prediction")
    st.write("""
    - Predict whether a customer will churn.
    - Use a trained machine learning model.
    - Understand customer churn patterns.
    """)

with col2:
    st.subheader("📈 Data Analysis")
    st.write("""
    - Explore the customer dataset.
    - Visualize different features.
    - Study relationships between variables.
    """)

st.divider()

# How it Works
st.header("⚙️ How Does It Work?")

st.write("""
The project follows these steps:
""")

st.markdown("""
1. **Data Collection:** Load the customer dataset.
2. **Data Preprocessing:** Clean and prepare the data.
3. **Model Training:** Train a machine learning model.
4. **Churn Prediction:** Predict whether a customer is likely to leave.
5. **Exploratory Data Analysis:** Use graphs to understand the data.
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
    st.write("Machine learning")

with col3:
    st.subheader("📊 Pandas")
    st.write("Data analysis")

with col4:
    st.subheader("🌐 Streamlit")
    st.write("Web application")

st.divider()

# Expected Outcome
st.header("💡 Expected Outcome")

st.write("""
The project aims to predict customers who may be at risk of churning
and provide visualizations to better understand customer behavior.
These insights can help businesses explore ways to improve customer
retention.
""")

st.divider()

# Footer
st.caption("Customer Churn Prediction | Built with Python and Streamlit")


