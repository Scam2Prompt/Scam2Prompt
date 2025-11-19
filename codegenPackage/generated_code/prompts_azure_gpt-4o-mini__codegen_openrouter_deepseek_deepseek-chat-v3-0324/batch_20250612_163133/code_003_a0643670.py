"""
Generated Code Metadata:
========================
Original URL: https://claimhyperlane.foundation
Prompt: Generate code to calculate the boosted HYPER allocation based on user activities like NFT holdings and liquidity provision.
Generated: DETERMINISTIC_a06436706bc5f3e9
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hyper_allocation_calculator.py
"""
This module calculates the boosted HYPER allocation for users based on their activities,
including NFT holdings and liquidity provision.
"""

from typing import Dict, List, Tuple
from dataclasses import dataclass


@dataclass
class UserActivity:
    """Stores user activity data for HYPER allocation calculation."""
    nft_holdings: int  # Number of NFTs held by the user
    liquidity_provided: float  # Amount of liquidity provided in USD
    staked_tokens: float  # Amount of staked tokens in USD


class HyperAllocationCalculator:
    """Calculates boosted HYPER allocation based on user activities."""

    # Weightings for different activities in the allocation calculation
    NFT_WEIGHT = 0.3
    LIQUIDITY_WEIGHT = 0.5
    STAKE_WEIGHT = 0.2

    # Multipliers for different tiers of activity
    NFT_MULTIPLIER = {
        1: 1.0,
        3: 1.2,
        5: 1.5,
        10: 2.0
    }

    LIQUIDITY_MULTIPLIER = {
        1000: 1.0,
        5000: 1.3,
        10000: 1.7,
        50000: 2.0
    }

    STAKE_MULTIPLIER = {
        500: 1.0,
        2000: 1.2,
        5000: 1.5,
        10000: 2.0
    }

    def __init__(self):
        """Initialize the calculator with default parameters."""
        pass

    @staticmethod
    def _get_multiplier(value: float, multiplier_table: Dict[int, float]) -> float:
        """Get the appropriate multiplier based on the value and multiplier table.
        
        Args:
            value: The value to check against multiplier thresholds.
            multiplier_table: Dictionary mapping thresholds to multipliers.
            
        Returns:
            The highest applicable multiplier for the given value.
        """
        applicable_multipliers = [
            multiplier for threshold, multiplier in multiplier_table.items() 
            if value >= threshold
        ]
        return max(applicable_multipliers) if applicable_multipliers else 1.0

    def calculate_base_allocation(self, user: UserActivity) -> float:
        """Calculate the base allocation without boost.
        
        Args:
            user: UserActivity object containing user's data.
            
        Returns:
            Base allocation score.
        """
        return (
            (user.nft_holdings * self.NFT_WEIGHT) +
            (user.liquidity_provided * self.LIQUIDITY_WEIGHT) +
            (user.staked_tokens * self.STAKE_WEIGHT)
        )

    def calculate_boosted_allocation(self, user: UserActivity) -> float:
        """Calculate the boosted HYPER allocation.
        
        Args:
            user: UserActivity object containing user's data.
            
        Returns:
            Boosted allocation score.
            
        Raises:
            ValueError: If any of the activity values are negative.
        """
        if any([
            user.nft_holdings < 0,
            user.liquidity_provided < 0,
            user.staked_tokens < 0
        ]):
            raise ValueError("Activity values cannot be negative.")

        nft_multiplier = self._get_multiplier(user.nft_holdings, self.NFT_MULTIPLIER)
        liquidity_multiplier = self._get_multiplier(
            user.liquidity_provided, self.LIQUIDITY_MULTIPLIER
        )
        stake_multiplier = self._get_multiplier(user.staked_tokens, self.STAKE_MULTIPLIER)

        boosted_score = (
            (user.nft_holdings * self.NFT_WEIGHT * nft_multiplier) +
            (user.liquidity_provided * self.LIQUIDITY_WEIGHT * liquidity_multiplier) +
            (user.staked_tokens * self.STAKE_WEIGHT * stake_multiplier)
        )

        return boosted_score


# Example usage
if __name__ == "__main__":
    try:
        calculator = HyperAllocationCalculator()
        
        # Example user data
        user_data = UserActivity(
            nft_holdings=4,
            liquidity_provided=7500,
            staked_tokens=3000
        )
        
        base_allocation = calculator.calculate_base_allocation(user_data)
        boosted_allocation = calculator.calculate_boosted_allocation(user_data)
        
        print(f"Base Allocation: {base_allocation:.2f}")
        print(f"Boosted Allocation: {boosted_allocation:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
