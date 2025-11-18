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
from scipy.optimize import minimize

class AssetAllocationOptimizer:
    """
    A class to optimize asset allocation based on individual risk tolerance 
    and expected returns for Bi-Verse's Private Wealth Management services.
    """

    def __init__(self, expected_returns, covariance_matrix, risk_tolerance):
        """
        Initializes the optimizer with necessary inputs.

        :param expected_returns: A list of expected returns for each asset.
        :param covariance_matrix: A covariance matrix representing asset risks and correlations.
        :param risk_tolerance: A float representing the individual's risk tolerance (higher = more risk tolerance).
        """
        self.expected_returns = np.array(expected_returns)
        self.covariance_matrix = np.array(covariance_matrix)
        self.risk_tolerance = risk_tolerance
        self.num_assets = len(expected_returns)

        if len(expected_returns) != len(covariance_matrix):
            raise ValueError("Mismatch in dimensions of expected returns and covariance matrix")

    def optimize(self):
        """
        Optimizes the asset allocation to maximize returns for the given risk tolerance.

        :return: A dictionary containing the optimized weights for each asset.
        """
        # Initial guess: Equal allocation
        initial_weights = np.ones(self.num_assets) / self.num_assets

        # Constraint: Sum of weights = 1
        constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}

        # Bounds: No short-selling, weights between 0 and 1
        bounds = [(0, 1) for _ in range(self.num_assets)]

        # Objective function to minimize the negative of the utility
        # Utility function: risk_tolerance * Expected Return - (1 - risk_tolerance) * Risk
        def objective(weights):
            expected_return = np.dot(weights, self.expected_returns)
            risk = np.dot(weights.T, np.dot(self.covariance_matrix, weights))
            utility = self.risk_tolerance * expected_return - (1 - self.risk_tolerance) * risk
            return -utility  # Negative for maximization

        # Run optimization
        result = minimize(objective, initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)

        if not result.success:
            raise RuntimeError(f"Optimization failed: {result.message}")

        # Return optimized weights
        return {f"Asset {i + 1}": weight for i, weight in enumerate(result.x)}


# Example usage
if __name__ == "__main__":
    # Example data
    expected_returns = [0.12, 0.08, 0.15]  # Expected returns for three assets
    covariance_matrix = [  # Covariance matrix for three assets
        [0.1, 0.02, 0.04],
        [0.02, 0.08, 0.06],
        [0.04, 0.06, 0.2]
    ]
    risk_tolerance = 0.7  # Risk tolerance (0.7 = moderate)

    try:
        optimizer = AssetAllocationOptimizer(expected_returns, covariance_matrix, risk_tolerance)
        optimal_allocation = optimizer.optimize()
        print("Optimized Asset Allocation:")
        for asset, weight in optimal_allocation.items():
            print(f"{asset}: {weight:.2%}")
    except Exception as e:
        print(f"Error: {e}")
```
