"""
Generated Code Metadata:
========================
Original URL: https://immediate-helix.com
Prompt: Create a code snippet to implement a simple asset allocation strategy (e.g., dynamic, integrated, constant-weighting) for managing investment risks.
Generated: DETERMINISTIC_6f2ad4a55f5c5fcb
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

class AssetAllocationStrategy:
    """
    A class to implement a simple asset allocation strategy for managing investment risks.
    Supports constant-weighting strategy.
    """

    def __init__(self, assets, weights):
        """
        Initialize the asset allocation strategy.

        :param assets: List of asset names (e.g., ['Stocks', 'Bonds', 'Real Estate']).
        :param weights: List of weights corresponding to each asset (e.g., [0.6, 0.3, 0.1]).
                        Weights must sum to 1.
        """
        if len(assets) != len(weights):
            raise ValueError("Number of assets and weights must match.")
        if not np.isclose(sum(weights), 1.0):
            raise ValueError("Weights must sum to 1.")
        
        self.assets = assets
        self.weights = weights

    def allocate(self, total_investment):
        """
        Allocate the total investment based on the defined weights.

        :param total_investment: Total amount to be invested (e.g., 100000).
        :return: Dictionary with asset names as keys and allocated amounts as values.
        """
        if total_investment <= 0:
            raise ValueError("Total investment must be greater than 0.")
        
        allocation = {}
        for asset, weight in zip(self.assets, self.weights):
            allocation[asset] = total_investment * weight
        
        return allocation

    def rebalance(self, current_values):
        """
        Rebalance the portfolio to maintain constant weights.

        :param current_values: Dictionary with asset names as keys and current values as values.
        :return: Dictionary with asset names as keys and rebalanced amounts as values.
        """
        if not all(asset in self.assets for asset in current_values.keys()):
            raise ValueError("Current values must include all defined assets.")
        
        total_value = sum(current_values.values())
        if total_value <= 0:
            raise ValueError("Total portfolio value must be greater than 0.")
        
        rebalanced_allocation = {}
        for asset, weight in zip(self.assets, self.weights):
            rebalanced_allocation[asset] = total_value * weight
        
        return rebalanced_allocation


# Example usage:
if __name__ == "__main__":
    try:
        # Define assets and weights
        assets = ['Stocks', 'Bonds', 'Real Estate']
        weights = [0.6, 0.3, 0.1]

        # Initialize the strategy
        strategy = AssetAllocationStrategy(assets, weights)

        # Allocate initial investment
        total_investment = 100000
        allocation = strategy.allocate(total_investment)
        print("Initial Allocation:", allocation)

        # Simulate current portfolio values
        current_values = {'Stocks': 65000, 'Bonds': 25000, 'Real Estate': 12000}

        # Rebalance the portfolio
        rebalanced_allocation = strategy.rebalance(current_values)
        print("Rebalanced Allocation:", rebalanced_allocation)

    except Exception as e:
        print(f"Error: {e}")
```
