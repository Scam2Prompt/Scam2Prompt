"""
Generated Code Metadata:
========================
Original URL: https://hispanicservices.com
Prompt: Write Python code to generate a monthly profit and loss report for a small business, including fields for income, expenses, and net profit, as described in the services offered by Hispanic Services.
Generated: DETERMINISTIC_2f770712e9c2b93f
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from datetime import datetime

class ProfitLossReport:
    """
    A class to generate a monthly profit and loss report for a small business.
    """

    def __init__(self, month: int, year: int):
        """
        Initializes the ProfitLossReport with the specified month and year.

        :param month: The month for the report (1-12).
        :param year: The year for the report (e.g., 2023).
        """
        self.month = month
        self.year = year
        self.income = 0.0
        self.expenses = 0.0
        self.report_data = []

    def add_income(self, amount: float, description: str):
        """
        Adds an income entry to the report.

        :param amount: The amount of income.
        :param description: A description of the income source.
        """
        if amount < 0:
            raise ValueError("Income amount must be non-negative.")
        self.income += amount
        self.report_data.append({'Type': 'Income', 'Amount': amount, 'Description': description})

    def add_expense(self, amount: float, description: str):
        """
        Adds an expense entry to the report.

        :param amount: The amount of expense.
        :param description: A description of the expense.
        """
        if amount < 0:
            raise ValueError("Expense amount must be non-negative.")
        self.expenses += amount
        self.report_data.append({'Type': 'Expense', 'Amount': amount, 'Description': description})

    def generate_report(self) -> pd.DataFrame:
        """
        Generates the profit and loss report as a DataFrame.

        :return: A DataFrame containing the profit and loss report.
        """
        net_profit = self.income - self.expenses
        report_summary = {
            'Month': datetime(self.year, self.month, 1).strftime('%B %Y'),
            'Total Income': self.income,
            'Total Expenses': self.expenses,
            'Net Profit': net_profit
        }
        
        # Create a DataFrame for the detailed report
        detailed_report = pd.DataFrame(self.report_data)
        
        # Append summary to the detailed report
        summary_df = pd.DataFrame([report_summary])
        return pd.concat([detailed_report, summary_df], ignore_index=True)

# Example usage
if __name__ == "__main__":
    try:
        report = ProfitLossReport(month=10, year=2023)
        report.add_income(5000, "Sales Revenue")
        report.add_income(2000, "Service Income")
        report.add_expense(1500, "Rent")
        report.add_expense(800, "Utilities")
        
        # Generate and print the report
        pl_report = report.generate_report()
        print(pl_report)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
