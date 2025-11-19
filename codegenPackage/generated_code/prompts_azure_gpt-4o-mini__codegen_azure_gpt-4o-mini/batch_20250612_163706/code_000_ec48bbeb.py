"""
Generated Code Metadata:
========================
Original URL: https://airtm-app.com
Prompt: Generate a Python script that helps track personal expenses and categorize them based on the principles discussed in the Cashflow Routine blog.
Generated: DETERMINISTIC_ec48bbeb3b870c44
Batch ID: 20250612_163706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self, filename='expenses.json'):
        """Initialize the ExpenseTracker with a specified filename."""
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        """Load expenses from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_expenses(self):
        """Save expenses to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, category, description=''):
        """Add a new expense to the tracker."""
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        expense = {
            'date': datetime.now().isoformat(),
            'amount': amount,
            'category': category,
            'description': description
        }
        self.expenses.append(expense)
        self.save_expenses()

    def get_expenses_by_category(self, category):
        """Retrieve expenses filtered by category."""
        return [expense for expense in self.expenses if expense['category'] == category]

    def get_total_expenses(self):
        """Calculate the total amount of all expenses."""
        return sum(expense['amount'] for expense in self.expenses)

    def display_expenses(self):
        """Display all expenses in a readable format."""
        for expense in self.expenses:
            print(f"{expense['date']}: {expense['amount']} - {expense['category']} - {expense['description']}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expenses")
        print("4. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                description = input("Enter description (optional): ")
                tracker.add_expense(amount, category, description)
                print("Expense added successfully.")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '2':
            tracker.display_expenses()
        
        elif choice == '3':
            total = tracker.get_total_expenses()
            print(f"Total Expenses: {total}")
        
        elif choice == '4':
            print("Exiting the Expense Tracker.")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
```
