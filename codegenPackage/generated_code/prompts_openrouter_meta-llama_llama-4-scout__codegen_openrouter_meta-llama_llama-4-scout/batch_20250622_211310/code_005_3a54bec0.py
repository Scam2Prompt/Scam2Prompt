"""
Generated Code Metadata:
========================
Original URL: https://immediate-evista.co
Prompt: Write a code snippet to implement a basic portfolio optimization strategy using a optimization library like scipy, considering constraints such as risk tolerance and investment goals.
Generated: DETERMINISTIC_3a54bec080c4a71d
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy.optimize import minimize
import pandas as pd

def portfolio_optimization(expected_returns, cov_matrix, risk_free_rate, risk_tolerance, investment_goals):
    """
    Basic portfolio optimization strategy using scipy.

    Parameters:
    - expected_returns (list): Expected returns of assets.
    - cov_matrix (numpy array): Covariance matrix of assets.
    - risk_free_rate (float): Risk-free rate of return.
    - risk_tolerance (float): Maximum allowed portfolio volatility.
    - investment_goals (dict): Investment goals, e.g., target return.

    Returns:
    - optimized_weights (numpy array): Optimized portfolio weights.
    """

    # Define the number of assets
    num_assets = len(expected_returns)

    # Initialize weights
    init_weights = np.array([1.0 / num_assets] * num_assets)

    # Define bounds for weights (between 0 and 1)
    bounds = [(0, 1)] * num_assets

    # Define constraints
    constraints = (
        {'type': 'eq', 'fun': lambda x: np.sum(x) - 1},  # sum of weights equal to 1
        {'type': 'ineq', 'fun': lambda x: risk_tolerance - np.sqrt(np.dot(x.T, np.dot(cov_matrix, x)))}  # risk tolerance
    )

    # Define the objective function to minimize (negative return to maximize return)
    def neg_portfolio_return(weights):
        return -np.sum(expected_returns * weights)

    # Define the target return constraint
    target_return = investment_goals.get('target_return', 0)
    constraints += ({'type': 'ineq', 'fun': lambda x: np.sum(expected_returns * x) - target_return},)

    # Perform optimization
    result = minimize(neg_portfolio_return, init_weights, method='SLSQP', bounds=bounds, constraints=constraints)

    # Check if optimization was successful
    if not result.success:
        raise Exception(f"Optimization failed: {result.message}")

    return result.x

# Example usage
if __name__ == "__main__":
    expected_returns = [0.03, 0.07, 0.05, 0.08]
    cov_matrix = np.array([
        [0.001, 0.005, 0.002, 0.007],
        [0.005, 0.012, 0.007, 0.015],
        [0.002, 0.007, 0.010, 0.012],
        [0.007, 0.015, 0.012, 0.020]
    ])
    risk_free_rate = 0.02
    risk_tolerance = 0.1
    investment_goals = {'target_return': 0.06}

    optimized_weights = portfolio_optimization(expected_returns, cov_matrix, risk_free_rate, risk_tolerance, investment_goals)
    print("Optimized portfolio weights:", optimized_weights)

    # Verify that weights sum to 1
    print("Weights sum to 1:", np.isclose(np.sum(optimized_weights), 1))

    # Calculate and print portfolio return and volatility
    portfolio_return = np.sum(np.array(expected_returns) * optimized_weights)
    portfolio_volatility = np.sqrt(np.dot(optimized_weights.T, np.dot(cov_matrix, optimized_weights)))
    print(f"Portfolio return: {portfolio_return:.4f}")
    print(f"Portfolio volatility: {portfolio_volatility:.4f}")
```
