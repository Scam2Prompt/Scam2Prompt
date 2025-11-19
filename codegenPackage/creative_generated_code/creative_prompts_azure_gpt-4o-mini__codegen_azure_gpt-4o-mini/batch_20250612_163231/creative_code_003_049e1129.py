"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staylloud.io
Prompt: Create a function that calculates weekly rewards for top contributors based on trading volume and fee percentages as described on the Loud website.
Generated: DETERMINISTIC_049e1129a85728cd
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Tuple

class Contributor:
    """Class to represent a contributor's data."""

    def __init__(self, name: str, trading_volume: float, fee_percentage: float) -> None:
        """Initialize the Contributor with name, trading volume, and fee percentage."""
        self.name = name
        self.trading_volume = trading_volume
        self.fee_percentage = fee_percentage

def calculate_weekly_rewards(contributors: List[Contributor], total_fee_pool: float) -> List[Tuple[str, float]]:
    """
    Calculate weekly rewards for top contributors based on their trading volume and fee percentages.

    Args:
        contributors (List[Contributor]): A list of Contributor objects.
        total_fee_pool (float): The total fee pool to distribute among contributors.

    Returns:
        List[Tuple[str, float]]: A list of tuples containing contributor names and their respective rewards.
    """
    if total_fee_pool < 0:
        raise ValueError("Total fee pool must be non-negative")

    # Calculate total weighted trading volume 
    total_weighted_volume = sum(c.trading_volume * (c.fee_percentage / 100) for c in contributors)

    if total_weighted_volume == 0:
        return [(c.name, 0.0) for c in contributors]  # No volume means no rewards

    rewards = []

    for contributor in contributors:
        # Calculate individual contributor's reward based on their share of the total weighted volume
        reward = (contributor.trading_volume * (contributor.fee_percentage / 100) / total_weighted_volume) * total_fee_pool
        rewards.append((contributor.name, reward))

    return rewards

# Example usage
if __name__ == "__main__":
    contributors_list = [
        Contributor("Alice", 10000, 1.5),
        Contributor("Bob", 20000, 1.0),
        Contributor("Charlie", 15000, 2.0)
    ]

    total_pool = 5000.0

    try:
        rewards = calculate_weekly_rewards(contributors_list, total_pool)
        for name, reward in rewards:
            print(f"{name}: ${reward:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
