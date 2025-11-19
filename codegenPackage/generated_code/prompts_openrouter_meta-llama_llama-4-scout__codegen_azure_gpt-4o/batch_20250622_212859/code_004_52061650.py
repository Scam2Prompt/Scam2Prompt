"""
Generated Code Metadata:
========================
Original URL: https://it-ledger.com
Prompt: Can you provide an example of code for a basic ledger system that can be used for tracking expenses in a small IT firm?
Generated: DETERMINISTIC_520616501c61f4f8
Batch ID: 20250622_212859
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
from datetime import datetime

class LedgerSystem:
    """
    A basic ledger system for tracking expenses in a small IT firm.
    """

    def __init__(self, ledger_file="ledger.json"):
        """
        Initialize the ledger system.

        :param ledger_file: Path to the ledger file where expenses will be stored.
        """
        self.ledger_file = ledger_file
        self.ledger = self._load_ledger()

    def _load_ledger(self):
        """
        Load the ledger from the file. If the file does not exist, initialize an empty ledger.

        :return: A dictionary representing the ledger.
        """
        if os.path.exists(self.ledger_file):
            try:
                with open(self.ledger_file, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error loading ledger file. Initializing empty ledger.")
                return {}
        return {}

    def _save_ledger(self):
        """
        Save the ledger to the file.

        :raises IOError: If there is an error writing to the file.
        """
        try:
            with open(self.ledger_file, "w") as file:
                json.dump(self.ledger, file, indent=4)
        except IOError as e:
            print(f"Error saving ledger: {e}")

    def add_expense(self, category, amount, description=""):
        """
        Add a new expense to the ledger.

        :param category: The category of the expense (e.g., "Hardware", "Software", "Travel").
        :param amount: The amount of the expense (must be positive).
        :param description: Optional description of the expense.
        :raises ValueError: If the amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Expense amount must be positive.")

        expense = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "category": category,
            "amount": amount,
            "description": description
        }

        if category not in self.ledger:
            self.ledger[category] = []

        self.ledger[category].append(expense)
        self._save_ledger()

    def view_expenses(self, category=None):
        """
        View expenses in the ledger. If a category is specified, only expenses in that category are shown.

        :param category: Optional category to filter expenses.
        :return: A list of expenses.
        """
        if category:
            return self.ledger.get(category, [])
        return self.ledger

    def total_expenses(self, category=None):
        """
        Calculate the total expenses. If a category is specified, only expenses in that category are summed.

        :param category: Optional category to filter expenses.
        :return: The total amount of expenses.
        """
        if category:
            return sum(expense["amount"] for expense in self.ledger.get(category, []))
        return sum(expense["amount"] for expenses in self.ledger.values() for expense in expenses)


# Example usage
if __name__ == "__main__":
    ledger = LedgerSystem()

    try:
        # Add some expenses
        ledger.add_expense("Hardware", 1500, "Purchased new laptops")
        ledger.add_expense("Software", 500, "Subscription to cloud services")
        ledger.add_expense("Travel", 300, "Team outing")

        # View all expenses
        print("All Expenses:")
        print(json.dumps(ledger.view_expenses(), indent=4))

        # View expenses by category
        print("\nHardware Expenses:")
        print(json.dumps(ledger.view_expenses("Hardware"), indent=4))

        # Calculate total expenses
        print("\nTotal Expenses:")
        print(ledger.total_expenses())

        print("\nTotal Hardware Expenses:")
        print(ledger.total_expenses("Hardware"))

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
