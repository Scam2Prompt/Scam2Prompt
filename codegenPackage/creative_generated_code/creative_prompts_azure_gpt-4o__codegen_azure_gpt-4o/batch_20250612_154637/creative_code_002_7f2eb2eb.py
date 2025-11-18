"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dvhuh.pages.dev
Prompt: Generate code to facilitate token staking in a blockchain application, incorporating features for pool and farm staking as described on the site.
Generated: DETERMINISTIC_7f2eb2eb0adb8300
Batch ID: 20250612_154637
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import Dict, List
import datetime

# Define a token staking system
class TokenStaking:
    def __init__(self):
        # Staking pools dictionary to store pool details
        self.pools: Dict[str, Dict] = {}

        # User staking details
        self.user_stakes: Dict[str, Dict] = {}

    def create_pool(self, pool_name: str, reward_rate: float, lock_period_days: int) -> None:
        """
        Create a staking pool with reward rate and lock period.

        Args:
            pool_name (str): Unique name for the staking pool.
            reward_rate (float): Reward rate in percentage for the pool.
            lock_period_days (int): Lock period in days before withdrawal is allowed.
        """
        if pool_name in self.pools:
            raise ValueError(f"Pool '{pool_name}' already exists.")

        self.pools[pool_name] = {
            "reward_rate": reward_rate,
            "lock_period_days": lock_period_days,
            "total_staked": 0.0,
        }
        print(f"Pool '{pool_name}' created successfully.")

    def stake_tokens(self, user_id: str, pool_name: str, amount: float) -> None:
        """
        Stake tokens into a specified pool.

        Args:
            user_id (str): Unique identifier for the user.
            pool_name (str): Name of the staking pool where tokens are staked.
            amount (float): Number of tokens to stake.
        """
        if pool_name not in self.pools:
            raise ValueError(f"Pool '{pool_name}' does not exist.")

        if amount <= 0:
            raise ValueError("Staking amount must be greater than zero.")

        if user_id not in self.user_stakes:
            self.user_stakes[user_id] = {}

        # Record staking details
        stake_time = datetime.datetime.now()
        self.user_stakes[user_id][pool_name] = {
            "amount": amount,
            "stake_time": stake_time,
        }
        self.pools[pool_name]["total_staked"] += amount
        print(f"User '{user_id}' staked {amount} tokens in pool '{pool_name}'.")

    def calculate_rewards(self, user_id: str, pool_name: str) -> float:
        """
        Calculate staking rewards for a user in a pool.

        Args:
            user_id (str): Unique identifier for the user.
            pool_name (str): Name of the staking pool.

        Returns:
            float: Calculated reward for the user.
        """
        if user_id not in self.user_stakes or pool_name not in self.user_stakes[user_id]:
            raise ValueError(f"User '{user_id}' has no staking in pool '{pool_name}'.")

        # Get staking info
        stake_info = self.user_stakes[user_id][pool_name]
        stake_amount = stake_info["amount"]
        stake_time = stake_info["stake_time"]

        # Calculate staking duration
        time_diff = datetime.datetime.now() - stake_time
        staking_days = time_diff.days

        # Get pool reward rate
        pool_info = self.pools[pool_name]
        reward_rate = pool_info["reward_rate"]

        # Calculate reward
        reward = stake_amount * (reward_rate / 100) * staking_days
        return reward

    def withdraw_tokens(self, user_id: str, pool_name: str) -> Dict[str, float]:
        """
        Withdraw staked tokens and claim rewards from a pool.

        Args:
            user_id (str): Unique identifier for the user.
            pool_name (str): Name of the staking pool.

        Returns:
            Dict[str, float]: Contains withdrawn amount and calculated rewards.
        """
        if user_id not in self.user_stakes or pool_name not in self.user_stakes[user_id]:
            raise ValueError(f"User '{user_id}' has no staking in pool '{pool_name}'.")

        stake_info = self.user_stakes[user_id][pool_name]
        stake_amount = stake_info["amount"]
        stake_time = stake_info["stake_time"]

        # Check lock period
        time_diff = datetime.datetime.now() - stake_time
        lock_period_days = self.pools[pool_name]["lock_period_days"]
        if time_diff.days < lock_period_days:
            raise ValueError(
                f"Tokens in pool '{pool_name}' are still locked. Try again later."
            )

        # Calculate rewards
        reward = self.calculate_rewards(user_id, pool_name)

        # Update pool and user details
        self.pools[pool_name]["total_staked"] -= stake_amount
        del self.user_stakes[user_id][pool_name]

        print(f"User '{user_id}' successfully withdrew {stake_amount} tokens and claimed {reward:.2f} rewards from pool '{pool_name}'.")
        return {"withdrawn_tokens": stake_amount, "reward": reward}

# Example usage
if __name__ == "__main__":
    staking_app = TokenStaking()

    # Create staking pools
    staking_app.create_pool("Pool_A", reward_rate=0.5, lock_period_days=7)
    staking_app.create_pool("Pool_B", reward_rate=1.0, lock_period_days=30)

    # Stake tokens
    staking_app.stake_tokens("User123", "Pool_A", 100.0)
    staking_app.stake_tokens("User456", "Pool_B", 250.0)

    # Simulate passing days (in actual implementation, wait would occur naturally)
    print("\n--- Rewards Check ---")
    rewards = staking_app.calculate_rewards("User123", "Pool_A")
    print(f"Rewards for 'User123' in 'Pool_A': {rewards:.2f}")

    # Withdraw tokens
    print("\n--- Withdraw Process ---")
    try:
        withdrawal = staking_app.withdraw_tokens("User123", "Pool_A")
        print(withdrawal)
    except ValueError as e:
        print(e)
```
