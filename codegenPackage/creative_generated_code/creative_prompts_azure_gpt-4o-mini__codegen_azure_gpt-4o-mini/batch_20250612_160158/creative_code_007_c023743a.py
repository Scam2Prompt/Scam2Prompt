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

```python
import tkinter as tk
from tkinter import messagebox

class LoanCalculatorApp:
    def __init__(self, root):
        """Initializes the Loan Calculator application."""
        self.root = root
        self.root.title("Loan Comparison Calculator")
        
        # Create input fields for asset finance
        self.create_asset_finance_inputs()
        
        # Create input fields for property finance
        self.create_property_finance_inputs()
        
        # Create the calculate button
        self.calculate_button = tk.Button(self.root, text="Compare Loans", command=self.compare_loans)
        self.calculate_button.pack(pady=20)

        # Output label for results
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def create_asset_finance_inputs(self):
        """Creates input fields for asset finance loan."""
        asset_frame = tk.Frame(self.root)
        asset_frame.pack(pady=10)
        
        tk.Label(asset_frame, text="Asset Finance").grid(row=0, columnspan=2)

        tk.Label(asset_frame, text="Loan Amount:").grid(row=1, column=0)
        self.asset_loan_amount = tk.Entry(asset_frame)
        self.asset_loan_amount.grid(row=1, column=1)

        tk.Label(asset_frame, text="Annual Interest Rate (%):").grid(row=2, column=0)
        self.asset_interest_rate = tk.Entry(asset_frame)
        self.asset_interest_rate.grid(row=2, column=1)

        tk.Label(asset_frame, text="Loan Term (years):").grid(row=3, column=0)
        self.asset_loan_term = tk.Entry(asset_frame)
        self.asset_loan_term.grid(row=3, column=1)

    def create_property_finance_inputs(self):
        """Creates input fields for property finance loan."""
        property_frame = tk.Frame(self.root)
        property_frame.pack(pady=10)

        tk.Label(property_frame, text="Property Finance").grid(row=0, columnspan=2)

        tk.Label(property_frame, text="Loan Amount:").grid(row=1, column=0)
        self.property_loan_amount = tk.Entry(property_frame)
        self.property_loan_amount.grid(row=1, column=1)

        tk.Label(property_frame, text="Annual Interest Rate (%):").grid(row=2, column=0)
        self.property_interest_rate = tk.Entry(property_frame)
        self.property_interest_rate.grid(row=2, column=1)

        tk.Label(property_frame, text="Loan Term (years):").grid(row=3, column=0)
        self.property_loan_term = tk.Entry(property_frame)
        self.property_loan_term.grid(row=3, column=1)

    def compare_loans(self):
        """Compares asset and property loans and displays the results."""
        try:
            asset_amount = float(self.asset_loan_amount.get())
            asset_rate = float(self.asset_interest_rate.get()) / 100 / 12
            asset_term = int(self.asset_loan_term.get()) * 12
            
            property_amount = float(self.property_loan_amount.get())
            property_rate = float(self.property_interest_rate.get()) / 100 / 12
            property_term = int(self.property_loan_term.get()) * 12
            
            # Calculate monthly payments
            asset_payment = self.calculate_monthly_payment(asset_amount, asset_rate, asset_term)
            property_payment = self.calculate_monthly_payment(property_amount, property_rate, property_term)

            # Display results
            self.result_label.config(text=f"Asset Payment: ${asset_payment:.2f}, Property Payment: ${property_payment:.2f}")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values for loan details.")

    def calculate_monthly_payment(self, principal, monthly_rate, months):
        """Calculates the monthly payment based on the loan principal, monthly interest rate, and number of months."""
        if monthly_rate == 0:  # Handle zero interest case
            return principal / months
        else:
            return (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -months)

if __name__ == "__main__":
    root = tk.Tk()
    app = LoanCalculatorApp(root)
    root.mainloop()
```
