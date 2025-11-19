"""
Generated Code Metadata:
========================
Original URL: https://ahmetiwealth.com
Prompt: Create a Python script that simulates the "Pay Yourself First" strategy in personal finance, inspired by the guidelines from Ahmeti Wealth Management.
Generated: DETERMINISTIC_ee1c4f1d9eeded1a
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class PayYourselfFirst:
    def __init__(self, income, savings_percentage, expenses):
        """
        Initializes the PayYourselfFirst class with income, savings percentage, and expenses.

        :param income: Monthly income (float)
        :param savings_percentage: Percentage of income to save (float)
        :param expenses: List of monthly expenses (list of floats)
        """
        self.income = income
        self.savings_percentage = savings_percentage / 100  # Convert percentage to decimal
        self.expenses = expenses

    def calculate_savings(self):
        """
        Calculates the amount to save based on the income and savings percentage.

        :return: Amount to save (float)
        """
        savings = self.income * self.savings_percentage
        return savings

    def calculate_remaining_income(self):
        """
        Calculates the remaining income after savings and expenses.

        :return: Remaining income (float)
        """
        savings = self.calculate_savings()
        total_expenses = sum(self.expenses)
        remaining_income = self.income - savings - total_expenses
        return remaining_income

    def generate_report(self):
        """
        Generates a financial report summarizing income, savings, expenses, and remaining income.

        :return: Financial report (dict)
        """
        report = {
            "Income": self.income,
            "Savings": self.calculate_savings(),
            "Expenses": self.expenses,
            "Total Expenses": sum(self.expenses),
            "Remaining Income": self.calculate_remaining_income()
        }
        return report

    def save_report_to_file(self, filename):
        """
        Saves the financial report to a JSON file.

        :param filename: Name of the file to save the report (str)
        """
        report = self.generate_report()
        try:
            with open(filename, 'w') as file:
                json.dump(report, file, indent=4)
            print(f"Report saved to {filename}")
        except IOError as e:
            print(f"Error saving report to file: {e}")

def main():
    """
    Main function to execute the Pay Yourself First strategy simulation.
    """
    # User-defined parameters
    income = 5000.0  # Monthly income
    savings_percentage = 20.0  # Percentage of income to save
    expenses = [1500.0, 800.0, 300.0, 200.0]  # List of monthly expenses

    # Create an instance of PayYourselfFirst
    pypf = PayYourselfFirst(income, savings_percentage, expenses)

    # Generate and print the financial report
    report = pypf.generate_report()
    print(json.dumps(report, indent=4))

    # Save the report to a file
    pypf.save_report_to_file("financial_report.json")

if __name__ == "__main__":
    main()
```
