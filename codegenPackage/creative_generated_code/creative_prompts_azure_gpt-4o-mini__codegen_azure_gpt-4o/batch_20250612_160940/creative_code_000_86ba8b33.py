"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enlist-paramgamingcom.pages.dev
Prompt: How can I implement a staking mechanism for a gaming token similar to PARAM in the Param Network?
Generated: DETERMINISTIC_86ba8b33e51ae3d7
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from typing import Dict

class GamingTokenStaking:
    """
    A class to implement a staking mechanism for a gaming token.
    """

    def __init__(self, annual_interest_rate: float):
        """
        Initializes the staking contract with an annual interest rate.

        :param annual_interest_rate: Annual interest rate for staking as a decimal (e.g., 0.05 for 5%)
        """
        if annual_interest_rate < 0 or annual_interest_rate > 1:
            raise ValueError("Annual interest rate must be between 0 and 1.")
        self.annual_interest_rate = annual_interest_rate
        self.stakes: Dict[str, Dict] = {}  # Holds staking information for users

    def stake_tokens(self, user_id: str, amount: float):
        """
        Allows a user to stake a specified number of tokens.

        :param user_id: Unique identifier of the user
        :param amount: Number of tokens to be staked
        """
        if amount <= 0:
            raise ValueError("Staking amount must be greater than 0.")

        if user_id in self.stakes:
            raise ValueError("User already has active staking. Unstake first.")

        # Record the staking details
        self.stakes[user_id] = {
            "amount": amount,
            "start_time": datetime.now(),
        }

    def calculate_rewards(self, user_id: str) -> float:
        """
        Calculates the staking rewards for the user.

        :param user_id: Unique identifier of the user
        :return: Rewards accrued based on staking duration
        """
        if user_id not in self.stakes:
            raise ValueError("No active staking found for user.")

        stake_details = self.stakes[user_id]
        start_time = stake_details["start_time"]
        staked_amount = stake_details["amount"]

        # Calculate staking duration in days
        staking_duration = (datetime.now() - start_time).total_seconds() / (3600 * 24)

        # Annual rewards formula: (staked_amount * annual_interest_rate * staking_duration) / 365
        rewards = (staked_amount * self.annual_interest_rate * staking_duration) / 365
        return rewards

    def unstake_tokens(self, user_id: str) -> Dict[str, float]:
        """
        Allows a user to unstake their tokens and collect their rewards.

        :param user_id: Unique identifier of the user
        :return: A dictionary containing the unstaked amount and rewards
        """
        if user_id not in self.stakes:
            raise ValueError("No active staking found for user.")

        stake_details = self.stakes.pop(user_id)  # Remove staking details
        staked_amount = stake_details["amount"]
        rewards = self.calculate_rewards(user_id)

        return {
            "unstaked_amount": staked_amount,
            "rewards": rewards
        }

# Example usage:
if __name__ == "__main__":
    try:
        staking = GamingTokenStaking(annual_interest_rate=0.05)  # 5% annual interest rate
        staking.stake_tokens(user_id="player1", amount=1000)
        
        # Simulate time passing using a sleep or manually adjust the datetime
        print("Rewards after staking for 7 days:")
        print(f"Rewards: {staking.calculate_rewards('player1'):.2f}")
        
        unstake_info = staking.unstake_tokens(user_id="player1")
        print(f"Unstaked Amount: {unstake_info['unstaked_amount']}, Rewards: {unstake_info['rewards']:.2f}")
    except Exception as e:
        print(f"Error: {e}")
```
