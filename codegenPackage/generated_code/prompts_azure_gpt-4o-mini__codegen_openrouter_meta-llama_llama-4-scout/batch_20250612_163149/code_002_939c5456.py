"""
Generated Code Metadata:
========================
Original URL: https://wynn-seven.vercel.app
Prompt: Generate a function that calculates potential earnings based on user engagement and multipliers for a rewards program similar to $WYNN Hunt.
Generated: DETERMINISTIC_939c5456d4c25e7c
Batch ID: 20250612_163149
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

class EngagementType(str, Enum):
    """Enum for different types of user engagement."""
    LOGIN = "login"
    REFERRAL = "referral"
    PURCHASE = "purchase"

class RewardsProgram:
    """Class representing a rewards program with engagement multipliers."""

    def __init__(self, multipliers: Dict[EngagementType, float], base_earnings: float):
        """
        Initialize the rewards program.

        Args:
        - multipliers (Dict[EngagementType, float]): A dictionary of engagement types and their corresponding multipliers.
        - base_earnings (float): The base earnings for a single engagement unit.
        """
        self.multipliers = multipliers
        self.base_earnings = base_earnings

    def calculate_earnings(self, engagement: Dict[EngagementType, int]) -> float:
        """
        Calculate potential earnings based on user engagement and multipliers.

        Args:
        - engagement (Dict[EngagementType, int]): A dictionary of engagement types and their frequencies.

        Returns:
        - float: The total potential earnings.

        Raises:
        - ValueError: If engagement type is not found in multipliers.
        """
        total_earnings = 0.0
        for engagement_type, frequency in engagement.items():
            if engagement_type not in self.multipliers:
                raise ValueError(f"Engagement type '{engagement_type}' not found in multipliers.")
            multiplier = self.multipliers[engagement_type]
            earnings = self.base_earnings * frequency * multiplier
            total_earnings += earnings
        return total_earnings


def main():
    # Example usage:
    multipliers = {
        EngagementType.LOGIN: 0.1,
        EngagementType.REFERRAL: 5.0,
        EngagementType.PURCHASE: 0.05
    }
    base_earnings = 10.0

    rewards_program = RewardsProgram(multipliers, base_earnings)

    user_engagement = {
        EngagementType.LOGIN: 10,
        EngagementType.REFERRAL: 2,
        EngagementType.PURCHASE: 5
    }

    try:
        earnings = rewards_program.calculate_earnings(user_engagement)
        print(f"Total potential earnings: ${earnings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
