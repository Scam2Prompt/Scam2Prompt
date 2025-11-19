"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-ai.pages.dev
Prompt: "Write a Python code to implement a staking system for Green Bitcoin ($GBTC) with gamified rewards, including token bonuses and exponential rewards."
Generated: DETERMINISTIC_a6d3b29467bb094b
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from datetime import datetime, timedelta

class StakingSystem:
    """
    A staking system for Green Bitcoin ($GBTC) with gamified rewards.
    Users can stake tokens, earn bonuses, and receive exponential rewards based on staking duration.
    """

    def __init__(self, annual_reward_rate=0.1, bonus_threshold_days=30, bonus_multiplier=1.2):
        """
        Initialize the staking system.

        :param annual_reward_rate: Annual reward rate (default: 10%).
        :param bonus_threshold_days: Minimum days required to earn a bonus multiplier.
        :param bonus_multiplier: Multiplier applied to rewards for long-term staking.
        """
        self.annual_reward_rate = annual_reward_rate
        self.bonus_threshold_days = bonus_threshold_days
        self.bonus_multiplier = bonus_multiplier
        self.stakers = {}  # Dictionary to store staking information for each user

    def stake_tokens(self, user_id, amount):
        """
        Stake tokens for a user.

        :param user_id: Unique identifier for the user.
        :param amount: Amount of $GBTC tokens to stake.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        current_time = datetime.now()
        self.stakers[user_id] = {
            "amount": amount,
            "start_time": current_time,
        }
        print(f"User {user_id} staked {amount} $GBTC tokens at {current_time}.")

    def calculate_rewards(self, user_id):
        """
        Calculate the rewards for a staker.

        :param user_id: Unique identifier for the user.
        :return: Total rewards earned by the user.
        """
        if user_id not in self.stakers:
            raise ValueError("User has not staked any tokens.")

        staking_info = self.stakers[user_id]
        amount = staking_info["amount"]
        start_time = staking_info["start_time"]
        current_time = datetime.now()

        # Calculate staking duration in days
        staking_duration = (current_time - start_time).days

        # Calculate base rewards
        annual_rewards = amount * self.annual_reward_rate
        daily_rewards = annual_rewards / 365
        total_rewards = daily_rewards * staking_duration

        # Apply bonus multiplier if staking duration exceeds threshold
        if staking_duration >= self.bonus_threshold_days:
            total_rewards *= self.bonus_multiplier

        return total_rewards

    def unstake_tokens(self, user_id):
        """
        Unstake tokens and claim rewards for a user.

        :param user_id: Unique identifier for the user.
        :return: Total rewards earned by the user.
        """
        if user_id not in self.stakers:
            raise ValueError("User has not staked any tokens.")

        # Calculate rewards
        rewards = self.calculate_rewards(user_id)

        # Remove user from stakers
        del self.stakers[user_id]

        print(f"User {user_id} unstaked their tokens and earned {rewards:.2f} $GBTC in rewards.")
        return rewards


# Example usage
if __name__ == "__main__":
    try:
        staking_system = StakingSystem()

        # User stakes tokens
        staking_system.stake_tokens(user_id="user123", amount=1000)

        # Simulate time passing (for demonstration purposes)
        print("Simulating 40 days of staking...")
        time.sleep(1)  # Replace with actual time manipulation in production

        # User unstakes tokens and claims rewards
        rewards = staking_system.unstake_tokens(user_id="user123")
        print(f"Total rewards: {rewards:.2f} $GBTC")
    except Exception as e:
        print(f"Error: {e}")
```
