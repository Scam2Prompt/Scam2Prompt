"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-xai-games.pages.dev
Prompt: Write a script that calculates the reward multiplier for different staking tiers in the Xai staking system.
Generated: DETERMINISTIC_59e0a235d0beb546
Batch ID: 20250612_140300
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingTier:
    """
    Class to represent a staking tier and calculate the reward multiplier based on the tier.
    """

    def __init__(self, tier_name: str, min_stake: float, max_stake: float, multiplier: float):
        """
        Initializes a StakingTier instance.

        :param tier_name: The name of the staking tier.
        :param min_stake: Minimum staked amount for this tier.
        :param max_stake: Maximum staked amount for this tier.
        :param multiplier: Reward multiplier for this tier.
        """
        self.tier_name = tier_name
        self.min_stake = min_stake
        self.max_stake = max_stake
        self.multiplier = multiplier

    def is_within_tier(self, stake_amount: float) -> bool:
        """
        Checks if a given stake amount falls within the tier's limits.

        :param stake_amount: The amount being staked.
        :return: True if within tier limits, False otherwise.
        """
        return self.min_stake <= stake_amount <= self.max_stake


class StakingSystem:
    """
    Class to manage the staking tiers and calculate the reward multipliers.
    """

    def __init__(self):
        """
        Initializes a StakingSystem with predefined tiers.
        """
        self.tiers = [
            StakingTier("Bronze", 0, 1000, 1.0),
            StakingTier("Silver", 1001, 5000, 1.5),
            StakingTier("Gold", 5001, 20000, 2.0),
            StakingTier("Platinum", 20001, float('inf'), 3.0)
        ]

    def get_reward_multiplier(self, stake_amount: float) -> float:
        """
        Retrieves the reward multiplier for a given stake amount.

        :param stake_amount: The amount being staked.
        :return: The reward multiplier corresponding to the stake amount.
        :raises ValueError: If stake amount is negative.
        """
        if stake_amount < 0:
            raise ValueError("Stake amount cannot be negative.")

        for tier in self.tiers:
            if tier.is_within_tier(stake_amount):
                return tier.multiplier
        
        # If stake does not fall into any defined tier
        raise ValueError("Stake amount does not fall into any defined staking tier.")


if __name__ == "__main__":
    staking_system = StakingSystem()

    try:
        stake = float(input("Enter the stake amount: "))
        multiplier = staking_system.get_reward_multiplier(stake)
        print(f"The reward multiplier for a stake of {stake} is: {multiplier}")
    except ValueError as e:
        print(f"Error: {e}")
```
