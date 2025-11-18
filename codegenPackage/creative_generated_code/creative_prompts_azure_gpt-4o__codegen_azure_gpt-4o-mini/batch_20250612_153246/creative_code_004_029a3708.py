"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hameiriz.co.il
Prompt: Suggest libraries or tools for creating a budget and tracking expenses for a non-profit organization in Israel, aligned with the strategies described by Zvika Hameiri's firm.
Generated: DETERMINISTIC_029a3708625a8a0c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# expense_tracker.py

"""
This script provides a basic structure for a budget and expense tracking application.
It's designed for non-profit organizations in Israel, adhering to the strategies provided by Zvika Hameiri's firm.
"""

import json
import os
from datetime import datetime

class ExpenseTracker:
    """
    A class to track expenses and budgets for a non-profit organization.
    """

    def __init__(self, filename='expenses.json'):
        """
        Initializes the ExpenseTracker instance.

        :param filename: The file where expenses will be stored in JSON format.
        """
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        """
        Load expenses from a JSON file.

        :return: A list of expenses or an empty list if the file does not exist.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("Error: Failed to decode JSON. Starting with an empty expense list.")
                    return []
        return []

    def save_expenses(self):
        """
        Save the current expenses to the JSON file.
        """
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.expenses, file, ensure_ascii=False, indent=4)

    def add_expense(self, amount, category, description):
        """
        Add a new expense to the tracker.

        :param amount: The amount of the expense.
        :param category: The category of the expense.
        :param description: A brief description of the expense.
        """
        try:
            expense = {
                'amount': amount,
                'category': category,
                'description': description,
                'date': datetime.now().isoformat()
            }
            self.expenses.append(expense)
            self.save_expenses()
            print("Expense added successfully.")
        except Exception as e:
            print(f"Error: Unable to add expense. {str(e)}")

    def get_total_expenses(self):
        """
        Calculate the total amount of all expenses.

        :return: The total expenses as a float.
        """
        return sum(expense['amount'] for expense in self.expenses)

    def get_expenses_by_category(self, category):
        """
        Get a list of expenses filtered by category.

        :param category: The category to filter by.
        :return: A list of expenses in the specified category.
        """
        return [expense for expense in self.expenses if expense['category'] == category]

    def print_expenses(self):
        """
        Print all recorded expenses in a formatted way.
        """
        for expense in self.expenses:
            print(f"Date: {expense['date']}, Amount: {expense['amount']}, "
                  f"Category: {expense['category']}, Description: {expense['description']}")

def main():
    """
    Main function to demonstrate the functionality of the ExpenseTracker.
    """
    tracker = ExpenseTracker()

    # Example usage
    tracker.add_expense(100.0, 'Travel', 'Bus ticket to conference')
    tracker.add_expense(250.0, 'Food', 'Catering for event')

    print("Total Expenses: ", tracker.get_total_expenses())
    print("\nAll Expenses:")
    tracker.print_expenses()

if __name__ == "__main__":
    main()
```
