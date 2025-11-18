"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-token.pages.dev
Prompt: Write a script to calculate staking rewards for DOGE20 tokens based on the percentage of the staking pool and the fixed two-year distribution period.
Generated: DETERMINISTIC_e7b5ebbbd9ae99c1
Batch ID: 20250612_152710
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
    A class to calculate staking rewards for DOGE20 tokens based on the percentage 
    of the staking pool and a fixed two-year distribution period.
    """
    
    def __init__(self, total_rewards: float, duration_in_years: int = 2):
        """
        Initialize the calculator with total rewards and duration.

        Args:
            total_rewards (float): Total rewards distributed over the staking period.
            duration_in_years (int): Duration of staking rewards distribution in years (default is 2 years).
        """
        self.total_rewards = total_rewards
        self.duration_in_years = duration_in_years
        self.duration_in_days = duration_in_years * 365  # Assuming no leap years
    
    def calculate_daily_rewards(self):
        """
        Calculate the daily reward based on the total rewards and distribution period.

        Returns:
            float: The daily reward amount.
        """
        return self.total_rewards / self.duration_in_days
    
    def calculate_rewards(self, staking_pool_percentage: float, days_staked: int):
        """
        Calculate the rewards earned for a given staking pool percentage and staking duration.

        Args:
            staking_pool_percentage (float): The percentage of the staking pool owned (0-100).
            days_staked (int): Number of days the tokens were staked.

        Returns:
            float: The total rewards earned.
        """
        if not (0 <= staking_pool_percentage <= 100):
            raise ValueError("Staking pool percentage must be between 0 and 100.")
        if days_staked < 0:
            raise ValueError("Days staked cannot be negative.")
        
        daily_rewards = self.calculate_daily_rewards()
        # Convert percentage to a decimal (e.g., 50% -> 0.5)
        staking_share = staking_pool_percentage / 100
        # Calculate total rewards earned
        return daily_rewards * staking_share * days_staked


def main():
    """
    Main function to demonstrate reward calculation.
    """
    try:
        # Example configuration
        TOTAL_REWARDS = 5000000  # Total pool rewards in DOGE20 tokens
        TWO_YEARS = 2  # Distribution period in years

        # Create the calculator instance
        calculator = StakingRewardsCalculator(TOTAL_REWARDS, TWO_YEARS)

        # Input from user (or system)
        staking_percentage = float(input("Enter your staking pool percentage (0-100): "))
        days_staked = int(input("Enter the number of days you staked: "))

        # Calculate rewards
        rewards = calculator.calculate_rewards(staking_percentage, days_staked)
        print(f"Your staking rewards: {rewards:.2f} DOGE20 tokens")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
