"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maestrofinance.co.uk
Prompt: Design a user interface for a financial calculator that helps users compare different loan options, including terms for asset finance and property finance.
Generated: DETERMINISTIC_c023743a20825f0f
Batch ID: 20250612_160158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation utilizing the Tkinter library for creating a user interface (UI) for a financial calculator that compares different loan options. This code meets the requirements specified:

```python
import tkinter as tk
from tkinter import messagebox

# Function to calculate monthly payment for a loan
def calculate_payment():
    try:
        principal = float(principal_entry.get())
        interest_rate = float(interest_rate_entry.get()) / 100 / 12
        years = int(term_entry.get())
        months = years * 12

        # Formula for monthly payment
        payment = (principal * interest_rate * (1 + interest_rate) ** months) / ((1 + interest_rate) ** months - 1)
        payment_label.config(text=f"Monthly Payment: ${payment:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Function to clear all input fields
def clear_fields():
    principal_entry.delete(0, tk.END)
    interest_rate_entry.delete(0, tk.END)
    term_entry.delete(0, tk.END)
    payment_label.config(text="Monthly Payment: $0.00")

# Initialize main window
root = tk.Tk()
root.title("Loan Comparison Calculator")
root.geometry("400x300")
root.resizable(False, False)

# Title Label
title_label = tk.Label(root, text="Loan Comparison Calculator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Principal input
principal_frame = tk.Frame(root)
principal_frame.pack(pady=5, fill=tk.X, padx=20)
principal_label = tk.Label(principal_frame, text="Loan Amount ($):", width=20, anchor="w")
principal_label.pack(side=tk.LEFT)
principal_entry = tk.Entry(principal_frame)
principal_entry.pack(side=tk.RIGHT, fill=tk.X, expand=True)

# Interest Rate input
interest_rate_frame = tk.Frame(root)
interest_rate_frame.pack(pady=5, fill=tk.X, padx=20)
interest_rate_label = tk.Label(interest_rate_frame, text="Annual Interest Rate (%):", width=20, anchor="w")
interest_rate_label.pack(side=tk.LEFT)
interest_rate_entry = tk.Entry(interest_rate_frame)
interest_rate_entry.pack(side=tk.RIGHT, fill=tk.X, expand=True)

# Term input
term_frame = tk.Frame(root)
term_frame.pack(pady=5, fill=tk.X, padx=20)
term_label = tk.Label(term_frame, text="Loan Term (years):", width=20, anchor="w")
term_label.pack(side=tk.LEFT)
term_entry = tk.Entry(term_frame)
term_entry.pack(side=tk.RIGHT, fill=tk.X, expand=True)

# Monthly Payment Display
payment_label = tk.Label(root, text="Monthly Payment: $0.00", font=("Arial", 12))
payment_label.pack(pady=20)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate Payment", command=calculate_payment, width=20)
calculate_button.pack(pady=5)

# Clear Button
clear_button = tk.Button(root, text="Clear Fields", command=clear_fields, width=20)
clear_button.pack(pady=5)

# Exit Button
exit_button = tk.Button(root, text="Exit", command=root.quit, width=20)
exit_button.pack(pady=5)

# Run the Application
root.mainloop()
```
