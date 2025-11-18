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
import numpy as np
import pandas as pd
from scipy.optimize import minimize

# Define a function to calculate portfolio return
def portfolio_return(weights, returns):
    """
    Calculate portfolio return given weights and asset returns.

    Parameters:
    weights (numpy.ndarray): Asset weights in the portfolio.
    returns (numpy.ndarray): Expected returns for each asset.

    Returns:
    float: Portfolio expected return.
    """
    return np.dot(weights, returns)

# Define a function to calculate portfolio risk (standard deviation)
def portfolio_risk(weights, cov_matrix):
    """
    Calculate portfolio risk (standard deviation) given weights and covariance matrix.

    Parameters:
    weights (numpy.ndarray): Asset weights in the portfolio.
    cov_matrix (numpy.ndarray): Covariance matrix of asset returns.

    Returns:
    float: Portfolio risk (standard deviation).
    """
    return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

# Define the optimization function
def optimize_portfolio(expected_returns, cov_matrix, risk_free_rate=0.02):
    """
    Optimize portfolio weights to maximize the Sharpe ratio.

    Parameters:
    expected_returns (numpy.ndarray): Expected returns for each asset.
    cov_matrix (numpy.ndarray): Covariance matrix of asset returns.
    risk_free_rate (float): Risk-free rate of return (default: 0.02).

    Returns:
    dict: Optimized portfolio weights and performance metrics.
    """
    num_assets = len(expected_returns)
    
    # Initial weights (equal allocation)
    initial_weights = np.ones(num_assets) / num_assets
    
    # Constraints: weights must sum to 1
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    
    # Bounds: weights between 0 and 1
    bounds = tuple((0, 1) for _ in range(num_assets))
    
    # Objective function: negative Sharpe ratio (to maximize, minimize negative)
    def negative_sharpe_ratio(weights):
        port_return = portfolio_return(weights, expected_returns)
        port_risk = portfolio_risk(weights, cov_matrix)
        sharpe_ratio = (port_return - risk_free_rate) / port_risk
        return -sharpe_ratio
    
    # Perform optimization
    result = minimize(negative_sharpe_ratio, initial_weights, bounds=bounds, constraints=constraints)
    
    # Capture optimized weights
    optimized_weights = result.x
    
    # Calculate performance metrics
    final_return = portfolio_return(optimized_weights, expected_returns)
    final_risk = portfolio_risk(optimized_weights, cov_matrix)
    final_sharpe = (final_return - risk_free_rate) / final_risk
    
    return {
        'weights': optimized_weights,
        'return': final_return,
        'risk': final_risk,
        'sharpe_ratio': final_sharpe
    }

# Example Usage
if __name__ == "__main__":
    # Simulated data (replace with actual data for production use)
    assets = ["BTC", "ETH", "Gold", "Silver", "SPY", "QQQ"]
    expected_returns = np.array([0.12, 0.18, 0.04, 0.06, 0.08, 0.10])  # Annualized expected returns
    cov_matrix = np.array([
        [0.15, 0.10, 0.02, 0.02, 0.03, 0.04],
        [0.10, 0.20, 0.03, 0.03, 0.05, 0.06],
        [0.02, 0.03, 0.05, 0.02, 0.01, 0.02],
        [0.02, 0.03, 0.02, 0.06, 0.01, 0.02],
        [0.03, 0.05, 0.01, 0.01, 0.10, 0.08],
        [0.04, 0.06, 0.02, 0.02, 0.08, 0.12]
    ])  # Covariance matrix
    
    # Risk-free rate
    risk_free_rate = 0.02
    
    # Optimize portfolio
    optimal_portfolio = optimize_portfolio(expected_returns, cov_matrix, risk_free_rate)
    
    # Display results
    print("Optimized Portfolio:")
    for asset, weight in zip(assets, optimal_portfolio['weights']):
        print(f"{asset}: {weight:.2%}")
    print(f"Expected Return: {optimal_portfolio['return']:.2%}")
    print(f"Risk (Standard Deviation): {optimal_portfolio['risk']:.2%}")
    print(f"Sharpe Ratio: {optimal_portfolio['sharpe_ratio']:.2f}")
```
