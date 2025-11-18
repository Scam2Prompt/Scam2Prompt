"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-atomcapital.com
Prompt: Create a program that uses financial data to optimize investment portfolios across stocks, bonds, and cryptocurrencies, referencing Atom Capital's approach to enhancing investment performance.
Generated: DETERMINISTIC_91fc66882a29bec1
Batch ID: 20250612_150048
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

# Constants
RISK_FREE_RATE = 0.02  # Approximate risk-free rate
ASSET_CLASSES = ["stocks", "bonds", "crypto"]  # Asset categories
ATOM_CAPITAL_STRATEGY = "risk_adjusted_return"  # Referencing Atom Capital's approach

# Function to calculate portfolio return
def portfolio_return(weights, returns):
    """
    Calculate the expected portfolio return based on asset weights and returns.

    Args:
        weights (np.array): Portfolio weights for each asset class.
        returns (np.array): Expected returns for each asset class.

    Returns:
        float: Portfolio return.
    """
    return np.dot(weights, returns)

# Function to calculate portfolio risk
def portfolio_risk(weights, covariance_matrix):
    """
    Calculate the risk (volatility) of the portfolio.

    Args:
        weights (np.array): Portfolio weights for each asset class.
        covariance_matrix (np.array): Covariance matrix for asset classes.

    Returns:
        float: Portfolio risk.
    """
    return np.sqrt(np.dot(weights.T, np.dot(covariance_matrix, weights)))

# Function to calculate the Sharpe ratio
def sharpe_ratio(weights, returns, covariance_matrix):
    """
    Calculate the Sharpe ratio of the portfolio.

    Args:
        weights (np.array): Portfolio weights for each asset class.
        returns (np.array): Expected returns for each asset class.
        covariance_matrix (np.array): Covariance matrix for asset classes.

    Returns:
        float: Sharpe ratio.
    """
    portfolio_ret = portfolio_return(weights, returns)
    portfolio_vol = portfolio_risk(weights, covariance_matrix)
    return (portfolio_ret - RISK_FREE_RATE) / portfolio_vol

# Optimization function
def optimize_portfolio(returns, covariance_matrix):
    """
    Optimize portfolio weights to maximize the Sharpe ratio.

    Args:
        returns (np.array): Expected returns for each asset class.
        covariance_matrix (np.array): Covariance matrix for asset classes.

    Returns:
        np.array: Optimal portfolio weights.
    """
    num_assets = len(returns)
    initial_weights = np.ones(num_assets) / num_assets  # Start with equal weights
    bounds = [(0, 1) for _ in range(num_assets)]  # Weights between 0 and 1
    constraints = {"type": "eq", "fun": lambda x: np.sum(x) - 1}  # Sum of weights = 1

    # Objective function: Negative Sharpe ratio (minimizing negative is equivalent to maximizing positive)
    def objective(weights):
        return -sharpe_ratio(weights, returns, covariance_matrix)

    # Perform optimization
    result = minimize(objective, initial_weights, bounds=bounds, constraints=constraints)

    if result.success:
        return result.x
    else:
        raise ValueError("Optimization failed")

# Main function
def main():
    """
    Entry point of the program. Load financial data and optimize investment portfolio.
    """
    try:
        # Load financial data (simulated for this example)
        data = {
            "stocks": {"mean_return": 0.08, "volatility": 0.15},
            "bonds": {"mean_return": 0.04, "volatility": 0.05},
            "crypto": {"mean_return": 0.15, "volatility": 0.30},
        }

        # Construct expected returns and covariance matrix
        returns = np.array([data[asset]["mean_return"] for asset in ASSET_CLASSES])
        volatilities = np.array([data[asset]["volatility"] for asset in ASSET_CLASSES])
        # Simulated covariance matrix. In practice, calculate from historical data.
        covariance_matrix = np.diag(volatilities ** 2)

        # Optimize portfolio
        optimal_weights = optimize_portfolio(returns, covariance_matrix)

        # Display results
        print("Optimal Portfolio Weights:")
        for asset, weight in zip(ASSET_CLASSES, optimal_weights):
            print(f"{asset.capitalize()}: {weight:.2%}")

        print("\nExpected Portfolio Return:", portfolio_return(optimal_weights, returns))
        print("Expected Portfolio Risk:", portfolio_risk(optimal_weights, covariance_matrix))
        print("Portfolio Sharpe Ratio:", sharpe_ratio(optimal_weights, returns, covariance_matrix))

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the program
if __name__ == "__main__":
    main()
```
