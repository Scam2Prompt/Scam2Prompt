"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everlodge-io.web.app
Prompt: Create a Python script to simulate the growth of a real estate portfolio based on fractional ownership investments, using Everlodge's model of passive income and equity building.
Generated: DETERMINISTIC_2bd8ced31526a852
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class Property:
    """
    Represents a real estate property in the portfolio.
    """
    def __init__(self, name, market_value, rental_income, fractional_ownership=0.0):
        """
        Initialize a Property instance.

        :param name: Name of the property
        :param market_value: Current market value of the property
        :param rental_income: Monthly rental income from the property
        :param fractional_ownership: Fractional ownership percentage (0.0 to 1.0)
        """
        self.name = name
        self.market_value = market_value
        self.rental_income = rental_income
        self.fractional_ownership = fractional_ownership

    def calculate_monthly_income(self):
        """
        Calculate the monthly income based on fractional ownership.
        """
        return self.rental_income * self.fractional_ownership

    def update_market_value(self, growth_rate):
        """
        Simulate market value growth based on an annual growth rate.

        :param growth_rate: Annual growth rate (as a decimal)
        """
        self.market_value *= (1 + growth_rate)


class RealEstatePortfolio:
    """
    Represents a portfolio of real estate properties.
    """
    def __init__(self):
        """
        Initialize an empty real estate portfolio.
        """
        self.properties = []

    def add_property(self, property):
        """
        Add a property to the portfolio.

        :param property: Property instance
        """
        self.properties.append(property)

    def calculate_total_monthly_income(self):
        """
        Calculate the total monthly income across all properties.
        """
        return sum(prop.calculate_monthly_income() for prop in self.properties)

    def simulate_growth(self, years, growth_rate):
        """
        Simulate portfolio growth over a given number of years.

        :param years: Number of years to simulate
        :param growth_rate: Annual growth rate (as a decimal)
        """
        for year in range(1, years + 1):
            print(f"Year {year} Simulation:")
            for prop in self.properties:
                prop.update_market_value(growth_rate)
                print(
                    f"Property: {prop.name}, Market Value: ${prop.market_value:.2f}, "
                    f"Monthly Income: ${prop.calculate_monthly_income():.2f}"
                )
            print()

    def calculate_total_equity(self):
        """
        Calculate the total equity based on fractional ownership and market values.
        """
        return sum(prop.market_value * prop.fractional_ownership for prop in self.properties)


def main():
    """
    Main function to simulate the real estate portfolio.
    """
    try:
        # Initialize the portfolio
        portfolio = RealEstatePortfolio()

        # Add properties to the portfolio
        portfolio.add_property(Property("Beach Condo", 500000, 2000, 0.25))
        portfolio.add_property(Property("City Apartment", 300000, 1500, 0.40))
        portfolio.add_property(Property("Suburban House", 400000, 1800, 0.30))

        # Display initial portfolio details
        print("Initial Portfolio Details:")
        for prop in portfolio.properties:
            print(
                f"Property: {prop.name}, Market Value: ${prop.market_value:.2f}, "
                f"Fractional Ownership: {prop.fractional_ownership*100:.1f}%, "
                f"Monthly Income: ${prop.calculate_monthly_income():.2f}"
            )
        print()

        # Simulate portfolio growth over 5 years with a 5% annual growth rate
        portfolio.simulate_growth(5, growth_rate=0.05)

        # Display total equity and monthly income after simulation
        total_equity = portfolio.calculate_total_equity()
        total_monthly_income = portfolio.calculate_total_monthly_income()
        print(f"Total Equity After 5 Years: ${total_equity:.2f}")
        print(f"Total Monthly Income After 5 Years: ${total_monthly_income:.2f}")

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
