"""
Generated Code Metadata:
========================
Original URL: https://hispanicservices.com
Prompt: Develop a basic profit and loss statement template for a small business, including fields for revenue, expenses, and net income.
Generated: DETERMINISTIC_f834cbd152b18c2a
Batch ID: 20250622_205045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# profit_loss_statement.py

class ProfitLossStatement:
    """
    A basic profit and loss statement template for a small business.
    """

    def __init__(self):
        """
        Initializes a ProfitLossStatement object with empty revenue and expense fields.
        """
        self.revenue = {}
        self.expenses = {}

    def add_revenue(self, description, amount):
        """
        Adds a revenue stream to the profit and loss statement.

        Args:
            description (str): A brief description of the revenue stream.
            amount (float): The amount of revenue.

        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Revenue amount cannot be negative")
        self.revenue[description] = amount

    def add_expense(self, description, amount):
        """
        Adds an expense to the profit and loss statement.

        Args:
            description (str): A brief description of the expense.
            amount (float): The amount of the expense.

        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Expense amount cannot be negative")
        self.expenses[description] = amount

    def calculate_total_revenue(self):
        """
        Calculates the total revenue.

        Returns:
            float: The total revenue.
        """
        return sum(self.revenue.values())

    def calculate_total_expenses(self):
        """
        Calculates the total expenses.

        Returns:
            float: The total expenses.
        """
        return sum(self.expenses.values())

    def calculate_net_income(self):
        """
        Calculates the net income.

        Returns:
            float: The net income.
        """
        total_revenue = self.calculate_total_revenue()
        total_expenses = self.calculate_total_expenses()
        return total_revenue - total_expenses

    def generate_profit_loss_statement(self):
        """
        Generates a profit and loss statement.

        Returns:
            str: A formatted profit and loss statement.
        """
        statement = "Profit and Loss Statement\n"
        statement += "-------------------------\n"

        statement += "Revenue:\n"
        for description, amount in self.revenue.items():
            statement += f"  {description}: ${amount:.2f}\n"
        statement += f"Total Revenue: ${self.calculate_total_revenue():.2f}\n"

        statement += "\nExpenses:\n"
        for description, amount in self.expenses.items():
            statement += f"  {description}: ${amount:.2f}\n"
        statement += f"Total Expenses: ${self.calculate_total_expenses():.2f}\n"

        statement += f"\nNet Income: ${self.calculate_net_income():.2f}\n"

        return statement


def main():
    try:
        statement = ProfitLossStatement()

        statement.add_revenue("Sales", 10000.0)
        statement.add_revenue("Services", 5000.0)

        statement.add_expense("Rent", 2000.0)
        statement.add_expense("Utilities", 500.0)
        statement.add_expense("Salaries", 3000.0)

        print(statement.generate_profit_loss_statement())
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
