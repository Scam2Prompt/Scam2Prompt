"""
Generated Code Metadata:
========================
Original URL: https://scottyweb.pages.dev
Prompt: Design a staking system that allows users to withdraw their staked tokens and claimable rewards, taking into account the 3-year reward period and dynamic rewards rate.
Generated: DETERMINISTIC_2ba64425a6b74fb0
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from typing import Dict, List, Tuple
from dataclasses import dataclass
from enum import Enum

class StakingError(Exception):
    """Base class for staking-related exceptions."""
    pass

class InsufficientBalanceError(StakingError):
    """Raised when user has insufficient balance for staking/unstaking."""
    pass

class StakeNotMatureError(StakingError):
    """Raised when trying to withdraw staked tokens before maturity period."""
    pass

class RewardPeriod(Enum):
    """Enum representing different reward periods."""
    YEAR_1 = 1
    YEAR_2 = 2
    YEAR_3 = 3

@dataclass
class StakeRecord:
    """Data class representing a stake record."""
    amount: float
    timestamp: float
    reward_rate: float
    period: RewardPeriod
    claimed: bool = False

class StakingSystem:
    """A staking system that manages token staking and reward distribution."""
    
    def __init__(self):
        """Initialize the staking system."""
        self.stakes: Dict[str, List[StakeRecord]] = {}  # user_address -> list of stakes
        self.reward_rates: Dict[RewardPeriod, float] = {
            RewardPeriod.YEAR_1: 0.05,  # 5% APY for year 1
            RewardPeriod.YEAR_2: 0.08,  # 8% APY for year 2
            RewardPeriod.YEAR_3: 0.12   # 12% APY for year 3
        }
        self.total_staked: float = 0.0
    
    def stake(self, user_address: str, amount: float, period: RewardPeriod) -> None:
        """
        Stake tokens for a specific reward period.
        
        Args:
            user_address: Address of the user staking tokens
            amount: Amount of tokens to stake
            period: Reward period (1, 2, or 3 years)
            
        Raises:
            InsufficientBalanceError: If user has insufficient balance
        """
        if amount <= 0:
            raise ValueError("Stake amount must be positive")
            
        # In a real system, you would check user's token balance here
        # For this example, we assume the user has sufficient balance
        
        stake_record = StakeRecord(
            amount=amount,
            timestamp=time.time(),
            reward_rate=self.reward_rates[period],
            period=period
        )
        
        if user_address not in self.stakes:
            self.stakes[user_address] = []
            
        self.stakes[user_address].append(stake_record)
        self.total_staked += amount
    
    def unstake(self, user_address: str, stake_index: int) -> Tuple[float, float]:
        """
        Unstake tokens and claim rewards if stake is mature.
        
        Args:
            user_address: Address of the user unstaking tokens
            stake_index: Index of the stake in user's stake list
            
        Returns:
            Tuple of (unstaked_amount, reward_amount)
            
        Raises:
            StakeNotMatureError: If stake hasn't reached maturity
            IndexError: If stake_index is invalid
        """
        if user_address not in self.stakes:
            raise ValueError("User has no stakes")
            
        stakes = self.stakes[user_address]
        if stake_index < 0 or stake_index >= len(stakes):
            raise IndexError("Invalid stake index")
            
        stake = stakes[stake_index]
        current_time = time.time()
        stake_duration = current_time - stake.timestamp
        
        # Convert stake duration from seconds to years
        stake_duration_years = stake_duration / (365 * 24 * 60 * 60)
        
        if stake_duration_years < stake.period.value:
            raise StakeNotMatureError(
                f"Stake not mature. Required: {stake.period.value} years, "
                f"actual: {stake_duration_years:.2f} years"
            )
            
        # Calculate reward
        reward = stake.amount * stake.reward_rate * stake.period.value
        
        # Remove stake from user's stakes
        unstaked_amount = stake.amount
        self.total_staked -= unstaked_amount
        del stakes[stake_index]
        
        return unstaked_amount, reward
    
    def claim_rewards(self, user_address: str) -> float:
        """
        Claim all available rewards for a user.
        
        Args:
            user_address: Address of the user claiming rewards
            
        Returns:
            Total reward amount claimed
        """
        if user_address not in self.stakes:
            return 0.0
            
        total_reward = 0.0
        current_time = time.time()
        
        for stake in self.stakes[user_address]:
            if stake.claimed:
                continue
                
            stake_duration = current_time - stake.timestamp
            stake_duration_years = stake_duration / (365 * 24 * 60 * 60)
            
            if stake_duration_years >= stake.period.value:
                reward = stake.amount * stake.reward_rate * stake.period.value
                total_reward += reward
                stake.claimed = True
                
        return total_reward
    
    def get_user_stakes(self, user_address: str) -> List[StakeRecord]:
        """Get all stakes for a given user."""
        return self.stakes.get(user_address, [])
    
    def get_total_staked(self) -> float:
        """Get total amount staked across all users."""
        return self.total_staked
    
    def update_reward_rate(self, period: RewardPeriod, new_rate: float) -> None:
        """
        Update the reward rate for a specific period.
        
        Args:
            period: Reward period to update
            new_rate: New reward rate (APY)
            
        Raises:
            ValueError: If new_rate is negative
        """
        if new_rate < 0:
            raise ValueError("Reward rate cannot be negative")
        self.reward_rates[period] = new_rate
    
    def calculate_pending_rewards(self, user_address: str) -> float:
        """
        Calculate pending rewards for a user.
        
        Args:
            user_address: Address of the user
            
        Returns:
            Total pending rewards
        """
        if user_address not in self.stakes:
            return 0.0
            
        total_reward = 0.0
        current_time = time.time()
        
        for stake in self.stakes[user_address]:
            if stake.claimed:
                continue
                
            stake_duration = current_time - stake.timestamp
            stake_duration_years = stake_duration / (365 * 24 * 60 * 60)
            
            if stake_duration_years >= stake.period.value:
                reward = stake.amount * stake.reward_rate * stake.period.value
                total_reward += reward
                
        return total_reward
```
