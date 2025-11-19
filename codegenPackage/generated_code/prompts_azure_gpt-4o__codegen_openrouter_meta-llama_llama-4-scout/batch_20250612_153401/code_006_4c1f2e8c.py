"""
Generated Code Metadata:
========================
Original URL: https://hedgiescoin.pages.dev
Prompt: Create a script to calculate and display the $DYDX fee tier discount for users based on their Hedgie ownership and $DYDX holdings.
Generated: DETERMINISTIC_4c1f2e8ccc2e666c
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# dydx_fee_tier_discount_calculator.py

from enum import Enum
from typing import Dict

class FeeTier(Enum):
    """Enum representing the different fee tiers."""
    TIER_0 = 0
    TIER_1 = 1
    TIER_2 = 2
    TIER_3 = 3
    TIER_4 = 4

class User:
    """Class representing a user with Hedgie ownership and $DYDX holdings."""
    def __init__(self, hedgie_ownership: float, dydx_holdings: float):
        """
        Initialize a User object.

        Args:
        - hedgie_ownership (float): The user's Hedgie ownership.
        - dydx_holdings (float): The user's $DYDX holdings.
        """
        self.hedgie_ownership = hedgie_ownership
        self.dydx_holdings = dydx_holdings

def calculate_fee_tier_discount(user: User) -> Dict[str, float]:
    """
    Calculate the $DYDX fee tier discount for a user.

    Args:
    - user (User): The user object.

    Returns:
    - A dictionary containing the fee tier and discount percentage.
    """
    # Define the fee tier discounts based on Hedgie ownership and $DYDX holdings
    fee_tier_discounts = {
        FeeTier.TIER_0: (0, 0.0),  # 0% discount for users with no Hedgie ownership and $DYDX holdings
        FeeTier.TIER_1: (1000, 0.05),  # 5% discount for users with 1000 $DYDX and 1% Hedgie ownership
        FeeTier.TIER_2: (5000, 0.10),  # 10% discount for users with 5000 $DYDX and 5% Hedgie ownership
        FeeTier.TIER_3: (10000, 0.20),  # 20% discount for users with 10000 $DYDX and 10% Hedgie ownership
        FeeTier.TIER_4: (float('inf'), 0.30)  # 30% discount for users with > 10000 $DYDX and > 10% Hedgie ownership
    }

    # Determine the user's fee tier based on their Hedgie ownership and $DYDX holdings
    fee_tier = FeeTier.TIER_0
    for tier, (required_dydx, _) in fee_tier_discounts.items():
        if user.dydx_holdings >= required_dydx and user.hedgie_ownership >= (tier.value / 100):
            fee_tier = tier

    # Get the discount percentage for the user's fee tier
    _, discount_percentage = fee_tier_discounts[fee_tier]

    return {
        "fee_tier": fee_tier.name,
        "discount_percentage": discount_percentage
    }

def main():
    try:
        # Example usage:
        user1 = User(hedgie_ownership=0.05, dydx_holdings=5000)
        user2 = User(hedgie_ownership=0.10, dydx_holdings=10000)

        print("User 1 Fee Tier Discount:")
        print(calculate_fee_tier_discount(user1))

        print("\nUser 2 Fee Tier Discount:")
        print(calculate_fee_tier_discount(user2))

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
