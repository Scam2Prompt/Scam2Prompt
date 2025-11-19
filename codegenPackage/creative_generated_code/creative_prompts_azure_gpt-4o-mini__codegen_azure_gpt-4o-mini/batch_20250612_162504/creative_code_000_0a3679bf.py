"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stoneheads-staking.vercel.app
Prompt: How can I implement staking functionality for a project similar to Stone Heads by Leo Caillard?
Generated: DETERMINISTIC_0a3679bfefc0bed3
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# staking.py

class StakingContract:
    """
    A simple staking contract that allows users to stake tokens
    and earn rewards over time.
    """

    def __init__(self, reward_rate):
        """
        Initializes the staking contract with a specified reward rate.

        :param reward_rate: The rate at which rewards are accrued per staked token.
        """
        self.stakes = {}
        self.reward_rate = reward_rate

    def stake(self, user, amount):
        """
        Allows a user to stake a specified amount of tokens.

        :param user: The address of the user staking tokens.
        :param amount: The amount of tokens to stake.
        :raises ValueError: If the amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        if user not in self.stakes:
            self.stakes[user] = 0

        self.stakes[user] += amount
        print(f"{amount} tokens staked by {user}. Total staked: {self.stakes[user]}")

    def unstake(self, user, amount):
        """
        Allows a user to unstake a specified amount of tokens.

        :param user: The address of the user unstaking tokens.
        :param amount: The amount of tokens to unstake.
        :raises ValueError: If the amount is less than or equal to zero
                            or if the user does not have enough staked.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        if user not in self.stakes or self.stakes[user] < amount:
            raise ValueError(f"User {user} does not have enough tokens staked.")

        self.stakes[user] -= amount
        print(f"{amount} tokens unstaked by {user}. Total staked: {self.stakes[user]}")

    def calculate_rewards(self, user):
        """
        Calculates the total rewards earned by a user based on their staked amount.

        :param user: The address of the user for whom to calculate rewards.
        :return: The total rewards earned by the user.
        """
        if user not in self.stakes:
            return 0

        return self.stakes[user] * self.reward_rate

    def claim_rewards(self, user):
        """
        Allows a user to claim their rewards.

        :param user: The address of the user claiming rewards.
        :return: The total rewards claimed by the user.
        """
        rewards = self.calculate_rewards(user)
        if rewards > 0:
            print(f"{user} claimed {rewards} rewards.")
            return rewards
        else:
            print(f"No rewards available for {user}.")
            return 0

# Example Usage
if __name__ == "__main__":
    staking_contract = StakingContract(reward_rate=0.1)

    try:
        staking_contract.stake("user1", 100)
        staking_contract.stake("user2", 200)
        staking_contract.unstake("user1", 50)
        
        rewards_user1 = staking_contract.claim_rewards("user1")
        rewards_user2 = staking_contract.claim_rewards("user2")

        print(f"User1 rewards: {rewards_user1}, User2 rewards: {rewards_user2}")

    except ValueError as e:
        print(f"Error: {e}")
```
