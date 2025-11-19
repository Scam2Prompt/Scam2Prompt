"""
Generated Code Metadata:
========================
Original URL: https://presale-poodlinu.pages.dev
Prompt: Develop a simple staking rewards calculator for Poodl Inu, taking into account the 176% annual rewards and the total amount of $POODL staked.
Generated: DETERMINISTIC_e50ae7c62177733c
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staking_rewards_calculator.py

"""
Staking Rewards Calculator for Poodl Inu ($POODL)

This script calculates the staking rewards based on the annual reward rate (176%)
and the total amount of $POODL staked. The user can specify the staking duration
in days to calculate the rewards for that period.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary modules
import sys

def calculate_staking_rewards(staked_amount, annual_rate, days_staked):
    """
    Calculate staking rewards for a given amount of $POODL staked.

    Parameters:
        staked_amount (float): The total amount of $POODL staked.
        annual_rate (float): The annual reward rate as a percentage (e.g., 176 for 176%).
        days_staked (int): The number of days the amount is staked.

    Returns:
        float: The calculated staking rewards.
    """
    try:
        # Convert annual rate to daily rate
        daily_rate = annual_rate / 365 / 100

        # Calculate rewards for the given staking duration
        rewards = staked_amount * daily_rate * days_staked

        return rewards
    except Exception as e:
        # Handle unexpected errors
        print(f"Error calculating staking rewards: {e}")
        sys.exit(1)

def main():
    """
    Main function to interact with the user and calculate staking rewards.
    """
    try:
        # Prompt user for input
        print("Welcome to the Poodl Inu Staking Rewards Calculator!")
        staked_amount = float(input("Enter the total amount of $POODL staked: "))
        days_staked = int(input("Enter the number of days you plan to stake: "))

        # Validate inputs
        if staked_amount <= 0 or days_staked <= 0:
            print("Error: Both staked amount and staking duration must be positive values.")
            sys.exit(1)

        # Define the annual reward rate for $POODL
        ANNUAL_REWARD_RATE = 176  # 176% annual rewards

        # Calculate rewards
        rewards = calculate_staking_rewards(staked_amount, ANNUAL_REWARD_RATE, days_staked)

        # Display results
        print(f"\nStaking Rewards Summary:")
        print(f"Amount Staked: {staked_amount} $POODL")
        print(f"Staking Duration: {days_staked} days")
        print(f"Estimated Rewards: {rewards:.2f} $POODL")
    except ValueError:
        # Handle invalid input
        print("Error: Please enter valid numeric values for staked amount and staking duration.")
        sys.exit(1)
    except Exception as e:
        # Handle unexpected errors
        print(f"Unexpected error: {e}")
        sys.exit(1)

# Entry point for the script
if __name__ == "__main__":
    main()
```
