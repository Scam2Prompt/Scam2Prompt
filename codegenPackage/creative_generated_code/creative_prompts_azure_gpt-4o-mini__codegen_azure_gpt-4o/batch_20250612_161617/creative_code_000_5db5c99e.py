"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://green-bitcoins-en.pages.dev
Prompt: Generate a Python script to implement a staking mechanism for the Green Bitcoin ($GBTC) that allows users to earn rewards based on their staked amount.
Generated: DETERMINISTIC_5db5c99eebb26566
Batch ID: 20250612_161617
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


class StakingMechanism:
    """
    A class to implement a staking mechanism for Green Bitcoin ($GBTC).
    Users can stake their GBTC to earn rewards based on the staked amount and duration.
    """

    def __init__(self, annual_reward_rate: float = 0.05):
        """
        Initialize the staking mechanism.

        :param annual_reward_rate: Annual reward rate (as a decimal), default is 5% (0.05).
        """
        self.annual_reward_rate = annual_reward_rate
        self.stakers = {}  # Dictionary to hold staker information.

    def stake_tokens(self, user_id: str, amount: float):
        """
        Stake tokens for a user.

        :param user_id: Unique identifier for the user.
        :param amount: Amount of GBTC tokens to stake.
        :return: None
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than 0.")
        
        # Check if the user is already staking
        if user_id in self.stakers:
            self.stakers[user_id]["amount"] += amount
            self.stakers[user_id]["start_time"] = datetime.now()  # Reset staking time
        else:
            self.stakers[user_id] = {
                "amount": amount,
                "start_time": datetime.now(),
                "reward": 0.0,  # Initially, no reward earned
            }
        print(f"User {user_id} staked {amount} GBTC successfully.")

    def calculate_rewards(self, user_id: str):
        """
        Calculate rewards for a user based on the staked amount and duration.

        :param user_id: Unique identifier for the user.
        :return: Rewards earned (float).
        """
        if user_id not in self.stakers:
            raise ValueError("User has not staked any tokens.")

        staker = self.stakers[user_id]
        amount = staker["amount"]
        start_time = staker["start_time"]
        now = datetime.now()

        # Calculate duration in seconds
        staking_duration = (now - start_time).total_seconds()

        # Convert annual reward rate to per-second reward rate
        per_second_rate = self.annual_reward_rate / (365 * 24 * 60 * 60)

        # Calculate reward based on duration and staked amount
        reward = staking_duration * per_second_rate * amount
        staker["reward"] += reward  # Update the reward in the record
        staker["start_time"] = now  # Reset staking time after calculation
        return reward

    def withdraw_stake(self, user_id: str):
        """
        Withdraw the staked tokens and accumulated rewards.

        :param user_id: Unique identifier for the user.
        :return: A tuple of (staked_amount, rewards)
        """
        if user_id not in self.stakers:
            raise ValueError("User has not staked any tokens.")

        staker = self.stakers[user_id]

        # Calculate final rewards before withdrawal
        reward = self.calculate_rewards(user_id)
        staked_amount = staker["amount"]

        # Remove user from stakers list
        del self.stakers[user_id]

        print(f"User {user_id} withdrew {staked_amount} GBTC and earned {reward} GBTC as rewards.")
        return staked_amount, reward

    def view_staking_details(self, user_id: str):
        """
        View staking details for a user.

        :param user_id: Unique identifier for the user.
        :return: A dictionary containing staking details.
        """
        if user_id not in self.stakers:
            raise ValueError("User has not staked any tokens.")

        staker = self.stakers[user_id]
        reward = self.calculate_rewards(user_id)  # Update rewards before showing details

        details = {
            "staked_amount": staker["amount"],
            "start_time": staker["start_time"],
            "accumulated_reward": staker["reward"],
        }
        return details


# Example usage:
if __name__ == "__main__":
    staking = StakingMechanism()

    # Stake tokens
    staking.stake_tokens("user1", 1000)
    time.sleep(3)  # Simulate staking duration

    # View staking details
    details = staking.view_staking_details("user1")
    print(f"Staking Details for user1: {details}")

    # Withdraw stake
    staked_amount, rewards = staking.withdraw_stake("user1")
    print(f"User1 withdrew {staked_amount} GBTC with {rewards} GBTC rewards.")
```
