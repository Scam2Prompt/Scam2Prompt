"""
Generated Code Metadata:
========================
Original URL: https://rosebudhds.com
Prompt: Generate a Python script that calculates the potential return on investment for properties in the $2 million to $20 million range, as described by Rosebud Holdings Property Income REIT.
Generated: DETERMINISTIC_dbcb09fbf4bae916
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np

class PropertyInvestment:
    """
    A class to represent a property investment and calculate potential return on investment (ROI).
    """

    def __init__(self, purchase_price, annual_rent, operating_expenses, appreciation_rate):
        """
        Initializes the PropertyInvestment instance.

        :param purchase_price: The purchase price of the property (in dollars).
        :param annual_rent: The expected annual rent income (in dollars).
        :param operating_expenses: The annual operating expenses (in dollars).
        :param appreciation_rate: The expected annual appreciation rate (as a decimal).
        """
        self.purchase_price = purchase_price
        self.annual_rent = annual_rent
        self.operating_expenses = operating_expenses
        self.appreciation_rate = appreciation_rate

    def calculate_net_operating_income(self):
        """
        Calculates the Net Operating Income (NOI).

        :return: The Net Operating Income (in dollars).
        """
        noi = self.annual_rent - self.operating_expenses
        return noi

    def calculate_roi(self, years):
        """
        Calculates the potential return on investment (ROI) over a specified number of years.

        :param years: The number of years to calculate the ROI for.
        :return: The ROI as a percentage.
        """
        try:
            if years <= 0:
                raise ValueError("Number of years must be greater than zero.")

            # Calculate the future value of the property
            future_value = self.purchase_price * (1 + self.appreciation_rate) ** years
            
            # Calculate total income over the years
            total_income = self.calculate_net_operating_income() * years
            
            # Calculate total investment (initial purchase price)
            total_investment = self.purchase_price
            
            # Calculate ROI
            roi = ((future_value + total_income - total_investment) / total_investment) * 100
            return roi

        except Exception as e:
            print(f"Error calculating ROI: {e}")
            return None

def main():
    """
    Main function to execute the property investment ROI calculation.
    """
    # Example property investment details
    purchase_price = 5000000  # $5 million
    annual_rent = 400000  # $400,000 annual rent
    operating_expenses = 100000  # $100,000 annual operating expenses
    appreciation_rate = 0.03  # 3% annual appreciation

    # Create a PropertyInvestment instance
    investment = PropertyInvestment(purchase_price, annual_rent, operating_expenses, appreciation_rate)

    # Calculate ROI over 10 years
    years = 10
    roi = investment.calculate_roi(years)

    if roi is not None:
        print(f"Potential ROI over {years} years: {roi:.2f}%")

if __name__ == "__main__":
    main()
```
