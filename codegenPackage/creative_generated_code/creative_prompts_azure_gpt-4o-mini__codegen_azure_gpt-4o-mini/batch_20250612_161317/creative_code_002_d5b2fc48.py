"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://levva.net
Prompt: What are the different lock-up periods for staking $LVVA on Levva, and how do they affect the bonus rewards?
Generated: DETERMINISTIC_d5b2fc480903dbcc
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Staking:
    def __init__(self, lockup_periods, bonus_rewards):
        """
        Initializes the Staking class with lockup periods and their corresponding bonus rewards.

        :param lockup_periods: A dictionary where keys are lock-up periods (in days) and values are their bonus rewards.
        :param bonus_rewards: A list of bonus rewards corresponding to each lock-up period.
        """
        self.lockup_periods = lockup_periods  # Stores lockup periods and their rewards

    def get_bonus_reward(self, period):
        """
        Retrieves the bonus reward for a given lock-up period.

        :param period: The lock-up period for which to retrieve the bonus reward.
        :return: The bonus reward associated with the given lock-up period.
        :raises ValueError: If the period is not in the lockup periods.
        """
        if period in self.lockup_periods:
            return self.lockup_periods[period]
        else:
            raise ValueError(f"Invalid lock-up period: {period}. Available periods: {list(self.lockup_periods.keys())}")

    def calculate_total_reward(self, amount_staked, period):
        """
        Calculates the total reward based on the amount staked and the lock-up period.

        :param amount_staked: The amount of $LVVA staked.
        :param period: The lock-up period for which to calculate the reward.
        :return: Total calculated rewards.
        :raises ValueError: If the period is not in the lockup periods.
        """
        bonus_reward = self.get_bonus_reward(period)
        total_reward = amount_staked * (1 + bonus_reward)
        return total_reward

# Example usage
if __name__ == "__main__":
    # Define lock-up periods and their corresponding bonus rewards
    lockup_periods = {
        30: 0.05,  # 5% bonus for 30 days
        60: 0.10,  # 10% bonus for 60 days
        90: 0.15   # 15% bonus for 90 days
    }

    # Initialize the Staking class
    staking = Staking(lockup_periods, list(lockup_periods.values()))

    # Amount staked in dollars (example)
    amount_staked = 1000.0

    # Specify the lock-up period
    lockup_period = 60  # 60 days

    try:
        total_reward = staking.calculate_total_reward(amount_staked, lockup_period)
        print(f"Total reward for staking ${amount_staked} for {lockup_period} days: ${total_reward:.2f}")
    except ValueError as e:
        print(e)
```
