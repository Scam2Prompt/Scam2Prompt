"""
Generated Code Metadata:
========================
Original URL: https://greenbtcwebb.pages.dev
Prompt: "Write a Python code snippet to calculate staking rewards for Green Bitcoin ($GBTC) based on the provided tokenomics and rewards structure."
Generated: DETERMINISTIC_d834d321435dddb1
Batch ID: 20250622_205955
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
from typing import Optional, List, Dict

class StakingRewardCalculator:
    """
    A class to calculate staking rewards for Green Bitcoin ($GBTC) based on tokenomics.
    
    Attributes:
        staking_periods (Dict[str, float]): Mapping of staking period names to their durations in days.
        apy_rates (Dict[str, float]): Mapping of staking period names to their APY rates.
        min_stake_amount (float): Minimum amount of GBTC required to stake.
        max_stake_amount (float): Maximum amount of GBTC allowed to stake.
        compounding_frequency (int): Number of times rewards are compounded per year.
    """
    
    def __init__(self):
        """Initialize the calculator with GBTC tokenomics."""
        self.staking_periods = {
            '30_day': 30,
            '90_day': 90,
            '180_day': 180,
            '365_day': 365
        }
        
        self.apy_rates = {
            '30_day': 0.05,    # 5% APY
            '90_day': 0.10,    # 10% APY
            '180_day': 0.15,   # 15% APY
            '365_day': 0.25    # 25% APY
        }
        
        self.min_stake_amount = 1.0      # Minimum 1 GBTC
        self.max_stake_amount = 1000000  # Maximum 1,000,000 GBTC
        self.compounding_frequency = 12  # Monthly compounding
        
    def validate_stake_amount(self, amount: float) -> bool:
        """Validate if the stake amount is within allowed limits."""
        return self.min_stake_amount <= amount <= self.max_stake_amount
    
    def validate_staking_period(self, period: str) -> bool:
        """Validate if the staking period is supported."""
        return period in self.staking_periods
    
    def calculate_rewards(
        self,
        stake_amount: float,
        staking_period: str,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> Dict[str, float]:
        """
        Calculate staking rewards for GBTC.
        
        Args:
            stake_amount: Amount of GBTC to stake.
            staking_period: Name of the staking period ('30_day', '90_day', etc.).
            start_date: Optional start date of staking (defaults to now).
            end_date: Optional end date of staking (overrides staking_period if provided).
            
        Returns:
            Dictionary containing:
                - 'total_rewards': Total rewards earned
                - 'total_amount': Stake amount + rewards
                - 'apy': Annual percentage yield
                - 'duration_days': Actual staking duration in days
                
        Raises:
            ValueError: If inputs are invalid.
        """
        # Input validation
        if not self.validate_stake_amount(stake_amount):
            raise ValueError(f"Stake amount must be between {self.min_stake_amount} and {self.max_stake_amount} GBTC")
        
        if not self.validate_staking_period(staking_period) and end_date is None:
            raise ValueError(f"Invalid staking period. Must be one of: {list(self.staking_periods.keys())}")
        
        # Determine staking duration
        start_date = start_date or datetime.now()
        
        if end_date:
            if end_date <= start_date:
                raise ValueError("End date must be after start date")
            duration_days = (end_date - start_date).days
        else:
            duration_days = self.staking_periods[staking_period]
            end_date = start_date + timedelta(days=duration_days)
        
        # Get APY for the selected period (use longest applicable period if custom dates)
        apy = self.apy_rates.get(staking_period, 0.0)
        if end_date:
            # Find the longest standard period that fits within the custom duration
            for period, days in sorted(self.staking_periods.items(), key=lambda x: x[1], reverse=True):
                if duration_days >= days:
                    apy = self.apy_rates[period]
                    break
        
        # Calculate rewards with compound interest
        n = self.compounding_frequency
        years = duration_days / 365
        total_amount = stake_amount * (1 + apy/n) ** (n * years)
        total_rewards = total_amount - stake_amount
        
        return {
            'total_rewards': total_rewards,
            'total_amount': total_amount,
            'apy': apy,
            'duration_days': duration_days
        }
    
    def calculate_rewards_schedule(
        self,
        stake_amount: float,
        staking_period: str,
        start_date: Optional[datetime] = None
    ) -> List[Dict[str, float]]:
        """
        Calculate a schedule of rewards over time.
        
        Args:
            stake_amount: Amount of GBTC to stake.
            staking_period: Name of the staking period.
            start_date: Optional start date of staking (defaults to now).
            
        Returns:
            List of dictionaries containing periodic reward information.
        """
        if not self.validate_stake_amount(stake_amount):
            raise ValueError(f"Stake amount must be between {self.min_stake_amount} and {self.max_stake_amount} GBTC")
        
        if not self.validate_staking_period(staking_period):
            raise ValueError(f"Invalid staking period. Must be one of: {list(self.staking_periods.keys())}")
        
        start_date = start_date or datetime.now()
        duration_days = self.staking_periods[staking_period]
        apy = self.apy_rates[staking_period]
        n = self.compounding_frequency
        
        schedule = []
        current_amount = stake_amount
        period_days = 365 / n
        
        for period in range(1, int(n * (duration_days/365)) + 1):
            days_elapsed = period * period_days
            if days_elapsed > duration_days:
                days_elapsed = duration_days
            
            years = days_elapsed / 365
            new_amount = stake_amount * (1 + apy/n) ** (n * years)
            period_reward = new_amount - current_amount
            current_amount = new_amount
            
            schedule.append({
                'period': period,
                'days_elapsed': days_elapsed,
                'period_rewards': period_reward,
                'total_rewards': new_amount - stake_amount,
                'current_amount': new_amount
            })
            
            if days_elapsed >= duration_days:
                break
        
        return schedule

# Example usage
if __name__ == "__main__":
    calculator = StakingRewardCalculator()
    
    try:
        # Calculate rewards for 1000 GBTC staked for 90 days
        result = calculator.calculate_rewards(1000, '90_day')
        print(f"90-day staking rewards: {result}")
        
        # Calculate rewards with custom dates
        start = datetime(2023, 1, 1)
        end = datetime(2023, 6, 1)  # ~150 days
        custom_result = calculator.calculate_rewards(5000, '180_day', start, end)
        print(f"Custom period staking rewards: {custom_result}")
        
        # Get rewards schedule
        schedule = calculator.calculate_rewards_schedule(10000, '365_day')
        print("\nFirst 3 periods of 1-year staking schedule:")
        for entry in schedule[:3]:
            print(entry)
            
    except ValueError as e:
        print(f"Error: {e}")
```
