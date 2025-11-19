"""
Generated Code Metadata:
========================
Original URL: https://peaptoken.fun
Prompt: "Design a staking rewards program for the PEAP Token ecosystem, considering the 30% allocation for staking and rewards."
Generated: DETERMINISTIC_6b687f856b3ac35f
Batch ID: 20250622_212724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
"""
PEAP Token Staking Rewards Program
Implements a staking contract with rewards distribution from a 30% allocation pool.
"""

from dataclasses import dataclass
from typing import Dict, List
import time
from enum import Enum, auto

class StakingError(Exception):
    """Base class for staking-related exceptions."""
    pass

class InsufficientBalanceError(StakingError):
    """Raised when user doesn't have sufficient balance for staking/unstaking."""
    pass

class InvalidDurationError(StakingError):
    """Raised when staking duration is invalid."""
    pass

class StakeStatus(Enum):
    """Status of a stake."""
    ACTIVE = auto()
    COMPLETED = auto()
    WITHDRAWN = auto()

@dataclass
class Stake:
    """Represents a single staking position."""
    amount: float
    start_time: float
    duration: int  # in days
    status: StakeStatus
    last_claim_time: float
    claimed_rewards: float = 0.0

class PEAPStaking:
    """
    PEAP Token Staking Contract
    
    Attributes:
        total_staking_allocation: Total tokens allocated for staking rewards (30% of total supply)
        reward_rate: Annual percentage rate for staking rewards
        min_staking_duration: Minimum staking duration in days
        max_staking_duration: Maximum staking duration in days
    """
    
    def __init__(
        self,
        total_staking_allocation: float,
        reward_rate: float = 0.1,  # 10% APR by default
        min_staking_duration: int = 30,  # 30 days minimum
        max_staking_duration: int = 365  # 1 year maximum
    ):
        self.total_staking_allocation = total_staking_allocation
        self.remaining_rewards = total_staking_allocation
        self.reward_rate = reward_rate
        self.min_staking_duration = min_staking_duration
        self.max_staking_duration = max_staking_duration
        
        # Mapping from user address to their stakes
        self.user_stakes: Dict[str, List[Stake]] = {}
        
        # Total staked amount across all users
        self.total_staked = 0.0
        
    def stake(self, user: str, amount: float, duration: int) -> Stake:
        """
        Create a new stake for the user.
        
        Args:
            user: User address
            amount: Amount of tokens to stake
            duration: Staking duration in days
            
        Returns:
            The created Stake object
            
        Raises:
            InsufficientBalanceError: If user doesn't have enough tokens
            InvalidDurationError: If duration is outside allowed range
        """
        if amount <= 0:
            raise InsufficientBalanceError("Stake amount must be positive")
            
        if duration < self.min_staking_duration or duration > self.max_staking_duration:
            raise InvalidDurationError(
                f"Duration must be between {self.min_staking_duration} and {self.max_staking_duration} days"
            )
            
        current_time = time.time()
        new_stake = Stake(
            amount=amount,
            start_time=current_time,
            duration=duration,
            status=StakeStatus.ACTIVE,
            last_claim_time=current_time
        )
        
        if user not in self.user_stakes:
            self.user_stakes[user] = []
            
        self.user_stakes[user].append(new_stake)
        self.total_staked += amount
        
        return new_stake
    
    def calculate_rewards(self, stake: Stake, current_time: float = None) -> float:
        """
        Calculate accrued rewards for a stake.
        
        Args:
            stake: Stake to calculate rewards for
            current_time: Optional timestamp to use as current time
            
        Returns:
            Amount of rewards accrued
        """
        if current_time is None:
            current_time = time.time()
            
        if stake.status != StakeStatus.ACTIVE:
            return 0.0
            
        staking_end_time = stake.start_time + (stake.duration * 86400)  # Convert days to seconds
        effective_end_time = min(current_time, staking_end_time)
        
        staked_seconds = effective_end_time - stake.last_claim_time
        if staked_seconds <= 0:
            return 0.0
            
        # Calculate rewards based on APR
        annual_rewards = stake.amount * self.reward_rate
        rewards = (annual_rewards / 31536000) * staked_seconds  # 31536000 seconds in a year
        
        # Cap rewards at remaining allocation
        rewards = min(rewards, self.remaining_rewards)
        
        return rewards
    
    def claim_rewards(self, user: str, stake_index: int) -> float:
        """
        Claim rewards for a specific stake.
        
        Args:
            user: User address
            stake_index: Index of the stake in user's stake list
            
        Returns:
            Amount of rewards claimed
            
        Raises:
            IndexError: If stake_index is invalid
        """
        if user not in self.user_stakes or stake_index >= len(self.user_stakes[user]):
            raise IndexError("Invalid stake index")
            
        stake = self.user_stakes[user][stake_index]
        if stake.status != StakeStatus.ACTIVE:
            return 0.0
            
        rewards = self.calculate_rewards(stake)
        if rewards <= 0:
            return 0.0
            
        stake.claimed_rewards += rewards
        stake.last_claim_time = time.time()
        self.remaining_rewards -= rewards
        
        return rewards
    
    def unstake(self, user: str, stake_index: int) -> float:
        """
        Unstake tokens and claim any remaining rewards.
        
        Args:
            user: User address
            stake_index: Index of the stake in user's stake list
            
        Returns:
            Amount of tokens unstaked
            
        Raises:
            IndexError: If stake_index is invalid
        """
        if user not in self.user_stakes or stake_index >= len(self.user_stakes[user]):
            raise IndexError("Invalid stake index")
            
        stake = self.user_stakes[user][stake_index]
        
        # Claim any remaining rewards first
        self.claim_rewards(user, stake_index)
        
        # Mark stake as withdrawn
        stake.status = StakeStatus.WITHDRAWN
        self.total_staked -= stake.amount
        
        return stake.amount
    
    def get_user_stakes(self, user: str) -> List[Stake]:
        """
        Get all stakes for a user.
        
        Args:
            user: User address
            
        Returns:
            List of Stake objects for the user
        """
        return self.user_stakes.get(user, [])
    
    def get_total_staked(self) -> float:
        """
        Get total amount staked across all users.
        
        Returns:
            Total staked amount
        """
        return self.total_staked
    
    def get_remaining_rewards(self) -> float:
        """
        Get remaining rewards in the staking pool.
        
        Returns:
            Remaining rewards available
        """
        return self.remaining_rewards
```
