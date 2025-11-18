"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallstreetpepelive.com
Prompt: Generate code to implement a staking mechanism for WEPE tokens, referencing the staking features described on the Wall Street Pepe website.
Generated: DETERMINISTIC_0b16a999fc83c1f3
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# staking_mechanism.py

import time
from typing import Dict


class StakingMechanism:
    """
    Implements a staking mechanism for WEPE tokens.
    Allows users to stake tokens and earn rewards based on the duration of staking.
    """

    def __init__(self, reward_rate: float):
        """
        Initializes the staking mechanism.

        :param reward_rate: The reward rate per second (e.g., 0.0001 WEPE tokens per second).
        """
        self.reward_rate = reward_rate
        self.stakes = {}  # Dictionary to store user stakes. Format: {user_id: {'amount': float, 'start_time': int}}

    def stake_tokens(self, user_id: str, amount: float) -> None:
        """
        Allows a user to stake WEPE tokens.

        :param user_id: The unique identifier of the user.
        :param amount: The number of WEPE tokens to stake.
        :raises ValueError: If the staking amount is invalid.
        """
        if amount <= 0:
            raise ValueError("Staking amount must be greater than zero.")

        # Check if the user has an active stake
        if user_id in self.stakes:
            raise ValueError("User already has an active stake. Withdraw tokens before staking again.")

        # Record staking details
        self.stakes[user_id] = {
            'amount': amount,
            'start_time': int(time.time())
        }

    def calculate_rewards(self, user_id: str) -> float:
        """
        Calculates the staking rewards for a user based on the duration of staking.

        :param user_id: The unique identifier of the user.
        :return: The earned rewards as a float.
        :raises KeyError: If the user does not have an active stake.
        """
        if user_id not in self.stakes:
            raise KeyError("User does not have an active stake.")

        stake = self.stakes[user_id]
        duration = int(time.time()) - stake['start_time']  # Calculate staking duration in seconds
        rewards = stake['amount'] * self.reward_rate * duration  # Calculate rewards
        return rewards

    def withdraw_tokens(self, user_id: str) -> Dict[str, float]:
        """
        Allows a user to withdraw their staked tokens and earned rewards.

        :param user_id: The unique identifier of the user.
        :return: A dictionary containing the withdrawn tokens and rewards.
        :raises KeyError: If the user does not have an active stake.
        """
        if user_id not in self.stakes:
            raise KeyError("User does not have an active stake.")

        # Calculate rewards and return the full amount
        stake = self.stakes.pop(user_id)
        rewards = self.calculate_rewards(user_id)
        withdrawal_info = {
            'staked_tokens': stake['amount'],
            'rewards': rewards
        }
        return withdrawal_info

    def get_active_stakes(self) -> Dict[str, Dict[str, float]]:
        """
        Returns a summary of all active stakes.

        :return: A dictionary containing active stakes for all users.
        Format: {user_id: {'amount': float, 'start_time': int}}
        """
        return self.stakes


# Example usage (if needed for testing purposes):
if __name__ == "__main__":
    staking = StakingMechanism(reward_rate=0.0001)  # Initialize with a reward rate
    try:
        staking.stake_tokens("user1", 100)  # User stakes 100 WEPE tokens
        time.sleep(5)  # Simulate staking duration of 5 seconds
        rewards = staking.calculate_rewards("user1")  # Calculate user rewards
        print(f"Rewards earned by user1: {rewards:.6f} WEPE tokens")
        withdrawal = staking.withdraw_tokens("user1")  # Withdraw staked tokens and rewards
        print(f"Withdrawal info: {withdrawal}")
    except Exception as e:
        print(f"Error: {e}")
```
