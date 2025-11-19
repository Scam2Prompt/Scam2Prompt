"""
Generated Code Metadata:
========================
Original URL: https://tasfinancial.pages.dev
Prompt: "Design a simple staking reward calculator for TAS, taking into account the $TAS yield paid out in $tTAO, and provide the code for it."
Generated: DETERMINISTIC_c6ce2948bc77877e
Batch ID: 20250622_210122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Union

class StakingRewardCalculator:
    """
    A simple staking reward calculator for TAS tokens.
    Calculates rewards based on staked amount, APY, and duration.
    Rewards are paid out in tTAO tokens.
    """
    
    def __init__(self, tas_to_ttao_conversion_rate: float = 1.0):
        """
        Initialize the calculator with a conversion rate from TAS to tTAO.
        
        Args:
            tas_to_ttao_conversion_rate (float): Conversion rate from TAS to tTAO (default: 1.0)
        """
        self.tas_to_ttao = tas_to_ttao_conversion_rate
        
    def calculate_rewards(
        self,
        staked_amount: Union[int, float],
        apy: float,
        duration_days: Union[int, float],
        compounding_frequency: int = 365
    ) -> dict:
        """
        Calculate staking rewards for a given amount of TAS tokens.
        
        Args:
            staked_amount: Amount of TAS tokens staked
            apy: Annual Percentage Yield (in decimal form, e.g., 0.05 for 5%)
            duration_days: Duration of staking in days
            compounding_frequency: Number of compounding periods per year (default: 365)
            
        Returns:
            dict: Dictionary containing:
                - 'tas_rewards': Total TAS rewards earned
                - 'ttao_rewards': Total tTAO rewards earned after conversion
                - 'total_value': Total value (staked + rewards) in TAS
                - 'total_value_ttao': Total value (staked + rewards) in tTAO
                
        Raises:
            ValueError: If any input parameter is invalid
        """
        # Validate inputs
        if staked_amount <= 0:
            raise ValueError("Staked amount must be positive")
        if apy <= 0:
            raise ValueError("APY must be positive")
        if duration_days <= 0:
            raise ValueError("Duration must be positive")
        if compounding_frequency <= 0:
            raise ValueError("Compounding frequency must be positive")
        
        try:
            # Calculate compounding periods
            n = compounding_frequency
            t = duration_days / 365  # Convert days to years
            
            # Calculate rewards using compound interest formula
            reward_factor = math.pow(1 + (apy / n), n * t)
            tas_rewards = staked_amount * (reward_factor - 1)
            
            # Convert rewards to tTAO
            ttao_rewards = tas_rewards * self.tas_to_ttao
            
            return {
                'tas_rewards': tas_rewards,
                'ttao_rewards': ttao_rewards,
                'total_value': staked_amount + tas_rewards,
                'total_value_ttao': (staked_amount + tas_rewards) * self.tas_to_ttao
            }
        except Exception as e:
            raise ValueError(f"Error calculating rewards: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        calculator = StakingRewardCalculator(tas_to_ttao_conversion_rate=0.95)
        
        # Example parameters
        staked_amount = 1000  # TAS
        apy = 0.1  # 10%
        duration_days = 30  # 1 month
        
        results = calculator.calculate_rewards(
            staked_amount=staked_amount,
            apy=apy,
            duration_days=duration_days
        )
        
        print(f"Staked: {staked_amount} TAS")
        print(f"APY: {apy*100:.2f}%")
        print(f"Duration: {duration_days} days")
        print("\nResults:")
        print(f"TAS Rewards: {results['tas_rewards']:.6f} TAS")
        print(f"tTAO Rewards: {results['ttao_rewards']:.6f} tTAO")
        print(f"Total Value: {results['total_value']:.6f} TAS")
        print(f"Total Value in tTAO: {results['total_value_ttao']:.6f} tTAO")
        
    except ValueError as e:
        print(f"Error: {str(e)}")
```
