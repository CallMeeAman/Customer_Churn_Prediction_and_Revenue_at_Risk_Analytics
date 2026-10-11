import streamlit as st
import pickle
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Churn Analysis", layout="wide")


# -------------------------------
# LOAD DATASET AND MODEL
# -------------------------------

with open("new_input.pkl", "rb") as file:
    df = pickle.load(file)

with open("new_model.pkl", "rb") as file:
    model = pickle.load(file)


# -------------------------------
# PREDICTIONS AND REVENUE AT RISK
# -------------------------------

data = df.copy()

predictions = model.predict(data)
probabilities = model.predict_proba(data)

# Find the probability column corresponding to class 1 (Churn)
churn_index = list(model.classes_).index(1)

data["Churn_Probability"] = probabilities[:, churn_index]
data["Predicted_Churn"] = predictions

# Expected monthly revenue at risk for each customer
data["Revenue_at_Risk"] = (
    data["Churn_Probability"] * data["Monthlycharges"]
)

# Create readable prediction labels
data["Churn_Status"] = data["Predicted_Churn"].map({
    0: "No Churn",
    1: "Churn"
})


# -------------------------------
# PAGE HEADER
# -------------------------------

st.title("Customer Churn Analysis")

st.write(
    "Analyze customer churn predictions, estimated monthly revenue at risk, "
    "and contract types contributing to churn risk."
)


# -------------------------------
# KEY METRICS
# -------------------------------

total_revenue_at_risk = data["Revenue_at_Risk"].sum()

predicted_churn_customers = (
    data["Predicted_Churn"] == 1
).sum()

total_customers = len(data)

predicted_churn_rate = (
    predicted_churn_customers / total_customers * 100
    if total_customers > 0 else 0
)

total_monthly_revenue = data["Monthlycharges"].sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Monthly Revenue at Risk",
    f"${total_revenue_at_risk:,.2f}"
)

col2.metric(
    "Customers Predicted to Churn",
    f"{predicted_churn_customers:,}"
)

col3.metric(
    "Predicted Churn Rate",
    f"{predicted_churn_rate:.2f}%"
)

col4.metric(
    "Total Monthly Revenue",
    f"${total_monthly_revenue:,.2f}"
)

st.divider()


# -------------------------------
# PLOTLY CONFIGURATION
# -------------------------------

# Disable chart interactions and hide the toolbar
chart_config = {
    "scrollZoom": False,
    "displayModeBar": False,
    "staticPlot": True
}


# Common formatting for larger, bolder graph labels
def style_chart(fig):
    fig.update_layout(
        font=dict(
            size=15,
            family="Arial"
        ),
        xaxis=dict(
            tickfont=dict(
                size=14,
                family="Arial Black"
            ),
            title_font=dict(size=16, family="Arial Black")
        ),
        yaxis=dict(
            tickfont=dict(
                size=14,
                family="Arial Black"
            ),
            title_font=dict(size=16, family="Arial Black")
        ),
        title_font=dict(
            size=21,
            family="Arial Black"
        ),
        dragmode=False
    )

    return fig


# -------------------------------
# REVENUE AT RISK BY CONTRACT
# -------------------------------

st.subheader("Revenue at Risk by Contract Type")

risk_by_contract = (
    data.groupby("Contract")["Revenue_at_Risk"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig1 = px.bar(
    risk_by_contract,
    x="Contract",
    y="Revenue_at_Risk",
    labels={
        "Contract": "Contract Type",
        "Revenue_at_Risk": "Revenue at Risk ($)"
    },
    text="Revenue_at_Risk"
)

fig1.update_traces(
    texttemplate="$%{text:,.2f}",
    textposition="outside",
    textfont=dict(
        size=16,
        family="Arial Black"
    ),
    cliponaxis=False
)

fig1 = style_chart(fig1)

st.plotly_chart(
    fig1,
    use_container_width=True,
    config=chart_config
)

st.caption(
    "Shows the total estimated monthly revenue at risk for customers "
    "within each contract type."
)


# -------------------------------
# PREDICTED CHURN DISTRIBUTION
# -------------------------------

st.subheader("Predicted Churn vs. No Churn")

churn_counts = (
    data["Churn_Status"]
    .value_counts()
    .reindex(["Churn", "No Churn"], fill_value=0)
    .rename_axis("Churn_Status")
    .reset_index(name="Customers")
)

fig2 = px.bar(
    churn_counts,
    x="Churn_Status",
    y="Customers",
    labels={
        "Churn_Status": "Churn Status",
        "Customers": "Number of Customers"
    },
    text="Customers"
)

fig2.update_traces(
    textposition="outside",
    textfont=dict(
        size=17,
        family="Arial Black"
    ),
    cliponaxis=False
)

fig2 = style_chart(fig2)

st.plotly_chart(
    fig2,
    use_container_width=True,
    config=chart_config
)


# -------------------------------
# TOP 10 CUSTOMERS BY REVENUE AT RISK
# -------------------------------

st.subheader("Top 10 Customers by Revenue at Risk")

# Preserve original row numbers before sorting
top_customers = (
    data.assign(Customer_Row=data.index)
    .sort_values("Revenue_at_Risk", ascending=False)
    .head(10)
    .copy()
)

# Use actual customer IDs if available
if "customerID" in top_customers.columns:
    top_customers["Customer"] = (
        top_customers["customerID"].astype(str)
    )

elif "CustomerID" in top_customers.columns:
    top_customers["Customer"] = (
        top_customers["CustomerID"].astype(str)
    )

else:
    top_customers["Customer"] = (
        "Customer " +
        (top_customers["Customer_Row"] + 1).astype(str)
    )

# Sort for horizontal bar chart
top_customers_chart = top_customers.sort_values(
    "Revenue_at_Risk",
    ascending=True
)

fig3 = px.bar(
    top_customers_chart,
    x="Revenue_at_Risk",
    y="Customer",
    orientation="h",
    labels={
        "Customer": "Customer",
        "Revenue_at_Risk": "Revenue at Risk ($)"
    },
    text="Revenue_at_Risk"
)

fig3.update_traces(
    texttemplate="$%{x:,.2f}",
    textposition="outside",
    textfont=dict(
        size=16,
        family="Arial Black"
    ),
    cliponaxis=False
)

fig3 = style_chart(fig3)

# Make customer names larger and bolder
fig3.update_layout(
    yaxis=dict(
        tickfont=dict(
            size=14,
            family="Arial Black"
        ),
        title_font=dict(size=16, family="Arial Black")
    ),
    margin=dict(l=130, r=100, t=60, b=60)
)

st.plotly_chart(
    fig3,
    use_container_width=True,
    config=chart_config
)


# -------------------------------
# TOP 10 CUSTOMERS TABLE
# -------------------------------

display_columns = [
    "Contract",
    "Monthlycharges",
    "Churn_Probability",
    "Revenue_at_Risk"
]

st.dataframe(
    top_customers[display_columns].rename(columns={
        "Contract": "Contract Type",
        "Monthlycharges": "Monthly Charges ($)",
        "Churn_Probability": "Churn Probability",
        "Revenue_at_Risk": "Expected Monthly Revenue at Risk ($)"
    }).style.format({
        "Monthly Charges ($)": "${:.2f}",
        "Churn Probability": "{:.2%}",
        "Expected Monthly Revenue at Risk ($)": "${:.2f}"
    }),
    use_container_width=True
)


# -------------------------------
# CHURN PROBABILITY DISTRIBUTION
# -------------------------------

st.subheader("Customer Churn Probability Distribution")

data["Risk_Band"] = pd.cut(
    data["Churn_Probability"],
    bins=[0, 0.25, 0.50, 0.75, 1.0],
    labels=[
        "0–25%",
        "25–50%",
        "50–75%",
        "75–100%"
    ],
    include_lowest=True
)

risk_distribution = (
    data["Risk_Band"]
    .value_counts(sort=False)
    .rename_axis("Risk_Band")
    .reset_index(name="Customers")
)

fig4 = px.bar(
    risk_distribution,
    x="Risk_Band",
    y="Customers",
    labels={
        "Risk_Band": "Churn Probability",
        "Customers": "Number of Customers"
    },
    text="Customers",
    category_orders={
        "Risk_Band": [
            "0–25%",
            "25–50%",
            "50–75%",
            "75–100%"
        ]
    }
)

fig4.update_traces(
    textposition="outside",
    textfont=dict(
        size=17,
        family="Arial Black"
    ),
    cliponaxis=False
)

fig4 = style_chart(fig4)

st.plotly_chart(
    fig4,
    use_container_width=True,
    config=chart_config
)

st.caption(
    "Shows how many customers fall into each estimated churn-probability range."
)

