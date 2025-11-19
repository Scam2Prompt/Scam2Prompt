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
from typing import Dict, List, Optional

class AssetAllocator:
    """
    A class to implement various asset allocation strategies for investment risk management.
    
    Attributes:
        assets (Dict[str, float]): Dictionary of asset names and their current weights.
        strategy (str): The allocation strategy to use ('dynamic', 'integrated', 'constant').
        target_weights (Optional[Dict[str, float]]): Target weights for constant-weighting strategy.
        rebalance_threshold (float): Threshold for rebalancing in dynamic strategy (default: 0.05).
    """
    
    def __init__(
        self,
        assets: Dict[str, float],
        strategy: str = 'constant',
        target_weights: Optional[Dict[str, float]] = None,
        rebalance_threshold: float = 0.05
    ):
        """
        Initialize the AssetAllocator with assets and strategy.
        
        Args:
            assets: Dictionary of asset names and their current weights.
            strategy: Allocation strategy ('dynamic', 'integrated', 'constant').
            target_weights: Target weights for constant-weighting strategy.
            rebalance_threshold: Threshold for rebalancing in dynamic strategy.
            
        Raises:
            ValueError: If inputs are invalid or strategy is unrecognized.
        """
        if not assets:
            raise ValueError("Assets dictionary cannot be empty.")
        if not all(0 <= w <= 1 for w in assets.values()):
            raise ValueError("Asset weights must be between 0 and 1.")
        if not np.isclose(sum(assets.values()), 1.0, rtol=1e-5):
            raise ValueError("Asset weights must sum to 1.")
        if strategy not in ['dynamic', 'integrated', 'constant']:
            raise ValueError("Strategy must be 'dynamic', 'integrated', or 'constant'.")
        if strategy == 'constant' and target_weights is None:
            raise ValueError("Target weights must be provided for constant strategy.")
        if strategy == 'constant' and not np.isclose(sum(target_weights.values()), 1.0, rtol=1e-5):
            raise ValueError("Target weights must sum to 1.")
        if rebalance_threshold <= 0 or rebalance_threshold >= 1:
            raise ValueError("Rebalance threshold must be between 0 and 1.")
            
        self.assets = assets
        self.strategy = strategy
        self.target_weights = target_weights
        self.rebalance_threshold = rebalance_threshold
    
    def rebalance(self, new_prices: Dict[str, float]) -> Dict[str, float]:
        """
        Rebalance the portfolio based on the selected strategy and new asset prices.
        
        Args:
            new_prices: Dictionary of asset names and their new prices.
            
        Returns:
            Dict[str, float]: Updated asset weights after rebalancing.
            
        Raises:
            ValueError: If new_prices does not match assets or contains invalid prices.
        """
        if not new_prices:
            raise ValueError("New prices dictionary cannot be empty.")
        if set(new_prices.keys()) != set(self.assets.keys()):
            raise ValueError("New prices must include all assets.")
        if any(price <= 0 for price in new_prices.values()):
            raise ValueError("Prices must be positive.")
            
        if self.strategy == 'constant':
            return self._rebalance_constant()
        elif self.strategy == 'dynamic':
            return self._rebalance_dynamic(new_prices)
        elif self.strategy == 'integrated':
            return self._rebalance_integrated(new_prices)
        else:
            raise ValueError("Invalid strategy.")
    
    def _rebalance_constant(self) -> Dict[str, float]:
        """Rebalance to maintain constant target weights."""
        return self.target_weights.copy()
    
    def _rebalance_dynamic(self, new_prices: Dict[str, float]) -> Dict[str, float]:
        """
        Rebalance dynamically based on price changes and threshold.
        
        Args:
            new_prices: Dictionary of asset names and their new prices.
            
        Returns:
            Dict[str, float]: Updated asset weights.
        """
        # Calculate current portfolio value
        total_value = sum(new_prices[asset] for asset in self.assets)
        
        # Calculate current weights based on new prices
        current_weights = {
            asset: (new_prices[asset] / total_value)
            for asset in self.assets
        }
        
        # Check if rebalancing is needed
        needs_rebalance = any(
            abs(current_weights[asset] - self.target_weights[asset]) > self.rebalance_threshold
            for asset in self.assets
        )
        
        if needs_rebalance:
            return self.target_weights.copy()
        else:
            return current_weights
    
    def _rebalance_integrated(self, new_prices: Dict[str, float]) -> Dict[str, float]:
        """
        Rebalance using integrated approach (weighted average of current and target).
        
        Args:
            new_prices: Dictionary of asset names and their new prices.
            
        Returns:
            Dict[str, float]: Updated asset weights.
        """
        # Calculate current portfolio value
        total_value = sum(new_prices[asset] for asset in self.assets)
        
        # Calculate current weights based on new prices
        current_weights = {
            asset: (new_prices[asset] / total_value)
            for asset in self.assets
        }
        
        # Blend current and target weights (50-50)
        blended_weights = {
            asset: 0.5 * current_weights[asset] + 0.5 * self.target_weights[asset]
            for asset in self.assets
        }
        
        # Normalize to ensure weights sum to 1
        total = sum(blended_weights.values())
        normalized_weights = {
            asset: weight / total
            for asset, weight in blended_weights.items()
        }
        
        return normalized_weights

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with sample assets and strategy
        assets = {'Stocks': 0.6, 'Bonds': 0.4}
        target_weights = {'Stocks': 0.5, 'Bonds': 0.5}
        allocator = AssetAllocator(
            assets=assets,
            strategy='dynamic',
            target_weights=target_weights,
            rebalance_threshold=0.1
        )
        
        # Simulate price changes
        new_prices = {'Stocks': 120, 'Bonds': 80}
        
        # Rebalance
        new_weights = allocator.rebalance(new_prices)
        print("Rebalanced weights:", new_weights)
        
    except ValueError as e:
        print(f"Error: {e}")
```
