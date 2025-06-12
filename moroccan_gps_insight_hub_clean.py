
import streamlit as st
import pandas as pd
import plotly.express as px
import os
import os

st.set_page_config(page_title="Moroccan GPS Insight Hub", layout="centered")

# App Config
# Moroccan FA Logo + Custom Title
st.image("https://upload.wikimedia.org/wikipedia/fr/thumb/6/69/Logo_F%C3%A9d%C3%A9ration_Royale_Marocaine_Football.svg/1507px-Logo_F%C3%A9d%C3%A9ration_Royale_Marocaine_Football.svg.png",
    width=120)

st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <img src="https://ams.catapultsports.com/hc/theming_assets/01HZH068BKDCVXFNAEF6XZX86Q" width="120"/>
        
        <h2 style="flex-grow: 1; text-align: center; color: #d32f2f; margin: 0;">
            Moroccan GPS Insight Hub
        </h2>

        <img src="https://upload.wikimedia.org/wikipedia/fr/thumb/6/69/Logo_F%C3%A9d%C3%A9ration_Royale_Marocaine_Football.svg/1507px-Logo_F%C3%A9d%C3%A9ration_Royale_Marocaine_Football.svg.png" width="100"/>
    </div>
    <hr style="margin-top: 10px;">
""", unsafe_allow_html=True)

st.markdown("Upload your Catapult GPS data, select two metrics and get your insights.")

# Upload
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"]) 

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Display preview
    st.markdown("<h3 style='color:#2e7d32;'>📄 Data Preview</h3>", unsafe_allow_html=True)
    st.dataframe(df.head())

    # Detect numeric columns
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    st.markdown("<h3 style='color:#2e7d32;'>📊 Select Metrics</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        x_axis = st.selectbox("X-axis", numeric_cols)
    with col2:
        y_axis = st.selectbox("Y-axis", numeric_cols)

    # Check if optional columns exist
    hover_col = 'Name' if 'Name' in df.columns else None
    color_col = 'Equipe' if 'Equipe' in df.columns else None

    # Plot
    fig = px.scatter(
        df,
        x=x_axis,
        y=y_axis,
        hover_name=hover_col,
        color=color_col,
        title=f"{y_axis} vs {x_axis}"
    )
    st.plotly_chart(fig, use_container_width=True)
