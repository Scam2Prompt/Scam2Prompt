"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alghanim-capital.com
Prompt: Generate code using a financial analysis library to simulate wealth management strategies that align with Alghanim Capital's focus on safeguarding financial futures and achieving personalized goals.
Generated: DETERMINISTIC_d7efe8281313f7d7
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

class WealthManagementStrategy:
    """
    A class to simulate wealth management strategies for safeguarding financial futures
    and achieving personalized goals.
    """

    def __init__(self, initial_investment, risk_tolerance, investment_horizon):
        """
        Initializes the wealth management strategy with user-defined parameters.

        Parameters:
        initial_investment (float): Initial amount of money to invest.
        risk_tolerance (str): User's risk tolerance - low, medium, or high.
        investment_horizon (int): Number of years for investment.
        """
        self.initial_investment = initial_investment
        self.risk_tolerance = risk_tolerance
        self.investment_horizon = investment_horizon
        self.asset_allocations = self.set_asset_allocations()
        
    def set_asset_allocations(self):
        """
        Sets asset allocations based on risk tolerance.

        Returns:
        dict: Asset allocations for equities, bonds, and cash.
        """
        allocations = {
            'low': {'equities': 0.2, 'bonds': 0.7, 'cash': 0.1},
            'medium': {'equities': 0.5, 'bonds': 0.4, 'cash': 0.1},
            'high': {'equities': 0.8, 'bonds': 0.1, 'cash': 0.1},
        }
        return allocations.get(self.risk_tolerance, allocations['medium'])

    def simulate_growth(self):
        """
        Simulates the growth of the investment over the defined investment horizon.

        Returns:
        dict: A dictionary with yearly values of the investment.
        """
        yearly_values = {}
        current_value = self.initial_investment

        for year in range(1, self.investment_horizon + 1):
            annual_return = self.calculate_annual_return()
            current_value *= (1 + annual_return)
            yearly_values[year] = current_value

        return yearly_values

    def calculate_annual_return(self):
        """
        Calculates the expected annual return based on asset allocations.

        Returns:
        float: Expected annual return rate.
        """
        # Example return rates for each asset class
        return_rates = {
            'equities': 0.08,  # 8%
            'bonds': 0.03,     # 3%
            'cash': 0.01       # 1%
        }

        expected_return = sum(
            self.asset_allocations[asset] * return_rates[asset]
            for asset in self.asset_allocations
        )
        return expected_return

    def plot_growth(self, yearly_values):
        """
        Plots the growth of the investment over the investment horizon.

        Parameters:
        yearly_values (dict): A dictionary with yearly investment values.
        """
        years = list(yearly_values.keys())
        values = list(yearly_values.values())

        plt.figure(figsize=(10, 6))
        plt.plot(years, values, marker='o')
        plt.title('Investment Growth Over Time')
        plt.xlabel('Years')
        plt.ylabel('Investment Value ($)')
        plt.grid()
        plt.xticks(years)
        plt.show()

def main():
    """
    Main function to execute the wealth management strategy simulation.
    """
    try:
        # User-defined parameters
        initial_investment = float(input("Enter your initial investment amount ($): "))
        risk_tolerance = input("Enter your risk tolerance (low, medium, high): ").lower()
        investment_horizon = int(input("Enter your investment horizon (in years): "))

        # Instantiate the wealth management strategy
        strategy = WealthManagementStrategy(initial_investment, risk_tolerance, investment_horizon)

        # Simulate investment growth
        yearly_values = strategy.simulate_growth()

        # Plot the investment growth
        strategy.plot_growth(yearly_values)

    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
