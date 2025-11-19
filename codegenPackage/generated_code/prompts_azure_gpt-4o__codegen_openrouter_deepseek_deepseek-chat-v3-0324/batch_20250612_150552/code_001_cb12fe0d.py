"""
Generated Code Metadata:
========================
Original URL: https://app-everdome-staking.pages.dev
Prompt: Generate code to calculate daily staking rewards for DOME tokens based on the Everdome staking protocol, considering a lock period of 1-52 weeks.
Generated: DETERMINISTIC_cb12fe0d66cf54da
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from datetime import datetime, timedelta
from typing import Optional, Tuple

class StakingRewardCalculator:
    """
    Calculates daily staking rewards for DOME tokens based on the Everdome staking protocol.
    
    Attributes:
        BASE_APY (float): Base annual percentage yield (1%)
        BONUS_APY_PER_WEEK (float): Additional APY per week locked (0.5%)
        MAX_LOCK_WEEKS (int): Maximum lock period in weeks (52)
        MIN_LOCK_WEEKS (int): Minimum lock period in weeks (1)
        DAYS_IN_YEAR (int): Number of days in a year (365)
    """
    
    BASE_APY = 0.01  # 1%
    BONUS_APY_PER_WEEK = 0.005  # 0.5%
    MAX_LOCK_WEEKS = 52
    MIN_LOCK_WEEKS = 1
    DAYS_IN_YEAR = 365

    @classmethod
    def calculate_daily_rewards(
        cls,
        amount: float,
        lock_weeks: int,
        current_date: Optional[datetime] = None
    ) -> Tuple[float, datetime, datetime]:
        """
        Calculate daily staking rewards for a given amount and lock period.
        
        Args:
            amount: Amount of DOME tokens to stake
            lock_weeks: Number of weeks to lock tokens (1-52)
            current_date: Optional date to use as start date (defaults to now)
            
        Returns:
            Tuple containing:
                - daily_reward: Daily reward amount
                - start_date: Staking start date
                - end_date: Staking end date
                
        Raises:
            ValueError: If lock_weeks is outside valid range or amount is negative
        """
        if not cls.MIN_LOCK_WEEKS <= lock_weeks <= cls.MAX_LOCK_WEEKS:
            raise ValueError(
                f"Lock period must be between {cls.MIN_LOCK_WEEKS} and {cls.MAX_LOCK_WEEKS} weeks"
            )
        
        if amount < 0:
            raise ValueError("Staking amount cannot be negative")
            
        current_date = current_date or datetime.now()
        end_date = current_date + timedelta(weeks=lock_weeks)
        
        total_apy = cls.BASE_APY + (cls.BONUS_APY_PER_WEEK * lock_weeks)
        daily_rate = total_apy / cls.DAYS_IN_YEAR
        daily_reward = amount * daily_rate
        
        return daily_reward, current_date, end_date

    @classmethod
    def calculate_total_rewards(
        cls,
        amount: float,
        lock_weeks: int,
        current_date: Optional[datetime] = None
    ) -> Tuple[float, datetime, datetime]:
        """
        Calculate total staking rewards for the entire lock period.
        
        Args:
            amount: Amount of DOME tokens to stake
            lock_weeks: Number of weeks to lock tokens (1-52)
            current_date: Optional date to use as start date (defaults to now)
            
        Returns:
            Tuple containing:
                - total_reward: Total reward amount
                - start_date: Staking start date
                - end_date: Staking end date
        """
        daily_reward, start_date, end_date = cls.calculate_daily_rewards(
            amount, lock_weeks, current_date
        )
        days_staked = (end_date - start_date).days
        total_reward = daily_reward * days_staked
        
        return total_reward, start_date, end_date

    @classmethod
    def calculate_remaining_rewards(
        cls,
        amount: float,
        lock_weeks: int,
        start_date: datetime,
        current_date: Optional[datetime] = None
    ) -> Tuple[float, float, datetime]:
        """
        Calculate remaining rewards for an ongoing stake.
        
        Args:
            amount: Original staked amount
            lock_weeks: Original lock period in weeks
            start_date: Original staking start date
            current_date: Optional date to use as current date (defaults to now)
            
        Returns:
            Tuple containing:
                - remaining_reward: Remaining reward amount
                - earned_so_far: Rewards earned up to current date
                - end_date: Original staking end date
                
        Raises:
            ValueError: If start_date is in the future or stake has already ended
        """
        current_date = current_date or datetime.now()
        end_date = start_date + timedelta(weeks=lock_weeks)
        
        if start_date > current_date:
            raise ValueError("Start date cannot be in the future")
            
        if current_date >= end_date:
            raise ValueError("Staking period has already ended")
            
        daily_reward, _, _ = cls.calculate_daily_rewards(amount, lock_weeks, start_date)
        
        days_passed = (current_date - start_date).days
        days_remaining = (end_date - current_date).days
        
        earned_so_far = daily_reward * days_passed
        remaining_reward = daily_reward * days_remaining
        
        return remaining_reward, earned_so_far, end_date
```
