"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-dashboard.pages.dev
Prompt: Write a Python script to calculate staking rewards for $PEPU tokens based on the 4509% annual reward rate mentioned in Pepe Unchained.
Generated: DETERMINISTIC_3c771199fc0078fe
Batch ID: 20250612_153447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import argparse
import sys


def validate_positive_float(value):
    """
    Validates that the input value is a positive float.

    Args:
        value (str): The input value as a string.

    Returns:
        float: The validated positive float value.

    Raises:
        argparse.ArgumentTypeError: If the input value is not a positive float.
    """
    try:
        float_value = float(value)
        if float_value <= 0:
            raise argparse.ArgumentTypeError("Value must be greater than zero.")
        return float_value
    except ValueError as e:
        raise argparse.ArgumentTypeError("Invalid number format.") from e


def calculate_staking_rewards(principal, days_staked, annual_rate=4509):
    """
    Calculates staking rewards for $PEPU tokens.

    Args:
        principal (float): The initial token balance.
        days_staked (int): The number of days tokens are staked.
        annual_rate (float): The annual reward rate in percentage.

    Returns:
        float: The total reward earned.
    """
    try:
        daily_rate = annual_rate / 100 / 365  # Convert annual rate to daily rate
        rewards = principal * daily_rate * days_staked
        return rewards
    except Exception as e:
        print(f"Error calculating staking rewards: {e}")
        sys.exit(1)


def main():
    """
    Main function to run the staking reward calculator.
    """
    parser = argparse.ArgumentParser(
        description="Calculate staking rewards for $PEPU tokens."
    )
    parser.add_argument(
        "principal",
        type=validate_positive_float,
        help="Initial token balance (must be a positive number).",
    )
    parser.add_argument(
        "days_staked",
        type=int,
        help="Number of days tokens are staked (must be a positive integer).",
    )
    args = parser.parse_args()

    principal = args.principal
    days_staked = args.days_staked

    if days_staked <= 0:
        print("Error: Number of days staked must be greater than zero.")
        sys.exit(1)

    try:
        rewards = calculate_staking_rewards(principal, days_staked)
        print(f"Staking Rewards for {days_staked} days: {rewards:.2f} $PEPU tokens")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
