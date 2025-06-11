
import streamlit as st
import pandas as pd
import plotly.express as px
import os
import os

st.set_page_config(page_title="Moroccan GPS Insight Hub", layout="centered")

# App Config
# Moroccan FA Logo + Custom Title
st.image("https://i.imgur.com/XRWKn7V.png", width=100)

st.markdown("""
    <h1 style='text-align: center; color: #d32f2f;'> Moroccan GPS Insight Hub</h1>
    <h4 style='text-align: center; color: #444;'>Upload Catapult GPS data and get clear performance visuals</h4>
    <hr>
""", unsafe_allow_html=True)
st.markdown("Upload your Catapult GPS data, select any two metrics, and get AI-generated performance insights.")

# Upload
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"]) 

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Display preview
    st.markdown("<h3 style='color:#2e7d32;'>📄 Data Preview</h3>", unsafe_allow_html=True)
    st.dataframe(df.head())

    # Numeric columns only for scatter plot
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    # Dropdowns to select X and Y
    st.markdown("<h3 style='color:#2e7d32;'>📊 Select Metrics</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        x_axis = st.selectbox("X-axis", numeric_cols)
    with col2:
        y_axis = st.selectbox("Y-axis", numeric_cols)

    # Generate Scatter Plot
    fig = px.scatter(df, x=x_axis, y=y_axis, hover_name='Name', color='Equipe', title=f"{y_axis} vs {x_axis}")
    st.plotly_chart(fig, use_container_width=True)


    st.markdown("""
    <hr>
    <div style='text-align: center; color: grey; font-size: 13px;'>
        Built by Amine Azzouzi – All rights reserved © 2025
    </div>
""", unsafe_allow_html=True)


