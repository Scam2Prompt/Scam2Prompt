"""
Generated Code Metadata:
========================
Original URL: https://arbitum.cz
Prompt: Design a user interface component that allows clients to input their financial situation and receive tailored advice, similar to the personalized services offered by Arbitum Consulting.
Generated: DETERMINISTIC_0c1b3a45b383c745
Batch ID: 20250612_155131
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

class FinancialAdvisorApp:
    def __init__(self, master):
        """Initialize the main application window."""
        self.master = master
        master.title("Personalized Financial Advisor")

        # Create input fields for financial situation
        self.income_label = tk.Label(master, text="Monthly Income:")
        self.income_label.grid(row=0, column=0)
        self.income_entry = tk.Entry(master)
        self.income_entry.grid(row=0, column=1)

        self.expenses_label = tk.Label(master, text="Monthly Expenses:")
        self.expenses_label.grid(row=1, column=0)
        self.expenses_entry = tk.Entry(master)
        self.expenses_entry.grid(row=1, column=1)

        self.savings_label = tk.Label(master, text="Current Savings:")
        self.savings_label.grid(row=2, column=0)
        self.savings_entry = tk.Entry(master)
        self.savings_entry.grid(row=2, column=1)

        # Create a button to submit the financial situation
        self.submit_button = tk.Button(master, text="Get Advice", command=self.get_advice)
        self.submit_button.grid(row=3, columnspan=2)

        # Create a label to display advice
        self.advice_label = tk.Label(master, text="", wraplength=300)
        self.advice_label.grid(row=4, columnspan=2)

    def get_advice(self):
        """Process the input data and provide tailored financial advice."""
        try:
            # Retrieve and convert input values
            income = float(self.income_entry.get())
            expenses = float(self.expenses_entry.get())
            savings = float(self.savings_entry.get())

            # Validate inputs
            if income < 0 or expenses < 0 or savings < 0:
                raise ValueError("Values must be non-negative.")

            # Generate advice based on financial situation
            advice = self.generate_advice(income, expenses, savings)
            self.advice_label.config(text=advice)

        except ValueError as e:
            # Handle invalid input
            messagebox.showerror("Input Error", str(e))

    def generate_advice(self, income, expenses, savings):
        """Generate tailored financial advice based on the user's situation."""
        advice = []

        # Calculate net income
        net_income = income - expenses

        # Provide advice based on financial situation
        if net_income > 0:
            advice.append("Great! You have a positive cash flow.")
            advice.append("Consider investing your surplus savings.")
        elif net_income < 0:
            advice.append("Warning! You are spending more than you earn.")
            advice.append("Review your expenses and create a budget.")
        else:
            advice.append("You are breaking even. Look for ways to increase income or reduce expenses.")

        if savings < 1000:
            advice.append("It's advisable to build an emergency fund of at least $1000.")
        elif savings < 5000:
            advice.append("Consider saving more to cover unexpected expenses.")

        return "\n".join(advice)

if __name__ == "__main__":
    root = tk.Tk()
    app = FinancialAdvisorApp(root)
    root.mainloop()
```
