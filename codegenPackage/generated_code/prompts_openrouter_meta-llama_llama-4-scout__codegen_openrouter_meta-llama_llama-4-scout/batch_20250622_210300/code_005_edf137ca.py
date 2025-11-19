"""
Generated Code Metadata:
========================
Original URL: https://k.kakenvyf.com
Prompt: Write a code snippet in R or Python to calculate the potential return on investment (ROI) for a portfolio of properties, considering factors like rental income, property appreciation, and operating expenses.
Generated: DETERMINISTIC_edf137cab89de4a7
Batch ID: 20250622_210300
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd

class Property:
    """Represents a property with its financial details."""

    def __init__(self, purchase_price, rental_income, appreciation_rate, operating_expenses):
        """
        Initializes a Property object.

        Args:
            purchase_price (float): The initial purchase price of the property.
            rental_income (float): The annual rental income from the property.
            appreciation_rate (float): The annual appreciation rate of the property's value.
            operating_expenses (float): The annual operating expenses for the property.
        """
        self.purchase_price = purchase_price
        self.rental_income = rental_income
        self.appreciation_rate = appreciation_rate / 100  # Convert to decimal
        self.operating_expenses = operating_expenses

    def calculate_annual_roi(self):
        """
        Calculates the annual return on investment (ROI) for the property.

        Returns:
            float: The annual ROI as a decimal.
        """
        annual_appreciation = self.purchase_price * self.appreciation_rate
        net_operating_income = self.rental_income - self.operating_expenses
        total_return = net_operating_income + annual_appreciation
        roi = total_return / self.purchase_price
        return roi

    def calculate_total_return(self, years):
        """
        Calculates the total return on investment over a specified number of years.

        Args:
            years (int): The number of years to calculate the total return for.

        Returns:
            float: The total return on investment.
        """
        total_return = 0
        current_value = self.purchase_price
        for _ in range(years):
            annual_appreciation = current_value * self.appreciation_rate
            net_operating_income = self.rental_income - self.operating_expenses
            total_return += net_operating_income + annual_appreciation
            current_value += annual_appreciation
        return total_return


class Portfolio:
    """Represents a portfolio of properties."""

    def __init__(self):
        """Initializes an empty portfolio."""
        self.properties = []

    def add_property(self, property):
        """
        Adds a property to the portfolio.

        Args:
            property (Property): The property to add.
        """
        self.properties.append(property)

    def calculate_portfolio_roi(self, years):
        """
        Calculates the total return on investment for the portfolio over a specified number of years.

        Args:
            years (int): The number of years to calculate the total return for.

        Returns:
            float: The total return on investment for the portfolio.
        """
        total_return = 0
        total_investment = 0
        for prop in self.properties:
            total_investment += prop.purchase_price
            total_return += prop.calculate_total_return(years)
        portfolio_roi = total_return / total_investment
        return portfolio_roi


def main():
    try:
        # Create properties
        prop1 = Property(purchase_price=200000, rental_income=20000, appreciation_rate=5, operating_expenses=5000)
        prop2 = Property(purchase_price=300000, rental_income=30000, appreciation_rate=7, operating_expenses=6000)

        # Create portfolio and add properties
        portfolio = Portfolio()
        portfolio.add_property(prop1)
        portfolio.add_property(prop2)

        # Calculate and print ROI
        years = 5
        portfolio_roi = portfolio.calculate_portfolio_roi(years)
        print(f"Portfolio ROI over {years} years: {portfolio_roi * 100:.2f}%")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
