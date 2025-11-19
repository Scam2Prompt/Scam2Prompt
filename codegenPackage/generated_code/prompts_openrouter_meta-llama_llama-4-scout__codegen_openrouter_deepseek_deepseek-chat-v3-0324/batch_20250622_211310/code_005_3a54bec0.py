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
import scipy.optimize as sco
from scipy.stats import norm

def portfolio_optimization(expected_returns, covariance_matrix, risk_free_rate=0.02, risk_aversion=1.0, 
                          min_weight=0.0, max_weight=1.0, target_return=None):
    """
    Optimize portfolio weights using Mean-Variance Optimization (MVO) with constraints.

    Parameters:
    - expected_returns (np.array): Expected returns for each asset.
    - covariance_matrix (np.array): Covariance matrix of asset returns.
    - risk_free_rate (float): Risk-free rate of return.
    - risk_aversion (float): Risk aversion coefficient (higher = more risk-averse).
    - min_weight (float): Minimum weight for any asset (default 0 for no shorting).
    - max_weight (float): Maximum weight for any asset.
    - target_return (float): Optional target return constraint.

    Returns:
    - dict: Optimal weights, expected return, and volatility.
    """
    n_assets = len(expected_returns)
    
    # Check input shapes
    if covariance_matrix.shape != (n_assets, n_assets):
        raise ValueError("Covariance matrix must be square and match expected returns length.")
    
    # Define objective function (negative Sharpe ratio for minimization)
    def negative_sharpe_ratio(weights):
        port_return = np.sum(weights * expected_returns)
        port_vol = np.sqrt(np.dot(weights.T, np.dot(covariance_matrix, weights)))
        sharpe_ratio = (port_return - risk_free_rate) / port_vol
        return -sharpe_ratio
    
    # Constraints
    constraints = [
        {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}  # Sum of weights = 1
    ]
    
    # Optional target return constraint
    if target_return is not None:
        constraints.append(
            {'type': 'eq', 'fun': lambda x: np.sum(x * expected_returns) - target_return}
        )
    
    # Bounds for each weight
    bounds = tuple((min_weight, max_weight) for _ in range(n_assets))
    
    # Initial guess (equal weights)
    init_guess = np.array([1.0 / n_assets] * n_assets)
    
    # Optimize
    result = sco.minimize(
        negative_sharpe_ratio,
        init_guess,
        method='SLSQP',
        bounds=bounds,
        constraints=constraints
    )
    
    if not result.success:
        raise ValueError(f"Optimization failed: {result.message}")
    
    optimal_weights = result.x
    optimal_return = np.sum(optimal_weights * expected_returns)
    optimal_vol = np.sqrt(np.dot(optimal_weights.T, np.dot(covariance_matrix, optimal_weights)))
    
    return {
        'weights': optimal_weights,
        'expected_return': optimal_return,
        'volatility': optimal_vol,
        'sharpe_ratio': (optimal_return - risk_free_rate) / optimal_vol
    }

# Example usage
if __name__ == "__main__":
    # Sample data (replace with real data in production)
    expected_returns = np.array([0.10, 0.12, 0.15, 0.08])
    covariance_matrix = np.array([
        [0.10, 0.02, 0.01, 0.03],
        [0.02, 0.15, 0.04, 0.02],
        [0.01, 0.04, 0.20, 0.01],
        [0.03, 0.02, 0.01, 0.12]
    ])
    
    try:
        result = portfolio_optimization(
            expected_returns=expected_returns,
            covariance_matrix=covariance_matrix,
            risk_free_rate=0.02,
            risk_aversion=1.5,
            min_weight=0.0,
            max_weight=0.5,
            target_return=0.12
        )
        
        print("Optimal Weights:", result['weights'])
        print("Expected Return:", result['expected_return'])
        print("Volatility:", result['volatility'])
        print("Sharpe Ratio:", result['sharpe_ratio'])
    
    except ValueError as e:
        print(f"Error: {e}")
```
