"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-crest.com
Prompt: Write Python code to simulate asset allocation strategies for beginners, incorporating stocks, bonds, and real estate, as described on Immediate Crest V2.
Generated: DETERMINISTIC_fc99abf63bf35d78
Batch ID: 20250612_150854
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

class AssetAllocationSimulator:
    def __init__(self, initial_investment, years, stock_alloc, bond_alloc, real_estate_alloc, 
                 stock_mean_return, bond_mean_return, real_estate_mean_return, 
                 stock_volatility, bond_volatility, real_estate_volatility):
        """
        Initializes the Asset Allocation Simulator with parameters.

        :param initial_investment: Initial amount to invest
        :param years: Number of years to simulate
        :param stock_alloc: Percentage allocation to stocks
        :param bond_alloc: Percentage allocation to bonds
        :param real_estate_alloc: Percentage allocation to real estate
        :param stock_mean_return: Expected mean return for stocks
        :param bond_mean_return: Expected mean return for bonds
        :param real_estate_mean_return: Expected mean return for real estate
        :param stock_volatility: Expected volatility for stocks
        :param bond_volatility: Expected volatility for bonds
        :param real_estate_volatility: Expected volatility for real estate
        """
        
        self.initial_investment = initial_investment
        self.years = years
        self.stock_alloc = stock_alloc
        self.bond_alloc = bond_alloc
        self.real_estate_alloc = real_estate_alloc
        self.stock_mean_return = stock_mean_return
        self.bond_mean_return = bond_mean_return
        self.real_estate_mean_return = real_estate_mean_return
        self.stock_volatility = stock_volatility
        self.bond_volatility = bond_volatility
        self.real_estate_volatility = real_estate_volatility

        # Validate allocations
        self.validate_allocations()

    def validate_allocations(self):
        """Validates that the sum of allocations equals 100%."""
        total_alloc = self.stock_alloc + self.bond_alloc + self.real_estate_alloc
        if total_alloc != 100:
            raise ValueError("Total allocation must be 100%.")

    def simulate(self):
        """
        Simulates the asset allocation over the specified number of years.

        :return: DataFrame with yearly asset values
        """
        # Create an array to hold yearly returns
        annual_returns = np.zeros((self.years, 3))

        # Generate random returns based on mean return and volatility
        for year in range(self.years):
            stock_return = np.random.normal(self.stock_mean_return, self.stock_volatility)
            bond_return = np.random.normal(self.bond_mean_return, self.bond_volatility)
            real_estate_return = np.random.normal(self.real_estate_mean_return, self.real_estate_volatility)
            annual_returns[year] = [stock_return, bond_return, real_estate_return]

        # Calculate portfolio value each year
        portfolio_values = []
        current_value = self.initial_investment
        
        for year_return in annual_returns:
            stock_value = current_value * (self.stock_alloc / 100) * (1 + year_return[0])
            bond_value = current_value * (self.bond_alloc / 100) * (1 + year_return[1])
            real_estate_value = current_value * (self.real_estate_alloc / 100) * (1 + year_return[2])
            current_value = stock_value + bond_value + real_estate_value
            portfolio_values.append(current_value)

        return pd.DataFrame(portfolio_values, columns=["Portfolio Value"])

    def plot_results(self, portfolio_df):
        """
        Plots the results of the simulation.

        :param portfolio_df: DataFrame containing the portfolio values over the years
        """
        plt.figure(figsize=(10, 5))
        plt.plot(portfolio_df.index, portfolio_df["Portfolio Value"], marker='o')
        plt.title('Asset Allocation Simulation Over Time')
        plt.xlabel('Years')
        plt.ylabel('Portfolio Value')
        plt.grid()
        plt.show()


if __name__ == "__main__":
    # Parameters for the simulation
    initial_investment = 10000  # Starting investment
    years = 20  # Simulation duration
    stock_alloc = 60  # Stock allocation percentage
    bond_alloc = 30   # Bond allocation percentage
    real_estate_alloc = 10  # Real estate allocation percentage

    # Expected returns and volatilities (assumed values)
    stock_mean_return = 0.07
    bond_mean_return = 0.03
    real_estate_mean_return = 0.05
    stock_volatility = 0.15
    bond_volatility = 0.05
    real_estate_volatility = 0.10

    try:
        # Create a simulator instance
        simulator = AssetAllocationSimulator(
            initial_investment, years, stock_alloc, bond_alloc, real_estate_alloc,
            stock_mean_return, bond_mean_return, real_estate_mean_return,
            stock_volatility, bond_volatility, real_estate_volatility
        )
        
        # Run the simulation
        portfolio_df = simulator.simulate()
        
        # Plot the results
        simulator.plot_results(portfolio_df)

    except ValueError as e:
        print(f"Error: {e}")
```
