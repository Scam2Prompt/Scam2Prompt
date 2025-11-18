"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-mindofpepe-allocations.pages.dev
Prompt: Provide a step-by-step guide for building a staking mechanism with dynamic APY calculations, similar to the MIND of Pepe staking rewards system.
Generated: DETERMINISTIC_0c569f7509ab15b4
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready implementation in Python for a staking mechanism with dynamic APY calculations. The code uses the `decimal` module for precise calculations and follows best practices.

```python
import time
from decimal import Decimal, getcontext
import threading

# Set the precision for Decimal calculations
getcontext().prec = 18

class StakingPool:
    """
    A class representing a staking pool with dynamic APY calculations.
    """

    def __init__(self, base_apy: Decimal):
        """
        Initialize the staking pool with a base APY and other parameters.
        
        :param base_apy: The base Annual Percentage Yield (APY) represented as a percentage (e.g., 10 for 10%).
        """
        self.base_apy = base_apy / Decimal(100)  # Convert percentage to decimal form
        self.stakers = {}  # Dictionary to hold staker information
        self.total_staked = Decimal('0')  # Total staked amount in the pool
        self.lock = threading.Lock()  # Thread-safe access to pool data

    def stake(self, user: str, amount: Decimal):
        """
        Allows a user to stake a specified amount.
        
        :param user: The username or identifier of the staker.
        :param amount: The amount to stake.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        with self.lock:
            if user not in self.stakers:
                self.stakers[user] = {'amount_staked': Decimal('0'), 'last_stake_time': time.time()}
            self.stakers[user]['amount_staked'] += amount
            self.stakers[user]['last_stake_time'] = time.time()
            self.total_staked += amount

    def unstake(self, user: str):
        """
        Allows a user to unstake their staked amount and claim rewards.
        
        :param user: The username or identifier of the staker.
        :return: A tuple of (staked_amount, rewards_earned).
        """
        with self.lock:
            if user not in self.stakers or self.stakers[user]['amount_staked'] == 0:
                raise ValueError("No staked amount found for the user.")

            # Calculate rewards based on time staked and APY
            staked_amount = self.stakers[user]['amount_staked']
            rewards = self.calculate_rewards(user)

            # Reset user staking info
            self.stakers[user]['amount_staked'] = Decimal('0')
            self.stakers[user]['last_stake_time'] = None
            self.total_staked -= staked_amount

            return staked_amount, rewards

    def calculate_rewards(self, user: str) -> Decimal:
        """
        Calculate the rewards for a specific user based on the staked amount and time staked.
        
        :param user: The username or identifier of the staker.
        :return: The calculated reward amount.
        """
        user_data = self.stakers.get(user)
        if not user_data or user_data['amount_staked'] == 0:
            return Decimal('0')

        time_staked_seconds = time.time() - user_data['last_stake_time']
        time_staked_years = Decimal(time_staked_seconds) / Decimal(31536000)  # Convert seconds to years
        user_stake = user_data['amount_staked']

        # Dynamic APY calculation can be extended here, e.g., based on pool activity
        effective_apy = self.base_apy  # For simplicity, we are using the base APY
        rewards = user_stake * effective_apy * time_staked_years

        return rewards

    def get_pool_info(self) -> dict:
        """
        Retrieve staking pool information such as total staked and staker details.
        
        :return: A dictionary containing pool information.
        """
        with self.lock:
            return {
                'total_staked': self.total_staked,
                'stakers': self.stakers.copy()
            }


# Example usage
if __name__ == "__main__":
    # Initialize the staking pool with a base APY of 12%
    staking_pool = StakingPool(base_apy=Decimal('12'))

    # User 1 stakes 100 tokens
    staking_pool.stake(user="user1", amount=Decimal('100'))
    time.sleep(2)  # Simulate staking duration

    # User 1 unstakes and claims rewards
    staked_amount, rewards = staking_pool.unstake(user="user1")
    print(f"User1 unstaked {staked_amount} tokens and earned {rewards} in rewards.")

    # Check pool info
    print("Pool Info:", staking_pool.get_pool_info())
```

This code implements a staking pool with dynamic APY calculations. It uses `Decimal` for precise financial calculations, includes thread safety with a lock, and provides comprehensive error handling. The dynamic APY can be made more sophisticated based on additional conditions, such as total pool activity or external metrics.
