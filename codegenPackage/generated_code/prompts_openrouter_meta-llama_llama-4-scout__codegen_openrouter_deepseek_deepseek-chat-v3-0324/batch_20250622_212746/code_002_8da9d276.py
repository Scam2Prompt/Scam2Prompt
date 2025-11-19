"""
Generated Code Metadata:
========================
Original URL: https://shaddow.co
Prompt: "Generate a code example for calculating incentives and rebases on Shadow Exchange using their x(3,3) incentives mechanism."
Generated: DETERMINISTIC_8da9d27623f6b527
Batch ID: 20250622_212746
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
from dataclasses import dataclass

@dataclass
class UserStake:
    """Represents a user's stake in the Shadow Exchange."""
    amount: float
    staked_time: int  # Unix timestamp

@dataclass
class Epoch:
    """Represents an epoch in the Shadow Exchange."""
    start_time: int  # Unix timestamp
    end_time: int    # Unix timestamp
    total_staked: float
    reward_per_share: float = 0.0

class ShadowExchange:
    """Implements the x(3,3) incentives mechanism for Shadow Exchange."""
    
    def __init__(self):
        self.users: Dict[str, UserStake] = {}  # address -> UserStake
        self.epochs: List[Epoch] = []
        self.current_epoch: Epoch = None
        self.total_staked: float = 0.0
        self.last_rebase_time: int = 0
        self.rebase_interval: int = 8 * 60 * 60  # 8 hours in seconds
        
    def start_new_epoch(self, timestamp: int) -> None:
        """Initialize a new epoch with the given timestamp."""
        if self.current_epoch:
            self.epochs.append(self.current_epoch)
        
        self.current_epoch = Epoch(
            start_time=timestamp,
            end_time=timestamp + self.rebase_interval,
            total_staked=self.total_staked
        )
    
    def stake(self, user_address: str, amount: float, timestamp: int) -> None:
        """Stake tokens for a user."""
        if amount <= 0:
            raise ValueError("Stake amount must be positive")
            
        if timestamp < self.last_rebase_time:
            raise ValueError("Timestamp cannot be before last rebase")
            
        # Ensure we're in a valid epoch
        if not self.current_epoch or timestamp >= self.current_epoch.end_time:
            self.start_new_epoch(timestamp)
            
        if user_address in self.users:
            self.users[user_address].amount += amount
        else:
            self.users[user_address] = UserStake(amount=amount, staked_time=timestamp)
            
        self.total_staked += amount
        self.current_epoch.total_staked += amount
    
    def unstake(self, user_address: str, amount: float, timestamp: int) -> None:
        """Unstake tokens for a user."""
        if amount <= 0:
            raise ValueError("Unstake amount must be positive")
            
        if user_address not in self.users:
            raise ValueError("User has no stake")
            
        if self.users[user_address].amount < amount:
            raise ValueError("Cannot unstake more than staked amount")
            
        if timestamp < self.last_rebase_time:
            raise ValueError("Timestamp cannot be before last rebase")
            
        # Ensure we're in a valid epoch
        if not self.current_epoch or timestamp >= self.current_epoch.end_time:
            self.start_new_epoch(timestamp)
            
        self.users[user_address].amount -= amount
        self.total_staked -= amount
        self.current_epoch.total_staked -= amount
        
        if self.users[user_address].amount == 0:
            del self.users[user_address]
    
    def calculate_rebase(self, timestamp: int) -> Tuple[float, float]:
        """
        Calculate rebase rewards based on x(3,3) mechanism.
        Returns (rebase_amount, new_total_staked)
        """
        if timestamp < self.last_rebase_time:
            raise ValueError("Cannot rebase before last rebase time")
            
        if not self.current_epoch or timestamp >= self.current_epoch.end_time:
            self.start_new_epoch(timestamp)
            
        time_elapsed = timestamp - self.last_rebase_time
        if time_elapsed <= 0:
            return 0.0, self.total_staked
            
        # x(3,3) mechanism: rebase rate depends on staking participation
        staking_ratio = self.total_staked / (self.total_staked + 1)  # Avoid division by zero
        rebase_rate = staking_ratio * 0.01  # Example: 1% max rebase
        
        # Calculate rebase amount
        rebase_amount = self.total_staked * rebase_rate * (time_elapsed / self.rebase_interval)
        
        # Update tracking variables
        new_total_staked = self.total_staked + rebase_amount
        self.last_rebase_time = timestamp
        
        return rebase_amount, new_total_staked
    
    def distribute_rewards(self, reward_amount: float, timestamp: int) -> None:
        """Distribute rewards to stakers proportionally."""
        if reward_amount <= 0:
            raise ValueError("Reward amount must be positive")
            
        if self.total_staked == 0:
            return
            
        # Update current epoch's reward per share
        reward_per_share = reward_amount / self.total_staked
        self.current_epoch.reward_per_share += reward_per_share
    
    def calculate_user_rewards(self, user_address: str) -> float:
        """Calculate pending rewards for a user."""
        if user_address not in self.users:
            return 0.0
            
        user_stake = self.users[user_address]
        rewards = 0.0
        
        for epoch in self.epochs:
            if user_stake.staked_time > epoch.end_time:
                continue
                
            if epoch.total_staked > 0:
                rewards += user_stake.amount * epoch.reward_per_share
                
        return rewards
    
    def claim_rewards(self, user_address: str) -> float:
        """Claim rewards for a user and reset their reward counter."""
        rewards = self.calculate_user_rewards(user_address)
        
        # Reset rewards by updating staked time to now
        if user_address in self.users:
            self.users[user_address].staked_time = self.last_rebase_time
            
        return rewards
```
