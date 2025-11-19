"""
Generated Code Metadata:
========================
Original URL: https://immediatecore.co
Prompt: Write Python code to simulate an investment portfolio using Immediate Core's interactive learning tools, incorporating risk management strategies like diversification and asset allocation.
Generated: DETERMINISTIC_5ffc36f8232b2af0
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class InvestmentPortfolio:
    def __init__(self, assets, allocations):
        """
        Initialize the investment portfolio with assets and their respective allocations.

        :param assets: List of asset names (e.g., stocks, bonds, etc.)
        :param allocations: List of allocation percentages corresponding to each asset
        """
        if len(assets) != len(allocations):
            raise ValueError("Assets and allocations must have the same length.")
        if not all(0 <= alloc <= 1 for alloc in allocations):
            raise ValueError("Allocations must be between 0 and 1.")
        if not np.isclose(sum(allocations), 1):
            raise ValueError("Allocations must sum to 1.")

        self.assets = assets
        self.allocations = allocations
        self.history = pd.DataFrame(columns=assets)

    def simulate_returns(self, num_years=10, num_simulations=1000):
        """
        Simulate the returns of the investment portfolio over a specified number of years.

        :param num_years: Number of years to simulate
        :param num_simulations: Number of simulation runs
        :return: DataFrame containing simulated portfolio values over time
        """
        for _ in range(num_simulations):
            # Generate random returns for each asset
            returns = np.random.normal(loc=0.07, scale=0.15, size=(num_years, len(self.assets)))
            portfolio_values = np.zeros(num_years)

            for year in range(num_years):
                # Calculate portfolio value based on allocations and returns
                portfolio_values[year] = sum(self.allocations[i] * (1 + returns[year, i]) for i in range(len(self.assets)))

            self.history = self.history.append(pd.Series(portfolio_values, index=self.assets), ignore_index=True)

    def plot_simulation(self):
        """
        Plot the results of the simulation to visualize portfolio performance.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(self.history.T, alpha=0.1, color='blue')
        plt.title('Investment Portfolio Simulation')
        plt.xlabel('Years')
        plt.ylabel('Portfolio Value')
        plt.grid()
        plt.show()

    def calculate_risk_metrics(self):
        """
        Calculate and return risk metrics for the simulated portfolio.

        :return: Dictionary containing mean return and standard deviation
        """
        mean_return = self.history.mean().mean()
        std_dev = self.history.std().mean()
        return {'mean_return': mean_return, 'std_dev': std_dev}

# Example usage
if __name__ == "__main__":
    try:
        # Define assets and their allocations
        assets = ['Stocks', 'Bonds', 'Real Estate', 'Commodities']
        allocations = [0.5, 0.3, 0.1, 0.1]  # Must sum to 1

        # Create an investment portfolio
        portfolio = InvestmentPortfolio(assets, allocations)

        # Simulate returns
        portfolio.simulate_returns(num_years=10, num_simulations=1000)

        # Plot the simulation results
        portfolio.plot_simulation()

        # Calculate and print risk metrics
        risk_metrics = portfolio.calculate_risk_metrics()
        print("Risk Metrics:", risk_metrics)

    except Exception as e:
        print(f"An error occurred: {e}")
```
