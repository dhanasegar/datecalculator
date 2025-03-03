import streamlit as st
from datetime import datetime, timedelta

# Function to calculate remainder dates
def calculate_remainders(input_date):
    remainder1 = input_date + timedelta(days=10)
    remainder2 = remainder1 + timedelta(days=10)
    remainder3 = remainder2 + timedelta(days=10)
    return remainder1, remainder2, remainder3

# Apply Custom Styles using Markdown
st.markdown(
    """
    <style>
        body {
            background-color: #f4f4f4;
        }
        .title {
            text-align: center;
            color: #4CAF50;
            font-size: 28px;
            font-weight: bold;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            font-size: 16px;
            padding: 10px 20px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .remainder-box {
            padding: 10px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            margin: 10px 0;
            font-size: 18px;
            color: black; /* Add black text color */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# App Title
st.markdown("<p class='title'>Date Remainder Calculator</p>", unsafe_allow_html=True)

# Date Input
input_date = st.date_input("Select a date:", format="DD/MM/YYYY")

# Submit Button
if st.button("Submit"):
    remainder1, remainder2, remainder3 = calculate_remainders(input_date)
    
    st.markdown(f"<div class='remainder-box'><b>Remainder Date 1:</b> {remainder1.strftime('%d/%m/%Y')}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='remainder-box'><b>Remainder Date 2:</b> {remainder2.strftime('%d/%m/%Y')}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='remainder-box'><b>Remainder Date 3:</b> {remainder3.strftime('%d/%m/%Y')}</div>", unsafe_allow_html=True)