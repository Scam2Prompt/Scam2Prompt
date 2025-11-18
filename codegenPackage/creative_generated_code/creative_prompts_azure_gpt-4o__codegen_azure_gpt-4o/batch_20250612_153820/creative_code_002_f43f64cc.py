"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://good-games-guild.gitbook.io
Prompt: Generate code for a tier-based staking system for ArbiPad, incorporating the tier system details and user protection policy from the Good Games Guild documentation.
Generated: DETERMINISTIC_f43f64cc6a20018e
Batch ID: 20250612_153820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Dict, Optional


class StakingSystem:
    """
    A tier-based staking system for ArbiPad.
    Users are assigned tiers based on their staking amounts.
    Follows the tier system details and user protection policy from the Good Games Guild documentation.
    """

    def __init__(self):
        """
        Initialize the staking system with default tier thresholds and user data storage.
        """
        # Tier thresholds in terms of staking amount (in tokens)
        self.tier_thresholds = {
            "Bronze": 1000,  # Minimum tokens for Bronze tier
            "Silver": 5000,  # Minimum tokens for Silver tier
            "Gold": 10000,   # Minimum tokens for Gold tier
            "Platinum": 20000  # Minimum tokens for Platinum tier
        }
        # Dictionary to store user staking details
        self.users: Dict[str, Dict[str, Optional[int]]] = {}

    def stake_tokens(self, user_id: str, amount: int) -> str:
        """
        Allow a user to stake tokens and assign them to a tier.

        :param user_id: The unique identifier for the user.
        :param amount: The number of tokens the user wants to stake.
        :return: Confirmation message about staking and assigned tier.
        """
        if amount <= 0:
            return "Error: Staking amount must be greater than zero."

        # Update user's staking amount and calculate their tier
        self.users[user_id] = {"staked_amount": amount, "tier": self._calculate_tier(amount)}
        return f"User {user_id} has staked {amount} tokens and is assigned to the {self.users[user_id]['tier']} tier."

    def _calculate_tier(self, amount: int) -> str:
        """
        Determine the user's tier based on their staking amount.

        :param amount: The number of tokens the user has staked.
        :return: The corresponding tier name.
        """
        if amount >= self.tier_thresholds["Platinum"]:
            return "Platinum"
        elif amount >= self.tier_thresholds["Gold"]:
            return "Gold"
        elif amount >= self.tier_thresholds["Silver"]:
            return "Silver"
        elif amount >= self.tier_thresholds["Bronze"]:
            return "Bronze"
        else:
            return "No Tier"

    def unstake_tokens(self, user_id: str) -> str:
        """
        Allow a user to unstake their tokens and remove them from a tier.

        :param user_id: The unique identifier for the user.
        :return: Confirmation message regarding unstaking.
        """
        if user_id not in self.users:
            return "Error: User not found or no tokens staked."

        # Remove the user's staking data
        unstaked_amount = self.users[user_id]["staked_amount"]
        self.users.pop(user_id)
        return f"User {user_id} has unstaked {unstaked_amount} tokens and is no longer assigned to any tier."

    def get_user_tier(self, user_id: str) -> str:
        """
        Retrieve the tier of a specific user.

        :param user_id: The unique identifier for the user.
        :return: The user's tier or an error message if the user is not found.
        """
        if user_id not in self.users:
            return "Error: User not found or no tokens staked."

        return f"User {user_id} is in the {self.users[user_id]['tier']} tier."

    def get_tier_thresholds(self) -> Dict[str, int]:
        """
        Retrieve the tier thresholds for staking amounts.

        :return: Dictionary containing tier thresholds.
        """
        return self.tier_thresholds


if __name__ == "__main__":
    # Example usage of the staking system
    staking_system = StakingSystem()

    print(staking_system.stake_tokens("user123", 7000))  # User stakes tokens
    print(staking_system.get_user_tier("user123"))  # Retrieve user's tier
    print(staking_system.unstake_tokens("user123"))  # User unstakes tokens
    print(staking_system.get_user_tier("user123"))  # Attempt to retrieve tier after unstaking
```
