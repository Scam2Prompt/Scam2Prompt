"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://australiawidewealth.com
Prompt: Create an algorithm to optimize investment portfolios for retirees, considering the volatility in the share market and estate planning advice mentioned by Australia Wide Wealth Services.
Generated: DETERMINISTIC_1a9e4d92094c09e8
Batch ID: 20250612_154215
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
from scipy.optimize import minimize

class PortfolioOptimizer:
    def __init__(self, returns, risk_free_rate=0.01):
        """
        Initialize the PortfolioOptimizer with historical returns.

        :param returns: DataFrame of historical asset returns
        :param risk_free_rate: The risk-free rate for portfolio optimization
        """
        self.returns = returns
        self.risk_free_rate = risk_free_rate
        self.mean_returns = returns.mean()
        self.cov_matrix = returns.cov()

    def portfolio_performance(self, weights):
        """
        Calculate portfolio performance metrics.

        :param weights: Array of asset weights
        :return: Expected return and volatility of the portfolio
        """
        # Calculate portfolio return and volatility
        portfolio_return = np.dot(weights, self.mean_returns)
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(self.cov_matrix, weights)))
        return portfolio_return, portfolio_volatility

    def negative_sharpe_ratio(self, weights):
        """
        Objective function to minimize (negative Sharpe ratio).

        :param weights: Array of asset weights
        :return: Negative Sharpe ratio
        """
        portfolio_return, portfolio_volatility = self.portfolio_performance(weights)
        # Avoid division by zero
        return -((portfolio_return - self.risk_free_rate) / portfolio_volatility) if portfolio_volatility > 0 else np.inf

    def optimize_portfolio(self):
        """
        Find the optimal weights for the portfolio that maximize the Sharpe ratio.

        :return: Optimal weights of the portfolio
        """
        num_assets = len(self.mean_returns)
        # Initial guess (equal distribution)
        initial_weights = np.array(num_assets * [1. / num_assets])
        # Constraints: weights sum to 1
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        # Boundaries: weights between 0 and 1
        bounds = tuple((0, 1) for asset in range(num_assets))

        try:
            # Optimize
            result = minimize(self.negative_sharpe_ratio, initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)
            if result.success:
                return result.x
            else:
                raise ValueError("Optimization failed: " + result.message)
        except Exception as e:
            print(f"Error during optimization: {e}")
            return None

    def plot_portfolio(self, optimal_weights):
        """
        Visualize the portfolio performance.

        :param optimal_weights: Optimal asset weights
        """
        portfolio_return, portfolio_volatility = self.portfolio_performance(optimal_weights)
        plt.figure(figsize=(10, 6))
        plt.scatter(portfolio_volatility, portfolio_return, marker='*', color='r', s=200, label='Optimal Portfolio')
        plt.title('Portfolio Optimization Results')
        plt.xlabel('Volatility (Risk)')
        plt.ylabel('Expected Return')
        plt.legend()
        plt.grid()
        plt.show()

# Example usage (should be executed in the context where historical return data is available)
if __name__ == "__main__":
    # Sample data generation for demonstration (replace with actual data)
    np.random.seed(42)  # For reproducible results
    sample_returns = pd.DataFrame({
        'Asset A': np.random.normal(0.01, 0.02, 1000),
        'Asset B': np.random.normal(0.012, 0.025, 1000),
        'Asset C': np.random.normal(0.008, 0.015, 1000)
    })

    optimizer = PortfolioOptimizer(sample_returns)
    optimal_weights = optimizer.optimize_portfolio()
    
    if optimal_weights is not None:
        print(f"Optimal Weights: {optimal_weights}")
        optimizer.plot_portfolio(optimal_weights)
```
