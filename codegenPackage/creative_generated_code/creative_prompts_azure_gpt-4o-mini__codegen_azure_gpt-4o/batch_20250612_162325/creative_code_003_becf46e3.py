"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fdsgertyg4e4ty.pages.dev
Prompt: Generate a function to calculate the total value staked and the corresponding APR in the Renzo ecosystem.
Generated: DETERMINISTIC_becf46e3d84954ca
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List, Tuple


class StakeRecord:
    """
    A class to represent a stake record in the Renzo ecosystem.

    Attributes:
        amount (float): The amount staked.
        apr (float): The annual percentage rate (APR) for the stake.
    """
    def __init__(self, amount: float, apr: float):
        if amount < 0 or apr < 0:
            raise ValueError("Amount and APR must be non-negative values.")
        self.amount = amount
        self.apr = apr


def calculate_total_value_and_apr(stakes: List[StakeRecord]) -> Tuple[float, float]:
    """
    Calculates the total value staked and the weighted average APR in the Renzo ecosystem.

    Args:
        stakes (List[StakeRecord]): A list of StakeRecord objects representing stakes in the ecosystem.

    Returns:
        Tuple[float, float]: A tuple containing:
            - total_staked (float): The total value staked.
            - weighted_apr (float): The weighted average APR.
    """
    # Validate input
    if not all(isinstance(stake, StakeRecord) for stake in stakes):
        raise TypeError("All items in the stakes list must be instances of StakeRecord.")

    # Initialize variables
    total_staked = 0.0
    weighted_apr_sum = 0.0

    # Calculate total staked and weighted APR sum
    for stake in stakes:
        total_staked += stake.amount
        weighted_apr_sum += stake.amount * stake.apr

    # Calculate weighted APR, handle divide-by-zero if total_staked is zero
    weighted_apr = weighted_apr_sum / total_staked if total_staked > 0 else 0.0

    return total_staked, weighted_apr


# Example usage
if __name__ == "__main__":
    try:
        # Sample stakes
        stakes = [
            StakeRecord(amount=1000, apr=0.05),
            StakeRecord(amount=2000, apr=0.04),
            StakeRecord(amount=1500, apr=0.06)
        ]

        # Calculate and print results
        total_staked, weighted_apr = calculate_total_value_and_apr(stakes)
        print(f"Total Value Staked: {total_staked}")
        print(f"Weighted Average APR: {weighted_apr:.2%}")
    except Exception as e:
        print(f"Error: {e}")
```
