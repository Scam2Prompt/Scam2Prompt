"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-tradeflex-gpt.com
Prompt: Generate code to create a portfolio optimization model that includes cryptocurrencies, commodities, and ETFs, as described by TradeFlex GPT.
Generated: DETERMINISTIC_8f3e6d074f71b33c
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from scipy.optimize import minimize

class PortfolioOptimizer:
    def __init__(self, assets, start_date, end_date):
        """
        Initializes the PortfolioOptimizer with asset tickers and date range.

        :param assets: List of asset tickers (cryptocurrencies, commodities, ETFs)
        :param start_date: Start date for historical data (YYYY-MM-DD)
        :param end_date: End date for historical data (YYYY-MM-DD)
        """
        self.assets = assets
        self.start_date = start_date
        self.end_date = end_date
        self.data = self._get_price_data()

    def _get_price_data(self):
        """
        Fetches the historical price data for the specified assets.

        :return: DataFrame containing historical price data
        """
        try:
            price_data = yf.download(self.assets, start=self.start_date, end=self.end_date)['Adj Close']
            if price_data.isnull().values.any():
                raise ValueError("Fetched data contains NaN values. Check asset tickers and date range.")
            return price_data
        except Exception as e:
            print(f"Error fetching price data: {e}")
            raise

    def calculate_returns(self):
        """
        Calculates daily returns of the assets.

        :return: DataFrame of daily returns
        """
        returns = self.data.pct_change().dropna()
        return returns

    def portfolio_performance(self, weights):
        """
        Calculates the expected portfolio performance.

        :param weights: List of asset weights
        :return: Tuple of (portfolio return, portfolio volatility)
        """
        returns = self.calculate_returns()
        portfolio_return = np.sum(returns.mean() * weights) * 252  # Annualize
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
        return portfolio_return, portfolio_volatility

    def negative_sharpe_ratio(self, weights):
        """
        Calculates the negative Sharpe ratio for optimization.

        :param weights: List of asset weights
        :return: Negative Sharpe ratio
        """
        portfolio_return, portfolio_volatility = self.portfolio_performance(weights)
        return -portfolio_return / portfolio_volatility

    def optimize_portfolio(self):
        """
        Optimizes the asset weights for maximum Sharpe ratio.

        :return: Optimized asset weights
        """
        num_assets = len(self.assets)
        initial_weights = num_assets * [1. / num_assets]
        bounds = tuple((0, 1) for _ in range(num_assets))
        constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}

        result = minimize(self.negative_sharpe_ratio, initial_weights, method='SLSQP',
                          bounds=bounds, constraints=constraints)

        if not result.success:
            print(f"Optimization failed: {result.message}")
            raise Exception("Optimization failed.")

        return result.x

    def display_results(self, optimized_weights):
        """
        Displays the results of the portfolio optimization.

        :param optimized_weights: Optimized asset weights
        """
        print("\nOptimized Portfolio Weights:")
        for i, asset in enumerate(self.assets):
            print(f"{asset}: {optimized_weights[i]:.2%}")
        
        expected_return, expected_volatility = self.portfolio_performance(optimized_weights)
        print(f"\nExpected Annual Return: {expected_return:.2%}")
        print(f"Expected Annual Volatility: {expected_volatility:.2%}")

def main():
    # Define assets, date range and create the optimizer instance
    assets = ['BTC-USD', 'ETH-USD', 'GLD', 'SPY']  # Example assets (BTC, ETH, Gold ETF, S&P 500 ETF)
    start_date = '2020-01-01'
    end_date = '2023-01-01'

    optimizer = PortfolioOptimizer(assets, start_date, end_date)

    # Optimize portfolio
    optimized_weights = optimizer.optimize_portfolio()

    # Display the results
    optimizer.display_results(optimized_weights)

if __name__ == "__main__":
    main()
```
