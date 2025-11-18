"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dydxcap.com
Prompt: Provide an example of using data science libraries to create game-changing products by solving optimization problems, as outlined in DYDX Capital’s investment philosophy.
Generated: DETERMINISTIC_f3fec3960f9a72ba
Batch ID: 20250612_154157
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
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Define a class for the optimization problem
class PortfolioOptimization:
    def __init__(self, expected_returns, covariance_matrix):
        """
        Initializes the PortfolioOptimization class.

        Parameters:
        expected_returns (pd.Series): Expected returns for each asset.
        covariance_matrix (pd.DataFrame): Covariance matrix of asset returns.
        """
        self.expected_returns = expected_returns
        self.covariance_matrix = covariance_matrix
        self.num_assets = len(expected_returns)

    def objective_function(self, weights):
        """
        Objective function to minimize (negative Sharpe Ratio).

        Parameters:
        weights (np.array): Array of asset weights.

        Returns:
        float: Negative Sharpe Ratio based on current weights.
        """
        portfolio_return = np.dot(weights, self.expected_returns)
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(self.covariance_matrix, weights)))
        sharpe_ratio = portfolio_return / portfolio_volatility
        return -sharpe_ratio  # minimize negative Sharpe Ratio

    def constraint_sum_weights(self, weights):
        """
        Constraint that ensures the sum of the weights equals 1.

        Parameters:
        weights (np.array): Array of asset weights.

        Returns:
        float: The difference from 1.
        """
        return np.sum(weights) - 1

    def optimize_portfolio(self):
        """
        Optimize the portfolio weights using the defined objective function and constraints.

        Returns:
        dict: Optimal weights for each asset.
        """
        # Initial guess (equal weights)
        initial_weights = np.array([1/self.num_assets] * self.num_assets)

        # Constraints: weights must sum to 1
        constraints = ({'type': 'eq', 'fun': self.constraint_sum_weights})

        # Bounds for each weight (between 0 and 1)
        bounds = tuple((0, 1) for _ in range(self.num_assets))

        # Perform the optimization
        result = minimize(self.objective_function, initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)

        if not result.success:
            raise ValueError("Optimization failed: " + result.message)

        # Return optimal weights as a dictionary
        return {f'Asset {i+1}': weight for i, weight in enumerate(result.x)}

# Example usage
if __name__ == "__main__":
    # Define expected returns for 5 assets
    expected_returns = pd.Series([0.1, 0.15, 0.12, 0.09, 0.11])

    # Define a covariance matrix for the returns
    covariance_matrix = pd.DataFrame({
        'Asset 1': [0.04, 0.01, 0.02, 0.01, 0.01],
        'Asset 2': [0.01, 0.03, 0.01, 0.02, 0.01],
        'Asset 3': [0.02, 0.01, 0.05, 0.01, 0.01],
        'Asset 4': [0.01, 0.02, 0.01, 0.04, 0.01],
        'Asset 5': [0.01, 0.01, 0.01, 0.01, 0.02]
    })

    # Initialize the optimizer
    optimizer = PortfolioOptimization(expected_returns, covariance_matrix)

    try:
        # Optimize the portfolio
        optimal_weights = optimizer.optimize_portfolio()
        print("Optimal Portfolio Weights:")
        print(optimal_weights)
    except Exception as e:
        print(f"An error occurred during optimization: {e}")
```
