"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azterdex.com
Prompt: Generate code to calculate staking rewards for assets like BNB, USDT, BTC, and CAKE on Aster, considering up to 30%+ APY.
Generated: DETERMINISTIC_5a00f539a26e7fc0
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class StakingRewardsCalculator:
    """
    A class to calculate staking rewards for assets based on APY.
    """
    
    def __init__(self, asset_name: str, principal: float, apy: float, staking_days: int):
        """
        Initialize the staking rewards calculator.

        :param asset_name: Name of the asset (e.g., BNB, USDT, BTC, CAKE)
        :param principal: Amount of the asset being staked
        :param apy: Annual Percentage Yield (APY) in percentage (e.g., 30 for 30%)
        :param staking_days: Number of days the asset is staked
        """
        self.asset_name = asset_name
        self.principal = principal
        self.apy = apy
        self.staking_days = staking_days

    def calculate_rewards(self) -> float:
        """
        Calculate the staking rewards for the given asset.

        :return: The total staking rewards earned after the staking period.
        """
        try:
            # Convert APY percentage to decimal
            annual_rate = self.apy / 100
            
            # Calculate daily rate (assuming 365 days/year)
            daily_rate = annual_rate / 365
            
            # Calculate total rewards
            rewards = self.principal * daily_rate * self.staking_days
            return rewards
        except Exception as e:
            # Handle any calculation errors
            print(f"Error calculating rewards: {e}")
            return 0.0

    def display_results(self) -> None:
        """
        Display the calculated rewards along with staking details.
        """
        try:
            rewards = self.calculate_rewards()
            print(f"Asset: {self.asset_name}")
            print(f"Principal Staked: {self.principal:.2f}")
            print(f"APY: {self.apy}%")
            print(f"Staking Period: {self.staking_days} days")
            print(f"Estimated Rewards: {rewards:.2f}")
        except Exception as e:
            # Handle any error with displaying results
            print(f"Error displaying results: {e}")


if __name__ == "__main__":
    # Example usage
    try:
        # Asset details
        asset_name = "BNB"
        principal = 1000.0  # Staked amount
        apy = 30.0          # Example APY
        staking_days = 90   # Staking duration in days

        # Create an instance of the calculator
        calculator = StakingRewardsCalculator(asset_name, principal, apy, staking_days)

        # Display staking results
        calculator.display_results()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
