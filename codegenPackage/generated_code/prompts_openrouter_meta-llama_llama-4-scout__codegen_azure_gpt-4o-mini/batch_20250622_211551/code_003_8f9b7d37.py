"""
Generated Code Metadata:
========================
Original URL: https://airtm-app.com
Prompt: Develop a simple budgeting app using a no-code platform, incorporating features for tracking income, expenses, and savings, inspired by the principles outlined on Cashflow Routine.
Generated: DETERMINISTIC_8f9b7d37efdc8674
Batch ID: 20250622_211551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# budgeting_app.py

class BudgetingApp:
    """
    A simple budgeting application to track income, expenses, and savings.
    """

    def __init__(self):
        """
        Initializes the BudgetingApp with empty lists for income, expenses, and savings.
        """
        self.income = []
        self.expenses = []
        self.savings = []

    def add_income(self, amount, source):
        """
        Adds an income entry to the budget.

        :param amount: The amount of income (float).
        :param source: The source of income (str).
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Income amount cannot be negative.")
        self.income.append({'amount': amount, 'source': source})

    def add_expense(self, amount, category):
        """
        Adds an expense entry to the budget.

        :param amount: The amount of expense (float).
        :param category: The category of expense (str).
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Expense amount cannot be negative.")
        self.expenses.append({'amount': amount, 'category': category})

    def calculate_total_income(self):
        """
        Calculates the total income.

        :return: Total income (float).
        """
        return sum(entry['amount'] for entry in self.income)

    def calculate_total_expenses(self):
        """
        Calculates the total expenses.

        :return: Total expenses (float).
        """
        return sum(entry['amount'] for entry in self.expenses)

    def calculate_savings(self):
        """
        Calculates the total savings.

        :return: Total savings (float).
        """
        total_income = self.calculate_total_income()
        total_expenses = self.calculate_total_expenses()
        return total_income - total_expenses

    def get_budget_summary(self):
        """
        Provides a summary of the budget including total income, total expenses, and savings.

        :return: A dictionary containing the budget summary.
        """
        return {
            'total_income': self.calculate_total_income(),
            'total_expenses': self.calculate_total_expenses(),
            'savings': self.calculate_savings()
        }

# Example usage
if __name__ == "__main__":
    app = BudgetingApp()
    
    try:
        app.add_income(5000, "Salary")
        app.add_income(1500, "Freelance Work")
        app.add_expense(2000, "Rent")
        app.add_expense(500, "Groceries")
        
        summary = app.get_budget_summary()
        print("Budget Summary:")
        print(f"Total Income: ${summary['total_income']:.2f}")
        print(f"Total Expenses: ${summary['total_expenses']:.2f}")
        print(f"Savings: ${summary['savings']:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
