"""
Generated Code Metadata:
========================
Original URL: https://wwwasterdex.com
Prompt: Generate code to calculate staking rewards on Aster DEX for assets like BNB, USDT, BTC, and CAKE, considering an APY of up to 30%+.
Generated: DETERMINISTIC_46816270ed1c1646
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class StakingRewardCalculator:
    """
    A class to calculate staking rewards for various assets on Aster DEX.
    """

    def __init__(self, asset, amount, apy):
        """
        Initializes the staking reward calculator.

        :param asset: str - The asset being staked (e.g., 'BNB', 'USDT', 'BTC', 'CAKE').
        :param amount: float - The amount of the asset being staked.
        :param apy: float - The annual percentage yield (APY) for the asset.
        """
        self.asset = asset
        self.amount = amount
        self.apy = apy / 100  # Convert APY from percentage to decimal

    def calculate_rewards(self, days):
        """
        Calculate the staking rewards for a given number of days.

        :param days: int - The number of days the asset is staked.
        :return: float - The calculated rewards.
        """
        if days < 0:
            raise ValueError("Number of days cannot be negative.")
        if self.amount < 0:
            raise ValueError("Staked amount cannot be negative.")
        
        # Calculate daily interest rate
        daily_rate = self.apy / 365
        # Calculate rewards
        rewards = self.amount * daily_rate * days
        return rewards

    def display_rewards(self, days):
        """
        Display the staking rewards in a formatted manner.

        :param days: int - The number of days the asset is staked.
        """
        try:
            rewards = self.calculate_rewards(days)
            print(f"Staking {self.amount} {self.asset} for {days} days at an APY of {self.apy * 100}% yields:")
            print(f"Total Rewards: {rewards:.4f} {self.asset}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        # Define assets and their respective APYs
        assets = {
            'BNB': 30,
            'USDT': 25,
            'BTC': 20,
            'CAKE': 35
        }

        # Staking parameters
        amount_staked = 1000  # Amount to stake
        staking_days = 30      # Number of days to stake

        # Calculate and display rewards for each asset
        for asset, apy in assets.items():
            calculator = StakingRewardCalculator(asset, amount_staked, apy)
            calculator.display_rewards(staking_days)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
