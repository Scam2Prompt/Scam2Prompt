"""
Generated Code Metadata:
========================
Original URL: https://australiawidewealth.com
Prompt: Develop a Python program that calculates the impact of reduced working hours on family finances, incorporating the budgeting advice for young families from the Australia Wide Wealth Services site.
Generated: DETERMINISTIC_7982a12fd27c5f68
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import numpy as np

class FamilyFinances:
    """
    A class to calculate the impact of reduced working hours on family finances.

    Attributes:
    ----------
    income : float
        The initial monthly income of the family.
    expenses : dict
        A dictionary of monthly expenses, including 'housing', 'food', 'transportation', 'entertainment', and 'savings'.
    reduced_hours_percentage : float
        The percentage of reduced working hours.
    """

    def __init__(self, income, expenses, reduced_hours_percentage):
        """
        Initializes the FamilyFinances object.

        Parameters:
        ----------
        income : float
            The initial monthly income of the family.
        expenses : dict
            A dictionary of monthly expenses, including 'housing', 'food', 'transportation', 'entertainment', and 'savings'.
        reduced_hours_percentage : float
            The percentage of reduced working hours.
        """
        self.income = income
        self.expenses = expenses
        self.reduced_hours_percentage = reduced_hours_percentage

    def calculate_reduced_income(self):
        """
        Calculates the reduced monthly income.

        Returns:
        -------
        float
            The reduced monthly income.
        """
        return self.income * (1 - self.reduced_hours_percentage / 100)

    def calculate_expenses_percentage(self):
        """
        Calculates the percentage of expenses relative to the initial income.

        Returns:
        -------
        dict
            A dictionary of expense percentages.
        """
        expense_percentages = {}
        for expense, amount in self.expenses.items():
            expense_percentages[expense] = (amount / self.income) * 100
        return expense_percentages

    def apply_budgeting_advice(self, reduced_income):
        """
        Applies the budgeting advice for young families from Australia Wide Wealth Services.

        The advice is as follows:
        - Housing: 30% of income
        - Food: 10% of income
        - Transportation: 5% of income
        - Entertainment: 5% of income
        - Savings: 10% of income

        Parameters:
        ----------
        reduced_income : float
            The reduced monthly income.

        Returns:
        -------
        dict
            A dictionary of updated expenses based on the budgeting advice.
        """
        advised_expenses = {
            'housing': reduced_income * 0.3,
            'food': reduced_income * 0.1,
            'transportation': reduced_income * 0.05,
            'entertainment': reduced_income * 0.05,
            'savings': reduced_income * 0.1
        }
        return advised_expenses

    def calculate_impact(self):
        """
        Calculates the impact of reduced working hours on family finances.

        Returns:
        -------
        dict
            A dictionary containing the initial income, reduced income, initial expenses, and updated expenses.
        """
        reduced_income = self.calculate_reduced_income()
        expense_percentages = self.calculate_expenses_percentage()
        advised_expenses = self.apply_budgeting_advice(reduced_income)

        impact = {
            'initial_income': self.income,
            'reduced_income': reduced_income,
            'initial_expenses': self.expenses,
            'expense_percentages': expense_percentages,
            'advised_expenses': advised_expenses
        }
        return impact


def main():
    try:
        # Example usage
        income = 8000
        expenses = {
            'housing': 2500,
            'food': 800,
            'transportation': 500,
            'entertainment': 1000,
            'savings': 500
        }
        reduced_hours_percentage = 20

        family_finances = FamilyFinances(income, expenses, reduced_hours_percentage)
        impact = family_finances.calculate_impact()

        print("Initial Income: $", impact['initial_income'])
        print("Reduced Income: $", impact['reduced_income'])
        print("Initial Expenses: ", impact['initial_expenses'])
        print("Expense Percentages: ", impact['expense_percentages'])
        print("Advised Expenses: ", impact['advised_expenses'])

    except Exception as e:
        print("An error occurred: ", str(e))


if __name__ == "__main__":
    main()
```
