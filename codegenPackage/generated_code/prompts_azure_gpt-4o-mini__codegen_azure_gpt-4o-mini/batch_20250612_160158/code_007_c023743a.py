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

class LoanCalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Loan Comparison Calculator")

        # Labels and Entry fields for Loan Amount, Interest Rate, and Term
        self.loan_amount_label = tk.Label(master, text="Loan Amount:")
        self.loan_amount_label.grid(row=0, column=0)
        self.loan_amount_entry = tk.Entry(master)
        self.loan_amount_entry.grid(row=0, column=1)

        self.interest_rate_label = tk.Label(master, text="Interest Rate (%):")
        self.interest_rate_label.grid(row=1, column=0)
        self.interest_rate_entry = tk.Entry(master)
        self.interest_rate_entry.grid(row=1, column=1)

        self.term_label = tk.Label(master, text="Term (Years):")
        self.term_label.grid(row=2, column=0)
        self.term_entry = tk.Entry(master)
        self.term_entry.grid(row=2, column=1)

        # Buttons for calculating and clearing
        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate_loan)
        self.calculate_button.grid(row=3, column=0)

        self.clear_button = tk.Button(master, text="Clear", command=self.clear_fields)
        self.clear_button.grid(row=3, column=1)

        # Result display
        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=4, columnspan=2)

    def calculate_loan(self):
        """Calculate monthly payment and total payment for the loan."""
        try:
            # Retrieve and validate input values
            loan_amount = float(self.loan_amount_entry.get())
            interest_rate = float(self.interest_rate_entry.get()) / 100 / 12  # Monthly interest rate
            term_years = int(self.term_entry.get())
            term_months = term_years * 12

            # Calculate monthly payment using the formula for an annuity
            if interest_rate == 0:
                monthly_payment = loan_amount / term_months
            else:
                monthly_payment = (loan_amount * interest_rate) / (1 - (1 + interest_rate) ** -term_months)

            total_payment = monthly_payment * term_months

            # Display results
            self.result_label.config(text=f"Monthly Payment: ${monthly_payment:.2f}, Total Payment: ${total_payment:.2f}")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values for loan amount, interest rate, and term.")

    def clear_fields(self):
        """Clear all input fields and result display."""
        self.loan_amount_entry.delete(0, tk.END)
        self.interest_rate_entry.delete(0, tk.END)
        self.term_entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoanCalculatorApp(root)
    root.mainloop()
```
