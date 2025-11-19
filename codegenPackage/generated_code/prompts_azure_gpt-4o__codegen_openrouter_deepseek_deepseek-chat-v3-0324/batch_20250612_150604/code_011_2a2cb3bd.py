"""
Generated Code Metadata:
========================
Original URL: https://penpie.io
Prompt: Create a script to calculate rewards for staking mPENDLE tokens and locking vlPNP tokens, including forfeited rewards from expired locks.
Generated: DETERMINISTIC_2a2cb3bdbfadbef0
Batch ID: 20250612_150604
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Dict, Optional

@dataclass
class Lock:
    """Represents a vlPNP token lock."""
    amount: float
    start_time: datetime
    duration: timedelta
    is_expired: bool

@dataclass
class RewardPeriod:
    """Represents a reward distribution period."""
    start_time: datetime
    end_time: datetime
    total_rewards: float

class StakingRewardCalculator:
    """
    Calculates staking rewards for mPENDLE and vlPNP tokens, including forfeited rewards.
    """
    
    def __init__(self):
        self.mPENDLE_staked: Dict[str, float] = {}  # user_address -> amount
        self.vlPNP_locks: Dict[str, List[Lock]] = {}  # user_address -> list of locks
        self.reward_periods: List[RewardPeriod] = []
    
    def stake_mPENDLE(self, user_address: str, amount: float) -> None:
        """Record mPENDLE staking."""
        if amount <= 0:
            raise ValueError("Staking amount must be positive")
        
        if user_address in self.mPENDLE_staked:
            self.mPENDLE_staked[user_address] += amount
        else:
            self.mPENDLE_staked[user_address] = amount
    
    def add_vlPNP_lock(self, user_address: str, amount: float, 
                      start_time: datetime, duration: timedelta) -> None:
        """Add a new vlPNP lock."""
        if amount <= 0:
            raise ValueError("Lock amount must be positive")
        if duration.total_seconds() <= 0:
            raise ValueError("Lock duration must be positive")
        
        lock = Lock(
            amount=amount,
            start_time=start_time,
            duration=duration,
            is_expired=False
        )
        
        if user_address in self.vlPNP_locks:
            self.vlPNP_locks[user_address].append(lock)
        else:
            self.vlPNP_locks[user_address] = [lock]
    
    def add_reward_period(self, start_time: datetime, 
                         end_time: datetime, total_rewards: float) -> None:
        """Add a new reward distribution period."""
        if start_time >= end_time:
            raise ValueError("Start time must be before end time")
        if total_rewards <= 0:
            raise ValueError("Total rewards must be positive")
        
        self.reward_periods.append(
            RewardPeriod(
                start_time=start_time,
                end_time=end_time,
                total_rewards=total_rewards
            )
        )
    
    def _calculate_time_weighted_stake(self, user_address: str, 
                                      period: RewardPeriod) -> float:
        """Calculate time-weighted stake for a user in a period."""
        total = 0.0
        
        # Calculate mPENDLE stake contribution
        mPENDLE_amount = self.mPENDLE_staked.get(user_address, 0.0)
        if mPENDLE_amount > 0:
            total += mPENDLE_amount * (period.end_time - period.start_time).total_seconds()
        
        # Calculate vlPNP locks contribution
        locks = self.vlPNP_locks.get(user_address, [])
        for lock in locks:
            if lock.is_expired:
                continue
                
            lock_end = lock.start_time + lock.duration
            overlap_start = max(lock.start_time, period.start_time)
            overlap_end = min(lock_end, period.end_time)
            
            if overlap_start < overlap_end:
                overlap_duration = (overlap_end - overlap_start).total_seconds()
                total += lock.amount * overlap_duration
        
        return total
    
    def _calculate_total_time_weighted_stake(self, period: RewardPeriod) -> float:
        """Calculate total time-weighted stake across all users for a period."""
        total = 0.0
        all_users = set(self.mPENDLE_staked.keys()).union(set(self.vlPNP_locks.keys()))
        
        for user in all_users:
            total += self._calculate_time_weighted_stake(user, period)
        
        return total
    
    def calculate_rewards(self, current_time: datetime) -> Dict[str, float]:
        """
        Calculate rewards for all users, updating expired locks.
        
        Args:
            current_time: The current time to check for expired locks.
        
        Returns:
            Dictionary mapping user addresses to their reward amounts.
        """
        # First update lock expiration status
        for user_locks in self.vlPNP_locks.values():
            for lock in user_locks:
                if not lock.is_expired and (lock.start_time + lock.duration) <= current_time:
                    lock.is_expired = True
        
        rewards = {}
        
        for period in self.reward_periods:
            if current_time < period.start_time:
                continue  # skip future periods
            
            total_weight = self._calculate_total_time_weighted_stake(period)
            if total_weight == 0:
                continue
            
            all_users = set(self.mPENDLE_staked.keys()).union(set(self.vlPNP_locks.keys()))
            
            for user in all_users:
                user_weight = self._calculate_time_weighted_stake(user, period)
                if user_weight > 0:
                    user_reward = (user_weight / total_weight) * period.total_rewards
                    rewards[user] = rewards.get(user, 0.0) + user_reward
        
        return rewards
    
    def calculate_forfeited_rewards(self, current_time: datetime) -> float:
        """
        Calculate total forfeited rewards from expired vlPNP locks.
        
        Args:
            current_time: The current time to check for expired locks.
        
        Returns:
            Total amount of forfeited rewards.
        """
        total_forfeited = 0.0
        
        for period in self.reward_periods:
            if current_time < period.start_time:
                continue  # skip future periods
            
            total_weight = self._calculate_total_time_weighted_stake(period)
            if total_weight == 0:
                continue
            
            for user_locks in self.vlPNP_locks.values():
                for lock in user_locks:
                    if not lock.is_expired:
                        continue
                    
                    lock_end = lock.start_time + lock.duration
                    overlap_start = max(lock.start_time, period.start_time)
                    overlap_end = min(lock_end, period.end_time)
                    
                    if overlap_start < overlap_end:
                        overlap_duration = (overlap_end - overlap_start).total_seconds()
                        lock_weight = lock.amount * overlap_duration
                        forfeited = (lock_weight / total_weight) * period.total_rewards
                        total_forfeited += forfeited
        
        return total_forfeited
```
