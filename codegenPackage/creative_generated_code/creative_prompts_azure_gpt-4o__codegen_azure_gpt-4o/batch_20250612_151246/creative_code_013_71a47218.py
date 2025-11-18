"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://7364500043-8sj.pages.dev
Prompt: Provide code to calculate staking rewards for USDe stablecoin on Solana, inspired by the "Ethena déploie son stablecoin USDe sur Solana" article on Journal Du Coin.
Generated: DETERMINISTIC_71a47218e9bc987d
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# staking_rewards.py

import time

class USDeStaking:
    """
    A class to manage staking rewards for USDe stablecoin on Solana.
    """

    def __init__(self, annual_percentage_yield: float):
        """
        Initialize the staking module with the annual percentage yield (APY).
        
        Args:
            annual_percentage_yield (float): The annual yield rate as a percentage. (e.g., 5.0 for 5%)
        """
        if annual_percentage_yield < 0:
            raise ValueError("APY cannot be negative.")
        self.apy = annual_percentage_yield / 100  # Convert percentage to decimal

    def calculate_rewards(self, staked_amount: float, staking_duration_days: int) -> float:
        """
        Calculate the staking rewards for a given amount and duration.
        
        Args:
            staked_amount (float): The amount of USDe staked.
            staking_duration_days (int): The number of days the amount was staked.

        Returns:
            float: The calculated rewards based on APY.
        """
        if staked_amount <= 0:
            raise ValueError("Staked amount must be greater than 0.")
        if staking_duration_days < 0:
            raise ValueError("Staking duration cannot be negative.")

        # Calculate rewards based on APY and duration
        daily_rate = self.apy / 365  # APY divided into daily rate
        rewards = staked_amount * daily_rate * staking_duration_days
        return rewards

def main():
    """
    Main function to demonstrate staking rewards calculation.
    """
    try:
        # Initialize the staking system with a 5% APY
        staking_system = USDeStaking(annual_percentage_yield=5.0)

        # Example user input
        staked_amount = float(input("Enter the amount of USDe staked: "))
        staking_duration_days = int(input("Enter the number of days staked: "))

        # Calculate rewards
        rewards = staking_system.calculate_rewards(staked_amount, staking_duration_days)
        print(f"Staking rewards after {staking_duration_days} days: {rewards:.2f} USDe")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
