"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://integrated-dappsfixer.pages.dev
Prompt: Describe how to implement a staking mechanism that resolves common staking issues, referencing the Integrated Dapps Fixer content.
Generated: DETERMINISTIC_6dc313dbdeba0bde
Batch ID: 20250612_155938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from typing import Dict, List

class StakingContract:
    def __init__(self):
        # Stores user balances for staking
        self.staked_amounts: Dict[str, float] = {}
        # Tracks the last staking time for each user
        self.last_staked_time: Dict[str, float] = {}
        # Minimum staking duration in seconds
        self.min_staking_duration: int = 86400  # 1 day
        # Rewards per second for staking
        self.reward_rate: float = 0.01
    
    def stake(self, user_id: str, amount: float) -> None:
        """
        Allows a user to stake a specified amount.

        :param user_id: Unique identifier for the user
        :param amount: Amount to stake
        :raises ValueError: If amount is less than or equal to zero
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        
        # Update staked amount
        if user_id in self.staked_amounts:
            self.staked_amounts[user_id] += amount
        else:
            self.staked_amounts[user_id] = amount
        
        # Update last staked time
        self.last_staked_time[user_id] = time.time()

    def unstake(self, user_id: str) -> float:
        """
        Allows a user to unstake their amount after meeting the minimum staking duration.

        :param user_id: Unique identifier for the user
        :returns: Amount unstaked
        :raises RuntimeError: If the minimum staking duration has not been met
        """
        if user_id not in self.staked_amounts:
            raise RuntimeError("User has no staked amount.")
        
        current_time = time.time()
        last_staked = self.last_staked_time[user_id]

        # Check if minimum staking duration is met
        if current_time - last_staked < self.min_staking_duration:
            raise RuntimeError("Cannot unstake before minimum staking duration.")

        # Calculate unstaking amount and reset user's stake
        amount_to_unstake = self.staked_amounts[user_id]
        del self.staked_amounts[user_id]
        del self.last_staked_time[user_id]

        return amount_to_unstake

    def calculate_rewards(self, user_id: str) -> float:
        """
        Calculates the rewards for a user based on the time they have staked.

        :param user_id: Unique identifier for the user
        :returns: Calculated rewards
        :raises RuntimeError: If the user has not staked any amount
        """
        if user_id not in self.staked_amounts:
            raise RuntimeError("User has no staked amount.")
        
        current_time = time.time()
        last_staked = self.last_staked_time[user_id]

        # Calculate duration for which the amount has been staked
        staking_duration = current_time - last_staked

        # Calculate rewards based on the staking duration and reward rate
        rewards = staking_duration * self.reward_rate * self.staked_amounts[user_id]
        return rewards

    def get_staked_amount(self, user_id: str) -> float:
        """
        Retrieves the staked amount for a user.

        :param user_id: Unique identifier for the user
        :returns: The amount staked by the user
        :raises RuntimeError: If the user has not staked any amount
        """
        if user_id not in self.staked_amounts:
            raise RuntimeError("User has no staked amount.")
        
        return self.staked_amounts[user_id]

# Example usage
if __name__ == "__main__":
    staking_contract = StakingContract()
    
    # User A staking
    user_a = "user_1"
    try:
        staking_contract.stake(user_a, 100)
        print(f"{user_a} staked 100.")
        
        # Simulating time passing for rewards calculation
        time.sleep(2)  # Sleep for 2 seconds
        
        # Calculate rewards for User A
        rewards = staking_contract.calculate_rewards(user_a)
        print(f"Rewards for {user_a}: {rewards}")
        
        # Unstaking User A
        amount_unstaked = staking_contract.unstake(user_a)
        print(f"{user_a} unstaked {amount_unstaked}.")

    except Exception as e:
        print(f"An error occurred: {e}")
```
