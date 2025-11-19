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
class ProfitAndLossStatement:
    """
    A class to represent a basic Profit and Loss Statement for a small business.
    """

    def __init__(self):
        """
        Initializes the Profit and Loss Statement with default values.
        """
        self.revenue = 0.0
        self.expenses = 0.0
        self.net_income = 0.0

    def set_revenue(self, revenue: float):
        """
        Sets the revenue for the statement.

        :param revenue: The total revenue (float).
        :raises ValueError: If revenue is negative.
        """
        if revenue < 0:
            raise ValueError("Revenue cannot be negative.")
        self.revenue = revenue

    def set_expenses(self, expenses: float):
        """
        Sets the expenses for the statement.

        :param expenses: The total expenses (float).
        :raises ValueError: If expenses are negative.
        """
        if expenses < 0:
            raise ValueError("Expenses cannot be negative.")
        self.expenses = expenses

    def calculate_net_income(self):
        """
        Calculates the net income based on revenue and expenses.
        """
        self.net_income = self.revenue - self.expenses

    def display_statement(self):
        """
        Displays the Profit and Loss Statement.
        """
        print("Profit and Loss Statement")
        print("---------------------------")
        print(f"Revenue: ${self.revenue:,.2f}")
        print(f"Expenses: ${self.expenses:,.2f}")
        print(f"Net Income: ${self.net_income:,.2f}")

def main():
    """
    Main function to demonstrate the Profit and Loss Statement functionality.
    """
    try:
        # Create an instance of ProfitAndLossStatement
        statement = ProfitAndLossStatement()

        # Set revenue and expenses
        statement.set_revenue(15000.00)  # Example revenue
        statement.set_expenses(5000.00)   # Example expenses

        # Calculate net income
        statement.calculate_net_income()

        # Display the statement
        statement.display_statement()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
