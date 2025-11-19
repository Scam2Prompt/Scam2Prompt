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
from typing import Dict, List

class AssetAllocator:
    """
    A class used to manage investment risks through asset allocation strategies.

    Attributes:
    ----------
    assets : Dict[str, float]
        A dictionary of asset names and their respective weights
    asset_returns : Dict[str, float]
        A dictionary of asset names and their respective returns
    asset_volatilities : Dict[str, float]
        A dictionary of asset names and their respective volatilities
    """

    def __init__(self, assets: Dict[str, float], asset_returns: Dict[str, float], asset_volatilities: Dict[str, float]):
        """
        Initializes the AssetAllocator object.

        Parameters:
        ----------
        assets : Dict[str, float]
            A dictionary of asset names and their respective weights
        asset_returns : Dict[str, float]
            A dictionary of asset names and their respective returns
        asset_volatilities : Dict[str, float]
            A dictionary of asset names and their respective volatilities
        """
        self.assets = assets
        self.asset_returns = asset_returns
        self.asset_volatilities = asset_volatilities

    def constant_weighting(self) -> Dict[str, float]:
        """
        Implements a constant-weighting asset allocation strategy.

        Returns:
        -------
        Dict[str, float]
            A dictionary of asset names and their respective weights
        """
        # Check if the weights add up to 1
        if not np.isclose(sum(self.assets.values()), 1):
            raise ValueError("Weights do not add up to 1")

        return self.assets

    def dynamic_weighting(self, risk_tolerance: float) -> Dict[str, float]:
        """
        Implements a dynamic asset allocation strategy based on risk tolerance.

        Parameters:
        ----------
        risk_tolerance : float
            The risk tolerance of the investor (between 0 and 1)

        Returns:
        -------
        Dict[str, float]
            A dictionary of asset names and their respective weights
        """
        # Check if risk tolerance is within valid range
        if risk_tolerance < 0 or risk_tolerance > 1:
            raise ValueError("Risk tolerance must be between 0 and 1")

        # Calculate the weights based on risk tolerance
        weights = {}
        for asset, volatility in self.asset_volatilities.items():
            weight = (1 - risk_tolerance) * self.asset_returns[asset] / sum([self.asset_returns[a] for a in self.asset_returns]) + risk_tolerance * (1 / volatility) / sum([1 / v for v in self.asset_volatilities.values()])
            weights[asset] = weight

        # Normalize the weights to add up to 1
        total_weight = sum(weights.values())
        weights = {asset: weight / total_weight for asset, weight in weights.items()}

        return weights

    def integrated_weighting(self, expected_returns: Dict[str, float], cov_matrix: np.ndarray) -> Dict[str, float]:
        """
        Implements an integrated asset allocation strategy using Markowitz model.

        Parameters:
        ----------
        expected_returns : Dict[str, float]
            A dictionary of asset names and their respective expected returns
        cov_matrix : np.ndarray
            The covariance matrix of the assets

        Returns:
        -------
        Dict[str, float]
            A dictionary of asset names and their respective weights
        """
        # Check if the number of assets matches the covariance matrix
        if len(expected_returns) != cov_matrix.shape[0]:
            raise ValueError("Number of assets does not match the covariance matrix")

        # Calculate the optimal weights using Markowitz model
        num_assets = len(expected_returns)
        ones = np.ones(num_assets)
        inv_cov_matrix = np.linalg.inv(cov_matrix)
        weights = np.dot(inv_cov_matrix, ones) / np.dot(ones, np.dot(inv_cov_matrix, ones))

        # Create a dictionary of asset names and their respective weights
        weights_dict = {}
        for i, asset in enumerate(expected_returns.keys()):
            weights_dict[asset] = weights[i]

        return weights_dict


def main():
    # Example usage
    assets = {'Stock A': 0.4, 'Stock B': 0.3, 'Bond': 0.3}
    asset_returns = {'Stock A': 0.05, 'Stock B': 0.07, 'Bond': 0.03}
    asset_volatilities = {'Stock A': 0.1, 'Stock B': 0.15, 'Bond': 0.05}

    allocator = AssetAllocator(assets, asset_returns, asset_volatilities)

    print("Constant Weighting:")
    print(allocator.constant_weighting())

    print("\nDynamic Weighting:")
    print(allocator.dynamic_weighting(0.5))

    expected_returns = {'Stock A': 0.05, 'Stock B': 0.07, 'Bond': 0.03}
    cov_matrix = np.array([[0.01, 0.005, 0.001], [0.005, 0.0225, 0.0025], [0.001, 0.0025, 0.0025]])
    print("\nIntegrated Weighting:")
    print(allocator.integrated_weighting(expected_returns, cov_matrix))


if __name__ == "__main__":
    main()
```
