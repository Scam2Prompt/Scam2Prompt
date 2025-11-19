"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sonicslabs.pages.dev
Prompt: Describe the process of staking S tokens on Sonic and how it contributes to network security and rewards.
Generated: DETERMINISTIC_6a337a7f3dfc7831
Batch ID: 20250612_155723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script simulates the process of staking S tokens on the Sonic network. 
The staking process contributes to the network's security and rewards users for their participation.
"""

class SonicNetwork:
    def __init__(self):
        self.total_staked = 0
        self.stakers = {}

    def stake_tokens(self, user_id, amount):
        """
        Stake a given amount of S tokens for a user.

        Parameters:
        user_id (str): The unique identifier for the user.
        amount (float): The amount of S tokens to stake.

        Raises:
        ValueError: If the stake amount is not positive.
        """

        if amount <= 0:
            raise ValueError("Stake amount must be positive.")

        # Update total staked amount
        self.total_staked += amount
        
        # Update user's staked amount
        if user_id in self.stakers:
            self.stakers[user_id] += amount
        else:
            self.stakers[user_id] = amount

        print(f"User {user_id} staked {amount} S tokens.")
        print(f"Total staked in the network: {self.total_staked} S tokens.")

    def calculate_rewards(self, user_id):
        """
        Calculate rewards for a user based on their staked amount.

        Parameters:
        user_id (str): The unique identifier for the user.

        Returns:
        float: The calculated rewards for the user.
        """

        # Define a simple reward rate for demonstration
        reward_rate = 0.05  # 5% rewards for the staked amount
        staked_amount = self.stakers.get(user_id, 0)

        rewards = staked_amount * reward_rate
        print(f"User {user_id} has earned {rewards} S tokens in rewards.")
        return rewards

    def unstake_tokens(self, user_id, amount):
        """
        Unstake a given amount of S tokens for a user.

        Parameters:
        user_id (str): The unique identifier for the user.
        amount (float): The amount of S tokens to unstake.

        Raises:
        ValueError: If the unstake amount is not positive or exceeds the staked amount.
        """

        if amount <= 0:
            raise ValueError("Unstake amount must be positive.")

        if user_id not in self.stakers or self.stakers[user_id] < amount:
            raise ValueError("Insufficient staked amount to unstake.")

        # Update total staked amount
        self.total_staked -= amount

        # Update user's staked amount
        self.stakers[user_id] -= amount

        print(f"User {user_id} unstaked {amount} S tokens.")
        print(f"Total staked in the network: {self.total_staked} S tokens.")

# Example usage
if __name__ == "__main__":
    sonic = SonicNetwork()

    try:
        sonic.stake_tokens("user123", 100)
        sonic.calculate_rewards("user123")
        sonic.unstake_tokens("user123", 50)
        sonic.calculate_rewards("user123")
    except ValueError as e:
        print(f"Error: {e}")
```
