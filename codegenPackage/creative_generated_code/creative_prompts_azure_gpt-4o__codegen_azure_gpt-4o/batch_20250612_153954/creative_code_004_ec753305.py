"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jhwedfuhuifhw0928.xyz
Prompt: Write a script to calculate the total rewards earned per day based on the current APY and token balances provided by the Ethena platform.
Generated: DETERMINISTIC_ec7533052f48996b
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_daily_rewards(apy: float, token_balance: float) -> float:
    """
    Calculate the total rewards earned per day based on the current APY and token balance.

    Args:
        apy (float): The annual percentage yield (APY) as a percentage (e.g., 5.0 for 5% APY).
        token_balance (float): The balance of tokens held.

    Returns:
        float: The daily rewards earned.
    """
    try:
        # Validate inputs
        if apy < 0 or token_balance < 0:
            raise ValueError("APY and token balance must be non-negative numbers.")

        # Convert APY percentage to a decimal (e.g., 5% -> 0.05)
        apy_decimal = apy / 100

        # Calculate daily rewards (APY divided by 365 days)
        daily_rewards = (token_balance * apy_decimal) / 365

        return daily_rewards

    except ValueError as ve:
        print(f"ValueError: {ve}", file=sys.stderr)
        raise
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        raise


def main():
    """
    Main function to calculate daily rewards based on user-provided APY and token balance.
    """
    print("Welcome to the Ethena Rewards Calculator!")
    try:
        # Prompt the user for inputs
        apy = float(input("Enter the APY (Annual Percentage Yield) as a percentage (e.g., 5 for 5%): "))
        token_balance = float(input("Enter your token balance: "))

        # Calculate daily rewards
        daily_rewards = calculate_daily_rewards(apy, token_balance)

        # Display the result
        print(f"Based on your APY of {apy}% and token balance of {token_balance}, "
              f"your daily rewards are: {daily_rewards:.6f}")
    except ValueError:
        print("Invalid input. Please ensure you enter numeric values for APY and token balance.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    # Entry point of the script
    main()
```
