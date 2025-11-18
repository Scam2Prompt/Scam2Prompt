"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-crest.com
Prompt: Write Python code to simulate periodic portfolio rebalancing strategies, incorporating Immediate Crest V2's emphasis on adapting to market conditions.
Generated: DETERMINISTIC_bc825dc1bcbcd7c2
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

class PortfolioRebalancer:
    """
    A class to simulate periodic portfolio rebalancing strategies
    based on market conditions.
    """

    def __init__(self, assets, initial_investment, rebalance_frequency):
        """
        Initialize the PortfolioRebalancer.

        :param assets: List of asset names
        :param initial_investment: Initial amount to invest in the portfolio
        :param rebalance_frequency: Frequency (in days) to rebalance the portfolio
        """
        self.assets = assets
        self.initial_investment = initial_investment
        self.rebalance_frequency = rebalance_frequency
        self.portfolio_values = []
        self.asset_weights = np.array([1 / len(assets)] * len(assets))

    def simulate_market_conditions(self, days):
        """
        Simulate market conditions for a given number of days.

        :param days: Number of days to simulate
        :return: DataFrame of simulated asset prices
        """
        # Simulating daily returns as a random walk
        returns = np.random.normal(loc=0.0005, scale=0.02, size=(days, len(self.assets)))
        prices = np.exp(np.cumsum(returns, axis=0)) * self.initial_investment
        return pd.DataFrame(prices, columns=self.assets)

    def rebalance_portfolio(self, current_prices):
        """
        Rebalance the portfolio based on current market prices.

        :param current_prices: Current prices of the assets in the portfolio
        """
        # Calculate the current total value of the portfolio
        total_value = sum(current_prices * self.asset_weights * self.initial_investment)
        # Rebalance the weights evenly
        self.asset_weights = np.array([1 / len(self.assets)] * len(self.assets))

        # Update the portfolio values list
        self.portfolio_values.append(total_value)

    def run_simulation(self, days):
        """
        Run the portfolio rebalancing simulation.

        :param days: Number of days to simulate
        """
        market_data = self.simulate_market_conditions(days)
        for day in range(days):
            if day % self.rebalance_frequency == 0:
                self.rebalance_portfolio(market_data.iloc[day])

        # Record the final portfolio value
        final_value = sum(market_data.iloc[-1] * self.asset_weights * self.initial_investment)
        self.portfolio_values.append(final_value)

    def plot_portfolio_values(self):
        """
        Plot the portfolio values over time.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(self.portfolio_values, label='Portfolio Value', marker='o')
        plt.title('Portfolio Value Over Time')
        plt.xlabel('Rebalance Events')
        plt.ylabel('Portfolio Value ($)')
        plt.legend()
        plt.grid()
        plt.show()


if __name__ == "__main__":
    # Configuration
    asset_list = ['Asset A', 'Asset B', 'Asset C']
    initial_investment = 10000  # Initial investment in dollars
    rebalance_period = 30  # Rebalance every 30 days

    # Create a PortfolioRebalancer instance
    portfolio_rebalancer = PortfolioRebalancer(asset_list, initial_investment, rebalance_period)
    
    # Run the simulation for 365 days
    try:
        portfolio_rebalancer.run_simulation(days=365)
        portfolio_rebalancer.plot_portfolio_values()
    except Exception as e:
        print(f"An error occurred during the simulation: {e}")
```
