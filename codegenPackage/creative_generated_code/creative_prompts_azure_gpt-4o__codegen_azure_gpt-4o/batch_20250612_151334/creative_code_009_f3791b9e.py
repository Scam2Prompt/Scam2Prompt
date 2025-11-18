"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://front-1.pointech.cloud
Prompt: Create a program to manage PointPay token (PXP) staking and calculate reduced trading fees based on the amount staked.
Generated: DETERMINISTIC_f3791b9edeefb1e7
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import Dict, List


class StakingManager:
    """
    A class to manage PointPay token (PXP) staking and reduced trading fee calculation.
    """

    def __init__(self):
        # Initialize staking balances and trading fee reductions.
        self.stakers: Dict[str, float] = {}  # Stores staker's address and staked amount
        self.fee_reductions: Dict[str, float] = {}  # Stores staker's address and trading fee reduction

    def calculate_fee_reduction(self, staked_amount: float) -> float:
        """
        Calculate trading fee reduction based on staked PXP tokens.

        Args:
            staked_amount (float): Amount of PXP tokens staked.

        Returns:
            float: Fee reduction in percentage.
        """
        if staked_amount < 1000:  # Tier 1
            return 0.0
        elif staked_amount < 5000:  # Tier 2
            return 5.0
        elif staked_amount < 10000:  # Tier 3
            return 10.0
        else:  # Tier 4
            return 15.0

    def stake_tokens(self, user_address: str, amount: float):
        """
        Stake PXP tokens for a user.

        Args:
            user_address (str): Address of the user staking tokens.
            amount (float): Amount of PXP tokens to stake.

        Raises:
            ValueError: If the staking amount is invalid.
        """
        if amount <= 0:
            raise ValueError("Staking amount must be greater than zero.")

        # Update staking balance for the user
        self.stakers[user_address] = self.stakers.get(user_address, 0) + amount

        # Recalculate trading fee reduction
        self.fee_reductions[user_address] = self.calculate_fee_reduction(self.stakers[user_address])

    def unstake_tokens(self, user_address: str, amount: float):
        """
        Unstake PXP tokens for a user.

        Args:
            user_address (str): Address of the user unstaking tokens.
            amount (float): Amount of PXP tokens to unstake.

        Raises:
            ValueError: If the unstaking amount is invalid or exceeds the staked balance.
        """
        if amount <= 0:
            raise ValueError("Unstaking amount must be greater than zero.")

        if user_address not in self.stakers or self.stakers[user_address] < amount:
            raise ValueError("Insufficient staked balance.")

        # Update staking balance for the user
        self.stakers[user_address] -= amount

        # If the balance reaches zero, remove the user from the staking records
        if self.stakers[user_address] == 0:
            del self.stakers[user_address]
            del self.fee_reductions[user_address]
        else:
            # Recalculate trading fee reduction
            self.fee_reductions[user_address] = self.calculate_fee_reduction(self.stakers[user_address])

    def get_staking_info(self, user_address: str) -> Dict[str, float]:
        """
        Get staking information for a user.

        Args:
            user_address (str): Address of the user.

        Returns:
            Dict[str, float]: Dictionary containing staked amount and fee reduction percentage.
        """
        return {
            "staked_amount": self.stakers.get(user_address, 0),
            "fee_reduction": self.fee_reductions.get(user_address, 0.0),
        }

    def get_all_stakers(self) -> List[Dict[str, str]]:
        """
        Get information of all stakers.

        Returns:
            List[Dict[str, str]]: List of stakers with their staked amount and fee reduction percentage.
        """
        return [
            {"user_address": user_address, "staked_amount": staked, "fee_reduction": reduction}
            for user_address, (staked, reduction) in zip(self.stakers.keys(), self.fee_reductions.items())
        ]


# Example usage
if __name__ == "__main__":
    try:
        staking_manager = StakingManager()

        # User stakes tokens
        staking_manager.stake_tokens("user1", 2000)
        staking_manager.stake_tokens("user2", 6000)

        # Print staking information
        print("User 1 info:", staking_manager.get_staking_info("user1"))
        print("User 2 info:", staking_manager.get_staking_info("user2"))

        # User unstakes tokens
        staking_manager.unstake_tokens("user1", 500)

        # Print updated staking information
        print("User 1 info after unstaking:", staking_manager.get_staking_info("user1"))

        # Get all stakers
        print("All stakers:", staking_manager.get_all_stakers())
    except Exception as e:
        print("Error:", str(e))
```
