import streamlit as st

# Page setup
st.set_page_config(page_title="Tip Calculator", page_icon="💰")
st.title("💰 Tip Calculator")

# Input widgets
bill_amount = st.number_input("Total Bill Amount ($)", min_value=0.01, value=50.00)
tip_percentage = st.slider("Select tip percentage", min_value=0, max_value=30, value=15)
num_people = st.number_input("Number of People", min_value=1, value=2)

# Display results
st.metric(label="Per Person", value=f"${amount_per_person:.2f}")
st.success(f"Each person should pay: ${amount_per_person:.2f}")
