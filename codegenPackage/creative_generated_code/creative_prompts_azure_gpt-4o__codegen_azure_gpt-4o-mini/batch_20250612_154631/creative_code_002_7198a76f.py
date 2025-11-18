"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeinvestmentslimited.org
Prompt: Generate code to create a budgeting tool for businesses and families, incorporating financial advisory principles as described on Finance Investment Limited's website.
Generated: DETERMINISTIC_7198a76faf417b97
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# budgeting_tool.py

import json
from typing import List, Dict, Any

class BudgetEntry:
    """Class representing a single budget entry, either income or expense."""

    def __init__(self, category: str, amount: float, entry_type: str):
        if entry_type not in ['income', 'expense']:
            raise ValueError("Entry type must be 'income' or 'expense'.")
        if amount < 0:
            raise ValueError("Amount must be non-negative.")

        self.category = category
        self.amount = amount
        self.entry_type = entry_type

    def to_dict(self) -> Dict[str, Any]:
        """Convert budget entry to dictionary."""
        return {
            "category": self.category,
            "amount": self.amount,
            "entry_type": self.entry_type,
        }


class Budget:
    """Class representing a budget with multiple entries."""

    def __init__(self):
        self.entries: List[BudgetEntry] = []

    def add_entry(self, entry: BudgetEntry):
        """Add a new entry to the budget."""
        self.entries.append(entry)

    def total_income(self) -> float:
        """Calculate total income."""
        return sum(entry.amount for entry in self.entries if entry.entry_type == 'income')

    def total_expenses(self) -> float:
        """Calculate total expenses."""
        return sum(entry.amount for entry in self.entries if entry.entry_type == 'expense')

    def balance(self) -> float:
        """Calculate the balance (income - expenses)."""
        return self.total_income() - self.total_expenses()

    def to_json(self) -> str:
        """Convert budget to JSON format."""
        return json.dumps([entry.to_dict() for entry in self.entries], indent=4)


def main():
    """Main function to demonstrate the budgeting tool functionality."""
    budget = Budget()

    # Example entries
    try:
        budget.add_entry(BudgetEntry("Salary", 5000, "income"))
        budget.add_entry(BudgetEntry("Rent", 1500, "expense"))
        budget.add_entry(BudgetEntry("Groceries", 300, "expense"))
        budget.add_entry(BudgetEntry("Freelance", 1200, "income"))

        print("Total Income: $", budget.total_income())
        print("Total Expenses: $", budget.total_expenses())
        print("Balance: $", budget.balance())
        print("\nBudget Entries:")
        print(budget.to_json())

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

This code creates a budgeting tool that allows users to track income and expenses, calculate totals, and display results in a structured format. It includes error handling, ensuring that invalid entries are managed appropriately. The code is structured to be both reusable and easy to extend.
