"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daos-world-wl.pages.dev
Prompt: Explain how to design a farm-style rewards system for DAOs, similar to the "Farms 🧑‍🌾" feature on daos.world.
Generated: DETERMINISTIC_2b9b0ae5fb99e54c
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from datetime import datetime, timedelta


class FarmRewardSystem:
    """
    A class to implement a farm-style rewards system for Decentralized Autonomous Organizations (DAOs).
    """

    def __init__(self):
        """
        Initialize the reward system.
        """
        self.users = {}  # Stores user data
        self.pools = {}  # Stores staking pools

    def create_pool(self, pool_id, reward_rate, lock_duration):
        """
        Create a new staking pool.
        :param pool_id: str - Unique identifier for the staking pool
        :param reward_rate: float - Reward rate (tokens per second)
        :param lock_duration: int - Lock duration in seconds
        """
        if pool_id in self.pools:
            raise ValueError("Pool ID already exists.")

        self.pools[pool_id] = {
            "reward_rate": reward_rate,
            "lock_duration": lock_duration,
            "stakers": {}
        }

    def stake_tokens(self, user_id, pool_id, amount):
        """
        Stake tokens in a pool.
        :param user_id: str - Unique identifier for the user
        :param pool_id: str - Pool identifier
        :param amount: float - Amount of tokens to stake
        """
        if pool_id not in self.pools:
            raise ValueError("Pool does not exist.")
        if amount <= 0:
            raise ValueError("Stake amount must be positive.")

        pool = self.pools[pool_id]

        if user_id not in pool["stakers"]:
            pool["stakers"][user_id] = {
                "amount_staked": 0,
                "timestamp": datetime.now()
            }

        pool["stakers"][user_id]["amount_staked"] += amount
        pool["stakers"][user_id]["timestamp"] = datetime.now()

    def calculate_rewards(self, user_id, pool_id):
        """
        Calculate the rewards for a user based on staking time.
        :param user_id: str - Unique identifier for the user
        :param pool_id: str - Pool identifier
        :return: float - Amount of rewards earned
        """
        if pool_id not in self.pools:
            raise ValueError("Pool does not exist.")
        pool = self.pools[pool_id]

        if user_id not in pool["stakers"]:
            return 0.0

        staker = pool["stakers"][user_id]
        time_staked = (datetime.now() - staker["timestamp"]).total_seconds()
        return staker["amount_staked"] * pool["reward_rate"] * time_staked

    def withdraw_tokens(self, user_id, pool_id):
        """
        Withdraw staked tokens and claim rewards.
        :param user_id: str - Unique identifier for the user
        :param pool_id: str - Pool identifier
        :return: dict - Dictionary containing withdrawn amount and earned rewards
        """
        if pool_id not in self.pools:
            raise ValueError("Pool does not exist.")
        pool = self.pools[pool_id]

        if user_id not in pool["stakers"]:
            raise ValueError("User has not staked in this pool.")

        staker = pool["stakers"][user_id]
        time_staked = (datetime.now() - staker["timestamp"]).total_seconds()

        if time_staked < pool["lock_duration"]:
            raise ValueError("Tokens are still locked.")

        rewards = self.calculate_rewards(user_id, pool_id)
        amount_staked = staker["amount_staked"]

        # Remove staker record
        del pool["stakers"][user_id]

        return {
            "withdrawn_amount": amount_staked,
            "earned_rewards": rewards
        }


# Example usage
if __name__ == "__main__":
    # Initialize the farm reward system
    farm_system = FarmRewardSystem()

    # Create a staking pool
    farm_system.create_pool(pool_id="pool1", reward_rate=0.001, lock_duration=3600)

    # Stake tokens
    farm_system.stake_tokens(user_id="user123", pool_id="pool1", amount=100)

    # Simulate some time passing
    import time
    time.sleep(2)

    # Calculate rewards
    rewards = farm_system.calculate_rewards(user_id="user123", pool_id="pool1")
    print(f"Rewards earned: {rewards}")

    # Withdraw tokens and claim rewards
    try:
        result = farm_system.withdraw_tokens(user_id="user123", pool_id="pool1")
        print(f"Withdrawn: {result['withdrawn_amount']}, Rewards: {result['earned_rewards']}")
    except ValueError as e:
        print(f"Error: {e}")
```

This code provides a farm-style rewards system for a DAO, allowing users to stake tokens in pools, calculate rewards based on staking time, and withdraw their tokens and rewards after the lock duration. It includes error handling and adheres to best practices.
