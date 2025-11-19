"""
Generated Code Metadata:
========================
Original URL: https://beboldproperties.com
Prompt: Develop a case study on the effectiveness of Bebold Properties' proactive approach to property management in generating a strong income stream and supporting long-term capital growth for investors.
Generated: DETERMINISTIC_524762805e6d11b6
Batch ID: 20250622_211816
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
import numpy as np
import matplotlib.pyplot as plt

# Define a class to represent a property
class Property:
    def __init__(self, name, purchase_price, rental_income, expenses, growth_rate):
        """
        Initialize a Property object.

        Args:
            name (str): Name of the property.
            purchase_price (float): Purchase price of the property.
            rental_income (float): Monthly rental income of the property.
            expenses (float): Monthly expenses of the property.
            growth_rate (float): Annual growth rate of the property's value.
        """
        self.name = name
        self.purchase_price = purchase_price
        self.rental_income = rental_income
        self.expenses = expenses
        self.growth_rate = growth_rate

    def calculate_cash_flow(self):
        """
        Calculate the monthly cash flow of the property.

        Returns:
            float: Monthly cash flow.
        """
        return self.rental_income - self.expenses

    def calculate_annual_appreciation(self):
        """
        Calculate the annual appreciation of the property's value.

        Returns:
            float: Annual appreciation.
        """
        return self.purchase_price * (self.growth_rate / 100)

# Define a class to represent a portfolio of properties
class Portfolio:
    def __init__(self):
        """
        Initialize a Portfolio object.
        """
        self.properties = []

    def add_property(self, property):
        """
        Add a property to the portfolio.

        Args:
            property (Property): Property to add.
        """
        self.properties.append(property)

    def calculate_total_cash_flow(self):
        """
        Calculate the total monthly cash flow of the portfolio.

        Returns:
            float: Total monthly cash flow.
        """
        return sum(property.calculate_cash_flow() for property in self.properties)

    def calculate_total_annual_appreciation(self):
        """
        Calculate the total annual appreciation of the portfolio.

        Returns:
            float: Total annual appreciation.
        """
        return sum(property.calculate_annual_appreciation() for property in self.properties)

# Define a function to simulate a portfolio's performance over time
def simulate_portfolio_performance(portfolio, years):
    """
    Simulate a portfolio's performance over a specified number of years.

    Args:
        portfolio (Portfolio): Portfolio to simulate.
        years (int): Number of years to simulate.

    Returns:
        pd.DataFrame: DataFrame containing the portfolio's performance over time.
    """
    performance_data = {
        'Year': range(years + 1),
        'Total Cash Flow': [0] * (years + 1),
        'Total Appreciation': [0] * (years + 1),
        'Total Value': [0] * (years + 1)
    }

    total_value = sum(property.purchase_price for property in portfolio.properties)

    for year in range(years + 1):
        performance_data['Total Cash Flow'][year] = portfolio.calculate_total_cash_flow() * 12
        performance_data['Total Appreciation'][year] = portfolio.calculate_total_annual_appreciation()
        performance_data['Total Value'][year] = total_value + (portfolio.calculate_total_annual_appreciation() * year)

    return pd.DataFrame(performance_data)

# Create properties
property1 = Property('Property 1', 500000, 2500, 1000, 5)
property2 = Property('Property 2', 750000, 3500, 1500, 7)

# Create a portfolio and add properties
portfolio = Portfolio()
portfolio.add_property(property1)
portfolio.add_property(property2)

# Simulate portfolio performance
performance_data = simulate_portfolio_performance(portfolio, 10)

# Print performance data
print(performance_data)

# Plot performance data
plt.figure(figsize=(10,6))
plt.plot(performance_data['Year'], performance_data['Total Cash Flow'], label='Total Cash Flow')
plt.plot(performance_data['Year'], performance_data['Total Appreciation'], label='Total Appreciation')
plt.plot(performance_data['Year'], performance_data['Total Value'], label='Total Value')
plt.xlabel('Year')
plt.ylabel('Amount ($)')
plt.title('Portfolio Performance Over Time')
plt.legend()
plt.show()
```
