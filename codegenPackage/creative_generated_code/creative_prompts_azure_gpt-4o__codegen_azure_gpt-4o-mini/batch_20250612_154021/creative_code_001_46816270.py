"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wwwasterdex.com
Prompt: Generate code to calculate staking rewards on Aster DEX for assets like BNB, USDT, BTC, and CAKE, considering an APY of up to 30%+.
Generated: DETERMINISTIC_46816270ed1c1646
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
    def __init__(self, asset_name, amount_staked, annual_percentage_yield):
        """
        Initialize the StakingRewardCalculator with asset details.
        
        :param asset_name: Name of the asset being staked (e.g., 'BNB', 'USDT', 'BTC', 'CAKE')
        :param amount_staked: Amount of the asset being staked
        :param annual_percentage_yield: Annual Percentage Yield (APY) as a decimal (e.g., 0.30 for 30%)
        """
        self.asset_name = asset_name
        self.amount_staked = amount_staked
        self.annual_percentage_yield = annual_percentage_yield

    def calculate_rewards(self, staking_duration_days):
        """
        Calculate the staking rewards for a given duration.
        
        :param staking_duration_days: Duration of staking in days
        :return: Estimated rewards earned during the staking period
        """
        # Validate input values
        if self.amount_staked < 0:
            raise ValueError("Amount staked must be a non-negative value.")
        if self.annual_percentage_yield < 0:
            raise ValueError("Annual Percentage Yield must be a non-negative value.")
        if staking_duration_days < 0:
            raise ValueError("Staking duration must be a non-negative value.")

        # Calculate the daily yield from the annual yield
        daily_yield = self.annual_percentage_yield / 365
        
        # Calculate the total rewards over the staking period
        rewards = self.amount_staked * daily_yield * staking_duration_days
        return rewards

    def display_reward_summary(self, staking_duration_days):
        """
        Display a summary of the staking rewards.
        
        :param staking_duration_days: Duration of staking in days
        """
        try:
            rewards = self.calculate_rewards(staking_duration_days)
            print(f"Asset: {self.asset_name}")
            print(f"Amount Staked: {self.amount_staked} {self.asset_name}")
            print(f"Staking Duration: {staking_duration_days} days")
            print(f"Estimated Rewards: {rewards:.4f} {self.asset_name}")
        except ValueError as e:
            print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    # Initialize the staking calculator for BNB
    bnb_staker = StakingRewardCalculator(asset_name='BNB', amount_staked=1000, annual_percentage_yield=0.30)
    
    # Specify staking duration
    staking_duration = 30  # 30 days

    # Display staking rewards summary
    bnb_staker.display_reward_summary(staking_duration)
```
