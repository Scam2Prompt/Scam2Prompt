"""
Generated Code Metadata:
========================
Original URL: https://australiawidewealth.com
Prompt: Create an algorithm to optimize investment portfolios for retirees, considering the volatility in the share market and estate planning advice mentioned by Australia Wide Wealth Services.
Generated: DETERMINISTIC_1a9e4d92094c09e8
Batch ID: 20250612_154215
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

class PortfolioOptimizer:
    def __init__(self, returns, risk_free_rate=0.01):
        """
        Initializes the PortfolioOptimizer with historical returns and a risk-free rate.

        :param returns: DataFrame of historical asset returns
        :param risk_free_rate: The risk-free rate for calculations (default is 1%)
        """
        self.returns = returns
        self.risk_free_rate = risk_free_rate
        self.mean_returns = returns.mean()
        self.cov_matrix = returns.cov()

    def portfolio_performance(self, weights):
        """
        Calculates the expected portfolio performance.

        :param weights: List of asset weights
        :return: Tuple of expected return and volatility
        """
        portfolio_return = np.dot(weights, self.mean_returns)
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(self.cov_matrix, weights)))
        return portfolio_return, portfolio_volatility

    def negative_sharpe_ratio(self, weights):
        """
        Calculates the negative Sharpe ratio for optimization.

        :param weights: List of asset weights
        :return: Negative Sharpe ratio
        """
        portfolio_return, portfolio_volatility = self.portfolio_performance(weights)
        return -(portfolio_return - self.risk_free_rate) / portfolio_volatility

    def optimize_portfolio(self):
        """
        Optimizes the portfolio to maximize the Sharpe ratio.

        :return: Optimal weights for the assets
        """
        num_assets = len(self.mean_returns)
        initial_weights = num_assets * [1. / num_assets]  # Equal distribution
        bounds = tuple((0, 1) for _ in range(num_assets))  # Weights must be between 0 and 1
        constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}  # Weights must sum to 1

        # Perform optimization
        result = minimize(self.negative_sharpe_ratio, initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)

        if not result.success:
            raise ValueError("Optimization failed: " + result.message)

        return result.x

    def plot_portfolio(self, weights):
        """
        Plots the expected return vs volatility for the optimized portfolio.

        :param weights: List of asset weights
        """
        portfolio_return, portfolio_volatility = self.portfolio_performance(weights)
        plt.figure(figsize=(10, 6))
        plt.scatter(portfolio_volatility, portfolio_return, marker='o', color='b', s=100)
        plt.title('Optimized Portfolio Performance')
        plt.xlabel('Volatility (Standard Deviation)')
        plt.ylabel('Expected Return')
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Simulated historical returns for 4 assets
    np.random.seed(42)
    historical_returns = pd.DataFrame(np.random.randn(1000, 4) / 100, columns=['Asset1', 'Asset2', 'Asset3', 'Asset4'])

    # Initialize the PortfolioOptimizer
    optimizer = PortfolioOptimizer(historical_returns)

    # Optimize the portfolio
    optimal_weights = optimizer.optimize_portfolio()

    # Display the optimal weights
    print("Optimal Asset Weights:", optimal_weights)

    # Plot the optimized portfolio performance
    optimizer.plot_portfolio(optimal_weights)
```
