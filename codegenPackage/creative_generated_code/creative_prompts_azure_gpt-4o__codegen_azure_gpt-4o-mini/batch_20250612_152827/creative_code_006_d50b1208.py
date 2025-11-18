"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rosebudhds.com
Prompt: Create a Python script to model the impact of property portfolio diversification on long-term net asset value growth, using the principles described by Rosebud Holdings Property Income REIT.
Generated: DETERMINISTIC_d50b1208cb63b560
Batch ID: 20250612_152827
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

class PropertyPortfolio:
    """
    A class to model a property portfolio and its net asset value (NAV) growth
    based on diversification principles.
    """

    def __init__(self, initial_investment: float, num_properties: int, growth_rate: float):
        """
        Initializes the PropertyPortfolio with an initial investment, number of properties,
        and expected annual growth rate.

        :param initial_investment: The initial investment amount in the portfolio
        :param num_properties: The number of properties in the portfolio
        :param growth_rate: The expected annual growth rate of the NAV
        """
        self.initial_investment = initial_investment
        self.num_properties = num_properties
        self.growth_rate = growth_rate
        self.portfolio_value = initial_investment

    def simulate_growth(self, years: int) -> pd.DataFrame:
        """
        Simulates the growth of the property portfolio over a given number of years.

        :param years: Number of years to simulate growth
        :return: DataFrame containing the year, portfolio value, and NAV growth
        """
        if years < 0:
            raise ValueError("Years must be a non-negative integer.")
        
        # Initialize lists to store results
        years_list = []
        values_list = []
        
        # Simulate growth for each year
        for year in range(years + 1):
            # Calculate the NAV based on the growth rate
            self.portfolio_value *= (1 + self.growth_rate)
            years_list.append(year)
            values_list.append(self.portfolio_value)

        # Create a DataFrame to return results
        results = pd.DataFrame({'Year': years_list, 'Portfolio Value': values_list})
        return results

    def plot_growth(self, results: pd.DataFrame):
        """
        Plots the growth of the property portfolio over time.

        :param results: DataFrame containing the simulation results
        """
        plt.figure(figsize=(10, 6))
        plt.plot(results['Year'], results['Portfolio Value'], marker='o')
        plt.title('Property Portfolio NAV Growth Over Time')
        plt.xlabel('Year')
        plt.ylabel('Portfolio Value (€)')
        plt.grid()
        plt.yscale('log')  # Use log scale for better visualization of growth
        plt.show()

def main():
    """
    Main function to run the property portfolio simulation.
    """
    # Parameters
    initial_investment = 1000000  # Initial investment in Euros
    num_properties = 10            # Number of properties in the portfolio
    growth_rate = 0.05             # Expected annual growth rate (5%)
    years = 20                     # Number of years to simulate

    # Create a PropertyPortfolio instance
    portfolio = PropertyPortfolio(initial_investment, num_properties, growth_rate)

    try:
        # Simulate growth and get results
        results = portfolio.simulate_growth(years)

        # Plot the results
        portfolio.plot_growth(results)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
