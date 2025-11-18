"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hispanicservices.com
Prompt: Write Python code to generate a monthly profit and loss report for a small business, including fields for income, expenses, and net profit, as described in the services offered by Hispanic Services.
Generated: DETERMINISTIC_2f770712e9c2b93f
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class MonthlyProfitLossReport:
    def __init__(self, month, year):
        """
        Initializes the MonthlyProfitLossReport with the specified month and year.
        
        Args:
            month (int): The month for the report (1-12).
            year (int): The year for the report (e.g., 2023).
        """
        self.month = month
        self.year = year
        self.income_data = []
        self.expense_data = []

    def add_income(self, description, amount):
        """
        Adds an income entry to the report.
        
        Args:
            description (str): A description of the income source.
            amount (float): The amount of income generated.
        
        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Income amount cannot be negative.")
        self.income_data.append({'Description': description, 'Amount': amount})

    def add_expense(self, description, amount):
        """
        Adds an expense entry to the report.
        
        Args:
            description (str): A description of the expense.
            amount (float): The amount of the expense incurred.
        
        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Expense amount cannot be negative.")
        self.expense_data.append({'Description': description, 'Amount': amount})

    def generate_report(self):
        """
        Generates a monthly profit and loss report.
        
        Returns:
            dict: A dictionary containing the report summarizing income, expenses, and net profit.
        """
        total_income = sum(entry['Amount'] for entry in self.income_data)
        total_expenses = sum(entry['Amount'] for entry in self.expense_data)
        net_profit = total_income - total_expenses
        
        report = {
            'Month': self.month,
            'Year': self.year,
            'Total Income': total_income,
            'Total Expenses': total_expenses,
            'Net Profit': net_profit,
            'Income Details': self.income_data,
            'Expense Details': self.expense_data
        }
        
        return report

    def display_report(self):
        """
        Displays the generated report in a readable format.
        """
        report = self.generate_report()
        print(f"Profit and Loss Report for {report['Month']}/{report['Year']}")
        print(f"Total Income: ${report['Total Income']:.2f}")
        print(f"Total Expenses: ${report['Total Expenses']:.2f}")
        print(f"Net Profit: ${report['Net Profit']:.2f}")
        print("\nIncome Details:")
        for income in report['Income Details']:
            print(f" - {income['Description']}: ${income['Amount']:.2f}")
        print("\nExpense Details:")
        for expense in report['Expense Details']:
            print(f" - {expense['Description']}: ${expense['Amount']:.2f}")

if __name__ == "__main__":
    # Example usage of the MonthlyProfitLossReport class
    report = MonthlyProfitLossReport(month=9, year=2023)
    
    # Adding some income entries
    report.add_income("Service Revenue", 5000.00)
    report.add_income("Product Sales", 3000.00)
    
    # Adding some expense entries
    report.add_expense("Rent", 1500.00)
    report.add_expense("Utilities", 300.00)
    report.add_expense("Salaries", 2000.00)

    # Displaying the report
    report.display_report()
```
