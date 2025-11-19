"""
Generated Code Metadata:
========================
Original URL: https://scottyweb.pages.dev
Prompt: Design a staking system that allows users to withdraw their staked tokens and claimable rewards, taking into account the 3-year reward period and dynamic rewards rate.
Generated: DETERMINISTIC_2ba64425a6b74fb0
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class StakingSystem:
    def __init__(self, reward_rate_per_year):
        """
        Initialize the staking system.

        :param reward_rate_per_year: Annual reward rate (e.g., 0.05 for 5% per year)
        """
        self.reward_rate_per_year = reward_rate_per_year
        self.stakes = {}  # Stores user stakes in the format: {user_id: {"amount": float, "start_time": datetime}}

    def stake_tokens(self, user_id, amount):
        """
        Allows a user to stake tokens.

        :param user_id: Unique identifier for the user
        :param amount: Amount of tokens to stake
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        current_time = datetime.now()
        if user_id in self.stakes:
            # If user already has a stake, update the amount and reset the start time
            self.stakes[user_id]["amount"] += amount
            self.stakes[user_id]["start_time"] = current_time
        else:
            # Create a new stake entry for the user
            self.stakes[user_id] = {"amount": amount, "start_time": current_time}

    def calculate_rewards(self, user_id):
        """
        Calculate the claimable rewards for a user based on their stake and staking duration.

        :param user_id: Unique identifier for the user
        :return: Claimable rewards (float)
        """
        if user_id not in self.stakes:
            raise ValueError("User has no active stake.")

        stake_info = self.stakes[user_id]
        staked_amount = stake_info["amount"]
        start_time = stake_info["start_time"]
        current_time = datetime.now()

        # Calculate staking duration (capped at 3 years)
        staking_duration = min(current_time - start_time, timedelta(days=3 * 365))
        staking_years = staking_duration.days / 365.0

        # Calculate rewards based on the dynamic reward rate
        rewards = staked_amount * (self.reward_rate_per_year * staking_years)
        return rewards

    def withdraw(self, user_id):
        """
        Allows a user to withdraw their staked tokens and claimable rewards.

        :param user_id: Unique identifier for the user
        :return: A tuple containing the withdrawn amount and claimable rewards
        """
        if user_id not in self.stakes:
            raise ValueError("User has no active stake.")

        stake_info = self.stakes.pop(user_id)  # Remove the user's stake
        staked_amount = stake_info["amount"]
        rewards = self.calculate_rewards(user_id)

        return staked_amount, rewards


# Example usage:
if __name__ == "__main__":
    staking_system = StakingSystem(reward_rate_per_year=0.05)  # 5% annual reward rate

    # User stakes tokens
    staking_system.stake_tokens(user_id="user123", amount=1000)

    # Simulate some time passing (for demonstration purposes)
    import time
    time.sleep(2)  # Wait for 2 seconds

    # User withdraws their stake and rewards
    try:
        staked_amount, rewards = staking_system.withdraw(user_id="user123")
        print(f"Withdrawn Amount: {staked_amount}")
        print(f"Claimable Rewards: {rewards}")
    except ValueError as e:
        print(f"Error: {e}")
```
