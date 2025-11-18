"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://penpie.io
Prompt: Create a script to calculate rewards for staking mPENDLE tokens and locking vlPNP tokens, including forfeited rewards from expired locks.
Generated: DETERMINISTIC_2a2cb3bdbfadbef0
Batch ID: 20250612_150604
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class StakingRewardsCalculator:
    """
    A class to calculate rewards for staking mPENDLE tokens and locking vlPNP tokens.
    Includes forfeited rewards for expired locks.
    """

    def __init__(self, staking_rate, locking_rate, expired_penalty_rate):
        """
        Initializes the reward calculator with staking and locking rates.

        :param staking_rate: Reward rate per mPENDLE token staked (float, e.g., 0.05 for 5%)
        :param locking_rate: Reward rate per vlPNP token locked (float, e.g., 0.1 for 10%)
        :param expired_penalty_rate: Penalty rate for expired locks (float, e.g., 0.02 for 2%)
        """
        self.staking_rate = staking_rate
        self.locking_rate = locking_rate
        self.expired_penalty_rate = expired_penalty_rate

    def calculate_staking_rewards(self, staked_tokens):
        """
        Calculates rewards for mPENDLE tokens staked.

        :param staked_tokens: Number of mPENDLE tokens staked (int or float)
        :return: Reward amount (float)
        """
        if staked_tokens < 0:
            raise ValueError("Staked tokens must be non-negative.")
        return staked_tokens * self.staking_rate

    def calculate_locking_rewards(self, locked_tokens, lock_duration_days):
        """
        Calculates rewards for vlPNP tokens locked based on duration.

        :param locked_tokens: Number of vlPNP tokens locked (int or float)
        :param lock_duration_days: Duration of lock in days (int)
        :return: Reward amount (float)
        """
        if locked_tokens < 0 or lock_duration_days < 0:
            raise ValueError("Locked tokens and lock duration must be non-negative.")
        return locked_tokens * self.locking_rate * lock_duration_days

    def calculate_expired_forfeited_rewards(self, locked_tokens, lock_expiry_date):
        """
        Calculates forfeited rewards for expired locks.

        :param locked_tokens: Number of vlPNP tokens locked (int or float)
        :param lock_expiry_date: Expiry date of lock (datetime.date)
        :return: Forfeited reward amount (float)
        """
        if locked_tokens < 0:
            raise ValueError("Locked tokens must be non-negative.")
        
        current_date = datetime.date.today()
        if lock_expiry_date < current_date:
            # If the lock has expired, calculate forfeited rewards
            days_expired = (current_date - lock_expiry_date).days
            return locked_tokens * self.expired_penalty_rate * days_expired
        return 0.0

    def calculate_total_rewards(self, staked_tokens, locked_tokens, lock_duration_days, lock_expiry_date):
        """
        Calculates total rewards including staking, locking, and forfeited rewards.

        :param staked_tokens: Number of mPENDLE tokens staked (int or float)
        :param locked_tokens: Number of vlPNP tokens locked (int or float)
        :param lock_duration_days: Duration of lock in days (int)
        :param lock_expiry_date: Expiry date of lock (datetime.date)
        :return: Total reward amount (float)
        """
        staking_rewards = self.calculate_staking_rewards(staked_tokens)
        locking_rewards = self.calculate_locking_rewards(locked_tokens, lock_duration_days)
        forfeited_rewards = self.calculate_expired_forfeited_rewards(locked_tokens, lock_expiry_date)
        total_rewards = staking_rewards + locking_rewards - forfeited_rewards
        return total_rewards


# Example usage of the StakingRewardsCalculator
if __name__ == "__main__":
    try:
        # Initialize reward calculator with rates
        calculator = StakingRewardsCalculator(staking_rate=0.05, locking_rate=0.1, expired_penalty_rate=0.02)

        # Input values
        staked_tokens = 1000  # Example: 1000 mPENDLE tokens staked
        locked_tokens = 500  # Example: 500 vlPNP tokens locked
        lock_duration_days = 30  # Example: Locked for 30 days
        lock_expiry_date = datetime.date(2023, 10, 1)  # Example: Lock expired on October 1, 2023

        # Calculate rewards
        total_rewards = calculator.calculate_total_rewards(
            staked_tokens, locked_tokens, lock_duration_days, lock_expiry_date
        )

        # Output the total rewards
        print(f"Total Rewards: {total_rewards:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
