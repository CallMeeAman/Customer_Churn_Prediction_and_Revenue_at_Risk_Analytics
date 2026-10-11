import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

# This is the visualization code






st.set_page_config(
    page_title="Analysis Demo",
)

with open("new_input.pkl", "rb") as file:
   df = pickle.load(file)

st.subheader("Visualize")


features = [
    'Tenure',
    'Monthlycharges',
    'Totalcharges',
    'Phoneservice',
    'Contract'
]

col1, col2 = st.columns(2)

with col1:
    option1 = st.selectbox("Select Feature 1", features)

with col2:
    option2 = st.selectbox("Select Feature 2", features)

if st.button("Show Analysis", type="primary"):


    if option1 == option2:
        st.warning("Please select two different features.")
    else:

        numerical_cols = ['Tenure', 'Monthlycharges', 'Totalcharges']

        is_num1 = option1 in numerical_cols
        is_num2 = option2 in numerical_cols

        st.header("1. Univariate Analysis")

        col1, col2 = st.columns(2)


        with col1:
            st.subheader(f"Distribution of {option1}")
            fig, ax = plt.subplots(figsize=(6, 4))

            if is_num1:
                sns.histplot(data=df, x=option1, kde=True, ax=ax)
            else:
                sns.countplot(data=df, x=option1, ax=ax)
                ax.tick_params(axis='x', rotation=30)

            st.pyplot(fig)
            plt.close(fig)


        with col2:
            st.subheader(f"Distribution of {option2}")
            fig, ax = plt.subplots(figsize=(6, 4))

            if is_num2:
                sns.histplot(data=df, x=option2, kde=True, ax=ax)
            else:
                sns.countplot(data=df, x=option2, ax=ax)
                ax.tick_params(axis='x', rotation=30)

            st.pyplot(fig)
            plt.close(fig)

        st.header("2. Bivariate Analysis")

        fig, ax = plt.subplots(figsize=(8, 5))

        if is_num1 and is_num2:

            sns.scatterplot(
                data=df, x=option1, y=option2, ax=ax, alpha=0.5
            )

        elif not is_num1 and not is_num2:

            cross_tab = pd.crosstab(df[option1], df[option2])
            sns.heatmap(cross_tab, annot=True, fmt='d', cmap='Blues', ax=ax)

        elif is_num1 and not is_num2:

            sns.boxplot(
                data=df, x=option2, y=option1, ax=ax
            )
            ax.tick_params(axis='x', rotation=30)

        else:

            sns.boxplot(
                data=df, x=option1, y=option2, ax=ax
            )
            ax.tick_params(axis='x', rotation=30)

        ax.set_title(f"{option1} vs {option2}")
        st.pyplot(fig)
        plt.close(fig)