"""
Generated Code Metadata:
========================
Original URL: https://cryptoallstars-3ts.pages.dev
Prompt: Generate code to calculate potential rewards for holding and staking $STARS tokens based on the current APY.
Generated: DETERMINISTIC_e4fb73cf77ac80b1
Batch ID: 20250612_155910
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_staking_rewards(stars_amount, apy, staking_period_days):
    """
    Calculate potential rewards for holding and staking $STARS tokens.

    Parameters:
        stars_amount (float): The amount of $STARS tokens being staked.
        apy (float): The annual percentage yield (APY) as a percentage (e.g., 12.5 for 12.5% APY).
        staking_period_days (int): The number of days the tokens are staked.

    Returns:
        float: The estimated rewards earned from staking.
    """
    try:
        # Validate inputs
        if stars_amount <= 0:
            raise ValueError("The amount of $STARS tokens must be greater than zero.")
        if apy <= 0:
            raise ValueError("APY must be greater than zero.")
        if staking_period_days <= 0:
            raise ValueError("Staking period must be greater than zero.")

        # Convert APY from percentage to decimal
        apy_decimal = apy / 100

        # Calculate daily yield
        daily_yield = apy_decimal / 365

        # Calculate rewards
        rewards = stars_amount * daily_yield * staking_period_days

        return rewards

    except ValueError as ve:
        print(f"Input Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None


if __name__ == "__main__":
    # Example usage
    try:
        # Input values
        stars_amount = float(input("Enter the amount of $STARS tokens to stake: "))
        apy = float(input("Enter the APY (Annual Percentage Yield) as a percentage: "))
        staking_period_days = int(input("Enter the staking period in days: "))

        # Calculate rewards
        rewards = calculate_staking_rewards(stars_amount, apy, staking_period_days)

        if rewards is not None:
            print(f"Estimated rewards for staking {stars_amount} $STARS tokens for {staking_period_days} days at {apy}% APY: {rewards:.6f} $STARS")
        else:
            print("Failed to calculate rewards due to input errors or unexpected issues.")

    except ValueError:
        print("Invalid input. Please ensure you enter numeric values for all inputs.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
```
