import streamlit as st

# App title
st.title("💰 Tip Calculator")

# Bill input
bill = st.number_input("Enter the bill amount (¥):", min_value=0.0, step=100.0)

# Tip % slider
tip_percent = st.slider("Select tip percentage:", 0, 50, 15)

# Calculate tip and total
tip = bill * (tip_percent / 100)
total = bill + tip

# Display results
st.markdown("---")
st.subheader("💡 Calculation Result")
st.write(f"**Tip Amount:** ¥{tip:.0f}")
st.write(f"**Total Bill:** ¥{total:.0f}")
