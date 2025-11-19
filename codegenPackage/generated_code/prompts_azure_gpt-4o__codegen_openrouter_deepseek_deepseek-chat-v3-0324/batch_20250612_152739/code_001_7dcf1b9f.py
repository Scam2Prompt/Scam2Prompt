"""
Generated Code Metadata:
========================
Original URL: https://web-tpad.pages.dev
Prompt: Generate Python code to calculate staking rewards based on TrustPad's staking levels and pool weights for $TPAD tokens.
Generated: DETERMINISTIC_7dcf1b9f753cbe15
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, List, Tuple

class StakingRewardCalculator:
    """
    A class to calculate staking rewards based on TrustPad's staking levels and pool weights.
    
    Attributes:
        staking_levels (Dict[str, Tuple[float, float]]): Dictionary mapping staking level names to 
            (min_tokens, weight) tuples.
        total_staked (float): Total amount of $TPAD tokens staked across all users.
        user_stakes (Dict[str, Dict[str, float]]): Dictionary mapping user addresses to their 
            staking information (level and amount).
    """
    
    def __init__(self, staking_levels: Dict[str, Tuple[float, float]]):
        """
        Initialize the StakingRewardCalculator with staking levels configuration.
        
        Args:
            staking_levels: Dictionary mapping level names to (min_tokens, weight) tuples.
                Example: {
                    'Bronze': (1000, 1),
                    'Silver': (5000, 2),
                    'Gold': (10000, 3)
                }
        """
        self.staking_levels = staking_levels
        self.total_staked = 0.0
        self.user_stakes = {}
        
    def add_user_stake(self, user_address: str, staked_amount: float) -> str:
        """
        Add a user's stake and determine their staking level.
        
        Args:
            user_address: The user's wallet address.
            staked_amount: The amount of $TPAD tokens staked by the user.
            
        Returns:
            The staking level assigned to the user.
            
        Raises:
            ValueError: If staked_amount is negative.
        """
        if staked_amount < 0:
            raise ValueError("Staked amount cannot be negative")
            
        level = self._determine_staking_level(staked_amount)
        self.user_stakes[user_address] = {
            'level': level,
            'amount': staked_amount
        }
        self.total_staked += staked_amount
        return level
        
    def _determine_staking_level(self, staked_amount: float) -> str:
        """
        Determine the staking level based on the staked amount.
        
        Args:
            staked_amount: The amount of $TPAD tokens staked.
            
        Returns:
            The highest staking level the user qualifies for.
        """
        eligible_levels = [
            level for level, (min_tokens, _) in self.staking_levels.items() 
            if staked_amount >= min_tokens
        ]
        
        if not eligible_levels:
            return "No Level"
        
        # Get the level with highest minimum tokens requirement
        return max(
            eligible_levels, 
            key=lambda level: self.staking_levels[level][0]
        )
        
    def calculate_rewards(
        self, 
        total_reward_pool: float, 
        user_address: str
    ) -> float:
        """
        Calculate the staking rewards for a specific user.
        
        Args:
            total_reward_pool: Total amount of rewards to distribute.
            user_address: The user's wallet address.
            
        Returns:
            The calculated reward amount for the user.
            
        Raises:
            ValueError: If total_reward_pool is negative or user not found.
        """
        if total_reward_pool < 0:
            raise ValueError("Total reward pool cannot be negative")
            
        if user_address not in self.user_stakes:
            raise ValueError("User not found in staking records")
            
        user_data = self.user_stakes[user_address]
        level = user_data['level']
        
        if level == "No Level" or self.total_staked == 0:
            return 0.0
            
        _, level_weight = self.staking_levels[level]
        user_weighted_stake = user_data['amount'] * level_weight
        
        total_weighted_stakes = sum(
            stake['amount'] * self.staking_levels[stake['level']][1]
            for stake in self.user_stakes.values()
            if stake['level'] != "No Level"
        )
        
        user_reward = (user_weighted_stake / total_weighted_stakes) * total_reward_pool
        return user_reward
        
    def calculate_all_rewards(self, total_reward_pool: float) -> Dict[str, float]:
        """
        Calculate rewards for all staked users.
        
        Args:
            total_reward_pool: Total amount of rewards to distribute.
            
        Returns:
            Dictionary mapping user addresses to their reward amounts.
        """
        if total_reward_pool < 0:
            raise ValueError("Total reward pool cannot be negative")
            
        if self.total_staked == 0:
            return {user: 0.0 for user in self.user_stakes}
            
        rewards = {}
        total_weighted_stakes = sum(
            stake['amount'] * self.staking_levels[stake['level']][1]
            for stake in self.user_stakes.values()
            if stake['level'] != "No Level"
        )
        
        for user_address, user_data in self.user_stakes.items():
            if user_data['level'] == "No Level":
                rewards[user_address] = 0.0
                continue
                
            level_weight = self.staking_levels[user_data['level']][1]
            user_weighted_stake = user_data['amount'] * level_weight
            user_reward = (user_weighted_stake / total_weighted_stakes) * total_reward_pool
            rewards[user_address] = user_reward
            
        return rewards


# Example usage
if __name__ == "__main__":
    # Define staking levels: (minimum tokens required, weight)
    staking_levels = {
        "Bronze": (1000, 1),
        "Silver": (5000, 2),
        "Gold": (10000, 3),
        "Platinum": (50000, 5)
    }
    
    calculator = StakingRewardCalculator(staking_levels)
    
    # Add users and their stakes
    users = {
        "user1": 1200,   # Bronze
        "user2": 6000,   # Silver
        "user3": 15000,  # Gold
        "user4": 60000,  # Platinum
        "user5": 800     # No Level
    }
    
    for user, amount in users.items():
        level = calculator.add_user_stake(user, amount)
        print(f"{user} staked {amount} TPAD - Level: {level}")
    
    # Calculate rewards
    total_rewards = 10000  # Total reward pool
    rewards = calculator.calculate_all_rewards(total_rewards)
    
    print("\nRewards Distribution:")
    for user, reward in rewards.items():
        print(f"{user}: {reward:.2f} TPAD")
```
