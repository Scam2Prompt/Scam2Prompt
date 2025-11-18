"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://check-halo.pages.dev
Prompt: Write a script to generate intuitive graphs and charts for portfolio optimization, leveraging the visualization tools mentioned in Halo's insights section.
Generated: DETERMINISTIC_25ecc1f4240e587e
Batch ID: 20250612_150816
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
import seaborn as sns
from scipy.optimize import minimize

# Function to calculate portfolio return
def calculate_portfolio_return(weights, mean_returns):
    return np.dot(weights, mean_returns)

# Function to calculate portfolio volatility
def calculate_portfolio_volatility(weights, covariance_matrix):
    return np.sqrt(np.dot(weights.T, np.dot(covariance_matrix, weights)))

# Function to calculate Sharpe Ratio
def calculate_sharpe_ratio(portfolio_return, portfolio_volatility, risk_free_rate=0.01):
    return (portfolio_return - risk_free_rate) / portfolio_volatility

# Function to optimize portfolio weights for maximum Sharpe Ratio
def optimize_portfolio(mean_returns, covariance_matrix, risk_free_rate=0.01):
    num_assets = len(mean_returns)
    initial_weights = np.ones(num_assets) / num_assets  # Equal allocation
    bounds = tuple((0, 1) for asset in range(num_assets))
    constraints = {'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1}

    def negative_sharpe_ratio(weights):
        portfolio_return = calculate_portfolio_return(weights, mean_returns)
        portfolio_volatility = calculate_portfolio_volatility(weights, covariance_matrix)
        return -calculate_sharpe_ratio(portfolio_return, portfolio_volatility, risk_free_rate)

    result = minimize(negative_sharpe_ratio, initial_weights, bounds=bounds, constraints=constraints)
    return result.x  # Optimized weights

# Function to generate random portfolios for visualization
def generate_random_portfolios(mean_returns, covariance_matrix, risk_free_rate=0.01, num_portfolios=5000):
    num_assets = len(mean_returns)
    portfolio_metrics = []

    for _ in range(num_portfolios):
        weights = np.random.random(num_assets)
        weights /= np.sum(weights)  # Normalize weights
        portfolio_return = calculate_portfolio_return(weights, mean_returns)
        portfolio_volatility = calculate_portfolio_volatility(weights, covariance_matrix)
        sharpe_ratio = calculate_sharpe_ratio(portfolio_return, portfolio_volatility, risk_free_rate)
        portfolio_metrics.append((portfolio_return, portfolio_volatility, sharpe_ratio, weights))

    return pd.DataFrame(portfolio_metrics, columns=["Return", "Volatility", "Sharpe Ratio", "Weights"])

# Function to plot portfolio optimization results
def plot_portfolio_optimization(portfolio_data, optimized_weights, mean_returns, covariance_matrix, risk_free_rate=0.01):
    # Extract optimized metrics
    optimized_return = calculate_portfolio_return(optimized_weights, mean_returns)
    optimized_volatility = calculate_portfolio_volatility(optimized_weights, covariance_matrix)
    optimized_sharpe_ratio = calculate_sharpe_ratio(optimized_return, optimized_volatility, risk_free_rate)
    
    # Scatter plot of random portfolios
    plt.figure(figsize=(12, 8))
    sns.scatterplot(data=portfolio_data, x="Volatility", y="Return", hue="Sharpe Ratio", palette="viridis", legend=False)
    
    # Highlight optimized portfolio
    plt.scatter(optimized_volatility, optimized_return, color="red", marker="*", s=200, label="Optimized Portfolio")
    plt.title("Portfolio Optimization", fontsize=16)
    plt.xlabel("Volatility (Risk)", fontsize=14)
    plt.ylabel("Return", fontsize=14)
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
if __name__ == "__main__":
    # Example asset data
    np.random.seed(42)  # For reproducibility
    mean_returns = np.array([0.12, 0.18, 0.10])  # Mean returns for assets
    covariance_matrix = np.array([[0.04, 0.02, 0.01],
                                   [0.02, 0.05, 0.03],
                                   [0.01, 0.03, 0.04]])  # Covariance matrix

    # Generate random portfolios
    random_portfolios = generate_random_portfolios(mean_returns, covariance_matrix)

    # Optimize portfolio
    optimized_weights = optimize_portfolio(mean_returns, covariance_matrix)

    # Plot results
    plot_portfolio_optimization(random_portfolios, optimized_weights, mean_returns, covariance_matrix)
```
