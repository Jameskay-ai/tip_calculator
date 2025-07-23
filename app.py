# Core components for Streamnlit / pandas / numpy
import streamlit as st
import pandas as pd
import numpy as np

# Sidebar text display
st.markdown("Explanation:")
with st.sidebar:
    # Button to redirect to Python Landing page
    st.caption("To view other projects click here")
    with st.sidebar:
    st.markdown(
        """
        <a href="https://jameskay-ai.github.io/" target="_blank">
            <button style="background-color:#007BFF; color:white; padding:10px; border:none; border-radius:5px;">
                Back to main
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )
    st.divider()
    st.markdown("Category: Basic Level")
    st.markdown("""
    ## **Key Concepts Covered:**
    - ##### Standard I/O operations (**print()**), **input()**)
    - ##### Type casting (**float**, **int**)                
    - ##### Arithmetic operations and logic
    - ##### Variable assignment
    - ##### Output formatting with **round()** and f-strings
    """)   

    st.markdown("""
    ## **Detailed Explanation**
    Understanding the Python Code:

    ### *Basic Functions:**
    - ##### print() - Displays text to the screen
    - ##### input() - Gets text input from the user
    - ##### float() - Converts text to a decimal number
    - ##### int() - Converts text to a whole number
    - ##### round() - Rounds a number to specific decimal places
    """)

    st.markdown("""       
    ### **Variables:**
    - ##### bill - Stores the total bill amount
    - ##### tip - Stores the tip percentage
    - ##### people - Stores number of people splitting the bill
    - ##### Variables hold values that can be used later in calculations
    """)  
                
    st.markdown("""
    ### **Math Operations:**
    - ##### / - Division (tip / 100 converts percentage to decimal)
    - ##### * - Multiplication (bill * tip_percent calculates tip amount)
    - ##### + - Addition (bill + tip gives total with tip)
    - ##### = - Assignment (stores a value in a variable)
    """)  

    st.markdown("""
    ### **String Formatting:**

    - ##### f"text {variable}" - Inserts variable values into text
    - ##### Example: f"Each person pays: ${final_amount}" shows the calculated amount
    """)  

    st.markdown("""
    ### **Flow:**

    - ##### Get user input for bill, tip percentage, and number of people
    - ##### Convert tip percentage to decimal (15% becomes 0.15)
    - ##### Calculate tip amount by multiplying bill by tip decimal
    - ##### Add tip to original bill to get total
    - ##### Divide total by number of people
    - ##### Round to 2 decimal places for currency
    - ##### Display the final amount per person            
    """)  
                
   

# Main App display right side Interactive Portal
st.title("Welcome to the Python Porfolio")
st.subheader("💰 Restaurant Tip Calculator")
st.markdown("##### By: James Kay")
st.caption("The interactive web portal is hosted on Streamlit.io/cloud")
st.divider()

st.markdown("## Split the bill fairly with your friends, including the tip.")

# User inputs
bill_amount = st.number_input("What was the total Bill Amount ($)?", min_value=0.00, value=00.0)
tip_percentage = st.slider("What percentage tip would you like to give?", min_value=5, max_value=20, step=1, value=15)
people = st.number_input("How many people to split the bill?", min_value=2, step=1)

st.caption("Starting at 5%, tip can be increased in 1% increments.")

# Calculation
if bill_amount > 0 and people > 0:
    tip_as_percent = tip_percentage / 100
    total_tip_amount = bill_amount * tip_as_percent
    total_bill = bill_amount + total_tip_amount
    bill_per_person = total_bill / people
    final_amount = round(bill_per_person, 2)

    # Result
     
    st.markdown(f"### 💵 Each person should pay: **${final_amount:.2f}**")
else:
    st.warning("Please enter valid values for bill and number of people.")

st.divider()

with st.expander("### Show Python Code"):
    st.code("""
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
""")

st.divider()


with st.expander("### Show Streamlit Code"):
    st.code('''
        
# Core components for Streamnlit / pandas / numpy
import streamlit as st
import pandas as pd
import numpy as np

# Sidebar text display
st.markdown("Explanation:")
with st.sidebar:
    # Button to redirect to Python Landing page
    st.caption("To view other projects click here")
    primary_btn = st.button(label="Back to main")
    st.divider()
    st.markdown("Category: Basic Level")
    st.markdown("""
    ## **Key Concepts Covered:**
    - ##### Standard I/O operations (**print()**), **input()**)
    - ##### Type casting (**float**, **int**)                
    - ##### Arithmetic operations and logic
    - ##### Variable assignment
    - ##### Output formatting with **round()** and f-strings
    """)   

    st.markdown("""
    ## **Detailed Explanation**
    Understanding the Python Code:

    ### *Basic Functions:**
    - ##### print() - Displays text to the screen
    - ##### input() - Gets text input from the user
    - ##### float() - Converts text to a decimal number
    - ##### int() - Converts text to a whole number
    - ##### round() - Rounds a number to specific decimal places
    """)

    st.markdown("""       
    ### **Variables:**
    - ##### bill - Stores the total bill amount
    - ##### tip - Stores the tip percentage
    - ##### people - Stores number of people splitting the bill
    - ##### Variables hold values that can be used later in calculations
    """)  
                
    st.markdown("""
    ### **Math Operations:**
    - ##### / - Division (tip / 100 converts percentage to decimal)
    - ##### * - Multiplication (bill * tip_percent calculates tip amount)
    - ##### + - Addition (bill + tip gives total with tip)
    - ##### = - Assignment (stores a value in a variable)
    """)  

    st.markdown("""
    ### **String Formatting:**

    - ##### f"text {variable}" - Inserts variable values into text
    - ##### Example: f"Each person pays: ${final_amount}" shows the calculated amount
    """)  

    st.markdown("""
    ### **Flow:**

    - ##### Get user input for bill, tip percentage, and number of people
    - ##### Convert tip percentage to decimal (15% becomes 0.15)
    - ##### Calculate tip amount by multiplying bill by tip decimal
    - ##### Add tip to original bill to get total
    - ##### Divide total by number of people
    - ##### Round to 2 decimal places for currency
    - ##### Display the final amount per person            
    """)  
                
   

# Main App display right side Interactive Portal
st.title("Welcome to the Python Porfolio")
st.subheader("💰 Restaurant Tip Calculator")
st.markdown("##### By: James Kay")
st.caption("The interactive web portal is hosted on Streamlit.io/cloud")
st.divider()

st.markdown("## Split the bill fairly with your friends, including the tip.")

# User inputs
bill_amount = st.number_input("What was the total Bill Amount ($)?", min_value=0.00, value=00.0)
tip_percentage = st.slider("What percentage tip would you like to give?", min_value=5, max_value=20, step=1, value=15)
people = st.number_input("How many people to split the bill?", min_value=2, step=1)

st.caption("Starting at 5%, tip can be increased in 1% increments.")

# Calculation
if bill_amount > 0 and people > 0:
    tip_as_percent = tip_percentage / 100
    total_tip_amount = bill_amount * tip_as_percent
    total_bill = bill_amount + total_tip_amount
    bill_per_person = total_bill / people
    final_amount = round(bill_per_person, 2)

    # Result
     
    st.markdown(f"### 💵 Each person should pay: **${final_amount:.2f}**")
else:
    st.warning("Please enter valid values for bill and number of people.")

st.divider()

with st.expander("### Show Python Code"):
    st.code("""
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
""")

st.divider()

st.markdown("### Streamlit Code pasted here but not needed as it is already displayed")

''')
