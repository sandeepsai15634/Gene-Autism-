import streamlit as st
import pandas as pd
import joblib

# Load the optimized Random Forest model
model = joblib.load("rf_autism_model.pkl")

# App Configuration
st.set_page_config(page_title="Autism Gene Predictor", layout="centered")
st.title("🧬 Autism Genetic Score Prediction App")
st.write("Enter the gene features to predict if the case is **Syndromic (1)** or **Non-Syndromic (0)**.")

# Encoded options (replace with actual values if available)
genetic_category_options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
 # Placeholder: adjust as per label encoder

# Input fields for the three selected features
st.header("🔍 Input Features")

genetic_category = st.selectbox("Genetic Category (encoded)", genetic_category_options)
gene_score = st.slider("Gene Score", min_value=0.0, max_value=1.0, step=0.01, value=0.5)
number_of_reports = st.number_input("Number of Reports", min_value=0, value=1)

# Prepare input for prediction
input_data = pd.DataFrame([[
    genetic_category, number_of_reports, gene_score
]], columns=['genetic-category', 'number-of-reports', 'gene-score'])

# Predict and display result
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    result = "🟢 Syndromic (1)" if round(prediction) == 1 else "🔵 Non-Syndromic (0)"
    st.success(f"**Prediction Result:** {result}")
