"""
Generated Code Metadata:
========================
Original URL: https://bafybeidrtekz63j5fj7fsvnv5iu3jpcsbfwjdfvsaaml43ksqrp5impzy4.ipfs.dweb.link
Prompt: Describe the staking process for PARAM points and how it integrates with the Param Network's tokenomics.
Generated: DETERMINISTIC_38552dbfe05985b0
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
PARAM Staking Process and Integration with Param Network Tokenomics

This module simulates the staking process for PARAM points within the Param Network.
It includes classes and methods to handle staking, rewards calculation, and error handling.
"""

class ParamNetwork:
    def __init__(self):
        self.total_staked = 0.0
        self.stakers = {}

    def stake(self, user_id, amount):
        """
        Allows a user to stake a specified amount of PARAM points.

        :param user_id: Unique identifier for the user
        :param amount: Amount of PARAM points to stake
        :raises ValueError: If the amount is non-positive
        """
        if amount <= 0:
            raise ValueError("Staking amount must be greater than zero.")
        
        if user_id not in self.stakers:
            self.stakers[user_id] = 0.0
        
        self.stakers[user_id] += amount
        self.total_staked += amount
        print(f"User {user_id} staked {amount} PARAM points. Total staked: {self.total_staked}")

    def unstake(self, user_id, amount):
        """
        Allows a user to unstake a specified amount of PARAM points.

        :param user_id: Unique identifier for the user
        :param amount: Amount of PARAM points to unstake
        :raises ValueError: If the amount is non-positive or exceeds staked amount
        """
        if amount <= 0:
            raise ValueError("Unstaking amount must be greater than zero.")
        
        if user_id not in self.stakers or self.stakers[user_id] < amount:
            raise ValueError("Insufficient staked amount to unstake.")
        
        self.stakers[user_id] -= amount
        self.total_staked -= amount
        print(f"User {user_id} unstaked {amount} PARAM points. Total staked: {self.total_staked}")

    def calculate_rewards(self, user_id, reward_rate):
        """
        Calculates the rewards for a user based on their staked amount and a reward rate.

        :param user_id: Unique identifier for the user
        :param reward_rate: The rate at which rewards are calculated (e.g., per 1000 PARAM points)
        :return: Calculated rewards for the user
        :raises ValueError: If the user has no staked amount
        """
        if user_id not in self.stakers or self.stakers[user_id] <= 0:
            raise ValueError("User has no staked amount to calculate rewards.")
        
        staked_amount = self.stakers[user_id]
        rewards = (staked_amount / 1000) * reward_rate
        print(f"User {user_id} has earned {rewards} in rewards.")
        return rewards

# Example usage
if __name__ == "__main__":
    try:
        param_network = ParamNetwork()
        param_network.stake("user1", 500)
        param_network.stake("user2", 1000)
        rewards_user1 = param_network.calculate_rewards("user1", 10)
        param_network.unstake("user1", 200)
        rewards_user1_after_unstake = param_network.calculate_rewards("user1", 10)
    except ValueError as e:
        print(f"Error: {e}")
```
