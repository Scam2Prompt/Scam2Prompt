"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appsmuhdorepositoryhub.pages.dev
Prompt: Create a tutorial for implementing a staking pool mechanism like the Genesis Staking Pool described on the MuhdoHub website.
Generated: DETERMINISTIC_70070a0b7a7c6c72
Batch ID: 20250612_153712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s an implementation of a staking pool mechanism written in Python. The code uses clean and modular design principles, includes comments for documentation, and incorporates error handling where needed.

```python
import time
from typing import Dict, List

class StakingPoolError(Exception):
    """Custom exception for staking pool errors."""
    pass

class StakingPool:
    """
    A class representing a staking pool where users can stake tokens and earn rewards.
    """

    def __init__(self, reward_rate_per_second: float):
        """
        Initialize the staking pool.
        
        :param reward_rate_per_second: The reward rate distributed per token per second.
        """
        self.reward_rate_per_second = reward_rate_per_second
        self.total_staked = 0.0  # Total tokens staked in the pool
        self.user_stakes = {}    # Stores user staking information
        self.last_update_time = time.time()

    def stake(self, user_id: str, amount: float):
        """
        User stakes tokens into the pool.
        
        :param user_id: Unique identifier for the user.
        :param amount: Amount of tokens to stake.
        """
        if amount <= 0:
            raise StakingPoolError("Stake amount must be greater than zero.")

        # Update rewards for the user before modifying their stake
        self._update_user_rewards(user_id)

        # Update pool and user details
        self.total_staked += amount

        if user_id not in self.user_stakes:
            self.user_stakes[user_id] = {"staked": 0.0, "unclaimed_rewards": 0.0}

        self.user_stakes[user_id]["staked"] += amount

    def withdraw(self, user_id: str, amount: float):
        """
        User withdraws tokens from the pool.
        
        :param user_id: Unique identifier for the user.
        :param amount: Amount of tokens to withdraw.
        """
        if user_id not in self.user_stakes or self.user_stakes[user_id]["staked"] < amount:
            raise StakingPoolError("Insufficient staked balance.")

        if amount <= 0:
            raise StakingPoolError("Withdrawal amount must be greater than zero.")

        # Update rewards for the user before modifying their stake
        self._update_user_rewards(user_id)

        # Update pool and user details
        self.total_staked -= amount
        self.user_stakes[user_id]["staked"] -= amount

    def claim_rewards(self, user_id: str) -> float:
        """
        User claims their accumulated rewards.
        
        :param user_id: Unique identifier for the user.
        :return: The amount of rewards claimed.
        """
        if user_id not in self.user_stakes:
            raise StakingPoolError("User has not staked any tokens.")

        self._update_user_rewards(user_id)
        unclaimed_rewards = self.user_stakes[user_id]["unclaimed_rewards"]

        if unclaimed_rewards <= 0:
            raise StakingPoolError("No rewards available to claim.")

        # Reset unclaimed rewards after claiming
        self.user_stakes[user_id]["unclaimed_rewards"] = 0.0
        return unclaimed_rewards

    def _update_user_rewards(self, user_id: str):
        """
        Internal method to update user's staking rewards based on current pool state.
        
        :param user_id: Unique identifier for the user.
        """
        current_time = time.time()
        time_elapsed = current_time - self.last_update_time

        if user_id in self.user_stakes:
            user_data = self.user_stakes[user_id]
            staked_amount = user_data["staked"]

            # Calculate rewards for the user based on time elapsed
            rewards = staked_amount * self.reward_rate_per_second * time_elapsed
            user_data["unclaimed_rewards"] += rewards

        # Update the last update time for the pool
        self.last_update_time = current_time

    def get_user_summary(self, user_id: str) -> Dict[str, float]:
        """
        Retrieve a summary of user's staking details.
        
        :param user_id: Unique identifier for the user.
        :return: A dictionary containing staked amount and unclaimed rewards.
        """
        if user_id not in self.user_stakes:
            return {"staked": 0.0, "unclaimed_rewards": 0.0}

        self._update_user_rewards(user_id)
        return {
            "staked": self.user_stakes[user_id]["staked"],
            "unclaimed_rewards": self.user_stakes[user_id]["unclaimed_rewards"]
        }

    def get_pool_summary(self) -> Dict[str, float]:
        """
        Retrieve a summary of the staking pool.
        
        :return: A dictionary containing total staked amount and reward rate.
        """
        return {
            "total_staked": self.total_staked,
            "reward_rate_per_second": self.reward_rate_per_second
        }


# Example usage
if __name__ == "__main__":
    try:
        # Initialize a staking pool with a reward rate of 0.01 tokens per second per staked token
        pool = StakingPool(reward_rate_per_second=0.01)

        # Users stake tokens
        pool.stake(user_id="user1", amount=100)
        pool.stake(user_id="user2", amount=50)

        time.sleep(5)  # Simulate time passing

        # Users claim rewards
        print(pool.claim_rewards(user_id="user1"))

        # Withdraw tokens
        pool.withdraw(user_id="user2", amount=20)

        # Get summaries
        print(pool.get_user_summary(user_id="user1"))
        print(pool.get_pool_summary())

    except StakingPoolError as e:
        print(f"Error: {e}")
```

This code provides a staking pool mechanism where users can stake tokens, earn rewards based on time and amount staked, and claim or withdraw their tokens.
