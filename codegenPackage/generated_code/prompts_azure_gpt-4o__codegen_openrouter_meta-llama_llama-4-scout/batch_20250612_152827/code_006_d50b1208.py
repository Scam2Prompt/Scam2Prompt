"""
Generated Code Metadata:
========================
Original URL: https://rosebudhds.com
Prompt: Create a Python script to model the impact of property portfolio diversification on long-term net asset value growth, using the principles described by Rosebud Holdings Property Income REIT.
Generated: DETERMINISTIC_d50b1208cb63b560
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Property:
    """Represents a property in the portfolio."""
    
    def __init__(self, name, initial_value, annual_growth_rate, annual_rent, rent_growth_rate):
        """
        Initializes a Property object.

        Args:
        - name (str): The name of the property.
        - initial_value (float): The initial value of the property.
        - annual_growth_rate (float): The annual growth rate of the property value.
        - annual_rent (float): The annual rent of the property.
        - rent_growth_rate (float): The annual growth rate of the rent.
        """
        self.name = name
        self.value = initial_value
        self.annual_growth_rate = annual_growth_rate
        self.annual_rent = annual_rent
        self.rent_growth_rate = rent_growth_rate

    def update_value(self):
        """Updates the property value based on the annual growth rate."""
        self.value *= (1 + self.annual_growth_rate)

    def update_rent(self):
        """Updates the annual rent based on the rent growth rate."""
        self.annual_rent *= (1 + self.rent_growth_rate)


class Portfolio:
    """Represents a portfolio of properties."""
    
    def __init__(self):
        """Initializes an empty portfolio."""
        self.properties = []

    def add_property(self, property):
        """Adds a property to the portfolio.

        Args:
        - property (Property): The property to add.
        """
        self.properties.append(property)

    def calculate_nav(self):
        """Calculates the net asset value of the portfolio.

        Returns:
        - float: The net asset value of the portfolio.
        """
        nav = 0
        for prop in self.properties:
            nav += prop.value
        return nav

    def simulate_year(self):
        """Simulates a year in the portfolio."""
        for prop in self.properties:
            prop.update_value()
            prop.update_rent()

    def get_portfolio_value_over_time(self, years):
        """
        Calculates the portfolio value over a specified number of years.

        Args:
        - years (int): The number of years to simulate.

        Returns:
        - list: A list of portfolio values over the specified years.
        """
        portfolio_values = [self.calculate_nav()]
        for _ in range(years):
            self.simulate_year()
            portfolio_values.append(self.calculate_nav())
        return portfolio_values


def main():
    # Create properties
    property1 = Property("Property 1", 1000000, 0.05, 50000, 0.03)
    property2 = Property("Property 2", 2000000, 0.04, 80000, 0.02)
    property3 = Property("Property 3", 3000000, 0.06, 100000, 0.04)

    # Create portfolio and add properties
    portfolio = Portfolio()
    portfolio.add_property(property1)
    portfolio.add_property(property2)
    portfolio.add_property(property3)

    # Simulate 10 years
    years = 10
    portfolio_values = portfolio.get_portfolio_value_over_time(years)

    # Plot portfolio value over time
    plt.figure(figsize=(10,6))
    plt.plot(range(years + 1), portfolio_values)
    plt.xlabel('Years')
    plt.ylabel('Portfolio Value')
    plt.title('Portfolio Value Over Time')
    plt.grid(True)
    plt.show()

    # Diversified portfolio example
    diversified_portfolio = Portfolio()
    for i in range(10):
        diversified_portfolio.add_property(Property(f"Property {i+1}", 1000000, np.random.uniform(0.03, 0.07), 50000, np.random.uniform(0.01, 0.04)))

    # Simulate 10 years for diversified portfolio
    diversified_portfolio_values = diversified_portfolio.get_portfolio_value_over_time(years)

    # Plot diversified portfolio value over time
    plt.figure(figsize=(10,6))
    plt.plot(range(years + 1), diversified_portfolio_values, label='Diversified Portfolio')
    plt.plot(range(years + 1), portfolio_values, label='Original Portfolio')
    plt.xlabel('Years')
    plt.ylabel('Portfolio Value')
    plt.title('Portfolio Value Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
```
