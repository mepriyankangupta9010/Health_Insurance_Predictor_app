import streamlit as st
from prediction_helper import predict
from PIL import Image

# Page config
st.set_page_config(page_title="🏥 Health Insurance Predictor", layout="wide")

# Page title
st.markdown("""
    <h1 style='text-align: center; font-size: 48px; font-weight: bold; color: #1A237E;'>
        🏥 Health Insurance Predictor
    </h1>
""", unsafe_allow_html=True)

# Background gradient
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #E8F5E9, #FFF3E0);
    }
    input, select {
        font-size: 16px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Category options
categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Married', 'Unmarried'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer'],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High Blood Pressure', 'Diabetes & High BP',
        'Thyroid', 'Heart Disease', 'BP & Heart Disease', 'Diabetes & Thyroid',
        'Diabetes & Heart Disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# Input section header
st.markdown("<h2 style='text-align:center; color:#C62828;'>📋 Enter Your Details</h2>", unsafe_allow_html=True)

# Input layout: 3 columns
col1, col2, col3 = st.columns(3)

# Column 1
with col1:
    age = st.number_input("🎂 Age", min_value=18, max_value=100, value=30, step=1)
    gender = st.selectbox("⚧️ Gender", categorical_options['Gender'])
    bmi_category = st.selectbox("⚖️ BMI Category", categorical_options['BMI Category'])
    smoking_status = st.selectbox("🚬 Smoking Status", categorical_options['Smoking Status'])

# Column 2
with col2:
    income_lakhs = st.number_input("💰 Income (Lakhs)", min_value=0.0, max_value=200.0, value=10.0, step=0.5)
    number_of_dependants = st.number_input("👨‍👩‍👦 Number of Dependants", min_value=0, max_value=20, step=1)
    employment_status = st.selectbox("💼 Employment Status", categorical_options['Employment Status'])
    genetical_risk = st.number_input("🧬 Genetical Risk (0-5)", min_value=0, max_value=5, value=2, step=1)

# Column 3
with col3:
    marital_status = st.selectbox("💍 Marital Status", categorical_options['Marital Status'])
    region = st.selectbox("🌎 Region", categorical_options['Region'])
    medical_history = st.selectbox("🏥 Medical History", categorical_options['Medical History'])
    insurance_plan = st.selectbox("📜 Insurance Plan", categorical_options['Insurance Plan'])

# Collect inputs
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# Prediction Section
st.markdown('<h2 style="text-align:center; color:#C62828;">🔮 Prediction</h2>', unsafe_allow_html=True)

if st.button("🎯 Predict Insurance Cost"):
    prediction = predict(input_dict)

    try:
        formatted_prediction = f"{float(prediction):,.2f} $"
    except:
        formatted_prediction = str(prediction)

    st.markdown(f"""
        <div style="text-align:center; background:linear-gradient(to right, #43A047, #1B5E20); color:white;
        padding: 15px; font-size: 22px; font-weight: bold; border-radius: 10px; margin-top: 25px;">
            💰 Predicted Insurance Cost: {formatted_prediction}
        </div>
    """, unsafe_allow_html=True)