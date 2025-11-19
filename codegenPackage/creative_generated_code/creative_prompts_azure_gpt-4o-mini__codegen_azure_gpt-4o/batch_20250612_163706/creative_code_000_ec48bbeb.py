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
import datetime

class ExpenseTracker:
    """
    A class to track personal expenses and categorize them.
    """

    def __init__(self, data_file='expenses.json'):
        """
        Initialize the ExpenseTracker with a data file.

        Args:
            data_file (str): The file where expenses will be stored.
        """
        self.data_file = data_file
        self.expenses = self._load_expenses()

    def _load_expenses(self):
        """
        Load expenses from the data file if it exists, else return an empty dictionary.

        Returns:
            dict: A dictionary containing expenses.
        """
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            print("Warning: Corrupted data file. Starting fresh.")
            return {}

    def _save_expenses(self):
        """
        Save expenses to the data file in JSON format.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.expenses, file, indent=4)
        except Exception as e:
            print(f"Error saving expenses: {e}")

    def add_expense(self, amount, category, description=""):
        """
        Add a new expense to the tracker.

        Args:
            amount (float): The amount spent.
            category (str): The category of the expense.
            description (str): A brief description of the expense.
        """
        if amount <= 0:
            print("Error: Expense amount must be greater than zero.")
            return

        if not category:
            print("Error: Category cannot be empty.")
            return

        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        if category not in self.expenses:
            self.expenses[category] = []

        self.expenses[category].append(expense)
        self._save_expenses()
        print("Expense added successfully.")

    def view_expenses(self, category=None):
        """
        View expenses, optionally filtered by category.

        Args:
            category (str): The category to filter by. If None, display all expenses.

        Returns:
            list: A list of expenses in the requested category or all expenses.
        """
        if category:
            if category in self.expenses:
                return self.expenses[category]
            else:
                print(f"No expenses found for category: {category}")
                return []
        else:
            return self.expenses

    def delete_expense(self, category, index):
        """
        Delete an expense by category and index.

        Args:
            category (str): The category of the expense.
            index (int): The index of the expense in the category's list.
        """
        if category in self.expenses and 0 <= index < len(self.expenses[category]):
            deleted_expense = self.expenses[category].pop(index)
            if not self.expenses[category]:  # Remove category if empty
                del self.expenses[category]
            self._save_expenses()
            print(f"Deleted expense: {deleted_expense}")
        else:
            print("Error: Invalid category or index.")

    def summary(self):
        """
        Display a summary of expenses grouped by category.

        Returns:
            dict: A dictionary with categories as keys and total expenditure as values.
        """
        summary = {category: sum(expense["amount"] for expense in expenses)
                   for category, expenses in self.expenses.items()}
        
        print("Expense Summary:")
        for category, total in summary.items():
            print(f"{category}: ${total:.2f}")
        return summary


def main():
    """
    Main function to interact with the ExpenseTracker.
    """
    tracker = ExpenseTracker()

    print("Welcome to the Expense Tracker!")
    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Show Summary")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            try:
                amount = float(input("Enter the expense amount: "))
                category = input("Enter the expense category: ")
                description = input("Enter a brief description (optional): ")
                tracker.add_expense(amount, category, description)
            except ValueError:
                print("Error: Please enter a valid number for the amount.")
        elif choice == 2:
            category = input("Enter the category to view (or press Enter to view all): ")
            expenses = tracker.view_expenses(category.strip() if category else None)
            print(json.dumps(expenses, indent=4))
        elif choice == 3:
            category = input("Enter the category of the expense to delete: ")
            try:
                index = int(input("Enter the index of the expense to delete: "))
                tracker.delete_expense(category, index)
            except ValueError:
                print("Error: Please enter a valid number for the index.")
        elif choice == 4:
            tracker.summary()
        elif choice == 5:
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```
