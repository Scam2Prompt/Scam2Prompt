"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astedrex.com
Prompt: Generate code to calculate APY for staking assets like BNB, USDT, BTC, and CAKE on Aster's platform, incorporating the 30%+ APY rewards mentioned.
Generated: DETERMINISTIC_fac98f4bc5693030
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class StakingAPYCalculator:
    """
    A class to calculate APY (Annual Percentage Yield) for staking assets.
    """
    def __init__(self, apy_rate: float):
        """
        Initialize the calculator with a given APY rate.

        :param apy_rate: Annual Percentage Yield percentage (e.g., 30 for 30%)
        """
        if apy_rate <= 0:
            raise ValueError("APY rate must be greater than 0")
        self.apy_rate = apy_rate / 100  # Convert percentage to decimal

    def calculate_apy(self, principal: float, duration_days: int) -> float:
        """
        Calculate the rewards earned for a given principal over a staking duration.

        :param principal: The amount of assets staked (e.g., BNB, USDT, BTC, CAKE)
        :param duration_days: The number of days the assets are staked
        :return: The total rewards earned over the staking duration
        """
        if principal <= 0:
            raise ValueError("Principal amount must be greater than 0")
        if duration_days <= 0:
            raise ValueError("Duration days must be greater than 0")
        
        # Calculate APY rewards using compounding formula
        yearly_rewards = principal * self.apy_rate
        daily_rewards = yearly_rewards / 365  # Approx daily rewards
        total_rewards = daily_rewards * duration_days
        return total_rewards

    def display_rewards_breakdown(self, principal: float, duration_days: int):
        """
        Display a detailed breakdown of the staking rewards.

        :param principal: The amount of assets staked
        :param duration_days: The number of days the assets are staked
        """
        try:
            total_rewards = self.calculate_apy(principal, duration_days)
            breakdown = {
                "Principal": principal,
                "Staking Duration (days)": duration_days,
                "APY Rate (%)": self.apy_rate * 100,
                "Total Rewards": round(total_rewards, 2),
            }
            print(json.dumps(breakdown, indent=4))
        except ValueError as e:
            print(f"Error: {e}")


def main():
    """
    Main function to test the StakingAPYCalculator.
    """
    try:
        # Example APY rate: 30%
        apy_calculator = StakingAPYCalculator(apy_rate=30)
        
        # Example assets and duration
        staking_assets = {
            "BNB": 1000,  # Amount staked
            "USDT": 5000,
            "BTC": 0.1,
            "CAKE": 200,
        }
        duration_days = 90  # Example staking duration

        print("Staking APY Rewards Breakdown:")
        for asset, amount in staking_assets.items():
            print(f"\nAsset: {asset}")
            apy_calculator.display_rewards_breakdown(principal=amount, duration_days=duration_days)
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
```
