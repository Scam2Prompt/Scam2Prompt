"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gopluslabs.world
Prompt: Implement a staking mechanism for $GPS tokens with reward calculation, referencing GoPlus's staking features and APR details.
Generated: DETERMINISTIC_8cebdcfa7014294c
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from decimal import Decimal, getcontext
from datetime import datetime, timedelta

# Set the precision for Decimal operations
getcontext().prec = 6

class StakingPool:
    """
    A class to represent a staking pool for $GPS tokens.

    Attributes:
    -----------
    total_staked : Decimal
        The total amount of $GPS tokens staked in the pool.
    reward_rate : Decimal
        The annual percentage rate (APR) for staking rewards.
    staking_period : int
        The duration in days for which tokens are staked.
    stakes : dict
        A dictionary holding user stakes and their staking time.
    """

    def __init__(self, reward_rate: Decimal, staking_period: int):
        """
        Initializes the StakingPool with a given reward rate and staking period.

        Parameters:
        ----------
        reward_rate : Decimal
            The annual percentage rate (APR) for staking rewards.
        staking_period : int
            Duration in days for which tokens can be staked.
        """
        self.total_staked = Decimal(0)
        self.reward_rate = reward_rate
        self.staking_period = staking_period
        self.stakes = {}

    def stake(self, user_id: str, amount: Decimal):
        """
        Allows a user to stake a specified amount of $GPS tokens.

        Parameters:
        ----------
        user_id : str
            The ID of the user staking tokens.
        amount : Decimal
            The amount of $GPS tokens to stake.

        Raises:
        ------
        ValueError: If the amount staked is non-positive.
        """
        if amount <= 0:
            raise ValueError("Staking amount must be greater than zero.")
        
        # Update total staked amount and user's stake
        self.total_staked += amount
        self.stakes[user_id] = {
            'amount': amount,
            'timestamp': datetime.now()
        }

    def calculate_rewards(self, user_id: str) -> Decimal:
        """
        Calculates the staking rewards for a user based on the amount staked and the time staked.

        Parameters:
        ----------
        user_id : str
            The ID of the user for whom to calculate rewards.

        Returns:
        -------
        Decimal
            The calculated reward amount.

        Raises:
        ------
        KeyError: If the user has no stakes.
        """
        if user_id not in self.stakes:
            raise KeyError("User has no stakes.")
        
        stake_info = self.stakes[user_id]
        staked_amount = stake_info['amount']
        staked_time = datetime.now() - stake_info['timestamp']

        # Calculate the rewards based on the time staked and APR
        days_staked = staked_time.days
        if days_staked > self.staking_period:
            days_staked = self.staking_period

        # Simple reward calculation based on APR
        reward = (staked_amount * self.reward_rate * days_staked / 365)
        return reward

    def unstake(self, user_id: str) -> Decimal:
        """
        Allows a user to unstake their tokens and receive rewards.

        Parameters:
        ----------
        user_id : str
            The ID of the user unstaking tokens.

        Returns:
        -------
        Decimal
            The total amount of tokens returned to the user including rewards.

        Raises:
        ------
        KeyError: If the user has no stakes.
        """
        if user_id not in self.stakes:
            raise KeyError("User has no stakes.")
        
        # Calculate rewards and unstake amount
        rewards = self.calculate_rewards(user_id)
        staked_amount = self.stakes[user_id]['amount']
        
        # Remove user stake from the pool
        del self.stakes[user_id]
        self.total_staked -= staked_amount

        return staked_amount + rewards

# Example usage of the StakingPool class
if __name__ == "__main__":
    try:
        # Create a staking pool with an APR of 10%
        staking_pool = StakingPool(reward_rate=Decimal('0.10'), staking_period=30)

        # User stakes tokens
        staking_pool.stake(user_id="user123", amount=Decimal('1000.00'))
        
        # Simulate waiting for some time (for testing only)
        import time
        time.sleep(2)  # Sleep for 2 seconds to simulate staking time

        # Calculate rewards
        rewards = staking_pool.calculate_rewards(user_id="user123")
        print(f"Calculated rewards for user123: {rewards:.2f} GPS")

        # User unstakes tokens and receives rewards
        total_return = staking_pool.unstake(user_id="user123")
        print(f"Total amount returned to user123: {total_return:.2f} GPS")

    except Exception as e:
        print(f"An error occurred: {e}")
```
