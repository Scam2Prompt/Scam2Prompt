"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staklngstoryfoundatlon.org
Prompt: Develop a program to calculate estimated rewards based on the APR and total staked amount for validators on the Story Staking platform.
Generated: DETERMINISTIC_0d74b05de2583c8a
Batch ID: 20250612_154657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to calculate estimated rewards based on APR and total staked amount
# Developed for the Story Staking platform

# Import necessary libraries
from decimal import Decimal, getcontext

# Set up decimal precision for financial calculations
getcontext().prec = 10

def calculate_rewards(apr, staked_amount, days=365):
    """
    Calculate estimated rewards based on APR, staked amount, and staking period.

    Parameters:
    - apr (float): Annual Percentage Rate as a percentage (e.g., 10 for 10%).
    - staked_amount (float): The total amount staked in the validator (in tokens).
    - days (int): Number of days the rewards are calculated for (default: 365).

    Returns:
    - Decimal: Estimated rewards for the staking period.
    """
    try:
        # Validate input types and ranges
        if apr < 0 or staked_amount < 0 or days <= 0:
            raise ValueError("APR, staked amount, and days must be positive values.")

        # Convert inputs to Decimal for precision
        apr_decimal = Decimal(apr) / Decimal(100)  # Convert APR percentage to a multiplier
        staked_amount_decimal = Decimal(staked_amount)
        days_decimal = Decimal(days)

        # Calculate daily rewards rate
        daily_rate = apr_decimal / Decimal(365)

        # Calculate total rewards for the staking period
        estimated_rewards = staked_amount_decimal * daily_rate * days_decimal

        return estimated_rewards

    except Exception as e:
        # Handle invalid input or calculation errors
        print(f"Error calculating rewards: {e}")
        return None

def main():
    """
    Main function to interact with the user and calculate staking rewards.
    """
    print("Welcome to the Story Staking Rewards Calculator!")

    try:
        # Input APR
        apr = float(input("Enter the APR (Annual Percentage Rate) as a percentage (e.g., 10 for 10%): "))

        # Input staked amount
        staked_amount = float(input("Enter the total staked amount (in tokens): "))

        # Input staking period in days
        days = int(input("Enter the staking period (in days, default is 365): ") or 365)

        # Calculate rewards
        rewards = calculate_rewards(apr, staked_amount, days)

        if rewards is not None:
            print(f"\nEstimated rewards for {days} days: {rewards:.10f} tokens.")
        else:
            print("Unable to calculate rewards due to an error.")

    except ValueError:
        print("Invalid input. Please enter numeric values for APR, staked amount, and days.")

if __name__ == "__main__":
    main()
```
