"""
Generated Code Metadata:
========================
Original URL: https://immediate-orbirex.com
Prompt: Generate code that demonstrates how to implement an asset allocation strategy using Python, referencing the concepts of diversification and risk management discussed on Immediate Orbirex.
Generated: DETERMINISTIC_c2d55613a9ea8716
Batch ID: 20250612_150854
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
import yfinance as yf

class AssetAllocator:
    def __init__(self, tickers, weights):
        """
        Initializes the AssetAllocator with a list of asset tickers and their corresponding weights.

        :param tickers: List of asset tickers (e.g., ['AAPL', 'MSFT', 'GOOGL'])
        :param weights: List of weights corresponding to each ticker (must sum to 1)
        """
        if len(tickers) != len(weights):
            raise ValueError("The number of tickers must match the number of weights.")
        if not np.isclose(sum(weights), 1):
            raise ValueError("Weights must sum to 1.")
        
        self.tickers = tickers
        self.weights = weights
        self.data = None

    def fetch_data(self, start_date, end_date):
        """
        Fetches historical price data for the specified tickers.

        :param start_date: Start date for fetching data (format: 'YYYY-MM-DD')
        :param end_date: End date for fetching data (format: 'YYYY-MM-DD')
        """
        self.data = yf.download(self.tickers, start=start_date, end=end_date)['Adj Close']
        if self.data.isnull().values.any():
            raise ValueError("Fetched data contains NaN values. Please check the tickers and date range.")

    def calculate_returns(self):
        """
        Calculates daily returns for the asset data.

        :return: DataFrame of daily returns
        """
        if self.data is None:
            raise ValueError("Data not fetched. Please call fetch_data() first.")
        
        returns = self.data.pct_change().dropna()
        return returns

    def portfolio_performance(self):
        """
        Calculates the expected portfolio return and volatility.

        :return: Tuple of (expected return, expected volatility)
        """
        returns = self.calculate_returns()
        expected_return = np.dot(returns.mean(), self.weights) * 252  # Annualized return
        expected_volatility = np.sqrt(np.dot(self.weights.T, np.dot(returns.cov() * 252, self.weights)))  # Annualized volatility
        return expected_return, expected_volatility

    def plot_allocation(self):
        """
        Plots the asset allocation pie chart.
        """
        plt.figure(figsize=(8, 6))
        plt.pie(self.weights, labels=self.tickers, autopct='%1.1f%%', startangle=140)
        plt.title('Asset Allocation')
        plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
        plt.show()

# Example usage
if __name__ == "__main__":
    # Define asset tickers and their corresponding weights
    asset_tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']
    asset_weights = [0.25, 0.25, 0.25, 0.25]  # Equal allocation

    # Create an instance of AssetAllocator
    allocator = AssetAllocator(asset_tickers, asset_weights)

    # Fetch historical data
    try:
        allocator.fetch_data(start_date='2020-01-01', end_date='2023-01-01')
        
        # Calculate portfolio performance
        expected_return, expected_volatility = allocator.portfolio_performance()
        print(f"Expected Annual Return: {expected_return:.2%}")
        print(f"Expected Annual Volatility: {expected_volatility:.2%}")

        # Plot asset allocation
        allocator.plot_allocation()
    except Exception as e:
        print(f"An error occurred: {e}")
```
