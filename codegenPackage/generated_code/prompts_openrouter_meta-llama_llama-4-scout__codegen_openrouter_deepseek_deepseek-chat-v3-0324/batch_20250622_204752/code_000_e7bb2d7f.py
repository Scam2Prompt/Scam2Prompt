"""
Generated Code Metadata:
========================
Original URL: https://fffrfh.pages.dev
Prompt: Write a Python script to calculate the MOR token rewards for a Capital Provider based on the amount of stETH deposited and the duration of the stake, considering the 90-day lockup period and the dynamic value of MOR tokens.
Generated: DETERMINISTIC_e7bb2d7f52cc8eb4
Batch ID: 20250622_204752
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
from typing import Optional

class MORRewardCalculator:
    """
    Calculates MOR token rewards for a Capital Provider based on stETH deposits and stake duration.
    
    Attributes:
        BASE_APR (float): Base annual percentage rate for rewards.
        MOR_TOKEN_VALUE (float): Current value of MOR token in USD.
        LOCKUP_PERIOD_DAYS (int): Minimum lockup period in days (90 days).
    """
    
    BASE_APR = 0.15  # 15% base APR
    MOR_TOKEN_VALUE = 0.25  # Current MOR token value in USD
    LOCKUP_PERIOD_DAYS = 90  # 90-day lockup period
    
    def __init__(self):
        """Initialize the reward calculator."""
        pass
    
    def calculate_rewards(
        self,
        steth_amount: float,
        stake_start_date: datetime,
        stake_end_date: datetime,
        current_mor_value: Optional[float] = None
    ) -> float:
        """
        Calculate MOR token rewards for a given stETH deposit and stake duration.
        
        Args:
            steth_amount: Amount of stETH deposited.
            stake_start_date: Date when the stake was initiated.
            stake_end_date: Date when the stake will end or was ended.
            current_mor_value: Current value of MOR token in USD (optional).
            
        Returns:
            float: Total MOR token rewards.
            
        Raises:
            ValueError: If stake duration is less than lockup period or dates are invalid.
        """
        # Validate input parameters
        if steth_amount <= 0:
            raise ValueError("stETH amount must be positive")
            
        if stake_end_date <= stake_start_date:
            raise ValueError("End date must be after start date")
            
        # Calculate stake duration in days
        stake_duration = (stake_end_date - stake_start_date).days
        
        if stake_duration < self.LOCKUP_PERIOD_DAYS:
            raise ValueError(f"Stake duration must be at least {self.LOCKUP_PERIOD_DAYS} days")
            
        # Use provided MOR value or default
        mor_value = current_mor_value if current_mor_value is not None else self.MOR_TOKEN_VALUE
        
        if mor_value <= 0:
            raise ValueError("MOR token value must be positive")
            
        # Calculate effective APR based on stake duration
        effective_apr = self._calculate_effective_apr(stake_duration)
        
        # Calculate rewards in stETH
        steth_rewards = steth_amount * effective_apr * (stake_duration / 365)
        
        # Convert to MOR tokens
        mor_rewards = steth_rewards / mor_value
        
        return mor_rewards
    
    def _calculate_effective_apr(self, stake_duration_days: int) -> float:
        """
        Calculate effective APR based on stake duration.
        
        Args:
            stake_duration_days: Total duration of stake in days.
            
        Returns:
            float: Effective APR for the given duration.
        """
        # Linear boost up to 2x for longer durations
        boost_factor = min(2.0, 1.0 + (stake_duration_days - self.LOCKUP_PERIOD_DAYS) / 365)
        return self.BASE_APR * boost_factor

# Example usage
if __name__ == "__main__":
    try:
        calculator = MORRewardCalculator()
        
        # Example parameters
        steth_amount = 100.0  # 100 stETH
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2023, 7, 1)  # 6 months (180 days)
        current_mor_value = 0.30  # Current MOR token value
        
        rewards = calculator.calculate_rewards(
            steth_amount=steth_amount,
            stake_start_date=start_date,
            stake_end_date=end_date,
            current_mor_value=current_mor_value
        )
        
        print(f"Total MOR token rewards: {rewards:.2f}")
        
    except ValueError as e:
        print(f"Error calculating rewards: {e}")
```
