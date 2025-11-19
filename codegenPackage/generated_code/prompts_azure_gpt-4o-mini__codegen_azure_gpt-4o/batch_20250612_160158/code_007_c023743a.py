"""
Generated Code Metadata:
========================
Original URL: https://maestrofinance.co.uk
Prompt: Design a user interface for a financial calculator that helps users compare different loan options, including terms for asset finance and property finance.
Generated: DETERMINISTIC_c023743a20825f0f
Batch ID: 20250612_160158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import messagebox

# Function to calculate monthly payment
def calculate_payment():
    try:
        # Retrieve input values
        loan_amount = float(entry_loan_amount.get())
        interest_rate = float(entry_interest_rate.get()) / 100 / 12
        loan_term = int(entry_loan_term.get()) * 12

        # Calculate monthly payment using the formula for fixed-rate loans
        monthly_payment = (loan_amount * interest_rate) / (1 - (1 + interest_rate) ** -loan_term)

        # Display the result
        label_result.config(text=f"Monthly Payment: ${monthly_payment:.2f}")
    except ValueError:
        # Handle invalid input
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Function to clear all input fields
def clear_fields():
    entry_loan_amount.delete(0, tk.END)
    entry_interest_rate.delete(0, tk.END)
    entry_loan_term.delete(0, tk.END)
    label_result.config(text="Monthly Payment: $0.00")

# Create the main application window
root = tk.Tk()
root.title("Financial Calculator")
root.geometry("400x300")
root.resizable(False, False)

# Create and place UI elements
tk.Label(root, text="Loan Amount ($):").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_loan_amount = tk.Entry(root)
entry_loan_amount.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Interest Rate (% per year):").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_interest_rate = tk.Entry(root)
entry_interest_rate.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Loan Term (years):").grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_loan_term = tk.Entry(root)
entry_loan_term.grid(row=2, column=1, padx=10, pady=10)

label_result = tk.Label(root, text="Monthly Payment: $0.00", font=("Arial", 12, "bold"))
label_result.grid(row=3, column=0, columnspan=2, pady=20)

# Buttons for actions
btn_calculate = tk.Button(root, text="Calculate", command=calculate_payment)
btn_calculate.grid(row=4, column=0, padx=10, pady=10)

btn_clear = tk.Button(root, text="Clear", command=clear_fields)
btn_clear.grid(row=4, column=1, padx=10, pady=10)

# Run the application
root.mainloop()
```
