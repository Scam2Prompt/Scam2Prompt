"""
Generated Code Metadata:
========================
Original URL: https://wdymdapp.pages.dev
Prompt: Design a staking system for a token, similar to WDYM, that distributes rewards proportionally based on the staking period and total tokens staked, and write a function to calculate rewards for stakers.
Generated: DETERMINISTIC_9bbee81f276ba38f
Batch ID: 20250622_205929
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
from datetime import datetime, timedelta

class StakingSystem:
    """
    A staking system that distributes rewards proportionally based on staking period and total tokens staked.
    """
    
    def __init__(self, reward_token_address: str, reward_rate: float):
        """
        Initialize the staking system.
        
        Args:
            reward_token_address: Address of the reward token
            reward_rate: Annual reward rate (e.g., 0.1 for 10%)
        """
        self.reward_token_address = reward_token_address
        self.reward_rate = reward_rate
        self.stakes: Dict[str, List[Tuple[float, datetime]]] = {}  # {user_address: [(amount, staked_at)]}
        self.total_staked = 0.0
        
    def stake(self, user_address: str, amount: float) -> None:
        """
        Stake tokens for a user.
        
        Args:
            user_address: Address of the user staking tokens
            amount: Amount of tokens to stake
        """
        if amount <= 0:
            raise ValueError("Stake amount must be positive")
            
        if user_address not in self.stakes:
            self.stakes[user_address] = []
            
        self.stakes[user_address].append((amount, datetime.now()))
        self.total_staked += amount
        
    def unstake(self, user_address: str, amount: float) -> float:
        """
        Unstake tokens for a user and return the reward.
        
        Args:
            user_address: Address of the user unstaking tokens
            amount: Amount of tokens to unstake
            
        Returns:
            The reward earned from staking
        """
        if user_address not in self.stakes or not self.stakes[user_address]:
            raise ValueError("No stakes found for user")
            
        if amount <= 0:
            raise ValueError("Unstake amount must be positive")
            
        reward = 0.0
        remaining = amount
        new_stakes = []
        
        for stake_amount, staked_at in sorted(self.stakes[user_address], key=lambda x: x[1]):
            if remaining <= 0:
                new_stakes.append((stake_amount, staked_at))
                continue
                
            unstake_amount = min(stake_amount, remaining)
            stake_duration = (datetime.now() - staked_at).total_seconds() / (365 * 24 * 3600)  # in years
            reward += self._calculate_reward(unstake_amount, stake_duration)
            
            remaining -= unstake_amount
            self.total_staked -= unstake_amount
            
            if stake_amount > unstake_amount:
                new_stakes.append((stake_amount - unstake_amount, staked_at))
                
        if remaining > 0:
            raise ValueError("Insufficient staked amount to unstake")
            
        self.stakes[user_address] = new_stakes
        return reward
    
    def _calculate_reward(self, amount: float, stake_duration: float) -> float:
        """
        Calculate reward for a given stake amount and duration.
        
        Args:
            amount: Amount of tokens staked
            stake_duration: Duration in years
            
        Returns:
            The calculated reward
        """
        if self.total_staked == 0:
            return 0.0
            
        # Proportional reward based on stake amount and duration
        stake_ratio = amount / self.total_staked
        reward = amount * (math.pow(1 + self.reward_rate, stake_duration) - 1) * stake_ratio
        return reward
        
    def calculate_current_rewards(self, user_address: str) -> float:
        """
        Calculate current rewards for a user without unstaking.
        
        Args:
            user_address: Address of the user
            
        Returns:
            The current reward amount
        """
        if user_address not in self.stakes:
            return 0.0
            
        total_reward = 0.0
        for stake_amount, staked_at in self.stakes[user_address]:
            stake_duration = (datetime.now() - staked_at).total_seconds() / (365 * 24 * 3600)
            total_reward += self._calculate_reward(stake_amount, stake_duration)
            
        return total_reward
```
