"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitum.cz
Prompt: Design a user interface component that allows clients to input their financial situation and receive tailored advice, similar to the personalized services offered by Arbitum Consulting.
Generated: DETERMINISTIC_0c1b3a45b383c745
Batch ID: 20250612_155131
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
from typing import Dict

class FinancialAdvisorApp:
    def __init__(self, master):
        """Initializes the Financial Advisor Application."""
        self.master = master
        master.title("Personal Financial Advisor")

        # Create input fields
        self.create_widgets()

    def create_widgets(self):
        """Creates the user input fields and submit button."""
        # Instructions label
        self.instructions = tk.Label(self.master, text="Enter your financial situation:")
        self.instructions.grid(row=0, columnspan=2, pady=10)

        # Income input
        self.income_label = tk.Label(self.master, text="Monthly Income:")
        self.income_label.grid(row=1, column=0, sticky='e')
        self.income_entry = tk.Entry(self.master)
        self.income_entry.grid(row=1, column=1)

        # Expenses input
        self.expenses_label = tk.Label(self.master, text="Monthly Expenses:")
        self.expenses_label.grid(row=2, column=0, sticky='e')
        self.expenses_entry = tk.Entry(self.master)
        self.expenses_entry.grid(row=2, column=1)

        # Savings input
        self.savings_label = tk.Label(self.master, text="Current Savings:")
        self.savings_label.grid(row=3, column=0, sticky='e')
        self.savings_entry = tk.Entry(self.master)
        self.savings_entry.grid(row=3, column=1)

        # Submit button
        self.submit_button = tk.Button(self.master, text="Get Advice", command=self.get_advice)
        self.submit_button.grid(row=4, columnspan=2, pady=10)

    def get_advice(self):
        """Processes user input and generates tailored financial advice."""
        try:
            # Retrieve and convert input values
            income = float(self.income_entry.get())
            expenses = float(self.expenses_entry.get())
            savings = float(self.savings_entry.get())

            # Validate inputs
            if income < 0 or expenses < 0 or savings < 0:
                raise ValueError("Income, expenses, and savings must be non-negative.")

            # Generate advice based on the financial situation
            advice = self.generate_advice(income, expenses, savings)

            # Display advice
            messagebox.showinfo("Financial Advice", advice)

        except ValueError as e:
            # Handle input conversion and validation errors
            messagebox.showerror("Input Error", str(e))

    def generate_advice(self, income: float, expenses: float, savings: float) -> str:
        """Generates financial advice based on user inputs."""
        advice: Dict[str, str] = {}

        # Calculate financial metrics
        disposable_income = income - expenses
        savings_rate = (savings / income) if income > 0 else 0

        # Tailor advice based on metrics
        if disposable_income > 0:
            advice["Spending"] = "You're spending less than you earn. Great job!"
        else:
            advice["Spending"] = "Consider reducing your expenses."

        if savings_rate < 0.2:
            advice["Savings"] = "Try to save at least 20% of your income."
        else:
            advice["Savings"] = "You're on track with your savings!"

        return "\n".join(advice.values())

if __name__ == "__main__":
    root = tk.Tk()
    app = FinancialAdvisorApp(root)
    root.mainloop()
```
