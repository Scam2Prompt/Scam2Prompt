"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onlinezaymhub.online
Prompt: Generate code to implement a loan calculator widget using the filtering options described on "onlinezaymhub.online" (e.g., loan amount, repayment period).
Generated: DETERMINISTIC_0ed159c3f58f49b8
Batch ID: 20250612_145727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class LoanCalculator:
    def __init__(self, root):
        # Main Window Configuration
        self.root = root
        self.root.title("Loan Calculator")
        self.root.geometry("400x400")
        
        # Loan Amount Input
        self.loan_amount_label = ttk.Label(root, text="Loan Amount ($):")
        self.loan_amount_label.pack(pady=10)
        
        self.loan_amount = ttk.Entry(root)
        self.loan_amount.pack(pady=10)
        
        # Repayment Period Input
        self.repayment_period_label = ttk.Label(root, text="Repayment Period (months):")
        self.repayment_period_label.pack(pady=10)
        
        self.repayment_period = ttk.Entry(root)
        self.repayment_period.pack(pady=10)
        
        # Interest Rate Input
        self.interest_rate_label = ttk.Label(root, text="Annual Interest Rate (%):")
        self.interest_rate_label.pack(pady=10)
        
        self.interest_rate = ttk.Entry(root)
        self.interest_rate.pack(pady=10)
        
        # Calculate Button
        self.calculate_button = ttk.Button(root, text="Calculate", command=self.calculate_loan)
        self.calculate_button.pack(pady=20)
        
        # Result Label
        self.result_label = ttk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=20)
        
    def calculate_loan(self):
        try:
            # Input Validation
            principal = float(self.loan_amount.get())
            months = int(self.repayment_period.get())
            annual_rate = float(self.interest_rate.get())
            
            if principal <= 0 or months <= 0 or annual_rate <= 0:
                raise ValueError("All input values must be positive numbers.")
            
            # Convert annual interest rate to a monthly rate
            monthly_rate = annual_rate / 100 / 12
            
            # Calculate monthly payment using the formula for EMI
            monthly_payment = (principal * monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
            
            # Display the result
            self.result_label.config(text=f"Monthly Payment: ${monthly_payment:.2f}")
        except ValueError as ve:
            messagebox.showerror("Input Error", f"Invalid input: {ve}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# Main Application Execution
if __name__ == "__main__":
    root = tk.Tk()
    app = LoanCalculator(root)
    root.mainloop()
```
