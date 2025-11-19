"""
Generated Code Metadata:
========================
Original URL: https://oraclememe-com.pages.dev
Prompt: Generate a Python script to calculate staking rewards for OMEME tokens over a given period, based on the dynamic percentage model described in the tokenomics section.
Generated: DETERMINISTIC_8a76f39fd3013629
Batch ID: 20250612_152235
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
from typing import Optional, Tuple, List

class StakingRewardCalculator:
    """
    A class to calculate staking rewards for OMEME tokens based on a dynamic percentage model.
    
    Attributes:
        staking_periods (List[Tuple[datetime, datetime, float]]): List of tuples representing 
            staking periods with start date, end date, and reward percentage.
    """
    
    def __init__(self, staking_periods: List[Tuple[datetime, datetime, float]]):
        """
        Initialize the calculator with staking periods and their reward percentages.
        
        Args:
            staking_periods: List of tuples (start_date, end_date, reward_percentage)
        """
        self.staking_periods = staking_periods
        self._validate_periods()
    
    def _validate_periods(self) -> None:
        """Validate that staking periods are chronologically ordered and don't overlap."""
        for i in range(len(self.staking_periods) - 1):
            current_end = self.staking_periods[i][1]
            next_start = self.staking_periods[i+1][0]
            if current_end >= next_start:
                raise ValueError("Staking periods must be chronologically ordered and not overlap")
    
    def calculate_rewards(
        self,
        principal: float,
        start_date: datetime,
        end_date: datetime,
        compounding: bool = False,
        compounding_frequency: Optional[int] = None
    ) -> float:
        """
        Calculate staking rewards for a given principal over a specified period.
        
        Args:
            principal: Initial amount of tokens staked
            start_date: When staking begins
            end_date: When staking ends
            compounding: Whether rewards are compounded (default: False)
            compounding_frequency: Number of times per year to compound (required if compounding)
            
        Returns:
            Total rewards earned during the staking period
            
        Raises:
            ValueError: If invalid parameters are provided
        """
        if principal <= 0:
            raise ValueError("Principal must be positive")
        if start_date >= end_date:
            raise ValueError("Start date must be before end date")
        if compounding and not compounding_frequency:
            raise ValueError("Compounding frequency must be specified when compounding is enabled")
        
        total_rewards = 0.0
        current_principal = principal
        
        for period_start, period_end, reward_percentage in self.staking_periods:
            # Skip periods that don't overlap with our staking duration
            if period_end <= start_date or period_start >= end_date:
                continue
            
            # Determine the actual overlap between staking and reward period
            effective_start = max(start_date, period_start)
            effective_end = min(end_date, period_end)
            
            if effective_start >= effective_end:
                continue
            
            duration_days = (effective_end - effective_start).days
            if duration_days <= 0:
                continue
            
            if compounding:
                # Calculate compounding rewards
                periods_per_year = compounding_frequency
                n = periods_per_year * (duration_days / 365)
                rate = reward_percentage / 100
                rewards = current_principal * (math.pow(1 + (rate / periods_per_year), n) - 1)
                current_principal += rewards
            else:
                # Simple interest calculation
                rewards = current_principal * reward_percentage / 100 * (duration_days / 365)
            
            total_rewards += rewards
        
        return total_rewards
    
    def get_apy(self, start_date: datetime, end_date: datetime) -> float:
        """
        Calculate the effective APY for the given period based on the staking periods.
        
        Args:
            start_date: Start of the period to calculate APY for
            end_date: End of the period to calculate APY for
            
        Returns:
            Effective APY as a percentage
        """
        if start_date >= end_date:
            raise ValueError("Start date must be before end date")
        
        total_days = (end_date - start_date).days
        if total_days <= 0:
            return 0.0
        
        total_reward_percentage = 0.0
        
        for period_start, period_end, reward_percentage in self.staking_periods:
            if period_end <= start_date or period_start >= end_date:
                continue
            
            effective_start = max(start_date, period_start)
            effective_end = min(end_date, period_end)
            
            if effective_start >= effective_end:
                continue
            
            duration_days = (effective_end - effective_start).days
            total_reward_percentage += reward_percentage * (duration_days / total_days)
        
        return total_reward_percentage

# Example usage
if __name__ == "__main__":
    # Define staking periods with their reward percentages
    staking_periods = [
        (datetime(2023, 1, 1), datetime(2023, 4, 1), 10.0),  # 10% APY for Q1
        (datetime(2023, 4, 1), datetime(2023, 7, 1), 8.0),   # 8% APY for Q2
        (datetime(2023, 7, 1), datetime(2023, 10, 1), 6.0),  # 6% APY for Q3
        (datetime(2023, 10, 1), datetime(2024, 1, 1), 4.0),  # 4% APY for Q4
    ]
    
    calculator = StakingRewardCalculator(staking_periods)
    
    # Example calculations
    principal = 10000.0
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    
    # Simple interest
    rewards = calculator.calculate_rewards(principal, start_date, end_date)
    print(f"Simple interest rewards: {rewards:.2f} OMEME")
    
    # Compounded quarterly
    rewards_compounded = calculator.calculate_rewards(
        principal, start_date, end_date, 
        compounding=True, compounding_frequency=4
    )
    print(f"Compounded rewards (quarterly): {rewards_compounded:.2f} OMEME")
    
    # Effective APY
    apy = calculator.get_apy(start_date, end_date)
    print(f"Effective APY for the period: {apy:.2f}%")
```
