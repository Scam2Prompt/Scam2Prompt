"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://resolverpanel-dapp.pages.dev
Prompt: Provide a solution for optimizing APR activation in staking systems, inspired by the Web3 Resolver Panel's staking services.
Generated: DETERMINISTIC_28b89ec7c33c39ae
Batch ID: 20250612_150448
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from typing import List, Dict, Union

class StakingSystem:
    """
    A class to manage APR activation in staking systems, inspired by Web3 Resolver Panel's staking services.
    """

    def __init__(self):
        # Stores user stake and their activation times
        self.user_stakes: Dict[str, Dict[str, Union[float, int]]] = {}
        # Configurable APR tiers based on staking duration
        self.apr_tiers: List[Dict[str, Union[int, float]]] = [
            {"duration": 30, "apr": 5.0},  # 5% APR for 30 days
            {"duration": 90, "apr": 7.5},  # 7.5% APR for 90 days
            {"duration": 180, "apr": 10.0}, # 10% APR for 180 days
        ]

    def stake(self, user_id: str, amount: float):
        """
        Allows a user to stake a specific amount. Initializes their staking data.
        
        :param user_id: Unique identifier for the user
        :param amount: The amount being staked
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        
        # Record stake and current timestamp
        self.user_stakes[user_id] = {
            "amount": amount,
            "timestamp": int(time.time())  # Current time in seconds
        }
        print(f"User {user_id} has staked {amount} units.")

    def calculate_rewards(self, user_id: str) -> float:
        """
        Calculates the rewards for a user's stake based on the APR tiers.
        
        :param user_id: Unique identifier for the user
        :return: The calculated reward amount
        """
        if user_id not in self.user_stakes:
            raise ValueError("User has no active stake.")

        user_data = self.user_stakes[user_id]
        current_time = int(time.time())
        staking_duration = (current_time - user_data["timestamp"]) // (24 * 3600)  # Convert seconds to days
        
        # Determine applicable APR based on staking duration
        applicable_apr = 0.0
        for tier in self.apr_tiers:
            if staking_duration >= tier["duration"]:
                applicable_apr = tier["apr"]

        # Calculate reward
        annual_reward = (user_data["amount"] * applicable_apr) / 100
        daily_reward = annual_reward / 365.0  # Daily reward
        total_reward = daily_reward * staking_duration
        
        return total_reward

    def withdraw_rewards(self, user_id: str) -> float:
        """
        Allows a user to withdraw their staking rewards. Resets the staking timer.
        
        :param user_id: Unique identifier for the user
        :return: The total rewards withdrawn
        """
        if user_id not in self.user_stakes:
            raise ValueError("User has no active stake.")

        # Calculate rewards
        rewards = self.calculate_rewards(user_id)
        
        # Reset stake timer for the user
        self.user_stakes[user_id]["timestamp"] = int(time.time())
        print(f"User {user_id} has withdrawn {rewards:.2f} units in rewards.")
        
        return rewards

    def display_user_stake(self, user_id: str):
        """
        Displays the staking details for a specific user.
        
        :param user_id: Unique identifier for the user
        """
        if user_id not in self.user_stakes:
            print(f"No active stake found for user {user_id}.")
            return
        
        user_data = self.user_stakes[user_id]
        print(f"User {user_id} has staked {user_data['amount']} units since {time.ctime(user_data['timestamp'])}.")

# Example Usage
if __name__ == "__main__":
    staking_system = StakingSystem()
    
    # User stakes some amount
    staking_system.stake("user123", 1000.0)
    time.sleep(2)  # Simulate some time passing
    
    # Display user stake info
    staking_system.display_user_stake("user123")
    
    # Calculate rewards after some time
    rewards = staking_system.calculate_rewards("user123")
    print(f"Calculated rewards for user123: {rewards:.2f} units.")
    
    # User withdraws rewards
    staking_system.withdraw_rewards("user123")
```
