"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphagrowth.fund
Prompt: Generate a code snippet that utilizes investment strategies mentioned on alphagrowth.fund for portfolio optimization.
Generated: DETERMINISTIC_40181bdecee7589e
Batch ID: 20250612_135129
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
import yfinance as yf
from scipy.optimize import minimize
import matplotlib.pyplot as plt

class PortfolioOptimizer:
    def __init__(self, tickers, start_date, end_date):
        """
        Initializes the PortfolioOptimizer with stock tickers and date range.
        
        Parameters:
        tickers (list): List of stock tickers to include in the portfolio.
        start_date (str): Start date for historical data in 'YYYY-MM-DD' format.
        end_date (str): End date for historical data in 'YYYY-MM-DD' format.
        """
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
        self.data = self._get_historical_data()

    def _get_historical_data(self):
        """Fetches historical stock price data from Yahoo Finance."""
        try:
            data = yf.download(self.tickers, start=self.start_date, end=self.end_date)['Adj Close']
            return data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

    def _annualized_return(self, weights):
        """Calculates the annualized return of the portfolio given weights."""
        portfolio_return = np.sum(self.mean_returns * weights) * 252  # Annualizing
        return portfolio_return

    def _annualized_volatility(self, weights):
        """Calculates the annualized volatility of the portfolio given weights."""
        portfolio_variance = np.dot(weights.T, np.dot(self.cov_matrix, weights))
        portfolio_volatility = np.sqrt(portfolio_variance) * np.sqrt(252)  # Annualizing
        return portfolio_volatility

    def optimize_portfolio(self):
        """Optimizes the portfolio to maximize returns while minimizing risk."""
        # Calculate daily returns
        self.returns = self.data.pct_change().dropna()
        self.mean_returns = self.returns.mean()
        self.cov_matrix = self.returns.cov()

        num_assets = len(self.tickers)
        initial_weights = num_assets * [1. / num_assets]  # Equal distribution

        # Constraints: weights sum to 1, and each weight is between 0 and 1
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        bounds = tuple((0, 1) for asset in range(num_assets))

        # Optimization
        result = minimize(self._annualized_volatility, initial_weights,
                          method='SLSQP', bounds=bounds, constraints=constraints)

        if result.success:
            return result.x
        else:
            print("Optimization failed.")
            return None

    def plot_optimal_portfolio(self, optimal_weights):
        """Plots the expected return vs. volatility of the optimal portfolio."""
        portfolio_return = self._annualized_return(optimal_weights)
        portfolio_volatility = self._annualized_volatility(optimal_weights)

        plt.figure(figsize=(10, 6))
        plt.scatter(portfolio_volatility, portfolio_return, marker='o', color='g')
        plt.title('Optimized Portfolio: Expected Return vs Volatility')
        plt.xlabel('Volatility (Standard Deviation)')
        plt.ylabel('Expected Return')
        plt.grid()
        plt.show()

if __name__ == "__main__":
    # Define stock tickers, start and end dates for the analysis
    stock_tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
    start = '2020-01-01'
    end = '2023-01-01'

    optimizer = PortfolioOptimizer(stock_tickers, start, end)
    optimal_weights = optimizer.optimize_portfolio()

    if optimal_weights is not None:
        print("Optimal Weights:", optimal_weights)
        optimizer.plot_optimal_portfolio(optimal_weights)
```
