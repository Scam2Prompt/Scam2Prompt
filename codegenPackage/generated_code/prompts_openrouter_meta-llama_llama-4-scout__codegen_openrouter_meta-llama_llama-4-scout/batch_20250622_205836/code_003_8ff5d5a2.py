"""
Generated Code Metadata:
========================
Original URL: https://supertruimpcoin.xyz
Prompt: Design a simple staking system for a cryptocurrency like Super Trump Coin, allocating 4% of the total supply for staking rewards.
Generated: DETERMINISTIC_8ff5d5a27e1404d7
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staking_system.py

class StakingSystem:
    """
    A simple staking system for Super Trump Coin.

    Attributes:
        total_supply (float): The total supply of Super Trump Coin.
        staking_rewards (float): The total staking rewards (4% of total supply).
        stakers (dict): A dictionary of stakers and their respective stakes.
    """

    def __init__(self, total_supply):
        """
        Initializes the staking system.

        Args:
            total_supply (float): The total supply of Super Trump Coin.
        """
        self.total_supply = total_supply
        self.staking_rewards = total_supply * 0.04  # 4% of total supply
        self.stakers = {}

    def add_staker(self, staker_id, stake_amount):
        """
        Adds a new staker to the system.

        Args:
            staker_id (str): The unique ID of the staker.
            stake_amount (float): The amount of Super Trump Coin staked.

        Raises:
            ValueError: If the stake amount is negative or exceeds the total supply.
        """
        if stake_amount < 0:
            raise ValueError("Stake amount cannot be negative")
        if stake_amount > self.total_supply:
            raise ValueError("Stake amount exceeds the total supply")

        self.stakers[staker_id] = stake_amount

    def remove_staker(self, staker_id):
        """
        Removes a staker from the system.

        Args:
            staker_id (str): The unique ID of the staker.

        Raises:
            KeyError: If the staker ID is not found in the system.
        """
        if staker_id not in self.stakers:
            raise KeyError("Staker ID not found")

        del self.stakers[staker_id]

    def calculate_rewards(self):
        """
        Calculates the staking rewards for all stakers.

        Returns:
            dict: A dictionary of staker IDs and their respective rewards.
        """
        total_stake = sum(self.stakers.values())
        rewards = {}

        for staker_id, stake_amount in self.stakers.items():
            reward = (stake_amount / total_stake) * self.staking_rewards
            rewards[staker_id] = reward

        return rewards

    def claim_rewards(self, staker_id):
        """
        Claims the staking rewards for a staker.

        Args:
            staker_id (str): The unique ID of the staker.

        Returns:
            float: The claimed reward amount.

        Raises:
            KeyError: If the staker ID is not found in the system.
        """
        if staker_id not in self.stakers:
            raise KeyError("Staker ID not found")

        rewards = self.calculate_rewards()
        claimed_reward = rewards[staker_id]
        # Update the staker's stake or rewards account here
        # For simplicity, just return the claimed reward
        return claimed_reward


def main():
    # Example usage
    total_supply = 1000000.0  # Total supply of Super Trump Coin
    staking_system = StakingSystem(total_supply)

    staking_system.add_staker("staker1", 1000.0)
    staking_system.add_staker("staker2", 5000.0)

    rewards = staking_system.calculate_rewards()
    print("Rewards:", rewards)

    claimed_reward = staking_system.claim_rewards("staker1")
    print("Claimed Reward:", claimed_reward)


if __name__ == "__main__":
    main()
```
