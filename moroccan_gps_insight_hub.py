
import streamlit as st
import pandas as pd
import plotly.express as px
import openai
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

    # AI Interpretation
    st.subheader("🤖 AI Insight")
    openai.api_key = os.getenv("OPENAI_API_KEY")

    if openai.api_key:
        prompt = f"""
        Analyze the relationship between '{x_axis}' and '{y_axis}' from GPS data in a football context. 
        Mention what it means if values are high/low, suggest performance implications, and give possible reasons for outliers.
        """

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200
            )
            insight = response.choices[0].message.content
            st.markdown(insight)
        except Exception as e:
            st.warning("Could not load AI interpretation. Check API key or try again later.")
    else:
        st.info("AI insight requires an OpenAI API Key. Set it as 'OPENAI_API_KEY' in environment variables.")
