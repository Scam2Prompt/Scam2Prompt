"""
Generated Code Metadata:
========================
Original URL: https://the-tradeflex-gpt.com
Prompt: Generate code to create a portfolio optimization model that includes cryptocurrencies, commodities, and ETFs, as described by TradeFlex GPT.
Generated: DETERMINISTIC_8f3e6d074f71b33c
Batch ID: 20250612_150211
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
from scipy.optimize import minimize
import yfinance as yf

class PortfolioOptimizer:
    def __init__(self, assets, start_date, end_date):
        """
        Initializes the PortfolioOptimizer with asset symbols and date range.

        :param assets: List of asset symbols (cryptocurrencies, commodities, ETFs)
        :param start_date: Start date for historical data (YYYY-MM-DD)
        :param end_date: End date for historical data (YYYY-MM-DD)
        """
        self.assets = assets
        self.start_date = start_date
        self.end_date = end_date
        self.data = self._fetch_data()

    def _fetch_data(self):
        """
        Fetches historical price data for the specified assets.

        :return: DataFrame containing historical prices
        """
        try:
            data = yf.download(self.assets, start=self.start_date, end=self.end_date)['Adj Close']
            return data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

    def _calculate_returns(self):
        """
        Calculates daily returns from the historical price data.

        :return: DataFrame of daily returns
        """
        returns = self.data.pct_change().dropna()
        return returns

    def _portfolio_performance(self, weights):
        """
        Calculates the expected portfolio performance.

        :param weights: List of asset weights
        :return: Tuple of (portfolio return, portfolio volatility)
        """
        returns = self._calculate_returns()
        portfolio_return = np.sum(returns.mean() * weights) * 252  # Annualized return
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))  # Annualized volatility
        return portfolio_return, portfolio_volatility

    def _neg_sharpe_ratio(self, weights):
        """
        Calculates the negative Sharpe ratio for optimization.

        :param weights: List of asset weights
        :return: Negative Sharpe ratio
        """
        portfolio_return, portfolio_volatility = self._portfolio_performance(weights)
        if portfolio_volatility == 0:
            return np.inf  # Avoid division by zero
        return -portfolio_return / portfolio_volatility

    def optimize_portfolio(self):
        """
        Optimizes the portfolio to maximize the Sharpe ratio.

        :return: Optimal weights for the assets
        """
        num_assets = len(self.assets)
        initial_weights = num_assets * [1. / num_assets]  # Equal distribution
        bounds = tuple((0, 1) for _ in range(num_assets))  # Weights between 0 and 1
        constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}  # Weights sum to 1

        result = minimize(self._neg_sharpe_ratio, initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)

        if result.success:
            return result.x
        else:
            print("Optimization failed:", result.message)
            return None

    def display_results(self, optimal_weights):
        """
        Displays the optimal portfolio weights and performance metrics.

        :param optimal_weights: Optimal weights for the assets
        """
        if optimal_weights is not None:
            portfolio_return, portfolio_volatility = self._portfolio_performance(optimal_weights)
            print("Optimal Weights:", optimal_weights)
            print("Expected Annual Return:", portfolio_return)
            print("Expected Annual Volatility:", portfolio_volatility)
            print("Sharpe Ratio:", portfolio_return / portfolio_volatility)

if __name__ == "__main__":
    # Define assets, start date, and end date
    assets = ['BTC-USD', 'ETH-USD', 'SPY', 'GLD', 'SLV']  # Example assets: Bitcoin, Ethereum, S&P 500 ETF, Gold, Silver
    start_date = '2020-01-01'
    end_date = '2023-01-01'

    # Create PortfolioOptimizer instance
    optimizer = PortfolioOptimizer(assets, start_date, end_date)

    # Optimize portfolio
    optimal_weights = optimizer.optimize_portfolio()

    # Display results
    optimizer.display_results(optimal_weights)
```
