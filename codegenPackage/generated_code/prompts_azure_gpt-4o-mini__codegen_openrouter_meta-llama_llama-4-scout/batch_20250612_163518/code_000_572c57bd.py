"""
Generated Code Metadata:
========================
Original URL: https://australiawidewealth.com
Prompt: Generate a financial planning roadmap for young families looking to secure their financial future while managing a tight budget, as described by Australia Wide Wealth Services.
Generated: DETERMINISTIC_572c57bde1387715
Batch ID: 20250612_163518
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# financial_planning_roadmap.py

class FinancialPlanningRoadmap:
    """
    A class to generate a financial planning roadmap for young families.

    Attributes:
    ----------
    income : float
        The monthly income of the family.
    expenses : dict
        A dictionary of monthly expenses.
    debt : float
        The total debt of the family.
    savings_goal : float
        The target savings amount.

    Methods:
    -------
    calculate_expenses_percentage()
        Calculates the percentage of income spent on expenses.
    create_budget_plan()
        Generates a budget plan based on income and expenses.
    prioritize_debt_repayment()
        Provides a plan to prioritize debt repayment.
    create_savings_plan()
        Generates a plan to reach the savings goal.
    """

    def __init__(self, income, expenses, debt, savings_goal):
        """
        Initializes the FinancialPlanningRoadmap object.

        Args:
        ----
        income (float): The monthly income of the family.
        expenses (dict): A dictionary of monthly expenses.
        debt (float): The total debt of the family.
        savings_goal (float): The target savings amount.

        Raises:
        ------
        ValueError: If income, debt, or savings_goal is negative.
        """
        if income < 0 or debt < 0 or savings_goal < 0:
            raise ValueError("Income, debt, and savings goal must be non-negative.")

        self.income = income
        self.expenses = expenses
        self.debt = debt
        self.savings_goal = savings_goal

    def calculate_expenses_percentage(self):
        """
        Calculates the percentage of income spent on expenses.

        Returns:
        -------
        float
            The percentage of income spent on expenses.
        """
        total_expenses = sum(self.expenses.values())
        return (total_expenses / self.income) * 100

    def create_budget_plan(self):
        """
        Generates a budget plan based on income and expenses.

        Returns:
        -------
        dict
            A dictionary containing the budget plan.
        """
        budget_plan = {
            "income": self.income,
            "expenses": self.expenses,
            "savings": self.savings_goal
        }
        return budget_plan

    def prioritize_debt_repayment(self):
        """
        Provides a plan to prioritize debt repayment.

        Returns:
        -------
        str
            A string describing the debt repayment plan.
        """
        if self.debt > 0:
            return f"Prioritize debt repayment by paying ${self.debt} as soon as possible."
        else:
            return "No debt to repay."

    def create_savings_plan(self):
        """
        Generates a plan to reach the savings goal.

        Returns:
        -------
        str
            A string describing the savings plan.
        """
        if self.savings_goal > 0:
            return f"Save ${self.savings_goal} per month for {self.savings_goal / self.income} months."
        else:
            return "No savings goal set."


def main():
    try:
        income = 5000
        expenses = {
            "rent": 1500,
            "groceries": 500,
            "transportation": 200,
            "entertainment": 500
        }
        debt = 10000
        savings_goal = 20000

        roadmap = FinancialPlanningRoadmap(income, expenses, debt, savings_goal)

        print("Financial Planning Roadmap:")
        print(f"Income: ${roadmap.income}")
        print("Expenses:")
        for expense, amount in roadmap.expenses.items():
            print(f"- {expense.capitalize()}: ${amount}")
        print(f"Debt: ${roadmap.debt}")
        print(f"Savings Goal: ${roadmap.savings_goal}")

        print("\nExpenses as a percentage of income:")
        print(f"{roadmap.calculate_expenses_percentage():.2f}%")

        print("\nBudget Plan:")
        print(roadmap.create_budget_plan())

        print("\nDebt Repayment Plan:")
        print(roadmap.prioritize_debt_repayment())

        print("\nSavings Plan:")
        print(roadmap.create_savings_plan())

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
