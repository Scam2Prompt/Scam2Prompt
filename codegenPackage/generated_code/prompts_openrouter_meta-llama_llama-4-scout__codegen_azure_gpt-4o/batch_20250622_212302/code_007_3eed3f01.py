"""
Generated Code Metadata:
========================
Original URL: https://thenafl.org
Prompt: Create a simple staking rewards calculator for THENA FI's ecosystem.
Generated: DETERMINISTIC_3eed3f016d132700
Batch ID: 20250622_212302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staking_rewards_calculator.py

# Import necessary modules
import sys

def calculate_staking_rewards(staked_amount, annual_percentage_rate, days_staked):
    """
    Calculate staking rewards based on the staked amount, APR, and staking duration.

    Parameters:
        staked_amount (float): The amount of tokens staked.
        annual_percentage_rate (float): The annual percentage rate (APR) as a percentage (e.g., 12.5 for 12.5% APR).
        days_staked (int): The number of days the tokens are staked.

    Returns:
        float: The calculated staking rewards.
    """
    try:
        # Validate inputs
        if staked_amount <= 0:
            raise ValueError("Staked amount must be greater than zero.")
        if annual_percentage_rate <= 0:
            raise ValueError("APR must be greater than zero.")
        if days_staked <= 0:
            raise ValueError("Days staked must be greater than zero.")

        # Convert APR from percentage to decimal
        apr_decimal = annual_percentage_rate / 100

        # Calculate daily rewards rate
        daily_rate = apr_decimal / 365

        # Calculate rewards
        rewards = staked_amount * daily_rate * days_staked

        return rewards

    except ValueError as ve:
        print(f"Input Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def main():
    """
    Main function to interact with the user and calculate staking rewards.
    """
    print("Welcome to the THENA FI Staking Rewards Calculator!")

    try:
        # Get user inputs
        staked_amount = float(input("Enter the amount of tokens staked: "))
        annual_percentage_rate = float(input("Enter the annual percentage rate (APR) in %: "))
        days_staked = int(input("Enter the number of days staked: "))

        # Calculate rewards
        rewards = calculate_staking_rewards(staked_amount, annual_percentage_rate, days_staked)

        # Display results
        print(f"\nStaking Rewards Summary:")
        print(f"Staked Amount: {staked_amount} tokens")
        print(f"APR: {annual_percentage_rate}%")
        print(f"Days Staked: {days_staked} days")
        print(f"Estimated Rewards: {rewards:.6f} tokens")

    except ValueError:
        print("Invalid input. Please enter numeric values for staked amount, APR, and days staked.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
