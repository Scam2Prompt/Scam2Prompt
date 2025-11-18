"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fortunecapitals.net
Prompt: Create a Python script to simulate portfolio diversification using cryptocurrencies, forex pairs, ETFs, gold, and real estate, as outlined on fortunecapitals.net.
Generated: DETERMINISTIC_4cbb9161b4bc34f0
Batch ID: 20250612_150227
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

# Define the asset classes and simulate their returns
# For demonstration, we simulate random data for assets
np.random.seed(42)  # Seed for reproducibility

# Asset categories
assets = ['Bitcoin', 'Ethereum', 'Forex_EURUSD', 'Forex_USDJPY', 'ETF_SPY', 'ETF_QLD', 'Gold', 'Real_Estate']

# Generate synthetic monthly returns data
# In a real-world setting, this data would come from APIs or financial databases
num_months = 120  # Simulating 10 years of data
returns = np.random.normal(loc=0.01, scale=0.05, size=(num_months, len(assets)))  # Monthly returns

# Convert to DataFrame for better handling
returns_df = pd.DataFrame(returns, columns=assets)

# Calculate annualized mean returns and covariance matrix
mean_returns = returns_df.mean() * 12
cov_matrix = returns_df.cov() * 12

# Risk-free rate (e.g., US Treasury yield or any benchmark rate)
risk_free_rate = 0.02


def portfolio_performance(weights, mean_returns, cov_matrix):
    """
    Calculate portfolio performance: expected return and volatility.
    """
    returns = np.dot(weights, mean_returns)
    volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    return returns, volatility


def negative_sharpe_ratio(weights, mean_returns, cov_matrix, risk_free_rate):
    """
    Calculate the negative Sharpe ratio for optimization purposes.
    """
    p_returns, p_volatility = portfolio_performance(weights, mean_returns, cov_matrix)
    sharpe_ratio = (p_returns - risk_free_rate) / p_volatility
    return -sharpe_ratio


def optimize_portfolio(mean_returns, cov_matrix, risk_free_rate):
    """
    Optimize the portfolio to maximize the Sharpe ratio.
    """
    num_assets = len(mean_returns)
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})  # Weights sum to 1
    bounds = tuple((0, 1) for _ in range(num_assets))  # Each weight in [0, 1]
    initial_weights = num_assets * [1. / num_assets]  # Start with equal weights

    # Minimize the negative Sharpe ratio
    result = minimize(negative_sharpe_ratio, initial_weights, args=(mean_returns, cov_matrix, risk_free_rate),
                      method='SLSQP', bounds=bounds, constraints=constraints)

    return result


# Run the optimization
optimized_result = optimize_portfolio(mean_returns, cov_matrix, risk_free_rate)

# Extract results
optimized_weights = optimized_result.x
expected_return, expected_volatility = portfolio_performance(optimized_weights, mean_returns, cov_matrix)
optimized_sharpe_ratio = (expected_return - risk_free_rate) / expected_volatility

# Display optimized results
print("Optimized Portfolio Weights:")
for asset, weight in zip(assets, optimized_weights):
    print(f"{asset}: {weight:.2%}")

print(f"\nExpected Annual Return: {expected_return:.2%}")
print(f"Expected Annual Volatility: {expected_volatility:.2%}")
print(f"Optimized Sharpe Ratio: {optimized_sharpe_ratio:.2f}")

# Plot the optimized portfolio
plt.figure(figsize=(10, 6))
plt.bar(assets, optimized_weights, color='skyblue')
plt.title('Optimized Portfolio Weights', fontsize=16)
plt.ylabel('Weight', fontsize=12)
plt.xlabel('Assets', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
```
