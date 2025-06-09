
import streamlit as st
import pandas as pd
import plotly.express as px
import os
import os

st.set_page_config(page_title="Moroccan GPS Insight Hub", layout="centered")
st.sidebar.info(f"Key detected: {'✅' if os.getenv('OPENAI_API_KEY') else '❌'}")
st.set_page_config(page_title="Moroccan GPS Insight Hub", layout="centered")

# App Config
st.title("🇲🇦 Moroccan GPS Insight Hub")
st.markdown("Upload your Catapult GPS data, select any two metrics, and get AI-generated performance insights.")

# Upload
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"]) 

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Display preview
    st.subheader("📄 Data Preview")
    st.dataframe(df.head())

    # Numeric columns only for scatter plot
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    # Dropdowns to select X and Y
    st.subheader("📊 Select Metrics for Scatter Plot")
    col1, col2 = st.columns(2)
    with col1:
        x_axis = st.selectbox("X-axis", numeric_cols)
    with col2:
        y_axis = st.selectbox("Y-axis", numeric_cols)

    # Generate Scatter Plot
    fig = px.scatter(df, x=x_axis, y=y_axis, hover_name='Name', color='Equipe', title=f"{y_axis} vs {x_axis}")
    st.plotly_chart(fig, use_container_width=True)

