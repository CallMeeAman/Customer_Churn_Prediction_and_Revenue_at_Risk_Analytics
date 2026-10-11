import streamlit as st
import pickle
import pandas as pd
import numpy as np
import imblearn





# This is the Churn Prediction Code



st.set_page_config(
    page_title="Churn Prediction",
)

with open("new_input.pkl", "rb") as file:
   df = pickle.load(file)

with open("new_model.pkl", "rb") as file:
   model = pickle.load(file)


st.header("Enter your inputs")

tenure = float(st.slider("Tenure in months", 1, 80))
monthly_charges = float(st.slider("Monthly Charges in $", 1, 120))
total_charges = tenure * monthly_charges
phone_service = st.selectbox("Phone Service",['Yes','No'])
contact_service = st.selectbox("Contract Service",['Month-to-month','One year','Two year'])

if st.button("Predict", type="primary"):
    data = [[tenure, monthly_charges, total_charges, phone_service, contact_service]]
    columns = ['Tenure', 'Monthlycharges', 'Totalcharges', 'Phoneservice', 'Contract']

    one_df = pd.DataFrame(data, columns=columns)

    prediction = model.predict(one_df)
    probability = model.predict_proba(one_df)

    churn_probability = probability[0][1]
    revenue_at_risk = churn_probability * monthly_charges

    if prediction[0] == 0:
        st.subheader("The Customer will not Churn ✅")
    else:
        st.subheader("The Customer will Churn ⚠️")

    st.metric(
        label="Churn Probability",
        value=f"{churn_probability:.2%}"
    )

    st.metric(
        label="Expected Monthly Revenue at Risk",
        value=f"${revenue_at_risk:.2f}"
    )
