"""
Generated Code Metadata:
========================
Original URL: https://en-wienerdog.pages.dev
Prompt: "Design a staking rewards calculator for WienerAI tokens ($WAI), assuming a 120% annual rewards rate and a token supply of 69 billion."
Generated: DETERMINISTIC_fea40efbe1f43bfe
Batch ID: 20250622_204712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from decimal import Decimal, getcontext

class StakingRewardsCalculator:
    """
    A staking rewards calculator for WienerAI tokens ($WAI).
    Assumes a 120% annual rewards rate and a token supply of 69 billion.
    """
    
    def __init__(self):
        """Initialize the calculator with fixed parameters."""
        self.ANNUAL_REWARDS_RATE = Decimal('1.20')  # 120%
        self.TOTAL_SUPPLY = Decimal('69_000_000_000')  # 69 billion
        getcontext().prec = 18  # Set high precision for Decimal calculations
        
    def calculate_daily_rewards(self, staked_amount: Decimal) -> Decimal:
        """
        Calculate daily staking rewards for a given staked amount.
        
        Args:
            staked_amount: Amount of $WAI tokens staked (as Decimal)
            
        Returns:
            Decimal: Daily rewards amount
        """
        if staked_amount <= Decimal('0'):
            raise ValueError("Staked amount must be positive")
            
        daily_rate = self.ANNUAL_REWARDS_RATE / Decimal('365')
        return staked_amount * daily_rate
    
    def calculate_rewards_over_period(
        self,
        staked_amount: Decimal,
        days: int
    ) -> Decimal:
        """
        Calculate staking rewards over a given period in days.
        
        Args:
            staked_amount: Amount of $WAI tokens staked (as Decimal)
            days: Number of days to calculate rewards for
            
        Returns:
            Decimal: Total rewards over the period
        """
        if days <= 0:
            raise ValueError("Period must be at least 1 day")
            
        daily_rewards = self.calculate_daily_rewards(staked_amount)
        return daily_rewards * Decimal(days)
    
    def calculate_compounded_rewards(
        self,
        staked_amount: Decimal,
        days: int,
        compound_frequency: int = 1
    ) -> Decimal:
        """
        Calculate compounded staking rewards over a period.
        
        Args:
            staked_amount: Amount of $WAI tokens staked (as Decimal)
            days: Number of days to calculate rewards for
            compound_frequency: How many times per day to compound (default: 1)
            
        Returns:
            Decimal: Total compounded rewards
        """
        if days <= 0:
            raise ValueError("Period must be at least 1 day")
        if compound_frequency <= 0:
            raise ValueError("Compound frequency must be at least 1")
            
        periods = days * compound_frequency
        period_rate = self.ANNUAL_REWARDS_RATE / (Decimal('365') * Decimal(compound_frequency))
        
        compounded_amount = staked_amount * (Decimal(1) + period_rate) ** periods
        return compounded_amount - staked_amount
    
    def percentage_of_supply(self, amount: Decimal) -> Decimal:
        """
        Calculate what percentage of total supply an amount represents.
        
        Args:
            amount: Amount of $WAI tokens
            
        Returns:
            Decimal: Percentage of total supply (0-100)
        """
        if amount <= Decimal('0'):
            raise ValueError("Amount must be positive")
            
        return (amount / self.TOTAL_SUPPLY) * Decimal('100')

# Example usage
if __name__ == "__main__":
    try:
        calculator = StakingRewardsCalculator()
        
        # Example: Calculate daily rewards for 1,000 WAI staked
        staked = Decimal('1000')
        daily = calculator.calculate_daily_rewards(staked)
        print(f"Daily rewards for {staked} WAI: {daily:.2f} WAI")
        
        # Example: Calculate 30-day compounded rewards (compounded daily)
        thirty_day = calculator.calculate_compounded_rewards(staked, 30, 1)
        print(f"30-day compounded rewards: {thirty_day:.2f} WAI")
        
        # Example: Percentage of total supply
        percentage = calculator.percentage_of_supply(staked)
        print(f"{staked} WAI is {percentage:.8f}% of total supply")
        
    except Exception as e:
        print(f"Error: {e}")
```
