print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")

def calculate_tip(bill_amount, tip_percentage, num_people):
    tip_as_percent = tip_percentage / 100
    total_tip_amount = bill_amount * tip_as_percent
    total_bill = bill_amount + total_tip_amount
    bill_per_person = total_bill / people
    final_amount = round(bill_per_person, 2)
    
    return {
        'original_bill': bill_amount,
        'tip_percentage': tip_percentage,
        'tip_amount': round(total_tip_amount, 2),
        'total_bill': round(total_bill, 2),
        'num_people': num_people,
        'amount_per_person': final_amount
    }

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
