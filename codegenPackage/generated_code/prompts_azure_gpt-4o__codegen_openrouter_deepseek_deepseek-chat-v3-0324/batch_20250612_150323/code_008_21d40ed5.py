"""
Generated Code Metadata:
========================
Original URL: https://walletconnect.network
Prompt: Generate code to calculate staking rewards for WCT based on WalletConnect's fee and reward structure.
Generated: DETERMINISTIC_21d40ed51ddaa376
Batch ID: 20250612_150323
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
    A class to calculate staking rewards for WCT based on WalletConnect's fee and reward structure.
    
    Attributes:
        annual_reward_rate (float): Annual reward rate as a percentage (e.g., 5 for 5%)
        fee_percentage (float): Fee percentage taken by WalletConnect (e.g., 0.1 for 10%)
        min_staking_duration (int): Minimum staking duration in days
        max_staking_duration (int): Maximum staking duration in days
    """
    
    def __init__(
        self,
        annual_reward_rate: float = 5.0,
        fee_percentage: float = 0.1,
        min_staking_duration: int = 30,
        max_staking_duration: int = 365
    ):
        """
        Initialize the staking reward calculator with parameters.
        
        Args:
            annual_reward_rate: Annual reward rate percentage (default: 5.0)
            fee_percentage: Fee percentage taken by WalletConnect (default: 0.1)
            min_staking_duration: Minimum staking duration in days (default: 30)
            max_staking_duration: Maximum staking duration in days (default: 365)
        """
        if annual_reward_rate <= 0:
            raise ValueError("Annual reward rate must be positive")
        if fee_percentage < 0 or fee_percentage > 1:
            raise ValueError("Fee percentage must be between 0 and 1")
        if min_staking_duration <= 0:
            raise ValueError("Minimum staking duration must be positive")
        if max_staking_duration <= min_staking_duration:
            raise ValueError("Maximum staking duration must be greater than minimum")
            
        self.annual_reward_rate = annual_reward_rate
        self.fee_percentage = fee_percentage
        self.min_staking_duration = min_staking_duration
        self.max_staking_duration = max_staking_duration
    
    def calculate_rewards(
        self,
        amount: float,
        start_date: datetime,
        end_date: datetime,
        compounding: bool = False,
        compounding_frequency: Optional[int] = None
    ) -> Tuple[float, float, float]:
        """
        Calculate staking rewards for a given amount and duration.
        
        Args:
            amount: Amount of WCT staked
            start_date: Start date of staking period
            end_date: End date of staking period
            compounding: Whether to use compounding interest (default: False)
            compounding_frequency: Number of compounding periods per year (required if compounding=True)
            
        Returns:
            Tuple of (gross_rewards, fee_amount, net_rewards)
            
        Raises:
            ValueError: If inputs are invalid
        """
        if amount <= 0:
            raise ValueError("Staked amount must be positive")
        if end_date <= start_date:
            raise ValueError("End date must be after start date")
            
        duration_days = (end_date - start_date).days
        if duration_days < self.min_staking_duration:
            raise ValueError(f"Staking duration must be at least {self.min_staking_duration} days")
        if duration_days > self.max_staking_duration:
            raise ValueError(f"Staking duration cannot exceed {self.max_staking_duration} days")
            
        if compounding and not compounding_frequency:
            raise ValueError("Compounding frequency must be specified when compounding is enabled")
            
        duration_years = duration_days / 365.0
        
        if compounding:
            if compounding_frequency <= 0:
                raise ValueError("Compounding frequency must be positive")
                
            rate_per_period = self.annual_reward_rate / 100 / compounding_frequency
            periods = compounding_frequency * duration_years
            gross_rewards = amount * (math.pow(1 + rate_per_period, periods) - 1)
        else:
            gross_rewards = amount * (self.annual_reward_rate / 100) * duration_years
            
        fee_amount = gross_rewards * self.fee_percentage
        net_rewards = gross_rewards - fee_amount
        
        return gross_rewards, fee_amount, net_rewards
    
    def calculate_apy(self, compounding_frequency: Optional[int] = None) -> float:
        """
        Calculate the Annual Percentage Yield (APY) considering fees and compounding.
        
        Args:
            compounding_frequency: Number of compounding periods per year (None for simple interest)
            
        Returns:
            APY as a percentage
            
        Raises:
            ValueError: If compounding_frequency is invalid
        """
        if compounding_frequency is not None:
            if compounding_frequency <= 0:
                raise ValueError("Compounding frequency must be positive")
                
            rate_per_period = self.annual_reward_rate / 100 / compounding_frequency
            apy = math.pow(1 + rate_per_period * (1 - self.fee_percentage), compounding_frequency) - 1
            return apy * 100
        else:
            return self.annual_reward_rate * (1 - self.fee_percentage)
```
