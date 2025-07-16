import streamlit as st

# Page config
st.set_page_config(page_title="Tip Calculator", layout="centered")

# App title
st.title("💰 Tip Calculator")
st.markdown("Split the bill and calculate tips easily!")

# Inputs
bill = st.number_input("💵 What was the total bill? (¥)", min_value=0.0, step=100.0)
tip = st.selectbox("💡 What percentage tip would you like to give?", [10, 12, 15, 18, 20])
people = st.number_input("🧑‍🤝‍🧑 How many people to split the bill?", min_value=1, step=1)

# Calculation
if people > 0:
    tip_as_percent = tip / 100
    total_tip_amount = bill * tip_as_percent
    total_bill = bill + total_tip_amount
    bill_per_person = total_bill / people
    final_amount = round(bill_per_person, 2)

    # Results
    st.markdown("---")
    st.subheader("🧾 Result")
    st.write(f"**Each person should pay:** ¥{final_amount}")
