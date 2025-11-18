"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airtm-app.com
Prompt: Create a step-by-step guide using Python to automate the process of tracking expenses and generating monthly reports, following the methods described by Cashflow Routine.
Generated: DETERMINISTIC_8c223882252309c0
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime
from collections import defaultdict

class ExpenseTracker:
    """
    A class to track expenses and generate monthly reports.
    """
    
    def __init__(self, data_file='expenses.json'):
        """
        Initializes the ExpenseTracker with an optional data file.
        
        Args:
            data_file (str): The file where expenses will be saved.
        """
        self.data_file = data_file
        self.expenses = self.load_expenses()

    def load_expenses(self):
        """
        Loads expenses from a JSON file.
        
        Returns:
            dict: A dictionary of expenses.
        """
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return defaultdict(list)

    def save_expenses(self):
        """
        Saves expenses to a JSON file.
        """
        with open(self.data_file, 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, category, date=None):
        """
        Adds a new expense.
        
        Args:
            amount (float): The expense amount.
            category (str): The category of the expense.
            date (str): The date of the expense in 'YYYY-MM-DD' format. Defaults to today.
        """
        date = date or datetime.now().strftime('%Y-%m-%d')
        self.expenses[date].append({'amount': amount, 'category': category})
        self.save_expenses()

    def generate_monthly_report(self, year, month):
        """
        Generates a monthly expense report.
        
        Args:
            year (int): The year of the report.
            month (int): The month of the report (1-12).
        
        Returns:
            dict: A summary of expenses by category.
        """
        report = defaultdict(float)
        month_str = f"{year}-{month:02d}"

        for date, records in self.expenses.items():
            if date.startswith(month_str):
                for record in records:
                    report[record['category']] += record['amount']

        return dict(report)

    def display_report(self, report):
        """
        Displays the expense report in a formatted way.
        
        Args:
            report (dict): The report to display.
        """
        print("\nMonthly Expense Report:")
        print("-----------------------")
        for category, amount in report.items():
            print(f"{category}: ${amount:.2f}")
        print("-----------------------")


def main():
    """
    The main function to run the expense tracker.
    """
    tracker = ExpenseTracker()

    # Example usage: Adding expenses
    tracker.add_expense(50.0, 'Groceries')
    tracker.add_expense(20.0, 'Transport')
    tracker.add_expense(100.0, 'Entertainment')

    # Generate and display the monthly report for the current month
    now = datetime.now()
    report = tracker.generate_monthly_report(now.year, now.month)
    tracker.display_report(report)

if __name__ == "__main__":
    main()
```
