"""
Generated Code Metadata:
========================
Original URL: https://scottytheaidapp.pages.dev
Prompt: Design a staking pool system using a suitable programming language, ensuring that rewards are payable over 3 years and determined by the user's share of the pool.
Generated: DETERMINISTIC_f2c7701cfae24c84
Batch ID: 20250622_210914
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
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class Stake:
    user_id: str
    amount: float
    timestamp: datetime

class StakingPool:
    def __init__(self, total_rewards: float, reward_period_days: int = 365 * 3):
        """
        Initialize a staking pool with total rewards distributed over reward_period_days.
        
        Args:
            total_rewards: Total rewards to be distributed over the period
            reward_period_days: Duration of reward distribution in days (default: 3 years)
        """
        self.total_rewards = total_rewards
        self.reward_period = timedelta(days=reward_period_days)
        self.stakes: Dict[str, Stake] = {}
        self.total_staked = 0.0
        self.start_time = datetime.now()
    
    def stake(self, user_id: str, amount: float) -> None:
        """
        Add a user's stake to the pool.
        
        Args:
            user_id: Unique identifier for the user
            amount: Amount to stake
        """
        if user_id in self.stakes:
            raise ValueError("User already has an active stake")
        if amount <= 0:
            raise ValueError("Stake amount must be positive")
            
        self.stakes[user_id] = Stake(user_id, amount, datetime.now())
        self.total_staked += amount
    
    def unstake(self, user_id: str) -> float:
        """
        Remove a user's stake and return their earned rewards.
        
        Args:
            user_id: Unique identifier for the user
            
        Returns:
            Total rewards earned by the user
        """
        if user_id not in self.stakes:
            raise ValueError("User has no active stake")
            
        stake = self.stakes.pop(user_id)
        rewards = self.calculate_rewards(user_id)
        self.total_staked -= stake.amount
        return rewards
    
    def calculate_rewards(self, user_id: str) -> float:
        """
        Calculate rewards for a user based on their stake and time elapsed.
        
        Args:
            user_id: Unique identifier for the user
            
        Returns:
            Amount of rewards earned
        """
        if user_id not in self.stakes:
            raise ValueError("User has no active stake")
            
        stake = self.stakes[user_id]
        current_time = datetime.now()
        time_elapsed = current_time - stake.timestamp
        
        if time_elapsed.total_seconds() <= 0:
            return 0.0
        
        # Calculate share of pool at time of staking
        if self.total_staked == 0:
            share = 0.0
        else:
            share = stake.amount / self.total_staked
        
        # Calculate proportion of reward period elapsed
        period_elapsed = min(time_elapsed, self.reward_period)
        reward_period_seconds = self.reward_period.total_seconds()
        period_ratio = period_elapsed.total_seconds() / reward_period_seconds
        
        return share * self.total_rewards * period_ratio
    
    def get_estimated_apy(self) -> float:
        """
        Calculate the estimated annual percentage yield for the pool.
        
        Returns:
            Estimated APY as a decimal (e.g., 0.1 for 10%)
        """
        if self.total_staked == 0:
            return 0.0
        return (self.total_rewards / self.total_staked) * (365 / self.reward_period.days)
    
    def get_user_stake(self, user_id: str) -> float:
        """
        Get a user's current stake amount.
        
        Args:
            user_id: Unique identifier for the user
            
        Returns:
            Current stake amount
        """
        if user_id not in self.stakes:
            raise ValueError("User has no active stake")
        return self.stakes[user_id].amount
    
    def get_pool_info(self) -> Dict:
        """
        Get current pool information.
        
        Returns:
            Dictionary containing pool metrics
        """
        return {
            "total_staked": self.total_staked,
            "total_rewards": self.total_rewards,
            "start_time": self.start_time,
            "end_time": self.start_time + self.reward_period,
            "estimated_apy": self.get_estimated_apy(),
            "active_stakers": len(self.stakes)
        }
```
