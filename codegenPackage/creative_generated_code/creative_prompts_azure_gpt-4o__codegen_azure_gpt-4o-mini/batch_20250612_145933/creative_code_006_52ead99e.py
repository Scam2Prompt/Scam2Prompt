"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bi-verse.org
Prompt: Create a Python program to optimize asset allocation for Bi-Verse's "Private Wealth Management" services, considering individual risk tolerance and expected returns.
Generated: DETERMINISTIC_52ead99e1fead4c5
Batch ID: 20250612_145933
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
    """
    A class to optimize asset allocation for a portfolio based on risk tolerance and expected returns.
    """

    def __init__(self, returns: pd.DataFrame, risk_tolerance: float):
        """
        Initializes the PortfolioOptimizer with asset returns and risk tolerance.

        :param returns: A DataFrame of historical returns for each asset.
        :param risk_tolerance: A float representing the user's risk tolerance (0: low, 1: high).
        """
        self.returns = returns
        self.risk_tolerance = risk_tolerance
        self.num_assets = returns.shape[1]
        self.expected_returns = returns.mean() * 252  # Annualized returns
        self.covariance_matrix = returns.cov() * 252  # Annualized covariance

    def negative_sharpe_ratio(self, weights: np.ndarray) -> float:
        """
        Calculates the negative Sharpe ratio for given weights.

        :param weights: A numpy array of asset weights.
        :return: The negative Sharpe ratio.
        """
        portfolio_return = np.dot(weights, self.expected_returns)
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(self.covariance_matrix, weights)))
        sharpe_ratio = (portfolio_return - 0.02) / portfolio_volatility  # Assuming risk-free rate = 2%
        return -sharpe_ratio  # Minimize the negative Sharpe ratio

    def optimize_portfolio(self) -> dict:
        """
        Optimizes the portfolio based on user risk tolerance and expected returns.

        :return: A dictionary containing optimal weights and performance metrics.
        """
        # Constraints: weights sum to 1 and are between 0 and 1
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        bounds = tuple((0, 1) for _ in range(self.num_assets))
        
        # Initial guess (even allocation)
        initial_guess = np.array(self.num_assets * [1. / self.num_assets])
        
        # Optimization
        result = minimize(self.negative_sharpe_ratio, initial_guess, method='SLSQP', bounds=bounds, constraints=constraints)

        if not result.success:
            raise ValueError("Optimization failed: " + result.message)

        optimal_weights = result.x
        portfolio_return = np.dot(optimal_weights, self.expected_returns)
        portfolio_volatility = np.sqrt(np.dot(optimal_weights.T, np.dot(self.covariance_matrix, optimal_weights)))
        optimal_sharpe = (portfolio_return - 0.02) / portfolio_volatility

        return {
            'weights': optimal_weights,
            'expected_return': portfolio_return,
            'expected_volatility': portfolio_volatility,
            'sharpe_ratio': optimal_sharpe
        }

def main():
    """
    Main function to execute the portfolio optimization.
    """
    # Sample data: Replace with actual historical returns data
    data = {
        'Asset A': np.random.normal(0.01, 0.02, 1000),  # Simulated data
        'Asset B': np.random.normal(0.012, 0.025, 1000),
        'Asset C': np.random.normal(0.008, 0.015, 1000)
    }

    returns_df = pd.DataFrame(data)

    # User-defined risk tolerance (0: conservative, 1: aggressive)
    user_risk_tolerance = 0.6

    # Create an instance of PortfolioOptimizer
    optimizer = PortfolioOptimizer(returns_df, user_risk_tolerance)

    try:
        optimal_portfolio = optimizer.optimize_portfolio()
        print("Optimal Asset Weights:", optimal_portfolio['weights'])
        print("Expected Portfolio Return:", optimal_portfolio['expected_return'])
        print("Expected Portfolio Volatility:", optimal_portfolio['expected_volatility'])
        print("Sharpe Ratio:", optimal_portfolio['sharpe_ratio'])
    except ValueError as e:
        print(f"Error during optimization: {e}")

if __name__ == "__main__":
    main()
```
