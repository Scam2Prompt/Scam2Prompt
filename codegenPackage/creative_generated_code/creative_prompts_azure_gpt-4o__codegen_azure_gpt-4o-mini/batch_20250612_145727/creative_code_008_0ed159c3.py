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
from tkinter import messagebox

class LoanCalculator:
    def __init__(self, root):
        """Initialize the Loan Calculator widget."""
        self.root = root
        self.root.title("Loan Calculator")

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        """Create and place all widgets in the window."""
        # Loan Amount
        tk.Label(self.root, text="Loan Amount:").grid(row=0, column=0, padx=10, pady=10)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        # Repayment Period
        tk.Label(self.root, text="Repayment Period (months):").grid(row=1, column=0, padx=10, pady=10)
        self.period_entry = tk.Entry(self.root)
        self.period_entry.grid(row=1, column=1, padx=10, pady=10)

        # Interest Rate
        tk.Label(self.root, text="Interest Rate (%):").grid(row=2, column=0, padx=10, pady=10)
        self.rate_entry = tk.Entry(self.root)
        self.rate_entry.grid(row=2, column=1, padx=10, pady=10)

        # Calculate Button
        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate_loan)
        self.calculate_button.grid(row=3, columnspan=2, pady=10)

        # Result Label
        self.result_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.result_label.grid(row=4, columnspan=2, pady=10)

    def calculate_loan(self):
        """Calculate the monthly payment based on user inputs and display the result."""
        try:
            # Get user inputs
            loan_amount = float(self.amount_entry.get())
            repayment_period = int(self.period_entry.get())
            interest_rate = float(self.rate_entry.get()) / 100 / 12  # Convert annual interest rate to monthly

            # Validate inputs
            if loan_amount <= 0 or repayment_period <= 0 or interest_rate < 0:
                raise ValueError("All inputs must be positive numbers.")

            # Calculate monthly payment using the formula
            monthly_payment = (loan_amount * interest_rate) / (1 - (1 + interest_rate) ** -repayment_period)

            # Display the result
            self.result_label.config(text=f"Monthly Payment: ${monthly_payment:.2f}")

        except ValueError as ve:
            messagebox.showerror("Input Error", str(ve))
        except Exception as e:
            messagebox.showerror("Calculation Error", "An unexpected error occurred.")

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    # Initialize the loan calculator
    loan_calculator = LoanCalculator(root)
    # Run the application
    root.mainloop()
```
