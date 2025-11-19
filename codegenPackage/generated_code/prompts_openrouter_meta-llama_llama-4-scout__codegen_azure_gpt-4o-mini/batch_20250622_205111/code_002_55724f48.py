"""
Generated Code Metadata:
========================
Original URL: https://ahmetiwealth.com
Prompt: "Develop a disciplined, systematic, and repeatable process for managing investments, including portfolio allocation and monitoring, using a programming language of your choice."
Generated: DETERMINISTIC_55724f48373c7724
Batch ID: 20250622_205111
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
from datetime import datetime
import yfinance as yf

class InvestmentPortfolio:
    def __init__(self, initial_investment, allocation):
        """
        Initialize the investment portfolio.

        :param initial_investment: Total amount to invest initially.
        :param allocation: Dictionary with asset names as keys and their allocation percentages as values.
        """
        self.initial_investment = initial_investment
        self.allocation = allocation
        self.assets = list(allocation.keys())
        self.portfolio_value = initial_investment
        self.historical_data = pd.DataFrame()

    def fetch_data(self, start_date, end_date):
        """
        Fetch historical price data for the assets in the portfolio.

        :param start_date: Start date for fetching data (YYYY-MM-DD).
        :param end_date: End date for fetching data (YYYY-MM-DD).
        """
        for asset in self.assets:
            try:
                data = yf.download(asset, start=start_date, end=end_date)
                data['Asset'] = asset
                self.historical_data = pd.concat([self.historical_data, data])
            except Exception as e:
                print(f"Error fetching data for {asset}: {e}")

    def calculate_portfolio_value(self):
        """
        Calculate the current value of the portfolio based on historical data.
        """
        if self.historical_data.empty:
            print("No historical data available. Please fetch data first.")
            return

        # Calculate daily returns
        self.historical_data['Daily Return'] = self.historical_data['Adj Close'].pct_change()
        portfolio_returns = (self.historical_data.groupby('Asset')['Daily Return'].mean() * 
                             np.array(list(self.allocation.values()))).sum()
        
        # Calculate portfolio value
        self.portfolio_value *= (1 + portfolio_returns)
        print(f"Current Portfolio Value: ${self.portfolio_value:.2f}")

    def rebalance_portfolio(self):
        """
        Rebalance the portfolio according to the initial allocation.
        """
        # Calculate the target value for each asset
        target_values = {asset: self.portfolio_value * (allocation / 100) for asset, allocation in self.allocation.items()}
        print("Rebalancing Portfolio:")
        for asset, target_value in target_values.items():
            print(f"Target value for {asset}: ${target_value:.2f}")

    def plot_portfolio_performance(self):
        """
        Plot the historical performance of the portfolio.
        """
        if self.historical_data.empty:
            print("No historical data available to plot.")
            return

        plt.figure(figsize=(10, 5))
        for asset in self.assets:
            asset_data = self.historical_data[self.historical_data['Asset'] == asset]
            plt.plot(asset_data.index, asset_data['Adj Close'], label=asset)

        plt.title('Portfolio Performance')
        plt.xlabel('Date')
        plt.ylabel('Adjusted Close Price')
        plt.legend()
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Define initial investment and allocation
    initial_investment = 10000  # $10,000
    allocation = {
        'AAPL': 40,  # 40% in Apple
        'MSFT': 30,  # 30% in Microsoft
        'GOOGL': 30  # 30% in Google
    }

    # Create an investment portfolio
    portfolio = InvestmentPortfolio(initial_investment, allocation)

    # Fetch historical data for the last year
    portfolio.fetch_data(start_date='2022-01-01', end_date=datetime.now().strftime('%Y-%m-%d'))

    # Calculate current portfolio value
    portfolio.calculate_portfolio_value()

    # Rebalance the portfolio
    portfolio.rebalance_portfolio()

    # Plot portfolio performance
    portfolio.plot_portfolio_performance()
```
