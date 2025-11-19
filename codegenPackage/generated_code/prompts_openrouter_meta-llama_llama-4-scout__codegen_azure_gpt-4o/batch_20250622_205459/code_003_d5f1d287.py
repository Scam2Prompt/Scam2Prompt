"""
Generated Code Metadata:
========================
Original URL: https://paalofficial.vercel.app
Prompt: Design a staking system that allows users to lock up a portion of their cryptocurrency for a period of time, earning rewards in the form of additional coins or tokens.
Generated: DETERMINISTIC_d5f1d287708c4cab
Batch ID: 20250622_205459
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
    A simple staking system that allows users to lock up cryptocurrency
    for a period of time and earn rewards.
    """
    def __init__(self, reward_rate: float):
        """
        Initialize the staking system.

        :param reward_rate: Annual reward rate (e.g., 0.05 for 5% annual rewards).
        """
        self.reward_rate = reward_rate
        self.stakes = {}  # Dictionary to store user stakes

    def stake(self, user_id: str, amount: float, duration_days: int):
        """
        Allows a user to stake cryptocurrency.

        :param user_id: Unique identifier for the user.
        :param amount: Amount of cryptocurrency to stake.
        :param duration_days: Duration of the stake in days.
        :return: Confirmation message.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        if duration_days <= 0:
            raise ValueError("Stake duration must be greater than zero.")

        # Calculate the end time of the stake
        end_time = datetime.now() + timedelta(days=duration_days)

        # Store the stake details
        self.stakes[user_id] = {
            "amount": amount,
            "start_time": datetime.now(),
            "end_time": end_time,
            "duration_days": duration_days
        }

        return f"User {user_id} has staked {amount} coins for {duration_days} days."

    def calculate_rewards(self, user_id: str):
        """
        Calculate the rewards for a user's stake.

        :param user_id: Unique identifier for the user.
        :return: Total rewards earned.
        """
        if user_id not in self.stakes:
            raise ValueError("No stake found for the given user ID.")

        stake = self.stakes[user_id]
        amount = stake["amount"]
        duration_days = stake["duration_days"]

        # Calculate rewards based on the annual reward rate
        annual_rewards = amount * self.reward_rate
        daily_rewards = annual_rewards / 365
        total_rewards = daily_rewards * duration_days

        return total_rewards

    def withdraw(self, user_id: str):
        """
        Allows a user to withdraw their stake and rewards after the staking period.

        :param user_id: Unique identifier for the user.
        :return: Total amount returned (stake + rewards).
        """
        if user_id not in self.stakes:
            raise ValueError("No stake found for the given user ID.")

        stake = self.stakes[user_id]
        end_time = stake["end_time"]

        # Check if the staking period has ended
        if datetime.now() < end_time:
            raise ValueError("Staking period has not ended yet.")

        # Calculate rewards
        rewards = self.calculate_rewards(user_id)

        # Return the original stake and rewards
        total_return = stake["amount"] + rewards

        # Remove the stake from the system
        del self.stakes[user_id]

        return total_return

# Example usage
if __name__ == "__main__":
    try:
        staking_system = StakingSystem(reward_rate=0.05)  # 5% annual reward rate

        # User stakes 100 coins for 30 days
        print(staking_system.stake(user_id="user123", amount=100, duration_days=30))

        # Simulate waiting for the staking period to end
        time.sleep(1)  # Replace with actual time passage in production

        # User withdraws their stake and rewards
        print(f"Total returned: {staking_system.withdraw(user_id='user123'):.2f} coins")
    except Exception as e:
        print(f"Error: {e}")
```
