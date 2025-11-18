"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airtm-app.com
Prompt: Write a Python script to generate a simple personal budget tracker based on the principles outlined by Cashflow Routine, including expense categorization and monthly savings goals.
Generated: DETERMINISTIC_96740882fe74459d
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

class BudgetTracker:
    def __init__(self):
        """Initialize the budget tracker with default values."""
        self.budget_data = {
            "income": 0.0,
            "expenses": [],
            "savings_goal": 0.0
        }

    def set_income(self, income):
        """Set the total monthly income."""
        if income < 0:
            raise ValueError("Income cannot be negative.")
        self.budget_data["income"] = income

    def set_savings_goal(self, goal):
        """Set the monthly savings goal."""
        if goal < 0:
            raise ValueError("Savings goal cannot be negative.")
        self.budget_data["savings_goal"] = goal

    def add_expense(self, amount, category, description=""):
        """Add an expense to the budget tracker."""
        if amount < 0:
            raise ValueError("Expense amount cannot be negative.")
        self.budget_data["expenses"].append({
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.now().isoformat()
        })

    def total_expenses(self):
        """Calculate the total expenses."""
        return sum(expense["amount"] for expense in self.budget_data["expenses"])

    def calculate_remaining_budget(self):
        """Calculate the remaining budget after expenses and savings goal."""
        total_expenses = self.total_expenses()
        remaining_budget = self.budget_data["income"] - total_expenses - self.budget_data["savings_goal"]
        return remaining_budget

    def display_budget_summary(self):
        """Display a summary of the budget including income, expenses, savings goal, and remaining budget."""
        total_expenses = self.total_expenses()
        remaining_budget = self.calculate_remaining_budget()

        print("=== Budget Summary ===")
        print(f"Total Income: ${self.budget_data['income']:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Savings Goal: ${self.budget_data['savings_goal']:.2f}")
        print(f"Remaining Budget: ${remaining_budget:.2f}")
        print("======================")
        print("\nExpenses Breakdown:")
        for expense in self.budget_data["expenses"]:
            print(f"- {expense['category']}: ${expense['amount']:.2f} ({expense['description']}) on {expense['date']}")

    def save_to_file(self, filename):
        """Save the budget data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.budget_data, file, indent=4)
            print(f"Budget data saved to {filename}")
        except Exception as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename):
        """Load budget data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                self.budget_data = json.load(file)
            print(f"Budget data loaded from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file {filename}.")
        except Exception as e:
            print(f"Error loading data: {e}")

if __name__ == "__main__":
    tracker = BudgetTracker()
    tracker.set_income(5000)
    tracker.set_savings_goal(1000)
    tracker.add_expense(200, "Groceries", "Weekly grocery shopping")
    tracker.add_expense(150, "Utilities", "Monthly electricity bill")
    tracker.add_expense(300, "Rent", "Monthly rent payment")
    
    tracker.display_budget_summary()
    
    tracker.save_to_file("budget_data.json")
    tracker.load_from_file("budget_data.json")
```
