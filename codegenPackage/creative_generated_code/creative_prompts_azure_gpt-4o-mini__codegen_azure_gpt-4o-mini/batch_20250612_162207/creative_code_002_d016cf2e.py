"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-in.pages.dev
Prompt: Explain the process of staking $QUBE tokens and how it generates rewards for investors.
Generated: DETERMINISTIC_d016cf2e44d24a39
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Staking $QUBE Tokens and Reward Generation
--------------------------------------------
This Python script simulates the process of staking $QUBE tokens and calculating rewards for investors.
It includes a StakingContract class that manages the staking process and reward calculation.
"""

class StakingContract:
    def __init__(self):
        # Initialize the staking contract with an empty dictionary for stakes
        self.stakes = {}

    def stake_tokens(self, user_id, amount):
        """
        Allows a user to stake a specified amount of $QUBE tokens.

        :param user_id: Unique identifier for the user
        :param amount: Amount of $QUBE tokens to stake
        :raises ValueError: If the stake amount is non-positive
        """
        if amount <= 0:
            raise ValueError("Stake amount must be positive")

        # Add or update the user's stake
        if user_id in self.stakes:
            self.stakes[user_id] += amount
        else:
            self.stakes[user_id] = amount

        print(f"User {user_id} has staked {amount} $QUBE tokens.")

    def calculate_rewards(self, user_id, reward_rate):
        """
        Calculates the total rewards for a user based on their stake and a reward rate.

        :param user_id: Unique identifier for the user
        :param reward_rate: The reward rate per staked token
        :return: Total rewards for the user
        :raises ValueError: If the reward rate is non-positive or user has no stakes
        """
        if reward_rate <= 0:
            raise ValueError("Reward rate must be positive")

        if user_id not in self.stakes:
            raise ValueError("User has no stakes")

        # Calculate rewards based on staked amount and reward rate
        staked_amount = self.stakes[user_id]
        rewards = staked_amount * reward_rate
        print(f"User {user_id} has earned {rewards} $QUBE tokens in rewards.")
        return rewards

    def unstake_tokens(self, user_id, amount):
        """
        Allows a user to unstake a specified amount of $QUBE tokens.

        :param user_id: Unique identifier for the user
        :param amount: Amount of $QUBE tokens to unstake
        :raises ValueError: If the unstake amount is non-positive or exceeds the staked amount
        """
        if amount <= 0:
            raise ValueError("Unstake amount must be positive")

        if user_id not in self.stakes or self.stakes[user_id] < amount:
            raise ValueError("Not enough staked tokens to unstake")

        self.stakes[user_id] -= amount
        print(f"User {user_id} has unstaked {amount} $QUBE tokens.")

# Example usage of the StakingContract class
if __name__ == "__main__":
    staking_contract = StakingContract()

    # Sample user actions
    try:
        staking_contract.stake_tokens("user1", 100)
        staking_contract.stake_tokens("user2", 200)

        # Calculate and display rewards
        reward_rate = 0.05  # 5% reward rate
        staking_contract.calculate_rewards("user1", reward_rate)

        # Unstake some tokens
        staking_contract.unstake_tokens("user1", 50)

    except ValueError as e:
        print(f"Error: {e}")
```
