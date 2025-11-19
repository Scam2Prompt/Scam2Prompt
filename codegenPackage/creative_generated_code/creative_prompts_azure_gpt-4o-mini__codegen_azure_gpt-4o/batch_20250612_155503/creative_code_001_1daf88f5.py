"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earthmeta-net.web.app
Prompt: Write a Python script that calculates potential staking rewards based on the $EMT token's APY of 186% mentioned in the EarthMeta presale details.
Generated: DETERMINISTIC_1daf88f56459d8c5
Batch ID: 20250612_155503
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script: staking_rewards_calculator.py
Description: This script calculates potential staking rewards for the $EMT token based on an APY of 186%.
Author: Professional Developer
Date: YYYY-MM-DD
"""

# Import necessary modules
import sys

def calculate_staking_rewards(initial_investment: float, days: int, apy: float) -> float:
    """
    Calculate potential staking rewards for a given investment, duration, and APY.

    Args:
        initial_investment (float): The amount of $EMT tokens staked.
        days (int): The number of days the tokens are staked for.
        apy (float): The Annual Percentage Yield (APY) expressed as a percentage.

    Returns:
        float: The total amount of tokens (initial investment + rewards) after the staking period.
    """
    try:
        # Convert APY percentage into daily interest rate
        daily_rate = apy / 100 / 365
        
        # Calculate total rewards using compound interest formula
        total_amount = initial_investment * (1 + daily_rate) ** days

        return total_amount
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred while calculating staking rewards: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    """
    Main function to handle user input and display the staking rewards.
    """
    try:
        # Prompt user for initial investment, staking duration, and fixed APY
        print("Welcome to the $EMT Staking Rewards Calculator!")
        initial_investment = float(input("Enter your initial investment in $EMT tokens: "))
        days = int(input("Enter the number of days you plan to stake: "))
        fixed_apy = 186.0  # APY fixed to 186% based on EarthMeta presale details

        # Calculate staking rewards
        total_amount = calculate_staking_rewards(initial_investment, days, fixed_apy)

        # Display results
        rewards = total_amount - initial_investment
        print(f"\nResults:")
        print(f"Initial Investment: {initial_investment:.2f} $EMT")
        print(f"Staking Duration: {days} days")
        print(f"APY: {fixed_apy}%")
        print(f"Total Rewards Earned: {rewards:.2f} $EMT")
        print(f"Total Tokens After Staking: {total_amount:.2f} $EMT")
    except ValueError:
        # Handle invalid input for numerical values
        print("Invalid input. Please enter numerical values for investment and duration.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
