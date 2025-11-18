"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://battlebarkers.app
Prompt: Create a script to calculate the potential income from dividend-paying stocks or rental properties, aligning with the income generation strategies on Investolazlo.
Generated: DETERMINISTIC_03507fcf00853342
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class IncomeGenerator:
    """
    A class to calculate potential income from dividend-paying stocks 
    and rental properties.
    """

    def __init__(self):
        self.investments = []

    def add_dividend_stock(self, name, shares, dividend_per_share):
        """
        Adds a dividend-paying stock to the investments list.

        :param name: str - The name of the stock
        :param shares: int - The number of shares owned
        :param dividend_per_share: float - The annual dividend per share
        """
        try:
            dividend_income = shares * dividend_per_share
            self.investments.append({
                'type': 'dividend_stock',
                'name': name,
                'shares': shares,
                'dividend_per_share': dividend_per_share,
                'annual_income': dividend_income
            })
        except Exception as e:
            print(f"Error adding dividend stock: {e}")

    def add_rental_property(self, name, monthly_rent, expenses):
        """
        Adds a rental property to the investments list.

        :param name: str - The name of the property
        :param monthly_rent: float - The monthly rent of the property
        :param expenses: float - The monthly expenses associated with the property
        """
        try:
            net_monthly_income = monthly_rent - expenses
            annual_income = net_monthly_income * 12
            self.investments.append({
                'type': 'rental_property',
                'name': name,
                'monthly_rent': monthly_rent,
                'expenses': expenses,
                'annual_income': annual_income
            })
        except Exception as e:
            print(f"Error adding rental property: {e}")

    def calculate_total_income(self):
        """
        Calculates the total annual income from all investments.

        :return: float - The total annual income
        """
        try:
            total_income = sum(investment['annual_income'] for investment in self.investments)
            return total_income
        except Exception as e:
            print(f"Error calculating total income: {e}")
            return 0.0

    def display_investments(self):
        """
        Displays all investments and their annual income.
        """
        for investment in self.investments:
            print(f"{investment['type'].capitalize()} - {investment['name']}: "
                  f"${investment['annual_income']:,.2f} annual income")

# Example Usage
if __name__ == "__main__":
    income_generator = IncomeGenerator()
    
    # Add dividend stocks
    income_generator.add_dividend_stock(name='XYZ Corp', shares=100, dividend_per_share=2.5)
    income_generator.add_dividend_stock(name='ABC Inc', shares=50, dividend_per_share=1.8)

    # Add rental properties
    income_generator.add_rental_property(name='Downtown Apartment', monthly_rent=1500, expenses=300)
    income_generator.add_rental_property(name='Suburban House', monthly_rent=2000, expenses=400)

    # Display investments
    income_generator.display_investments()

    # Calculate and display total income
    total_income = income_generator.calculate_total_income()
    print(f"Total Annual Income: ${total_income:,.2f}")
```
