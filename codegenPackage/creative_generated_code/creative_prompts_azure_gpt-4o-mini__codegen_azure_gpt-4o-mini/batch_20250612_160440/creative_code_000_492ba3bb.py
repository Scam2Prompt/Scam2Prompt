"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeinvestmentslimited.org
Prompt: Generate a Python script to automate the process of budgeting for a small business, incorporating financial advisory principles from Finance Investment Limited.
Generated: DETERMINISTIC_492ba3bb0b7ac56f
Batch ID: 20250612_160440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from decimal import Decimal, InvalidOperation

class Budget:
    """
    A class to represent a budget for a small business.
    
    Attributes
    ----------
    income: Decimal
        Total income for the business.
    expenses: dict
        A dictionary to hold the different types of expenses and their amounts.
    savings: Decimal
        Total amount set aside for savings or investments.
    """
    
    def __init__(self):
        self.income = Decimal('0.00')
        self.expenses = {}
        self.savings = Decimal('0.00')

    def set_income(self, amount):
        """
        Set the total income for the budget.
        
        Parameters
        ----------
        amount : str
            The income amount as a string, which will be converted to Decimal.
            
        Raises
        ------
        ValueError
            If the provided amount is not a valid decimal number.
        """
        try:
            self.income = Decimal(amount)
        except InvalidOperation:
            raise ValueError(f"Invalid income amount: {amount}")

    def add_expense(self, category, amount):
        """
        Add an expense to the budget.
        
        Parameters
        ----------
        category : str
            The category of the expense.
        amount : str
            The expense amount as a string, which will be converted to Decimal.
            
        Raises
        ------
        ValueError
            If the provided amount is not a valid decimal number.
        """
        try:
            amount_decimal = Decimal(amount)
            self.expenses[category] = self.expenses.get(category, Decimal('0.00')) + amount_decimal
        except InvalidOperation:
            raise ValueError(f"Invalid expense amount: {amount}")

    def calculate_savings(self):
        """
        Calculate the total savings based on income and expenses.
        
        Returns
        -------
        Decimal
            The total savings amount.
        """
        total_expenses = sum(self.expenses.values())
        self.savings = self.income - total_expenses
        return self.savings

    def to_json(self):
        """
        Convert the budget data to a JSON string.
        
        Returns
        -------
        str
            JSON representation of the budget data.
        """
        budget_data = {
            'income': str(self.income),
            'expenses': {category: str(amount) for category, amount in self.expenses.items()},
            'savings': str(self.savings)
        }
        return json.dumps(budget_data, indent=4)

def main():
    """
    Main function to execute the budgeting process for a small business.
    """
    budget = Budget()
    
    # Set income
    try:
        budget.set_income(input("Enter total income: "))
    except ValueError as e:
        print(e)
        return

    # Add expenses
    while True:
        category = input("Enter expense category (or type 'done' to finish): ")
        if category.lower() == 'done':
            break
        amount = input(f"Enter amount for {category}: ")
        try:
            budget.add_expense(category, amount)
        except ValueError as e:
            print(e)

    # Calculate savings
    savings = budget.calculate_savings()
    print(f"Total savings calculated: {savings:.2f}")

    # Output budget data
    print("Budget details:")
    print(budget.to_json())

if __name__ == '__main__':
    main()
```
