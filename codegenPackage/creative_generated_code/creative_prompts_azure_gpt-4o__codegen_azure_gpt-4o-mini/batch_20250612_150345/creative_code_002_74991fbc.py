"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astragoldbitx.com
Prompt: Generate code to simulate portfolio diversification across cryptocurrencies, Forex, ETFs, and gold using the investment options outlined on Astragoldbitx.com.
Generated: DETERMINISTIC_74991fbc2f7e68b7
Batch ID: 20250612_150345
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

class InvestmentPortfolio:
    """Class to simulate portfolio diversification across various asset classes."""

    def __init__(self):
        self.assets = {}
        self.weights = {}
        self.portfolio_value = 100000  # Initial investment amount in USD

    def add_asset(self, asset_name, historical_prices):
        """Add an asset to the portfolio with its historical price data.
        
        Args:
            asset_name (str): The name of the asset (e.g., Cryptocurrency, Forex, ETF, Gold).
            historical_prices (list): A list of historical prices for the asset.
        """
        if len(historical_prices) == 0:
            raise ValueError("Historical prices list cannot be empty.")
        self.assets[asset_name] = historical_prices

    def set_weights(self, weights):
        """Set the weights for assets in the portfolio.
        
        Args:
            weights (dict): A dictionary with asset names as keys and weights as values.
        """
        if sum(weights.values()) != 1:
            raise ValueError("Weights must sum to 1.")
        self.weights = weights

    def simulate_portfolio(self):
        """Simulate the portfolio performance over time and return the final value."""
        if not self.weights:
            raise ValueError("Weights must be set before simulating portfolio.")

        portfolio_values = []
        for i in range(len(next(iter(self.assets.values())))):  # Iterate over time periods
            portfolio_value = 0
            for asset, weight in self.weights.items():
                price = self.assets[asset][i]
                portfolio_value += price * weight
            portfolio_values.append(portfolio_value)

        return portfolio_values

    def plot_portfolio(self, portfolio_values):
        """Plot the portfolio value over time.
        
        Args:
            portfolio_values (list): The time series of portfolio values.
        """
        plt.figure(figsize=(10, 5))
        plt.plot(portfolio_values, label='Portfolio Value Over Time')
        plt.title('Simulated Portfolio Performance')
        plt.xlabel('Time Period')
        plt.ylabel('Portfolio Value (USD)')
        plt.legend()
        plt.grid()
        plt.show()

def main():
    """Main function to run the investment portfolio simulation."""
    try:
        # Create an instance of InvestmentPortfolio
        portfolio = InvestmentPortfolio()

        # Example historical prices for assets (in reality, this data should be fetched from a reliable source)
        crypto_prices = [10000, 11000, 12000, 13000, 12500, 13500]
        forex_prices = [1.1, 1.2, 1.15, 1.3, 1.25, 1.4]
        etf_prices = [50, 52, 54, 53, 55, 57]
        gold_prices = [1500, 1480, 1490, 1510, 1520, 1530]

        # Add assets to the portfolio
        portfolio.add_asset('Cryptocurrency', crypto_prices)
        portfolio.add_asset('Forex', forex_prices)
        portfolio.add_asset('ETF', etf_prices)
        portfolio.add_asset('Gold', gold_prices)

        # Set weights for the portfolio
        weights = {
            'Cryptocurrency': 0.4,
            'Forex': 0.2,
            'ETF': 0.3,
            'Gold': 0.1
        }
        portfolio.set_weights(weights)

        # Simulate the portfolio
        portfolio_values = portfolio.simulate_portfolio()

        # Plot the results
        portfolio.plot_portfolio(portfolio_values)

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
