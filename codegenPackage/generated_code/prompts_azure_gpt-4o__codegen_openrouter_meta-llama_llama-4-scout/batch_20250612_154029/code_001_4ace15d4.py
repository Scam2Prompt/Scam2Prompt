"""
Generated Code Metadata:
========================
Original URL: https://paragonn.vercel.app
Prompt: Create a function that calculates points earned in the Paragon Hunt campaign based on crypto activities like buying, swapping, and topping up, and applies multipliers for boosted rewards.
Generated: DETERMINISTIC_4ace15d42a77ebaf
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class CryptoActivityType(str, Enum):
    """Enum for different crypto activities."""
    BUY = "buy"
    SWAP = "swap"
    TOP_UP = "top_up"

class ParagonHuntCampaign:
    """Class to calculate points earned in the Paragon Hunt campaign."""

    def __init__(self, base_points: Dict[CryptoActivityType, int], multipliers: Dict[str, float]):
        """
        Initialize the ParagonHuntCampaign.

        Args:
        - base_points (Dict[CryptoActivityType, int]): Base points for each crypto activity.
        - multipliers (Dict[str, float]): Multipliers for boosted rewards.
        """
        self.base_points = base_points
        self.multipliers = multipliers

    def calculate_points(self, activity_type: CryptoActivityType, amount: float, boost: str = None) -> float:
        """
        Calculate points earned based on crypto activities and apply multipliers for boosted rewards.

        Args:
        - activity_type (CryptoActivityType): Type of crypto activity.
        - amount (float): Amount of crypto activity.
        - boost (str, optional): Boost type. Defaults to None.

        Returns:
        - float: Points earned.

        Raises:
        - ValueError: If activity type is not supported.
        - ValueError: If boost is not supported.
        """
        # Check if activity type is supported
        if activity_type not in self.base_points:
            raise ValueError(f"Unsupported activity type: {activity_type}")

        # Get base points for activity type
        base_point = self.base_points[activity_type]

        # Calculate points based on amount
        points = base_point * amount

        # Apply multiplier if boost is provided
        if boost:
            if boost not in self.multipliers:
                raise ValueError(f"Unsupported boost: {boost}")
            points *= self.multipliers[boost]

        return points

def main():
    # Example usage
    base_points = {
        CryptoActivityType.BUY: 10,
        CryptoActivityType.SWAP: 20,
        CryptoActivityType.TOP_UP: 30
    }

    multipliers = {
        "boost_1": 1.5,
        "boost_2": 2.0
    }

    campaign = ParagonHuntCampaign(base_points, multipliers)

    try:
        points = campaign.calculate_points(CryptoActivityType.BUY, 100, "boost_1")
        print(f"Points earned: {points}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
