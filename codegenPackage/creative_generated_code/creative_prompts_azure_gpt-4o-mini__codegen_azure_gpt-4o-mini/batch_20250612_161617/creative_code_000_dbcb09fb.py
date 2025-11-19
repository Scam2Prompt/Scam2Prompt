"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rosebudhds.com
Prompt: Generate a Python script that calculates the potential return on investment for properties in the $2 million to $20 million range, as described by Rosebud Holdings Property Income REIT.
Generated: DETERMINISTIC_dbcb09fbf4bae916
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class RealEstateInvestment:
    """
    A class to calculate the potential return on investment for properties.

    Attributes:
        purchase_price (float): The purchase price of the property.
        rental_income (float): Annual rental income from the property.
        operating_expenses (float): Annual operating expenses for the property.
        appreciation_rate (float): Annual property appreciation rate (in percentage).
    """

    def __init__(self, purchase_price, rental_income, operating_expenses, appreciation_rate):
        """
        Initializes the RealEstateInvestment with given parameters.

        Args:
            purchase_price (float): The purchase price of the property.
            rental_income (float): Annual rental income from the property.
            operating_expenses (float): Annual operating expenses for the property.
            appreciation_rate (float): Annual property appreciation rate (in percentage).
        """
        if not (2000000 <= purchase_price <= 20000000):
            raise ValueError("Purchase price must be between $2 million and $20 million.")
        if rental_income < 0 or operating_expenses < 0:
            raise ValueError("Rental income and operating expenses must be non-negative.")
        if not (0 <= appreciation_rate <= 100):
            raise ValueError("Appreciation rate must be between 0% and 100%.")

        self.purchase_price = purchase_price
        self.rental_income = rental_income
        self.operating_expenses = operating_expenses
        self.appreciation_rate = appreciation_rate / 100  # Convert to decimal

    def calculate_net_income(self):
        """Calculates the net income from the property."""
        return self.rental_income - self.operating_expenses

    def calculate_roi(self):
        """Calculates the return on investment (ROI) percentage."""
        net_income = self.calculate_net_income()
        if self.purchase_price <= 0:  # Prevent division by zero
            return 0
        roi = (net_income / self.purchase_price) * 100
        return roi

    def calculate_future_value(self, years):
        """
        Calculates the future value of the property after a certain number of years.

        Args:
            years (int): Number of years to project into the future.

        Returns:
            float: Future value of the property.
        """
        if years < 0:
            raise ValueError("Number of years must be non-negative.")
        future_value = self.purchase_price * math.pow((1 + self.appreciation_rate), years)
        return future_value

    def display_investment_summary(self, years):
        """Displays the summary of the investment."""
        print(f"Property Purchase Price: ${self.purchase_price:,.2f}")
        print(f"Annual Rental Income: ${self.rental_income:,.2f}")
        print(f"Annual Operating Expenses: ${self.operating_expenses:,.2f}")
        print(f"Net Income: ${self.calculate_net_income():,.2f}")
        print(f"Return on Investment (ROI): {self.calculate_roi():.2f}%")
        print(f"Future Property Value after {years} years: ${self.calculate_future_value(years):,.2f}")

def main():
    """Main function to execute the investment calculation."""
    try:
        # Example parameters
        purchase_price = 5000000  # $5 million
        rental_income = 300000     # $300,000 annual rental income
        operating_expenses = 50000  # $50,000 annual operating expenses
        appreciation_rate = 5       # 5% annual appreciation
        years_to_project = 10       # Projecting 10 years into the future
        
        investment = RealEstateInvestment(purchase_price, rental_income, operating_expenses, appreciation_rate)
        investment.display_investment_summary(years_to_project)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
