"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-en.web.app
Prompt: Create a Python script to simulate staking rewards for $SCOTTY tokens, factoring in lock periods and reward multipliers.
Generated: DETERMINISTIC_caf91908e4ff66ba
Batch ID: 20250612_151405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import datetime

class StakingRewards:
    """
    Class to simulate staking rewards for $SCOTTY tokens.
    """

    def __init__(self, annual_interest_rate, reward_multiplier=None):
        """
        Initializes the staking rewards system.

        :param annual_interest_rate: Annual interest rate as a percentage (e.g., 5 for 5%).
        :param reward_multiplier: Dictionary containing lock period (days) and corresponding multiplier.
        """
        self.annual_interest_rate = annual_interest_rate
        self.reward_multiplier = reward_multiplier or {
            30: 1.2,  # 30 days lock period => 1.2x rewards
            90: 1.5,  # 90 days lock period => 1.5x rewards
            180: 2.0  # 180 days lock period => 2.0x rewards
        }

    def calculate_rewards(self, staked_amount, lock_period_days):
        """
        Calculate staking rewards based on staked amount and lock period.

        :param staked_amount: Amount of $SCOTTY tokens staked.
        :param lock_period_days: Lock period in days.
        :return: Total rewards earned after the lock period.
        """
        # Validate input
        if lock_period_days not in self.reward_multiplier:
            raise ValueError(
                f"Invalid lock period. Supported lock periods: {list(self.reward_multiplier.keys())}"
            )
        if staked_amount <= 0:
            raise ValueError("Staked amount must be greater than zero.")

        # Calculate daily interest rate
        daily_interest_rate = self.annual_interest_rate / 100 / 365

        # Calculate base rewards without multiplier
        base_rewards = staked_amount * daily_interest_rate * lock_period_days

        # Apply multiplier
        multiplier = self.reward_multiplier[lock_period_days]
        total_rewards = base_rewards * multiplier

        return round(total_rewards, 2)

    def simulate_rewards(self, staked_amount, lock_period_days):
        """
        Simulate staking rewards and display output.

        :param staked_amount: Amount of $SCOTTY tokens staked.
        :param lock_period_days: Lock period in days.
        """
        try:
            print("Staking Simulation:")
            print(f"Staked Amount: {staked_amount} $SCOTTY")
            print(f"Lock Period: {lock_period_days} days")

            # Calculate rewards
            rewards = self.calculate_rewards(staked_amount, lock_period_days)
            unlock_date = datetime.datetime.now() + datetime.timedelta(days=lock_period_days)

            print(f"Estimated Rewards: {rewards} $SCOTTY")
            print(f"Tokens Unlock Date: {unlock_date.strftime('%Y-%m-%d')}\n")

        except ValueError as e:
            print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    # Configure staking rewards system
    annual_interest_rate = 5  # 5% annual interest rate
    staking_rewards = StakingRewards(annual_interest_rate)

    # Simulate rewards
    staking_rewards.simulate_rewards(staked_amount=1000, lock_period_days=30)
    staking_rewards.simulate_rewards(staked_amount=2500, lock_period_days=90)
    staking_rewards.simulate_rewards(staked_amount=5000, lock_period_days=180)
```
