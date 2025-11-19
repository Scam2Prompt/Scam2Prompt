"""
Generated Code Metadata:
========================
Original URL: https://parallels.top
Prompt: Create a function that boosts in-game earnings based on the ownership of specific digital assets, such as Avatars, as described in the Parallel TCG system.
Generated: DETERMINISTIC_9d122eb5ad43e4b1
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List
from enum import Enum
from dataclasses import dataclass

class AssetType(str, Enum):
    """Enum for digital asset types."""
    AVATAR = "avatar"
    OTHER = "other"

@dataclass
class DigitalAsset:
    """Class representing a digital asset."""
    id: int
    type: AssetType
    rarity: str
    boost_multiplier: float

class EarningsCalculator:
    """Class responsible for calculating in-game earnings based on digital asset ownership."""

    def __init__(self, base_earnings: float, asset_boosts: Dict[int, float]):
        """
        Initialize the earnings calculator.

        Args:
        - base_earnings (float): The base earnings without any boosts.
        - asset_boosts (Dict[int, float]): A dictionary of asset IDs to their corresponding boost multipliers.
        """
        self.base_earnings = base_earnings
        self.asset_boosts = asset_boosts

    def calculate_earnings(self, owned_assets: List[DigitalAsset]) -> float:
        """
        Calculate the total earnings based on the owned digital assets.

        Args:
        - owned_assets (List[DigitalAsset]): A list of digital assets owned by the player.

        Returns:
        - float: The total earnings.
        """
        total_boost_multiplier = 1.0

        for asset in owned_assets:
            if asset.id in self.asset_boosts:
                total_boost_multiplier += self.asset_boosts[asset.id]
            elif asset.boost_multiplier > 0:
                total_boost_multiplier += asset.boost_multiplier
            else:
                # Log or handle invalid boost_multiplier
                pass

        total_earnings = self.base_earnings * total_boost_multiplier
        return max(total_earnings, 0)  # Ensure earnings are non-negative

def main():
    # Example usage
    base_earnings = 100.0
    asset_boosts = {
        1: 0.5,  # 50% boost for asset with ID 1
        2: 1.0   # 100% boost for asset with ID 2
    }

    calculator = EarningsCalculator(base_earnings, asset_boosts)

    owned_assets = [
        DigitalAsset(1, AssetType.AVATAR, "rare", 0),
        DigitalAsset(3, AssetType.OTHER, "common", 0.2)
    ]

    earnings = calculator.calculate_earnings(owned_assets)
    print(f"Total earnings: {earnings}")

if __name__ == "__main__":
    main()
```
