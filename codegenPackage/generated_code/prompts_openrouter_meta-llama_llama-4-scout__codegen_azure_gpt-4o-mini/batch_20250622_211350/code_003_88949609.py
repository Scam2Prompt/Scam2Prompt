"""
Generated Code Metadata:
========================
Original URL: https://bakedsolclaim.pages.dev
Prompt: Design a staking system for Solstorm's Quests feature, including reward calculation and distribution mechanisms.
Generated: DETERMINISTIC_889496095171551b
Batch ID: 20250622_211350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from typing import Dict, List

class StakingSystem:
    def __init__(self):
        # Initialize the staking system with an empty dictionary for user stakes
        self.user_stakes: Dict[str, float] = {}
        self.reward_rate: float = 0.1  # Reward rate per second
        self.staking_start_time: Dict[str, float] = {}

    def stake(self, user_id: str, amount: float) -> None:
        """
        Allows a user to stake a certain amount of tokens.
        
        :param user_id: The ID of the user staking tokens.
        :param amount: The amount of tokens to stake.
        :raises ValueError: If the amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        
        # Update the user's stake and record the staking start time
        self.user_stakes[user_id] = self.user_stakes.get(user_id, 0) + amount
        self.staking_start_time[user_id] = time.time()

    def unstake(self, user_id: str) -> float:
        """
        Allows a user to unstake their tokens and receive rewards.
        
        :param user_id: The ID of the user unstaking tokens.
        :return: The total amount of tokens returned to the user (staked + rewards).
        :raises ValueError: If the user has no stakes.
        """
        if user_id not in self.user_stakes or self.user_stakes[user_id] <= 0:
            raise ValueError("User has no stakes to unstake.")
        
        # Calculate rewards based on the time staked
        staked_amount = self.user_stakes[user_id]
        staking_duration = time.time() - self.staking_start_time[user_id]
        rewards = self.calculate_rewards(staked_amount, staking_duration)

        # Reset user's stake and return the total amount
        total_return = staked_amount + rewards
        del self.user_stakes[user_id]
        del self.staking_start_time[user_id]
        
        return total_return

    def calculate_rewards(self, amount: float, duration: float) -> float:
        """
        Calculate the rewards based on the staked amount and duration.
        
        :param amount: The amount of tokens staked.
        :param duration: The duration for which the tokens were staked (in seconds).
        :return: The calculated rewards.
        """
        return amount * self.reward_rate * duration

    def get_user_stake(self, user_id: str) -> float:
        """
        Retrieve the current stake of a user.
        
        :param user_id: The ID of the user.
        :return: The amount of tokens staked by the user.
        """
        return self.user_stakes.get(user_id, 0)

    def get_total_staked(self) -> float:
        """
        Get the total amount of tokens currently staked in the system.
        
        :return: The total amount of staked tokens.
        """
        return sum(self.user_stakes.values())

# Example usage
if __name__ == "__main__":
    staking_system = StakingSystem()
    
    # User stakes tokens
    staking_system.stake("user1", 100)
    time.sleep(2)  # Simulate time passing
    
    # User unstakes tokens and receives rewards
    total_return = staking_system.unstake("user1")
    print(f"Total returned to user1: {total_return:.2f} tokens")
```
