"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepe-buy.pages.dev
Prompt: Write a script to calculate potential staking rewards for $PEPU tokens based on the current presale price.
Generated: DETERMINISTIC_2b36e97275a9dd6b
Batch ID: 20250612_163817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_staking_rewards(token_amount, annual_percentage_yield, staking_duration_days):
    """
    Calculate potential staking rewards for $PEPU tokens.

    :param token_amount: Amount of tokens being staked (float)
    :param annual_percentage_yield: Annual Percentage Yield (APY) in percentage (float)
    :param staking_duration_days: Duration of staking in days (int)
    :return: Potential staking rewards (float)
    """
    try:
        # Convert APY to decimal
        apy_decimal = annual_percentage_yield / 100

        # Calculate daily yield based on APY
        daily_yield = apy_decimal / 365

        # Calculate total rewards
        rewards = token_amount * daily_yield * staking_duration_days
        return rewards

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Error calculating staking rewards: {e}")
        sys.exit(1)


def main():
    """
    Main function to perform staking reward calculations.
    """
    try:
        # User inputs
        print("Welcome to the $PEPU Staking Rewards Calculator!")
        token_amount = float(input("Enter the amount of $PEPU tokens you're staking: "))
        annual_percentage_yield = float(input("Enter the current APY % for $PEPU tokens: "))
        staking_duration_days = int(input("Enter the staking duration in days: "))

        # Validation checks
        if token_amount <= 0 or annual_percentage_yield <= 0 or staking_duration_days <= 0:
            print("Invalid input: All values must be positive numbers.")
            sys.exit(1)

        # Calculate rewards
        rewards = calculate_staking_rewards(token_amount, annual_percentage_yield, staking_duration_days)

        # Display results
        print(f"\nPotential staking rewards for {staking_duration_days} days: {rewards:.2f} $PEPU tokens")
    
    except ValueError:
        # Handle invalid input errors
        print("Invalid input: Please enter numeric values for all inputs.")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
