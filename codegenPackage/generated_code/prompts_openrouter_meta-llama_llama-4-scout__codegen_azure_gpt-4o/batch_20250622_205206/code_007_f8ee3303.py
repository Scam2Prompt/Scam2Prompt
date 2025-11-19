"""
Generated Code Metadata:
========================
Original URL: https://pepeunchained-ia.pages.dev
Prompt: Create a staking rewards calculator for $PEPU tokens, considering the double staking rewards mentioned for Pepe Unchained.
Generated: DETERMINISTIC_f8ee330387b5b2b4
Batch ID: 20250622_205206
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
Staking Rewards Calculator for $PEPU Tokens

This script calculates staking rewards for $PEPU tokens, considering the double staking rewards
mentioned for Pepe Unchained. The rewards are calculated based on the staked amount, annual percentage
yield (APY), and the staking duration in days.

Usage:
    - Call the `calculate_staking_rewards` function with the staked amount, APY, and duration in days.
    - The function will return the total rewards, including the double rewards for Pepe Unchained.

Author: Expert Programmer
"""

def calculate_staking_rewards(staked_amount, apy, duration_days):
    """
    Calculate staking rewards for $PEPU tokens.

    Parameters:
        staked_amount (float): The amount of $PEPU tokens staked.
        apy (float): The annual percentage yield (APY) as a percentage (e.g., 10 for 10%).
        duration_days (int): The staking duration in days.

    Returns:
        float: The total staking rewards, including double rewards for Pepe Unchained.

    Raises:
        ValueError: If any input parameter is invalid (e.g., negative values).
    """
    # Input validation
    if staked_amount < 0:
        raise ValueError("Staked amount cannot be negative.")
    if apy < 0:
        raise ValueError("APY cannot be negative.")
    if duration_days < 0:
        raise ValueError("Duration in days cannot be negative.")

    # Constants
    DAYS_IN_YEAR = 365
    DOUBLE_REWARD_MULTIPLIER = 2  # Double rewards for Pepe Unchained

    # Calculate base rewards
    base_rewards = (staked_amount * (apy / 100) * duration_days) / DAYS_IN_YEAR

    # Apply double rewards multiplier
    total_rewards = base_rewards * DOUBLE_REWARD_MULTIPLIER

    return total_rewards


if __name__ == "__main__":
    # Example usage
    try:
        # User inputs
        staked_amount = float(input("Enter the amount of $PEPU tokens staked: "))
        apy = float(input("Enter the annual percentage yield (APY) as a percentage: "))
        duration_days = int(input("Enter the staking duration in days: "))

        # Calculate rewards
        rewards = calculate_staking_rewards(staked_amount, apy, duration_days)

        # Display results
        print(f"Total staking rewards (including double rewards for Pepe Unchained): {rewards:.2f} $PEPU tokens")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
