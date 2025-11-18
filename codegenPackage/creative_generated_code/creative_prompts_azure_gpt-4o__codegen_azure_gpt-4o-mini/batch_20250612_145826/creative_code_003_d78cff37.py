"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrogg.pages.dev
Prompt: Write code to implement a staking platform with two pools: one offering higher returns with a locked schedule and another allowing flexible withdrawals, as described in the War Chest feature.
Generated: DETERMINISTIC_d78cff37e3dd3664
Batch ID: 20250612_145826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class StakingPool:
    """
    A class to represent a staking pool.
    """
    def __init__(self, name: str, interest_rate: float, lock_period: Optional[timedelta] = None):
        """
        Initializes a staking pool.

        :param name: Name of the staking pool.
        :param interest_rate: Interest rate of the pool (as a decimal).
        :param lock_period: Duration for which funds are locked (None for flexible withdrawals).
        """
        self.name = name
        self.interest_rate = interest_rate
        self.lock_period = lock_period
        self.stakers: Dict[str, float] = {}
        self.locked_stakes: Dict[str, datetime] = {}

    def stake(self, user: str, amount: float):
        """
        Allows a user to stake a certain amount in the pool.

        :param user: The user staking the amount.
        :param amount: The amount to stake.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        
        if user in self.stakers:
            self.stakers[user] += amount
        else:
            self.stakers[user] = amount

        if self.lock_period:
            self.locked_stakes[user] = datetime.now() + self.lock_period

    def withdraw(self, user: str, amount: float):
        """
        Allows a user to withdraw a certain amount from the pool.

        :param user: The user withdrawing the amount.
        :param amount: The amount to withdraw.
        """
        if user in self.stakers:
            if self.lock_period and datetime.now() < self.locked_stakes[user]:
                raise Exception("Funds are locked; withdrawal not allowed.")

            if amount > self.stakers[user]:
                raise ValueError("Insufficient balance to withdraw.")

            self.stakers[user] -= amount
            if self.stakers[user] == 0:
                del self.stakers[user]
                del self.locked_stakes[user]  # Clean up if user has no balance
        else:
            raise ValueError("User has no stakes in this pool.")

    def calculate_interest(self, user: str) -> float:
        """
        Calculates interest for a user based on their staked amount.

        :param user: The user to calculate interest for.
        :return: Calculated interest amount.
        """
        if user in self.stakers:
            return self.stakers[user] * self.interest_rate
        else:
            raise ValueError("User has no stakes in this pool.")

class StakingPlatform:
    """
    A class to represent a staking platform with multiple pools.
    """
    def __init__(self):
        self.pools: Dict[str, StakingPool] = {}

    def add_pool(self, name: str, interest_rate: float, lock_period: Optional[timedelta] = None):
        """
        Adds a new staking pool to the platform.

        :param name: Name of the staking pool.
        :param interest_rate: Interest rate for the new pool.
        :param lock_period: Duration for which funds are locked (None for flexible).
        """
        if name in self.pools:
            raise ValueError("A pool with this name already exists.")
        
        self.pools[name] = StakingPool(name, interest_rate, lock_period)

    def get_pool(self, name: str) -> StakingPool:
        """
        Retrieves a staking pool by its name.

        :param name: Name of the staking pool.
        :return: StakingPool object.
        """
        if name in self.pools:
            return self.pools[name]
        else:
            raise ValueError("Pool not found.")

# Example Usage
if __name__ == "__main__":
    platform = StakingPlatform()
    platform.add_pool("High Return Pool", interest_rate=0.10, lock_period=timedelta(days=30))
    platform.add_pool("Flexible Pool", interest_rate=0.05)

    # User actions
    user = "alice"
    
    # Staking in the High Return Pool
    high_return_pool = platform.get_pool("High Return Pool")
    high_return_pool.stake(user, 1000)

    # Calculate interest
    interest = high_return_pool.calculate_interest(user)
    print(f"Interest for {user} in High Return Pool: {interest}")

    # Attempt to withdraw before lock period
    try:
        high_return_pool.withdraw(user, 500)
    except Exception as e:
        print(e)

    # Wait for lock period to expire (simulation)
    high_return_pool.locked_stakes[user] -= timedelta(days=30)

    # Now withdraw
    high_return_pool.withdraw(user, 500)
    print(f"Balance after withdrawal: {high_return_pool.stakers[user]}")
```
