"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimedsonic.pages.dev
Prompt: How can I implement staking functionality for my users based on the Staking feature mentioned on the Guildhall site?
Generated: DETERMINISTIC_18631fb56e4d5b9d
Batch ID: 20250612_155855
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

class StakingSystem:
    """
    A simple staking system implementation.
    """

    def __init__(self, annual_interest_rate: float):
        """
        Initializes the staking system with an annual interest rate.

        Args:
            annual_interest_rate (float): Annual interest rate in percentage (e.g., 5 for 5%).
        """
        self.annual_interest_rate = annual_interest_rate / 100
        self.stakes = {}  # Stores user stakes as {user_id: {amount, start_time}}

    def stake(self, user_id: str, amount: float):
        """
        Allows a user to stake a certain amount.

        Args:
            user_id (str): Unique identifier for the user.
            amount (float): The amount to stake.

        Raises:
            ValueError: If the amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Staking amount must be greater than zero.")

        current_time = datetime.now()
        self.stakes[user_id] = {
            "amount": amount,
            "start_time": current_time
        }

        print(f"User '{user_id}' staked {amount} tokens at {current_time}.")

    def calculate_rewards(self, user_id: str):
        """
        Calculates the rewards for a user based on the staking duration.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            float: The calculated rewards.

        Raises:
            KeyError: If the user does not have an active stake.
        """
        if user_id not in self.stakes:
            raise KeyError(f"User '{user_id}' does not have an active stake.")

        stake_info = self.stakes[user_id]
        amount = stake_info["amount"]
        start_time = stake_info["start_time"]

        # Calculate staking duration in days
        current_time = datetime.now()
        duration = (current_time - start_time).total_seconds() / (60 * 60 * 24)

        # Annual interest rate applied to the staking amount
        rewards = (amount * self.annual_interest_rate * duration) / 365
        return rewards

    def unstake(self, user_id: str):
        """
        Unstakes a user's tokens and calculates rewards.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            dict: Contains the original staked amount and calculated rewards.

        Raises:
            KeyError: If the user does not have an active stake.
        """
        if user_id not in self.stakes:
            raise KeyError(f"User '{user_id}' does not have an active stake.")

        stake_info = self.stakes.pop(user_id)  # Remove stake from storage
        original_amount = stake_info["amount"]
        rewards = self.calculate_rewards(user_id)

        print(f"User '{user_id}' unstaked {original_amount} tokens with {rewards:.2f} rewards.")
        return {
            "original_amount": original_amount,
            "rewards": rewards
        }


# Example usage:
if __name__ == "__main__":
    # Initialize staking system with a 5% annual interest rate
    staking_system = StakingSystem(annual_interest_rate=5)

    try:
        # User stakes tokens
        staking_system.stake(user_id="user123", amount=1000)

        # Simulate some time passing (e.g., 30 days)
        time.sleep(1)  # For demonstration purposes, replace with actual time logic

        # Calculate rewards for the user
        rewards = staking_system.calculate_rewards(user_id="user123")
        print(f"Calculated rewards: {rewards:.2f} tokens.")

        # User unstakes tokens
        result = staking_system.unstake(user_id="user123")
        print(f"Unstake result: {result}")

    except Exception as e:
        print(f"Error: {e}")
```
