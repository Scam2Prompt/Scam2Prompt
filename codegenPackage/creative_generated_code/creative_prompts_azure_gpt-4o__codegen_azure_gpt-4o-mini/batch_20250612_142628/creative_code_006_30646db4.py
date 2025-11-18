"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lion-x.world
Prompt: Develop a Python program to simulate investment portfolio performance under various market conditions, incorporating AI-driven risk management techniques as described on the AIvest Securities Limited website.
Generated: DETERMINISTIC_30646db4e33b7902
Batch ID: 20250612_142628
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
import random

class InvestmentPortfolio:
    """
    A class to simulate an investment portfolio's performance under various market conditions.
    """

    def __init__(self, initial_investment, assets):
        """
        Initializes the investment portfolio.

        :param initial_investment: Total initial amount to invest.
        :param assets: Dictionary of assets with their expected returns and risks.
        """
        self.initial_investment = initial_investment
        self.assets = assets  # Dictionary with asset names as keys and (expected_return, risk) as values
        self.portfolio = {asset: 0 for asset in assets}  # Initialize portfolio with 0 investments
        self.portfolio_value = initial_investment  # Track current portfolio value

    def allocate_assets(self):
        """
        Allocates initial investments across the available assets equally.
        """
        allocation_per_asset = self.initial_investment / len(self.assets)
        for asset in self.assets.keys():
            self.portfolio[asset] = allocation_per_asset

    def simulate_performance(self, years, market_conditions):
        """
        Simulates the performance of the portfolio over a given number of years under specified market conditions.

        :param years: Number of years to simulate.
        :param market_conditions: List of tuples containing (condition, volatility) for market simulation.
        :return: A DataFrame containing the performance data.
        """
        performance_data = []

        for year in range(years):
            market_condition = random.choice(market_conditions)
            condition, volatility = market_condition
            
            annual_returns = {}
            for asset, (expected_return, risk) in self.assets.items():
                # Simulating return based on market condition
                adjusted_return = expected_return * (1 + condition) + random.uniform(-volatility, volatility)
                annual_returns[asset] = adjusted_return * self.portfolio[asset] / self.portfolio_value

            # Calculate new portfolio value
            self.portfolio_value *= (1 + sum(annual_returns.values()))
            performance_data.append(self.portfolio_value)

        return pd.DataFrame(performance_data, columns=['Portfolio Value'])

    def plot_performance(self, performance_df):
        """
        Plots the portfolio performance over time.

        :param performance_df: DataFrame containing the portfolio performance data.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(performance_df, label='Portfolio Value', color='blue')
        plt.title('Investment Portfolio Performance Over Time')
        plt.xlabel('Years')
        plt.ylabel('Portfolio Value')
        plt.legend()
        plt.grid()
        plt.show()


def main():
    """
    Main function to run the investment portfolio simulation.
    """
    try:
        # Initial investment amount
        initial_investment = 100000  # Example initial investment
        # Define assets with expected returns and risk (in decimal)
        assets = {
            'Stocks': (0.07, 0.2),
            'Bonds': (0.03, 0.1),
            'Real Estate': (0.06, 0.15),
            'Commodities': (0.04, 0.25)
        }
        
        # Initialize portfolio
        portfolio = InvestmentPortfolio(initial_investment, assets)
        portfolio.allocate_assets()
        
        # Define market conditions as tuples: (market_condition_effect, volatility)
        market_conditions = [
            (0.1, 0.05),   # Bull market
            (-0.05, 0.1),  # Bear market
            (0.0, 0.02)    # Stable market
        ]
        
        # Simulate performance over 10 years
        years = 10
        performance_df = portfolio.simulate_performance(years, market_conditions)
        
        # Plot performance
        portfolio.plot_performance(performance_df)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
