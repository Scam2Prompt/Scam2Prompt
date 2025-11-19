"""
Generated Code Metadata:
========================
Original URL: https://scotty-ai.pages.dev
Prompt: Create a function that tracks the total staked amount and calculates the user's claimable rewards in the Scotty AI staking system.
Generated: DETERMINISTIC_f1d617bbe4bd1273
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ScottyAIStakingSystem:
    """
    A class representing the Scotty AI staking system.

    Attributes:
    ----------
    total_staked_amount : float
        The total amount staked by all users.
    reward_rate : float
        The rate at which rewards are calculated.
    user_stakes : dict
        A dictionary mapping user IDs to their staked amounts.

    Methods:
    -------
    stake(user_id, amount)
        Increases the total staked amount and the user's staked amount.
    unstake(user_id, amount)
        Decreases the total staked amount and the user's staked amount.
    calculate_rewards(user_id)
        Calculates the user's claimable rewards based on their staked amount and the reward rate.
    """

    def __init__(self, reward_rate):
        """
        Initializes the Scotty AI staking system.

        Args:
        ----
        reward_rate : float
            The rate at which rewards are calculated.
        """
        self.total_staked_amount = 0.0
        self.reward_rate = reward_rate
        self.user_stakes = {}

    def stake(self, user_id, amount):
        """
        Increases the total staked amount and the user's staked amount.

        Args:
        ----
        user_id : str
            The ID of the user staking.
        amount : float
            The amount being staked.

        Raises:
        ------
        ValueError
            If the staking amount is negative.
        """
        if amount < 0:
            raise ValueError("Staking amount cannot be negative")

        self.total_staked_amount += amount
        if user_id in self.user_stakes:
            self.user_stakes[user_id] += amount
        else:
            self.user_stakes[user_id] = amount

    def unstake(self, user_id, amount):
        """
        Decreases the total staked amount and the user's staked amount.

        Args:
        ----
        user_id : str
            The ID of the user unstaking.
        amount : float
            The amount being unstaked.

        Raises:
        ------
        ValueError
            If the unstaking amount is negative or exceeds the user's staked amount.
        """
        if amount < 0:
            raise ValueError("Unstaking amount cannot be negative")
        if user_id not in self.user_stakes or self.user_stakes[user_id] < amount:
            raise ValueError("Insufficient staked amount")

        self.total_staked_amount -= amount
        self.user_stakes[user_id] -= amount

    def calculate_rewards(self, user_id):
        """
        Calculates the user's claimable rewards based on their staked amount and the reward rate.

        Args:
        ----
        user_id : str
            The ID of the user.

        Returns:
        -------
        float
            The user's claimable rewards.

        Raises:
        ------
        ValueError
            If the user has not staked any amount.
        """
        if user_id not in self.user_stakes:
            raise ValueError("User has not staked any amount")

        user_staked_amount = self.user_stakes[user_id]
        rewards = user_staked_amount * self.reward_rate
        return rewards


def main():
    # Example usage:
    staking_system = ScottyAIStakingSystem(reward_rate=0.1)

    try:
        staking_system.stake("user1", 100.0)
        staking_system.stake("user2", 200.0)

        print("User 1 rewards:", staking_system.calculate_rewards("user1"))
        print("User 2 rewards:", staking_system.calculate_rewards("user2"))

        staking_system.unstake("user1", 50.0)
        print("User 1 rewards after unstaking:", staking_system.calculate_rewards("user1"))

    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
```
