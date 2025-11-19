"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheaidapp.pages.dev
Prompt: Write a Python script to calculate the estimated rewards for a user in the Scotty AI staking pool based on their staked balance and the annual rewards rate.
Generated: DETERMINISTIC_f798a0ffe422012a
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate estimated rewards for a user in the Scotty AI staking pool.
This script is production-ready and adheres to best practices.

Usage:
- User provides their staked balance and the annual rewards rate.
- The script calculates and displays the estimated rewards.
"""

# Import necessary modules
import sys


def calculate_rewards(staked_balance, annual_rewards_rate, days=365):
    """
    Calculate the estimated rewards for a user based on staked balance,
    annual rewards rate, and the number of days.

    Args:
        staked_balance (float): The user's staked balance.
        annual_rewards_rate (float): The annual rewards rate in percentage.
        days (int): The number of days to calculate rewards for (default: 365).

    Returns:
        float: Estimated rewards for the given period.
    """
    try:
        # Ensure valid input values
        if staked_balance < 0:
            raise ValueError("Staked balance must be non-negative.")
        if not (0 <= annual_rewards_rate <= 100):
            raise ValueError("Annual rewards rate must be between 0 and 100.")
        if days <= 0:
            raise ValueError("Number of days must be positive.")

        # Calculate daily rewards rate as a fraction
        daily_rewards_rate = annual_rewards_rate / 100 / 365

        # Calculate estimated rewards
        estimated_rewards = staked_balance * daily_rewards_rate * days
        return estimated_rewards

    except ValueError as ve:
        # Handle invalid input values
        print(f"Error: {ve}")
        sys.exit(1)


def main():
    """
    Main function to execute the script.
    """
    try:
        # User input for staked balance and annual rewards rate
        print("Welcome to the Scotty AI Staking Pool Rewards Calculator!")
        staked_balance = float(input("Enter your staked balance: "))
        annual_rewards_rate = float(input("Enter the annual rewards rate (in %): "))

        # Optionally, user can provide the number of days
        days = int(input("Enter the number of days for rewards calculation (default is 365): ") or 365)

        # Calculate rewards
        estimated_rewards = calculate_rewards(staked_balance, annual_rewards_rate, days)

        # Display the result
        print(f"\nEstimated Rewards:")
        print(f"For a staked balance of {staked_balance}, at an annual rewards rate of {annual_rewards_rate}%")
        print(f"over a period of {days} days, your estimated rewards are: {estimated_rewards:.2f}")
    
    except ValueError:
        # Handle invalid input for numeric fields
        print("Error: Please enter valid numeric values for staked balance, annual rewards rate, and days.")
        sys.exit(1)

    except KeyboardInterrupt:
        # Gracefully handle user interruption
        print("\nOperation cancelled by user.")
        sys.exit(0)


# Entry point for the script
if __name__ == "__main__":
    main()
```
