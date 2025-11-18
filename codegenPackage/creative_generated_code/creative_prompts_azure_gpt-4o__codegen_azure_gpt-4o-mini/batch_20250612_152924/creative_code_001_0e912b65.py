"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20en.pages.dev
Prompt: Generate code to calculate staking rewards for DOGE20 tokens based on the percentage of the staking pool held by a user.
Generated: DETERMINISTIC_0e912b652568259a
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingPool:
    """
    A class to represent a staking pool for DOGE20 tokens.
    """

    def __init__(self):
        """Initialize the staking pool with total and user stakes."""
        self.total_staked = 0.0  # Total amount staked in the pool
        self.user_stakes = {}     # Dictionary to hold user stakes

    def stake(self, user: str, amount: float):
        """
        Allows a user to stake a given amount of DOGE20 tokens.

        Args:
            user (str): The user's identifier.
            amount (float): The amount of DOGE20 tokens to stake.

        Raises:
            ValueError: If the stake amount is non-positive.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be positive.")

        self.total_staked += amount
        if user in self.user_stakes:
            self.user_stakes[user] += amount
        else:
            self.user_stakes[user] = amount

    def unstake(self, user: str, amount: float):
        """
        Allows a user to unstake a given amount of DOGE20 tokens.

        Args:
            user (str): The user's identifier.
            amount (float): The amount of DOGE20 tokens to unstake.

        Raises:
            ValueError: If the unstake amount is non-positive or exceeds user's stake.
        """
        if amount <= 0:
            raise ValueError("Unstake amount must be positive.")

        if user not in self.user_stakes or self.user_stakes[user] < amount:
            raise ValueError("Insufficient stake to unstake.")

        self.total_staked -= amount
        self.user_stakes[user] -= amount

    def calculate_rewards(self, user: str, reward_pool: float) -> float:
        """
        Calculate staking rewards for a user based on the percentage of the staking pool they hold.

        Args:
            user (str): The user's identifier.
            reward_pool (float): The total rewards available for distribution.

        Returns:
            float: The calculated rewards for the user.

        Raises:
            ValueError: If the user has no stakes or reward pool is non-positive.
        """
        if user not in self.user_stakes or self.user_stakes[user] == 0:
            raise ValueError("User has no stakes in the pool.")

        if reward_pool <= 0:
            raise ValueError("Reward pool must be positive.")

        # Calculate user's share of the staking pool
        user_share = self.user_stakes[user] / self.total_staked
        # Calculate rewards for the user
        user_rewards = user_share * reward_pool
        return user_rewards


# Example usage:
if __name__ == "__main__":
    staking_pool = StakingPool()
    
    # Staking tokens
    staking_pool.stake("user1", 100)
    staking_pool.stake("user2", 200)

    # Calculate rewards based on a reward pool
    try:
        rewards = staking_pool.calculate_rewards("user1", 50)
        print(f"User1 rewards: {rewards}")
    except ValueError as e:
        print(f"Error calculating rewards: {e}")

    # Unstaking tokens
    try:
        staking_pool.unstake("user1", 50)
    except ValueError as e:
        print(f"Error unstaking: {e}")
```
