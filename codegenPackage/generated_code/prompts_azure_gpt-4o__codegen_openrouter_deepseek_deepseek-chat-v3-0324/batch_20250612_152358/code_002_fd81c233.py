"""
Generated Code Metadata:
========================
Original URL: https://pepes-unchained.pages.dev
Prompt: Generate code to calculate double staking rewards for $PEPU tokens on a Layer 2 blockchain, considering the tokenomics outlined in Pepe Unchained.
Generated: DETERMINISTIC_fd81c23340df1fef
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Double Staking Rewards Calculator for $PEPU Tokens on Layer 2 Blockchain

import math
from decimal import Decimal, getcontext
from typing import Tuple

# Configure Decimal precision for accurate financial calculations
getcontext().prec = 18

class DoubleStakingRewardsCalculator:
    """
    A class to calculate double staking rewards for $PEPU tokens based on Pepe Unchained tokenomics.
    Handles reward calculations considering Layer 2 blockchain specifics.
    """
    
    def __init__(self, 
                 initial_stake: Decimal, 
                 apy_primary: Decimal, 
                 apy_secondary: Decimal, 
                 lock_period_days: int,
                 compounding_frequency: int = 365):
        """
        Initialize the calculator with staking parameters.
        
        Args:
            initial_stake (Decimal): Amount of $PEPU tokens staked
            apy_primary (Decimal): Annual Percentage Yield for primary staking (e.g., 0.15 for 15%)
            apy_secondary (Decimal): Annual Percentage Yield for secondary staking
            lock_period_days (int): Number of days tokens are locked
            compounding_frequency (int): Number of compounding periods per year (default: daily)
        """
        self.initial_stake = initial_stake
        self.apy_primary = apy_primary
        self.apy_secondary = apy_secondary
        self.lock_period_days = lock_period_days
        self.compounding_frequency = compounding_frequency
        
        # Validate inputs
        self._validate_inputs()
    
    def _validate_inputs(self) -> None:
        """Validate all input parameters for correctness."""
        if self.initial_stake <= Decimal('0'):
            raise ValueError("Initial stake must be positive")
        if self.apy_primary < Decimal('0') or self.apy_secondary < Decimal('0'):
            raise ValueError("APY values cannot be negative")
        if self.lock_period_days <= 0:
            raise ValueError("Lock period must be positive")
        if self.compounding_frequency <= 0:
            raise ValueError("Compounding frequency must be positive")
    
    def calculate_primary_rewards(self) -> Decimal:
        """
        Calculate rewards from primary staking.
        Uses compound interest formula: A = P(1 + r/n)^(nt)
        """
        periods = Decimal(self.lock_period_days) / Decimal(365) * Decimal(self.compounding_frequency)
        rate_per_period = self.apy_primary / Decimal(self.compounding_frequency)
        
        primary_rewards = self.initial_stake * ((Decimal(1) + rate_per_period) ** periods - Decimal(1))
        return primary_rewards.quantize(Decimal('1.00000000'))
    
    def calculate_secondary_rewards(self, primary_rewards: Decimal) -> Decimal:
        """
        Calculate rewards from secondary staking of primary rewards.
        Uses simple interest for secondary rewards as per Pepe Unchained tokenomics.
        Formula: A = P * r * t
        """
        time_years = Decimal(self.lock_period_days) / Decimal(365)
        secondary_rewards = primary_rewards * self.apy_secondary * time_years
        return secondary_rewards.quantize(Decimal('1.00000000'))
    
    def calculate_total_rewards(self) -> Tuple[Decimal, Decimal, Decimal]:
        """
        Calculate total rewards from both primary and secondary staking.
        
        Returns:
            Tuple[Decimal, Decimal, Decimal]: (primary_rewards, secondary_rewards, total_rewards)
        """
        primary = self.calculate_primary_rewards()
        secondary = self.calculate_secondary_rewards(primary)
        total = primary + secondary
        return (primary, secondary, total)
    
    def calculate_daily_rewards_breakdown(self) -> list:
        """
        Calculate daily breakdown of rewards over the lock period.
        
        Returns:
            list: List of dictionaries containing daily reward data
        """
        daily_data = []
        daily_rate_primary = (Decimal(1) + self.apy_primary / Decimal(365)) - Decimal(1)
        daily_rate_secondary = self.apy_secondary / Decimal(365)
        
        current_primary = self.initial_stake
        accumulated_secondary = Decimal(0)
        
        for day in range(1, self.lock_period_days + 1):
            # Calculate primary rewards (compounded daily)
            daily_primary_reward = current_primary * daily_rate_primary
            current_primary += daily_primary_reward
            
            # Calculate secondary rewards (simple interest on primary rewards)
            daily_secondary_reward = daily_primary_reward * daily_rate_secondary
            accumulated_secondary += daily_secondary_reward
            
            daily_data.append({
                'day': day,
                'primary_reward': daily_primary_reward.quantize(Decimal('1.00000000')),
                'secondary_reward': daily_secondary_reward.quantize(Decimal('1.00000000')),
                'total_primary': current_primary.quantize(Decimal('1.00000000')),
                'total_secondary': accumulated_secondary.quantize(Decimal('1.00000000'))
            })
        
        return daily_data


# Example usage
if __name__ == "__main__":
    try:
        # Initialize calculator with example parameters
        calculator = DoubleStakingRewardsCalculator(
            initial_stake=Decimal('10000'),  # 10,000 PEPU tokens
            apy_primary=Decimal('0.15'),     # 15% APY for primary staking
            apy_secondary=Decimal('0.10'),   # 10% APY for secondary staking
            lock_period_days=90,             # 90-day lock period
            compounding_frequency=365        # Daily compounding
        )
        
        # Calculate total rewards
        primary, secondary, total = calculator.calculate_total_rewards()
        print(f"Primary Rewards: {primary}")
        print(f"Secondary Rewards: {secondary}")
        print(f"Total Rewards: {total}")
        
        # Get daily breakdown (first 5 days for demonstration)
        daily_data = calculator.calculate_daily_rewards_breakdown()
        for day in daily_data[:5]:
            print(f"Day {day['day']}: Primary {day['primary_reward']}, Secondary {day['secondary_reward']}")
            
    except ValueError as e:
        print(f"Error in input parameters: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
