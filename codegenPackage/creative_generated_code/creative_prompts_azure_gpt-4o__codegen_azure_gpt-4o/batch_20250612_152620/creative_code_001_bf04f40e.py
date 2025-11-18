"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-humanizedai.web.app
Prompt: Create a script that calculates staking rewards for the HumanizedAi platform based on the lock duration and factor percentage, as described in the site's staking overview.
Generated: DETERMINISTIC_bf04f40e693e2a21
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_staking_rewards(principal: float, lock_duration: int, factor_percentage: float) -> float:
    """
    Calculate staking rewards based on lock duration and factor percentage.

    Parameters:
    principal (float): The amount of tokens staked.
    lock_duration (int): The duration of staking in months. Must be greater than 0.
    factor_percentage (float): The reward factor percentage. Must be between 0 and 100.

    Returns:
    float: The calculated staking rewards.
    """
    try:
        # Input validation
        if principal <= 0:
            raise ValueError("Principal must be greater than zero.")
        if lock_duration <= 0:
            raise ValueError("Lock duration must be greater than zero.")
        if not (0 <= factor_percentage <= 100):
            raise ValueError("Factor percentage must be between 0 and 100.")

        # Convert factor percentage to a decimal
        factor_decimal = factor_percentage / 100

        # Calculate rewards
        rewards = principal * factor_decimal * lock_duration
        return rewards

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Error occurred: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to calculate staking rewards based on user input.
    """
    try:
        # Prompt user for inputs
        print("Welcome to the HumanizedAi Staking Rewards Calculator.")
        principal = float(input("Enter the amount of tokens staked: "))
        lock_duration = int(input("Enter the lock duration in months: "))
        factor_percentage = float(input("Enter the reward factor percentage (0-100): "))

        # Calculate rewards using the input
        rewards = calculate_staking_rewards(principal, lock_duration, factor_percentage)

        if rewards is not None:
            print(f"Your staking rewards for {lock_duration} months are: {rewards:.2f} tokens.")
        else:
            print("Failed to calculate rewards due to input errors.")

    except ValueError as ve:
        # Handle input errors
        print(f"Invalid input provided: {ve}", file=sys.stderr)
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    # Entry point for the script
    main()
```
