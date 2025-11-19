"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shdw.so
Prompt: Describe how to set up liquidity pools that reward users based on their contributions, taking cues from the liquidity model of Shadow Exchange.
Generated: DETERMINISTIC_7915c0a7b47f0b80
Batch ID: 20250612_162335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready code implementation for setting up a liquidity pool reward system inspired by the Shadow Exchange liquidity model. This example uses Python with a simple smart contract-like approach:

```python
import math

class LiquidityPool:
    """
    A class to represent a liquidity pool.
    This pool rewards users based on their proportional contributions.
    """

    def __init__(self, pool_name):
        """
        Initialize the liquidity pool.

        :param pool_name: Name of the liquidity pool.
        """
        self.pool_name = pool_name
        self.total_liquidity = 0
        self.contributors = {}  # Maps user address to their contribution
        self.rewards = {}       # Maps user address to their accrued rewards

    def add_liquidity(self, user_address, amount):
        """
        Add liquidity to the pool from a specific user.

        :param user_address: Unique address or identifier for the user.
        :param amount: Liquidity amount to add.
        :raises ValueError: If amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Liquidity amount must be greater than zero.")

        self.total_liquidity += amount

        # Update user's contribution
        if user_address in self.contributors:
            self.contributors[user_address] += amount
        else:
            self.contributors[user_address] = amount

        # Initialize reward bucket for new contributors
        if user_address not in self.rewards:
            self.rewards[user_address] = 0

    def distribute_rewards(self, reward_pool):
        """
        Distribute rewards among users based on their proportional contribution.

        :param reward_pool: Total amount of rewards to distribute.
        :raises ValueError: If reward_pool is not positive.
        """
        if reward_pool <= 0:
            raise ValueError("Reward pool must be greater than zero.")

        if self.total_liquidity == 0:
            raise ValueError("No liquidity in the pool to distribute rewards.")

        for user_address, user_contribution in self.contributors.items():
            # Calculate proportional reward
            user_share = user_contribution / self.total_liquidity
            user_reward = reward_pool * user_share

            # Add to user's reward balance
            self.rewards[user_address] += user_reward

    def withdraw_liquidity(self, user_address, amount):
        """
        Withdraw liquidity from the pool for a specific user.

        :param user_address: Unique address or identifier for the user.
        :param amount: Liquidity amount to withdraw.
        :raises ValueError: If amount is not positive or exceeds user's contribution.
        """
        if amount <= 0:
            raise ValueError("Withdraw amount must be greater than zero.")

        if user_address not in self.contributors or self.contributors[user_address] < amount:
            raise ValueError("Insufficient liquidity to withdraw.")

        # Update user's contribution and pool's liquidity
        self.contributors[user_address] -= amount
        self.total_liquidity -= amount

        # Remove user from contributors if their balance reaches zero
        if self.contributors[user_address] == 0:
            del self.contributors[user_address]

    def claim_rewards(self, user_address):
        """
        Allow a user to claim their accrued rewards.

        :param user_address: Unique address or identifier for the user.
        :return: The claimed reward amount.
        :raises ValueError: If user has no accrued rewards.
        """
        if user_address not in self.rewards or self.rewards[user_address] <= 0:
            raise ValueError("No rewards available to claim.")

        # Retrieve and reset user's reward balance
        claimed_rewards = self.rewards[user_address]
        self.rewards[user_address] = 0
        return claimed_rewards

    def get_pool_summary(self):
        """
        Get a summary of the pool's state.

        :return: Summary dictionary containing pool name, total liquidity, contributors, and rewards.
        """
        return {
            "pool_name": self.pool_name,
            "total_liquidity": self.total_liquidity,
            "contributors": self.contributors,
            "rewards": self.rewards,
        }

# Example usage
if __name__ == "__main__":
    try:
        # Create a liquidity pool
        pool = LiquidityPool(pool_name="Shadow Exchange Pool")

        # Add liquidity
        pool.add_liquidity("user1", 1000)
        pool.add_liquidity("user2", 500)

        # Distribute rewards
        pool.distribute_rewards(reward_pool=300)

        # Withdraw liquidity
        pool.withdraw_liquidity("user1", 200)

        # Claim rewards
        claimed_rewards = pool.claim_rewards("user1")
        print(f"user1 claimed rewards: {claimed_rewards}")

        # Print pool summary
        summary = pool.get_pool_summary()
        print("Pool Summary:", summary)
    except ValueError as e:
        print(f"Error: {e}")
```

This code provides a structure for managing a liquidity pool with contributors and rewards, ensuring error handling and best practices.
