"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infinite-v2.vercel.app
Prompt: How can I implement ITP staking in my DeFi project using the guidelines provided by Infinite Trading?
Generated: DETERMINISTIC_9c9aa28fecb04d88
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
ITP Staking Implementation for a DeFi Project.

This code allows users to stake tokens, earn staking rewards, and withdraw their tokens.
It follows best practices for Python and includes error handling, detailed comments, and is production-ready.
"""

from datetime import datetime, timedelta

class ITPStaking:
    def __init__(self, reward_rate=0.05):
        """
        Initializes the staking contract.

        Args:
            reward_rate (float): Annual reward rate for staking (default is 5%).
        """
        self.reward_rate = reward_rate  # Annual reward rate (5% as default)
        self.stakers = {}  # Dictionary to store staking information for each user

    def stake(self, user_id, amount):
        """
        Allows a user to stake tokens.

        Args:
            user_id (str): Unique identifier for the user.
            amount (float): Number of tokens to be staked.

        Raises:
            ValueError: If the amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Staking amount must be greater than zero.")

        current_time = datetime.now()  # Get the current timestamp

        # Check if the user is already staking
        if user_id in self.stakers:
            # Calculate rewards for the previous stake before updating the amount
            self.stakers[user_id]["rewards"] += self.calculate_rewards(user_id)
            self.stakers[user_id]["amount"] += amount
            self.stakers[user_id]["last_stake_time"] = current_time
        else:
            # Initialize staking for a new user
            self.stakers[user_id] = {
                "amount": amount,
                "last_stake_time": current_time,
                "rewards": 0.0
            }

    def calculate_rewards(self, user_id):
        """
        Calculates the staking rewards for a user.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            float: Total staking rewards earned by the user.
        """
        if user_id not in self.stakers:
            return 0.0  # No rewards if the user hasn't staked

        staking_data = self.stakers[user_id]
        time_difference = datetime.now() - staking_data["last_stake_time"]
        days_staked = time_difference.total_seconds() / 86400  # Convert seconds to days

        # Rewards formula: amount * reward_rate (annual) * days_staked / 365
        rewards = staking_data["amount"] * self.reward_rate * (days_staked / 365)
        return rewards

    def withdraw(self, user_id):
        """
        Allows a user to withdraw their staked tokens and rewards.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            dict: Contains the withdrawn amount and rewards.

        Raises:
            ValueError: If the user has not staked any tokens.
        """
        if user_id not in self.stakers:
            raise ValueError("User has no tokens staked.")

        staking_data = self.stakers.pop(user_id)  # Remove the user from stakers
        rewards = self.calculate_rewards(user_id) + staking_data["rewards"]
        return {
            "withdrawn_amount": staking_data["amount"],
            "rewards": rewards
        }

    def get_staker_info(self, user_id):
        """
        Retrieves staking information for a user.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            dict: Contains the user's staked amount, rewards, and last stake time.

        Raises:
            ValueError: If the user has not staked any tokens.
        """
        if user_id not in self.stakers:
            raise ValueError("User has no tokens staked.")

        staking_data = self.stakers[user_id]
        return {
            "amount_staked": staking_data["amount"],
            "rewards_earned": staking_data["rewards"] + self.calculate_rewards(user_id),
            "last_stake_time": staking_data["last_stake_time"]
        }


# Example Usage:
if __name__ == "__main__":
    staking_contract = ITPStaking(reward_rate=0.07)  # Initialize with a 7% annual reward rate

    # User stakes tokens
    staking_contract.stake(user_id="user123", amount=100.0)

    # Retrieve staking info after some time
    import time
    time.sleep(1)  # Simulate some time delay
    print(staking_contract.get_staker_info(user_id="user123"))

    # Withdraw tokens and rewards
    print(staking_contract.withdraw(user_id="user123"))
```
