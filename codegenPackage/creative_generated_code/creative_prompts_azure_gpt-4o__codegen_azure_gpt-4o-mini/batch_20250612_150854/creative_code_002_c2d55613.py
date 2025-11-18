"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-orbirex.com
Prompt: Generate code that demonstrates how to implement an asset allocation strategy using Python, referencing the concepts of diversification and risk management discussed on Immediate Orbirex.
Generated: DETERMINISTIC_c2d55613a9ea8716
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
import yfinance as yf

class AssetAllocator:
    def __init__(self, tickers, weights):
        """
        Initializes the AssetAllocator with a list of asset tickers and their weights.

        :param tickers: List of asset tickers (e.g. ['AAPL', 'MSFT', 'GOOGL'])
        :param weights: List of weights corresponding to the assets (must sum to 1)
        """
        if len(tickers) != len(weights):
            raise ValueError("Length of tickers and weights must be equal.")
        if not np.isclose(sum(weights), 1):
            raise ValueError("Weights must sum to 1.")

        self.tickers = tickers
        self.weights = weights
        self.historical_data = None

    def fetch_data(self, start, end):
        """
        Fetch historical price data for the specified tickers.

        :param start: Start date for historical data (format: 'YYYY-MM-DD')
        :param end: End date for historical data (format: 'YYYY-MM-DD')
        """
        self.historical_data = yf.download(self.tickers, start=start, end=end)['Adj Close']
        if self.historical_data.isnull().values.any():
            raise ValueError("Fetched data contains null values. Please check the tickers and date range.")

    def calculate_portfolio_performance(self):
        """
        Calculate the expected return and risk (volatility) of the portfolio.

        :return: Tuple of (expected_return, volatility)
        """
        # Calculate daily returns
        daily_returns = self.historical_data.pct_change().dropna()

        # Calculate expected return and covariance matrix
        expected_return = np.dot(daily_returns.mean(), self.weights) * 252  # Annualized return
        covariance_matrix = daily_returns.cov() * 252  # Annualized covariance
        portfolio_variance = np.dot(self.weights, np.dot(covariance_matrix, self.weights))
        portfolio_volatility = np.sqrt(portfolio_variance)

        return expected_return, portfolio_volatility

    def plot_asset_allocation(self):
        """
        Plot the asset allocation pie chart.
        """
        plt.figure(figsize=(8, 8))
        plt.pie(self.weights, labels=self.tickers, autopct='%1.1f%%')
        plt.title('Asset Allocation')
        plt.show()

def main():
    # Define asset tickers and their corresponding weights
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']
    weights = [0.25, 0.25, 0.25, 0.25]

    # Instantiate the AssetAllocator
    allocator = AssetAllocator(tickers, weights)

    # Fetch historical data for the last year
    try:
        allocator.fetch_data(start='2022-01-01', end='2023-01-01')

        # Calculate portfolio performance
        expected_return, volatility = allocator.calculate_portfolio_performance()
        print(f"Expected Annual Return: {expected_return:.2%}")
        print(f"Portfolio Volatility: {volatility:.2%}")

        # Plot asset allocation
        allocator.plot_asset_allocation()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
