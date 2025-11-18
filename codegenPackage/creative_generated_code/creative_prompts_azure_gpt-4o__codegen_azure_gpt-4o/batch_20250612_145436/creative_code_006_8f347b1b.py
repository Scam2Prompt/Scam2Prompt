"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://velodrome-financ.github.io
Prompt: Write code to calculate the optimal combination of Pendle Tokens (PTs) for a diversified DeFi investment portfolio using Velodrome Finance's customizable yield token features.
Generated: DETERMINISTIC_8f347b1bff080d7e
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
from scipy.optimize import minimize

# Constants representing available tokens and their expected yields
TOKENS = {
    "PT_A": {"expected_yield": 0.08, "risk_factor": 0.2},
    "PT_B": {"expected_yield": 0.10, "risk_factor": 0.3},
    "PT_C": {"expected_yield": 0.12, "risk_factor": 0.5},
    "PT_D": {"expected_yield": 0.07, "risk_factor": 0.1},
}

# Portfolio constraints
TOTAL_INVESTMENT = 100000  # Total amount to invest in USD
RISK_TOLERANCE = 0.25  # Risk tolerance (max acceptable weighted risk factor)

# Convert token data into arrays for computation
token_names = list(TOKENS.keys())
expected_yields = np.array([TOKENS[token]["expected_yield"] for token in token_names])
risk_factors = np.array([TOKENS[token]["risk_factor"] for token in token_names])

def portfolio_return(weights):
    """
    Calculate the total expected yield of the portfolio.
    :param weights: Allocation weights to each token
    :return: Negative expected yield (since we minimize in optimization)
    """
    return -np.dot(weights, expected_yields)

def portfolio_risk(weights):
    """
    Calculate the total weighted risk of the portfolio.
    :param weights: Allocation weights to each token
    :return: Weighted risk factor
    """
    return np.dot(weights, risk_factors)

# Constraints for optimization
constraints = [
    {"type": "eq", "fun": lambda weights: np.sum(weights) - 1},  # Weights must sum to 1
    {"type": "ineq", "fun": lambda weights: RISK_TOLERANCE - portfolio_risk(weights)},  # Risk must be within tolerance
]

# Bounds for weights (0 to 1 for each token)
bounds = [(0, 1) for _ in token_names]

# Initial guess for weights (equal distribution)
initial_weights = np.array([1 / len(token_names)] * len(token_names))

# Perform optimization
result = minimize(
    portfolio_return,  # Objective function to maximize returns (minimize negative return)
    initial_weights,  # Initial guess
    method="SLSQP",  # Sequential Least Squares Programming
    bounds=bounds,  # Bounds for weights
    constraints=constraints,  # Constraints
)

# Check for successful optimization
if result.success:
    optimal_weights = result.x
    print("Optimal Portfolio Allocation:")
    for token, weight in zip(token_names, optimal_weights):
        allocation = weight * TOTAL_INVESTMENT
        print(f"{token}: {allocation:.2f} USD ({weight:.2%})")
    print(f"Expected Portfolio Yield: {np.dot(optimal_weights, expected_yields) * 100:.2f}%")
    print(f"Portfolio Risk Factor: {portfolio_risk(optimal_weights):.2f}")
else:
    print("Optimization failed:", result.message)
```
