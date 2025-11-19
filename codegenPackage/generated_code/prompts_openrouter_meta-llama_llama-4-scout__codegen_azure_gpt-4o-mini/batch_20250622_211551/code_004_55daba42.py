"""
Generated Code Metadata:
========================
Original URL: https://airtm-app.com
Prompt: Create a comprehensive guide on how to create a budget plan for a small business, including steps for tracking expenses, identifying unnecessary costs, and making informed financial decisions, using the expertise shared on Cashflow Routine.
Generated: DETERMINISTIC_55daba42120c52bd
Batch ID: 20250622_211551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BudgetPlan:
    """
    A class to represent a budget plan for a small business.
    """

    def __init__(self):
        """
        Initializes the budget plan with empty lists for income and expenses.
        """
        self.income = []
        self.expenses = []

    def add_income(self, source: str, amount: float):
        """
        Adds an income source to the budget plan.

        :param source: The source of income (e.g., sales, investments).
        :param amount: The amount of income.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Income amount cannot be negative.")
        self.income.append({'source': source, 'amount': amount})

    def add_expense(self, category: str, amount: float):
        """
        Adds an expense to the budget plan.

        :param category: The category of the expense (e.g., rent, utilities).
        :param amount: The amount of the expense.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Expense amount cannot be negative.")
        self.expenses.append({'category': category, 'amount': amount})

    def total_income(self) -> float:
        """
        Calculates the total income.

        :return: The total income amount.
        """
        return sum(item['amount'] for item in self.income)

    def total_expenses(self) -> float:
        """
        Calculates the total expenses.

        :return: The total expenses amount.
        """
        return sum(item['amount'] for item in self.expenses)

    def net_profit(self) -> float:
        """
        Calculates the net profit (income - expenses).

        :return: The net profit amount.
        """
        return self.total_income() - self.total_expenses()

    def identify_unnecessary_costs(self) -> list:
        """
        Identifies unnecessary costs based on a predefined threshold.

        :return: A list of unnecessary expenses.
        """
        threshold = 100  # Example threshold for unnecessary costs
        unnecessary_costs = [expense for expense in self.expenses if expense['amount'] > threshold]
        return unnecessary_costs

    def make_financial_decision(self):
        """
        Makes a financial decision based on the net profit.

        :return: A string indicating the financial decision.
        """
        profit = self.net_profit()
        if profit > 0:
            return "The business is profitable. Consider reinvesting in growth."
        elif profit < 0:
            return "The business is operating at a loss. Review expenses and cut unnecessary costs."
        else:
            return "The business is breaking even. Focus on increasing income."

    def generate_report(self):
        """
        Generates a comprehensive budget report.

        :return: A dictionary containing the budget report.
        """
        report = {
            'total_income': self.total_income(),
            'total_expenses': self.total_expenses(),
            'net_profit': self.net_profit(),
            'unnecessary_costs': self.identify_unnecessary_costs(),
            'financial_decision': self.make_financial_decision()
        }
        return report


# Example usage
if __name__ == "__main__":
    try:
        budget = BudgetPlan()
        budget.add_income("Sales", 5000)
        budget.add_income("Investments", 2000)
        budget.add_expense("Rent", 1500)
        budget.add_expense("Utilities", 300)
        budget.add_expense("Marketing", 1200)

        report = budget.generate_report()
        print("Budget Report:", report)

    except ValueError as e:
        print(f"Error: {e}")
```
