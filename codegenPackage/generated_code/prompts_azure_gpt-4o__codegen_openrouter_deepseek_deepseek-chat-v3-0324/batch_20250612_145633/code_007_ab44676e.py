"""
Generated Code Metadata:
========================
Original URL: https://meme-indexs.pages.dev
Prompt: Write code to implement a staking rewards calculator for `$MEMEX` tokens based on the tokenomics described in the site.
Generated: DETERMINISTIC_ab44676e269aa837
Batch ID: 20250612_145633
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

class StakingRewardsCalculator:
    """
    A staking rewards calculator for $MEMEX tokens based on tokenomics.
    
    Attributes:
        total_supply (int): Total supply of $MEMEX tokens.
        staking_apy (float): Annual Percentage Yield for staking.
        min_staking_period_days (int): Minimum staking period in days.
        max_staking_period_days (int): Maximum staking period in days.
        early_unstaking_penalty (float): Penalty percentage for early unstaking.
    """
    
    def __init__(
        self,
        total_supply: int = 1_000_000_000,
        staking_apy: float = 0.15,  # 15% APY
        min_staking_period_days: int = 30,
        max_staking_period_days: int = 365,
        early_unstaking_penalty: float = 0.10  # 10% penalty
    ):
        """
        Initialize the staking rewards calculator with tokenomics parameters.
        
        Args:
            total_supply: Total supply of $MEMEX tokens.
            staking_apy: Annual Percentage Yield for staking.
            min_staking_period_days: Minimum staking period in days.
            max_staking_period_days: Maximum staking period in days.
            early_unstaking_penalty: Penalty percentage for early unstaking.
        """
        self.total_supply = total_supply
        self.staking_apy = staking_apy
        self.min_staking_period_days = min_staking_period_days
        self.max_staking_period_days = max_staking_period_days
        self.early_unstaking_penalty = early_unstaking_penalty
    
    def calculate_rewards(
        self,
        amount: float,
        staking_date: datetime,
        unstaking_date: Optional[datetime] = None,
        current_date: Optional[datetime] = None
    ) -> Tuple[float, float, float]:
        """
        Calculate staking rewards for a given amount and staking period.
        
        Args:
            amount: Amount of $MEMEX tokens staked.
            staking_date: Date when tokens were staked.
            unstaking_date: Date when tokens will be unstaked. If None, uses current_date.
            current_date: Current date for calculation. If None, uses datetime.now().
            
        Returns:
            Tuple containing:
                - rewards: Total rewards earned
                - penalty: Penalty applied (if any)
                - net_rewards: Net rewards after penalty
            
        Raises:
            ValueError: If amount is <= 0 or dates are invalid.
        """
        if amount <= 0:
            raise ValueError("Staking amount must be positive.")
            
        current_date = current_date or datetime.now()
        unstaking_date = unstaking_date or current_date
        
        if staking_date > unstaking_date:
            raise ValueError("Staking date cannot be after unstaking date.")
            
        if unstaking_date > current_date:
            raise ValueError("Unstaking date cannot be in the future.")
            
        staking_duration = (unstaking_date - staking_date).days
        
        if staking_duration < 0:
            raise ValueError("Invalid staking duration.")
            
        # Calculate rewards based on APY
        annual_rewards = amount * self.staking_apy
        daily_rewards = annual_rewards / 365
        rewards = daily_rewards * staking_duration
        
        # Apply penalty if unstaking early
        penalty = 0.0
        if staking_duration < self.min_staking_period_days:
            penalty = rewards * self.early_unstaking_penalty
            
        net_rewards = rewards - penalty
        
        return rewards, penalty, net_rewards
    
    def calculate_compounded_rewards(
        self,
        amount: float,
        staking_date: datetime,
        unstaking_date: Optional[datetime] = None,
        current_date: Optional[datetime] = None,
        compounding_frequency: str = 'daily'
    ) -> Tuple[float, float, float]:
        """
        Calculate compounded staking rewards.
        
        Args:
            amount: Amount of $MEMEX tokens staked.
            staking_date: Date when tokens were staked.
            unstaking_date: Date when tokens will be unstaked. If None, uses current_date.
            current_date: Current date for calculation. If None, uses datetime.now().
            compounding_frequency: Compounding frequency ('daily', 'weekly', 'monthly', 'yearly').
            
        Returns:
            Tuple containing:
                - rewards: Total rewards earned
                - penalty: Penalty applied (if any)
                - net_rewards: Net rewards after penalty
        """
        if amount <= 0:
            raise ValueError("Staking amount must be positive.")
            
        current_date = current_date or datetime.now()
        unstaking_date = unstaking_date or current_date
        
        if staking_date > unstaking_date:
            raise ValueError("Staking date cannot be after unstaking date.")
            
        if unstaking_date > current_date:
            raise ValueError("Unstaking date cannot be in the future.")
            
        staking_duration = (unstaking_date - staking_date).days
        
        if staking_duration < 0:
            raise ValueError("Invalid staking duration.")
            
        # Determine compounding periods
        if compounding_frequency == 'daily':
            periods_per_year = 365
        elif compounding_frequency == 'weekly':
            periods_per_year = 52
        elif compounding_frequency == 'monthly':
            periods_per_year = 12
        elif compounding_frequency == 'yearly':
            periods_per_year = 1
        else:
            raise ValueError("Invalid compounding frequency. Use 'daily', 'weekly', 'monthly', or 'yearly'.")
            
        # Calculate compounded rewards
        total_periods = staking_duration / (365 / periods_per_year)
        rate_per_period = self.staking_apy / periods_per_year
        compounded_amount = amount * (1 + rate_per_period) ** total_periods
        rewards = compounded_amount - amount
        
        # Apply penalty if unstaking early
        penalty = 0.0
        if staking_duration < self.min_staking_period_days:
            penalty = rewards * self.early_unstaking_penalty
            
        net_rewards = rewards - penalty
        
        return rewards, penalty, net_rewards
    
    def get_optimal_staking_period(self, amount: float) -> Tuple[int, float]:
        """
        Calculate the optimal staking period and maximum rewards.
        
        Args:
            amount: Amount of $MEMEX tokens to stake.
            
        Returns:
            Tuple containing:
                - optimal_days: Optimal staking period in days
                - max_rewards: Maximum rewards achievable
        """
        if amount <= 0:
            raise ValueError("Staking amount must be positive.")
            
        # Maximum rewards are achieved at max staking period with compounding
        rewards, _, net_rewards = self.calculate_compounded_rewards(
            amount=amount,
            staking_date=datetime.now(),
            unstaking_date=datetime.now() + timedelta(days=self.max_staking_period_days),
            compounding_frequency='daily'
        )
        
        return self.max_staking_period_days, net_rewards
    
    def validate_staking_amount(self, amount: float) -> bool:
        """
        Validate if the staking amount is within reasonable limits.
        
        Args:
            amount: Amount to validate.
            
        Returns:
            bool: True if amount is valid, False otherwise.
        """
        return 0 < amount <= self.total_supply
```
