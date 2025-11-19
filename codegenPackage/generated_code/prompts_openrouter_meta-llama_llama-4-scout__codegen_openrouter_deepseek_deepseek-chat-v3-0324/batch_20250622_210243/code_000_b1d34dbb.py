"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-token.pages.dev
Prompt: Write a Python code snippet to calculate the staking rewards for Dogecoin20 (DOGE20) tokens, assuming a 2-year distribution period and a fixed supply of 140,000,000,000 tokens.
Generated: DETERMINISTIC_b1d34dbb244b26c5
Batch ID: 20250622_210243
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

class Dogecoin20StakingRewards:
    """
    Calculates staking rewards for Dogecoin20 (DOGE20) tokens over a 2-year distribution period.
    Assumes a fixed total supply of 140,000,000,000 tokens.
    """
    
    def __init__(self, total_supply: float = 140_000_000_000, distribution_period_years: int = 2):
        """
        Initialize the staking rewards calculator.
        
        Args:
            total_supply (float): Total supply of DOGE20 tokens (default: 140,000,000,000)
            distribution_period_years (int): Distribution period in years (default: 2)
        """
        self.total_supply = total_supply
        self.distribution_period_days = distribution_period_years * 365
        self.daily_distribution = total_supply / self.distribution_period_days
        
    def calculate_rewards(
        self,
        staked_amount: float,
        staking_start_date: datetime,
        staking_end_date: datetime = None,
        current_date: datetime = None
    ) -> float:
        """
        Calculate staking rewards for a given staking period.
        
        Args:
            staked_amount (float): Amount of DOGE20 tokens staked
            staking_start_date (datetime): Date when staking began
            staking_end_date (datetime, optional): Date when staking ended (defaults to current date if None)
            current_date (datetime, optional): Current date for calculation (defaults to now if None)
            
        Returns:
            float: Calculated staking rewards in DOGE20 tokens
            
        Raises:
            ValueError: If staking_end_date is before staking_start_date
        """
        if current_date is None:
            current_date = datetime.now()
            
        if staking_end_date is None:
            staking_end_date = current_date
            
        if staking_end_date < staking_start_date:
            raise ValueError("Staking end date cannot be before start date")
            
        staking_duration = (staking_end_date - staking_start_date).days
        
        if staking_duration <= 0:
            return 0.0
            
        # Calculate rewards based on staked proportion of total supply
        daily_reward = (staked_amount / self.total_supply) * self.daily_distribution
        total_reward = daily_reward * staking_duration
        
        return total_reward

# Example usage
if __name__ == "__main__":
    staking_calculator = Dogecoin20StakingRewards()
    
    # Example: Stake 1,000,000 DOGE20 for 30 days
    staked_amount = 1_000_000
    start_date = datetime.now() - timedelta(days=30)
    
    rewards = staking_calculator.calculate_rewards(
        staked_amount=staked_amount,
        staking_start_date=start_date
    )
    
    print(f"Staking rewards: {rewards:.2f} DOGE20")
```
