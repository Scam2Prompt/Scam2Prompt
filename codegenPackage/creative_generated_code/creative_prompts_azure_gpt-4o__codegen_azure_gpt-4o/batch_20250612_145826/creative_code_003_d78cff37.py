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
import time
from datetime import datetime, timedelta
import threading

class StakingPlatform:
    """
    A staking platform with two pools:
    1. Locked Pool (Higher returns, withdrawal locked for a specified duration)
    2. Flexible Pool (Lower returns, withdrawals allowed anytime)
    """

    # Initialize the platform
    def __init__(self):
        self.locked_pool = {}  # Store user stakes in locked pool
        self.flexible_pool = {}  # Store user stakes in flexible pool
        self.locked_pool_duration = 30  # Locked duration in days
        self.locked_pool_rate = 0.15  # 15% annual return
        self.flexible_pool_rate = 0.05  # 5% annual return
        self.locked_pool_lock_period = {}  # Store lock end dates for locked pool stakes

    def stake_locked_pool(self, user, amount):
        """
        Stake an amount into the locked pool.
        :param user: The username of the participant.
        :param amount: The amount to stake.
        :return: Confirmation message.
        """
        if amount <= 0:
            return "Error: Amount must be greater than 0."

        # Store stake and lock period
        self.locked_pool[user] = self.locked_pool.get(user, 0) + amount
        lock_end_date = datetime.now() + timedelta(days=self.locked_pool_duration)
        self.locked_pool_lock_period[user] = lock_end_date
        return f"{user} staked {amount} in the locked pool. Withdrawal is locked until {lock_end_date}."

    def stake_flexible_pool(self, user, amount):
        """
        Stake an amount into the flexible pool.
        :param user: The username of the participant.
        :param amount: The amount to stake.
        :return: Confirmation message.
        """
        if amount <= 0:
            return "Error: Amount must be greater than 0."

        # Store stake
        self.flexible_pool[user] = self.flexible_pool.get(user, 0) + amount
        return f"{user} staked {amount} in the flexible pool."

    def withdraw_locked_pool(self, user):
        """
        Withdraw from the locked pool if the lock period has ended.
        :param user: The username of the participant.
        :return: Withdrawal message.
        """
        if user not in self.locked_pool or self.locked_pool[user] == 0:
            return "Error: No funds staked in the locked pool."

        current_date = datetime.now()
        lock_end_date = self.locked_pool_lock_period.get(user)

        if current_date < lock_end_date:
            remaining_days = (lock_end_date - current_date).days
            return f"Error: Funds are locked for {remaining_days} more days."

        # Calculate returns (annual return prorated based on lock duration)
        amount = self.locked_pool[user]
        interest = amount * self.locked_pool_rate * (self.locked_pool_duration / 365)
        self.locked_pool[user] = 0
        return f"{user} withdrew {amount + interest:.2f} from the locked pool (including {interest:.2f} in returns)."

    def withdraw_flexible_pool(self, user):
        """
        Withdraw from the flexible pool anytime.
        :param user: The username of the participant.
        :return: Withdrawal message.
        """
        if user not in self.flexible_pool or self.flexible_pool[user] == 0:
            return "Error: No funds staked in the flexible pool."

        # Calculate returns (annual return prorated based on duration)
        amount = self.flexible_pool[user]
        stake_duration = 30  # For simplicity, assume 30 days staking period
        interest = amount * self.flexible_pool_rate * (stake_duration / 365)
        self.flexible_pool[user] = 0
        return f"{user} withdrew {amount + interest:.2f} from the flexible pool (including {interest:.2f} in returns)."

    def get_pool_status(self):
        """
        Get the current status of both pools.
        :return: A dictionary containing pool details.
        """
        return {
            "locked_pool": self.locked_pool,
            "flexible_pool": self.flexible_pool,
            "locked_pool_lock_dates": self.locked_pool_lock_period,
        }

# Example usage
if __name__ == "__main__":
    staking_platform = StakingPlatform()

    print(staking_platform.stake_locked_pool("Alice", 100))
    print(staking_platform.stake_flexible_pool("Bob", 50))

    time.sleep(1)  # Simulate time passing

    print(staking_platform.withdraw_locked_pool("Alice"))
    print(staking_platform.withdraw_flexible_pool("Bob"))

    print(staking_platform.get_pool_status())
```
