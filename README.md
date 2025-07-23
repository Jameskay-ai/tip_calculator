# 💰 Restaurant Tip Calculator | Streamlit App

Welcome to the **Python Portfolio Project** by **James Kay** — an interactive **tip calculator** built with Streamlit, showcasing foundational Python concepts in a clean, responsive web interface.

![Streamlit UI Screenshot](https://your-screenshot-url.com) <!-- Optional: Replace or delete this line if no screenshot -->

---

## 🚀 Live Demo
Check out the deployed app here:  
👉 [Click to open on Streamlit Cloud](https://jk-tip-calculator.streamlit.app/)

---

## 📌 About the Project

This project converts a basic console-based tip calculator into a fully interactive web application using Streamlit. It includes enhanced layout and styling via custom CSS and serves as an introductory project in my Python learning path.

---

## 🔍 Features

- 🌐 **Streamlit UI** for seamless interaction
- 🧮 **Tip calculator logic**: split bills fairly
- 🎨 **Custom sidebar styling**: navy & white theme
- 📋 **Detailed code explanation** in the sidebar
- 🧠 **Concept breakdown** for beginners
- 💾 **Code preview** (original Python and Streamlit version)

---

## 🧠 Key Python Concepts Demonstrated

| Category                | Concepts Covered                                       |
|------------------------|--------------------------------------------------------|
| **Input/Output**       | `input()`, `print()`, `st.number_input()`             |
| **Type Conversion**    | `int()`, `float()`                                     |
| **Math Operations**    | Division `/`, Multiplication `*`, Addition `+`         |
| **Variables**          | `bill`, `tip`, `people`, `final_amount`                |
| **Formatting Output**  | `round()`, `f-strings`                                 |
| **UI Components**      | `st.slider`, `st.expander`, `st.code`, `st.markdown`   |
| **CSS Styling**        | Custom Streamlit layout using HTML/CSS                 |

---

## 🖼️ User Interface Preview

The UI is designed with:
- 🟦 **Navy Blue Sidebar** (white text)
- ⚪ **White Main Content** (navy blue text)
- 🎛️ Sliders and input fields for real-time calculation
- 💬 Expandable sections to view source code

---

## 🧪 How It Works

1. User inputs:
   - Total bill amount
   - Tip percentage (via slider)
   - Number of people splitting the bill
2. App calculates:
   - Tip amount
   - Total bill with tip
   - Final amount per person (rounded to 2 decimals)
3. Output:
   - Final amount each person should pay

---

## 🧾 Code Snippet (Original Python)

```python
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
