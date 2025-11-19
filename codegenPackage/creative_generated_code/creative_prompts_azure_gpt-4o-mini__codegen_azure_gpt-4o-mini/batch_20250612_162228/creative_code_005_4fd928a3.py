"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icchatva.com
Prompt: Construct a financial planning tool in Python that reflects the financial consultancy services offered by Icchatva.
Generated: DETERMINISTIC_4fd928a38f2ceba4
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Budget:
    """A class to represent a monthly budget."""
    
    def __init__(self, income, expenses):
        """
        Initialize the Budget object.
        
        :param income: Total income for the month
        :param expenses: Dictionary of expenses categorized
        """
        self.income = income
        self.expenses = expenses
        self.total_expenses = sum(expenses.values())
        self.savings = self.calculate_savings()
    
    def calculate_savings(self):
        """Calculate total savings for the month."""
        return self.income - self.total_expenses
    
    def display_summary(self):
        """Display the budget summary."""
        print("Budget Summary:")
        print(f"Total Income: ${self.income:.2f}")
        print("Expenses:")
        for category, amount in self.expenses.items():
            print(f"  - {category}: ${amount:.2f}")
        print(f"Total Expenses: ${self.total_expenses:.2f}")
        print(f"Savings: ${self.savings:.2f}")

class Investment:
    """A class to represent an investment portfolio."""
    
    def __init__(self):
        """Initialize the investment portfolio."""
        self.portfolio = {}
    
    def add_investment(self, asset, amount):
        """
        Add an investment to the portfolio.
        
        :param asset: Name of the investment asset
        :param amount: Amount invested
        """
        if asset in self.portfolio:
            self.portfolio[asset] += amount
        else:
            self.portfolio[asset] = amount
    
    def display_portfolio(self):
        """Display the investment portfolio."""
        print("Investment Portfolio:")
        for asset, amount in self.portfolio.items():
            print(f"  - {asset}: ${amount:.2f}")

class FinancialPlan:
    """A class to represent a financial plan."""
    
    def __init__(self, budget, investments):
        """
        Initialize the FinancialPlan object.
        
        :param budget: A Budget object
        :param investments: An Investment object
        """
        self.budget = budget
        self.investments = investments
    
    def display_financial_plan(self):
        """Display the complete financial plan."""
        self.budget.display_summary()
        self.investments.display_portfolio()

def main():
    """Main function to run the financial planning tool."""
    try:
        # User inputs for budget
        income = float(input("Enter your total monthly income: "))
        expenses = {}
        while True:
            category = input("Enter expense category (or 'done' to finish): ")
            if category.lower() == 'done':
                break
            amount = float(input(f"Enter amount for {category}: "))
            expenses[category] = amount
        
        # Create Budget and Investment objects
        budget = Budget(income, expenses)
        investments = Investment()

        # User inputs for investments
        while True:
            asset = input("Enter investment asset (or 'done' to finish): ")
            if asset.lower() == 'done':
                break
            amount = float(input(f"Enter amount to invest in {asset}: "))
            investments.add_investment(asset, amount)

        # Create FinancialPlan and display it
        financial_plan = FinancialPlan(budget, investments)
        financial_plan.display_financial_plan()

    except ValueError as e:
        print(f"Error: {e}. Please enter valid numerical values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
