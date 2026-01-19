import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("Data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Title
st.title("Customer Churn Analysis Dashboard")

# Dropdown filter
contract = st.selectbox("Select Contract Type", df['Contract'].unique())

# Filter data
filtered = df[df['Contract'] == contract]

# KPI
churn_rate = (filtered['Churn'] == 'Yes').mean() * 100
st.metric("Churn Rate (%)", f"{churn_rate:.2f}")

# Chart
st.bar_chart(filtered['Churn'].value_counts())
