"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimisenow.net
Prompt: Write a code snippet that automates the tracking and reimbursement of expenses using a Digitised Expense Claims System (DECS).
Generated: DETERMINISTIC_7aa859c9be256796
Batch ID: 20250612_155830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from datetime import datetime

class Expense:
    """Class to represent an individual expense."""
    
    def __init__(self, amount, description, category):
        self.amount = amount
        self.description = description
        self.category = category
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        """Convert the expense to a dictionary."""
        return {
            'amount': self.amount,
            'description': self.description,
            'category': self.category,
            'date': self.date
        }

class ExpenseTracker:
    """Class to manage expense tracking and reimbursement."""
    
    def __init__(self):
        self.expenses = []
        self.file_path = 'expenses.json'
        self.load_expenses()

    def load_expenses(self):
        """Load expenses from a JSON file."""
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                try:
                    self.expenses = json.load(file)
                except json.JSONDecodeError:
                    print("Error: Could not decode JSON from expense file.")
                    self.expenses = []

    def save_expenses(self):
        """Save expenses to a JSON file."""
        with open(self.file_path, 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, description, category):
        """Add a new expense to the tracker."""
        new_expense = Expense(amount, description, category)
        self.expenses.append(new_expense.to_dict())
        self.save_expenses()
        print(f"Added expense: {new_expense.to_dict()}")

    def get_expenses(self):
        """Retrieve all recorded expenses."""
        return self.expenses

    def calculate_reimbursement(self):
        """Calculate total reimbursement amount."""
        total = sum(expense['amount'] for expense in self.expenses)
        return total

    def generate_report(self):
        """Generate a report of expenses."""
        report = {
            'total_expenses': len(self.expenses),
            'total_reimbursement': self.calculate_reimbursement(),
            'expenses': self.expenses
        }
        return report

def main():
    """Main function to run the expense tracking system."""
    tracker = ExpenseTracker()

    # Example Usage
    try:
        tracker.add_expense(50.00, "Office Supplies", "Supplies")
        tracker.add_expense(150.00, "Travel Expenses", "Travel")
        
        print("\nAll Expenses:")
        for expense in tracker.get_expenses():
            print(expense)
        
        report = tracker.generate_report()
        print("\nExpense Report:")
        print(json.dumps(report, indent=4))
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
