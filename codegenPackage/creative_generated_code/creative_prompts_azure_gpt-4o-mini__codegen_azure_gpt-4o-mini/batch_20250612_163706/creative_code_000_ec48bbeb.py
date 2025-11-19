"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airtm-app.com
Prompt: Generate a Python script that helps track personal expenses and categorize them based on the principles discussed in the Cashflow Routine blog.
Generated: DETERMINISTIC_ec48bbeb3b870c44
Batch ID: 20250612_163706
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

class Expense:
    """Class to represent an individual expense."""
    def __init__(self, amount: float, category: str, description: str, date: str = None):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        """Convert the expense to a dictionary for easy JSON serialization."""
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }

class ExpenseTracker:
    """Class to manage a list of expenses."""
    def __init__(self, filename: str):
        self.filename = filename
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        """Load expenses from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                self.expenses = [Expense(**data) for data in json.load(file)]
        except FileNotFoundError:
            print("Expense file not found. Starting with an empty expense list.")
        except json.JSONDecodeError:
            print("Error decoding JSON. Starting with an empty expense list.")
    
    def save_expenses(self):
        """Save expenses to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([expense.to_dict() for expense in self.expenses], file, indent=4)

    def add_expense(self, amount: float, category: str, description: str):
        """Add a new expense to the tracker."""
        if amount < 0:
            raise ValueError("Expense amount cannot be negative.")
        new_expense = Expense(amount, category, description)
        self.expenses.append(new_expense)
        self.save_expenses()

    def get_total_expenses(self):
        """Calculate the total expenses."""
        return sum(expense.amount for expense in self.expenses)

    def get_expenses_by_category(self, category: str):
        """Get expenses filtered by category."""
        return [expense for expense in self.expenses if expense.category == category]

    def display_expenses(self):
        """Display all tracked expenses."""
        for expense in self.expenses:
            print(f"{expense.date}: {expense.amount} - {expense.category} | {expense.description}")

def main():
    """Main function to run the expense tracker."""
    tracker = ExpenseTracker('expenses.json')

    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Get Total Expenses")
        print("4. Get Expenses by Category")
        print("5. Exit")

        choice = input("Select an option: ")
        
        if choice == '1':
            try:
                amount = float(input("Enter expense amount: "))
                category = input("Enter expense category: ")
                description = input("Enter expense description: ")
                tracker.add_expense(amount, category, description)
                print("Expense added successfully.")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '2':
            print("\nTracked Expenses:")
            tracker.display_expenses()
        
        elif choice == '3':
            total = tracker.get_total_expenses()
            print(f"Total Expenses: {total}")
        
        elif choice == '4':
            category = input("Enter category to filter expenses: ")
            filtered_expenses = tracker.get_expenses_by_category(category)
            print(f"\nExpenses in category '{category}':")
            for expense in filtered_expenses:
                print(f"{expense.date}: {expense.amount} - {expense.description}")
        
        elif choice == '5':
            print("Exiting the expense tracker.")
            break
        
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()
```
