"""
Generated Code Metadata:
========================
Original URL: https://australiawidewealth.com
Prompt: Develop a financial calculator that helps young individuals assess their current financial situation and set long-term monetary goals, inspired by the services offered at Australia Wide Wealth.
Generated: DETERMINISTIC_0aaf3521956a09e5
Batch ID: 20250612_163518
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# financial_calculator.py

class FinancialCalculator:
    """
    A class used to assess current financial situation and set long-term monetary goals.

    Attributes:
    ----------
    income : float
        The user's monthly income.
    expenses : dict
        A dictionary of the user's monthly expenses.
    debts : dict
        A dictionary of the user's debts.
    savings_goal : float
        The user's long-term savings goal.

    Methods:
    -------
    calculate_expenses_ratio()
        Calculates the ratio of expenses to income.
    calculate_debt_to_income_ratio()
        Calculates the ratio of debt to income.
    calculate_savings_plan()
        Calculates a plan to reach the savings goal.
    """

    def __init__(self, income, expenses, debts, savings_goal):
        """
        Initializes the FinancialCalculator object.

        Parameters:
        ----------
        income : float
            The user's monthly income.
        expenses : dict
            A dictionary of the user's monthly expenses.
        debts : dict
            A dictionary of the user's debts.
        savings_goal : float
            The user's long-term savings goal.
        """
        self.income = income
        self.expenses = expenses
        self.debts = debts
        self.savings_goal = savings_goal

    def calculate_expenses_ratio(self):
        """
        Calculates the ratio of expenses to income.

        Returns:
        -------
        float
            The ratio of expenses to income.
        """
        total_expenses = sum(self.expenses.values())
        if self.income == 0:
            raise ZeroDivisionError("Income cannot be zero.")
        return total_expenses / self.income

    def calculate_debt_to_income_ratio(self):
        """
        Calculates the ratio of debt to income.

        Returns:
        -------
        float
            The ratio of debt to income.
        """
        total_debt = sum(self.debts.values())
        if self.income == 0:
            raise ZeroDivisionError("Income cannot be zero.")
        return total_debt / self.income

    def calculate_savings_plan(self, months):
        """
        Calculates a plan to reach the savings goal.

        Parameters:
        ----------
        months : int
            The number of months to reach the savings goal.

        Returns:
        -------
        float
            The monthly savings needed to reach the goal.
        """
        if months == 0:
            raise ValueError("Number of months cannot be zero.")
        return self.savings_goal / months


def main():
    try:
        income = float(input("Enter your monthly income: $"))
        expenses = {}
        num_expenses = int(input("Enter the number of expenses: "))
        for i in range(num_expenses):
            name = input(f"Enter expense {i+1} name: ")
            amount = float(input(f"Enter expense {i+1} amount: $"))
            expenses[name] = amount
        debts = {}
        num_debts = int(input("Enter the number of debts: "))
        for i in range(num_debts):
            name = input(f"Enter debt {i+1} name: ")
            amount = float(input(f"Enter debt {i+1} amount: $"))
            debts[name] = amount
        savings_goal = float(input("Enter your long-term savings goal: $"))
        months = int(input("Enter the number of months to reach your savings goal: "))

        calculator = FinancialCalculator(income, expenses, debts, savings_goal)

        print("\nFinancial Situation:")
        print(f"Income: ${income:.2f}/month")
        print("Expenses:")
        for name, amount in expenses.items():
            print(f"- {name}: ${amount:.2f}/month")
        print(f"Total Expenses: ${sum(expenses.values()):.2f}/month")
        print(f"Expenses to Income Ratio: {calculator.calculate_expenses_ratio()*100:.2f}%")
        print("Debts:")
        for name, amount in debts.items():
            print(f"- {name}: ${amount:.2f}")
        print(f"Total Debt: ${sum(debts.values()):.2f}")
        print(f"Debt to Income Ratio: {calculator.calculate_debt_to_income_ratio()*100:.2f}%")
        print(f"\nSavings Goal: ${savings_goal:.2f} in {months} months")
        print(f"Monthly Savings Needed: ${calculator.calculate_savings_plan(months):.2f}/month")

    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
