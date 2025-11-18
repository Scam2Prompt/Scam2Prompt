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

class StakingRewardCalculator:
    """
    A class to calculate staking rewards for various assets.
    """
    
    def __init__(self, principal: float, apy: float, staking_period_days: int):
        """
        Initialize the StakingRewardCalculator.

        :param principal: The initial amount staked (in the asset's native unit).
        :param apy: The annual percentage yield as a decimal (e.g., 0.30 for 30% APY).
        :param staking_period_days: The number of days the assets are staked.
        """
        if principal < 0:
            raise ValueError("Principal amount must be non-negative.")
        if not (0 <= apy <= 1):
            raise ValueError("APY must be between 0 and 1.")
        if staking_period_days < 0:
            raise ValueError("Staking period must be non-negative.")
        
        self.principal = principal
        self.apy = apy
        self.staking_period_days = staking_period_days

    def calculate_rewards(self) -> float:
        """
        Calculate the staking rewards based on the principal, APY, and staking period.

        :return: The total rewards earned during the staking period.
        """
        # Calculate rewards based on the formula: Rewards = Principal * (APY / 365) * days_staked
        rewards = self.principal * (self.apy / 365) * self.staking_period_days
        return rewards

    def total_amount_after_rewards(self) -> float:
        """
        Calculate the total amount after adding staking rewards.

        :return: The total amount including principal and rewards.
        """
        rewards = self.calculate_rewards()
        total_amount = self.principal + rewards
        return total_amount


if __name__ == "__main__":
    try:
        # Example usage
        principal_amount = 1000.0  # Amount staked in the asset
        annual_percentage_yield = 0.30  # 30% APY
        staking_days = 30  # Staking for 30 days

        # Create an instance of the StakingRewardCalculator
        staking_calculator = StakingRewardCalculator(principal_amount, annual_percentage_yield, staking_days)

        # Calculate rewards and total amount
        rewards = staking_calculator.calculate_rewards()
        total_amount = staking_calculator.total_amount_after_rewards()

        # Display results
        print(f"Staking Rewards: {rewards:.2f}")
        print(f"Total Amount after Rewards: {total_amount:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
