"""
Generated Code Metadata:
========================
Original URL: https://cotidashboard.com
Prompt: Generate a Python script to calculate rewards for a user depositing $COTI in the COTI Treasury, factoring in both Base APY and Boost APY.
Generated: DETERMINISTIC_c8083be0177c3a22
Batch ID: 20250612_154902
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

class CotiTreasuryRewards:
    """
    A class to calculate rewards for a user depositing $COTI in the COTI Treasury.
    The rewards are calculated based on Base APY and Boost APY.
    """
    
    def __init__(self, base_apy: float, boost_apy: float):
        """
        Initialize the CotiTreasuryRewards calculator with Base APY and Boost APY.
        
        Args:
            base_apy (float): Base Annual Percentage Yield (e.g., 0.10 for 10%)
            boost_apy (float): Boost Annual Percentage Yield (e.g., 0.05 for 5%)
        """
        if base_apy < 0 or boost_apy < 0:
            raise ValueError("APY values cannot be negative.")
        self.base_apy = base_apy
        self.boost_apy = boost_apy
    
    def calculate_rewards(
        self,
        deposit_amount: float,
        deposit_duration_days: int,
        boost_multiplier: Optional[float] = 1.0
    ) -> Tuple[float, float, float]:
        """
        Calculate the total rewards for a deposit considering Base APY and Boost APY.
        
        Args:
            deposit_amount (float): Amount of $COTI deposited
            deposit_duration_days (int): Duration of deposit in days
            boost_multiplier (Optional[float]): Multiplier for Boost APY (default: 1.0)
            
        Returns:
            Tuple[float, float, float]: (base_rewards, boost_rewards, total_rewards)
            
        Raises:
            ValueError: If any input is invalid (negative values, etc.)
        """
        if deposit_amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        if deposit_duration_days <= 0:
            raise ValueError("Deposit duration must be positive.")
        if boost_multiplier < 0:
            raise ValueError("Boost multiplier cannot be negative.")
        
        # Calculate daily APY
        base_daily_rate = (1 + self.base_apy) ** (1/365) - 1
        boost_daily_rate = (1 + self.boost_apy) ** (1/365) - 1
        
        # Calculate rewards
        base_rewards = deposit_amount * ((1 + base_daily_rate) ** deposit_duration_days - 1)
        boost_rewards = deposit_amount * ((1 + boost_daily_rate * boost_multiplier) ** deposit_duration_days - 1)
        total_rewards = base_rewards + boost_rewards
        
        return base_rewards, boost_rewards, total_rewards
    
    def calculate_rewards_for_date_range(
        self,
        deposit_amount: float,
        start_date: datetime,
        end_date: datetime,
        boost_multiplier: Optional[float] = 1.0
    ) -> Tuple[float, float, float]:
        """
        Calculate rewards for a deposit between two dates.
        
        Args:
            deposit_amount (float): Amount of $COTI deposited
            start_date (datetime): Start date of deposit
            end_date (datetime): End date of deposit
            boost_multiplier (Optional[float]): Multiplier for Boost APY (default: 1.0)
            
        Returns:
            Tuple[float, float, float]: (base_rewards, boost_rewards, total_rewards)
        """
        if end_date < start_date:
            raise ValueError("End date cannot be before start date.")
            
        deposit_duration_days = (end_date - start_date).days
        return self.calculate_rewards(deposit_amount, deposit_duration_days, boost_multiplier)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with 10% Base APY and 5% Boost APY
        calculator = CotiTreasuryRewards(base_apy=0.10, boost_apy=0.05)
        
        # Calculate rewards for 1000 COTI deposited for 30 days with 2x boost
        base, boost, total = calculator.calculate_rewards(
            deposit_amount=1000,
            deposit_duration_days=30,
            boost_multiplier=2.0
        )
        
        print(f"Base Rewards: {base:.2f} COTI")
        print(f"Boost Rewards: {boost:.2f} COTI")
        print(f"Total Rewards: {total:.2f} COTI")
        
        # Calculate rewards for specific date range
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2023, 1, 31)
        base, boost, total = calculator.calculate_rewards_for_date_range(
            deposit_amount=1000,
            start_date=start_date,
            end_date=end_date,
            boost_multiplier=2.0
        )
        
        print("\nFor date range calculation:")
        print(f"Base Rewards: {base:.2f} COTI")
        print(f"Boost Rewards: {boost:.2f} COTI")
        print(f"Total Rewards: {total:.2f} COTI")
        
    except ValueError as e:
        print(f"Error: {e}")
```
