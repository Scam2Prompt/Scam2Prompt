"""
Generated Code Metadata:
========================
Original URL: https://monad.financial
Prompt: Compare and contrast different quantitative strategies for investing in digital assets, considering factors such as risk management and capital allocation.
Generated: DETERMINISTIC_88225a54dc59fbeb
Batch ID: 20250622_212100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script compares and contrasts different quantitative strategies for investing in digital assets.
It simulates three strategies: Mean-Reversion, Momentum, and Equal-Weight Allocation.
The script evaluates each strategy based on risk management and capital allocation.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulated price data for digital assets
np.random.seed(42)  # For reproducibility
dates = pd.date_range(start="2020-01-01", end="2023-01-01", freq="D")
assets = ["Asset_A", "Asset_B", "Asset_C"]
price_data = pd.DataFrame(
    np.random.normal(loc=1.001, scale=0.02, size=(len(dates), len(assets))).cumprod(axis=0),
    index=dates,
    columns=assets,
)

# Parameters for strategies
initial_capital = 100000  # Starting capital in USD
transaction_cost = 0.001  # Transaction cost as a percentage

# Helper function for calculating portfolio value
def calculate_portfolio_value(weights, prices, capital):
    """
    Calculate portfolio value given weights, prices, and capital.
    :param weights: Portfolio weights (array-like)
    :param prices: Current prices of assets (array-like)
    :param capital: Total capital available
    :return: Portfolio value
    """
    return np.dot(weights, prices) * capital

# Strategy 1: Mean-Reversion
def mean_reversion_strategy(prices, lookback=20):
    """
    Mean-Reversion strategy: Buy assets that are below their moving average.
    :param prices: Historical price data (DataFrame)
    :param lookback: Lookback period for moving average
    :return: Portfolio weights (DataFrame)
    """
    moving_avg = prices.rolling(window=lookback).mean()
    weights = (prices < moving_avg).astype(float)
    weights = weights.div(weights.sum(axis=1), axis=0).fillna(0)  # Normalize weights
    return weights

# Strategy 2: Momentum
def momentum_strategy(prices, lookback=20):
    """
    Momentum strategy: Buy assets with the highest price growth over the lookback period.
    :param prices: Historical price data (DataFrame)
    :param lookback: Lookback period for momentum calculation
    :return: Portfolio weights (DataFrame)
    """
    momentum = prices.pct_change(periods=lookback)
    weights = (momentum > 0).astype(float)
    weights = weights.div(weights.sum(axis=1), axis=0).fillna(0)  # Normalize weights
    return weights

# Strategy 3: Equal-Weight Allocation
def equal_weight_strategy(prices):
    """
    Equal-Weight strategy: Allocate capital equally across all assets.
    :param prices: Historical price data (DataFrame)
    :return: Portfolio weights (DataFrame)
    """
    weights = pd.DataFrame(
        np.ones_like(prices) / len(prices.columns),
        index=prices.index,
        columns=prices.columns,
    )
    return weights

# Evaluate strategies
def evaluate_strategy(prices, weights, initial_capital, transaction_cost):
    """
    Evaluate a strategy by calculating portfolio value over time.
    :param prices: Historical price data (DataFrame)
    :param weights: Portfolio weights (DataFrame)
    :param initial_capital: Starting capital
    :param transaction_cost: Transaction cost as a percentage
    :return: Portfolio value over time (Series)
    """
    portfolio_value = []
    capital = initial_capital
    for i in range(len(prices)):
        if i > 0:
            # Apply transaction costs
            capital -= transaction_cost * capital
        current_prices = prices.iloc[i]
        current_weights = weights.iloc[i]
        portfolio_value.append(calculate_portfolio_value(current_weights, current_prices, capital))
    return pd.Series(portfolio_value, index=prices.index)

# Generate weights for each strategy
mean_reversion_weights = mean_reversion_strategy(price_data)
momentum_weights = momentum_strategy(price_data)
equal_weight_weights = equal_weight_strategy(price_data)

# Evaluate portfolio values
mean_reversion_value = evaluate_strategy(price_data, mean_reversion_weights, initial_capital, transaction_cost)
momentum_value = evaluate_strategy(price_data, momentum_weights, initial_capital, transaction_cost)
equal_weight_value = evaluate_strategy(price_data, equal_weight_weights, initial_capital, transaction_cost)

# Plot results
plt.figure(figsize=(12, 6))
plt.plot(mean_reversion_value, label="Mean-Reversion Strategy")
plt.plot(momentum_value, label="Momentum Strategy")
plt.plot(equal_weight_value, label="Equal-Weight Strategy")
plt.title("Portfolio Value Over Time")
plt.xlabel("Date")
plt.ylabel("Portfolio Value (USD)")
plt.legend()
plt.grid()
plt.show()
```
