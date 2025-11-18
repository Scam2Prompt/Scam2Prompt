"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zealyi.github.io
Prompt: Create a Python script to calculate the annual percentage yield (APY) for the ORB/ETH liquidity pool on Zealy, considering high rewards exceeding 1,000%.
Generated: DETERMINISTIC_3a9f1b51c4ac50ad
Batch ID: 20250612_150858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sys

def calculate_apy(reward_rate: float, period_in_days: int) -> float:
    """
    Calculate the Annual Percentage Yield (APY) given the reward rate 
    and the time period over which rewards are calculated.

    Args:
        reward_rate (float): The reward rate for the liquidity pool in percentage terms (e.g., 1200 for 1200%).
        period_in_days (int): The duration (in days) over which the reward rate applies.

    Returns:
        float: The calculated APY in percentage terms.
    """
    try:
        if period_in_days <= 0:
            raise ValueError("Period in days must be a positive integer.")

        # Convert reward rate from percentage to decimal
        decimal_reward_rate = reward_rate / 100

        # Calculate APY using the formula: APY = (1 + r/n)^n - 1
        # where r is the decimal reward rate and n is the number of periods in a year.
        periods_in_a_year = 365 / period_in_days
        apy = (1 + decimal_reward_rate) ** periods_in_a_year - 1

        # Convert APY from decimal to percentage
        return apy * 100
    except Exception as e:
        print(f"Error calculating APY: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to prompt user input and calculate APY for the ORB/ETH liquidity pool.
    """
    try:
        print("Welcome to the APY Calculator for the ORB/ETH Liquidity Pool on Zealy!")

        # Prompting user for input values
        reward_rate = float(input("Enter the reward rate (as a percentage, e.g., 1200 for 1200%): "))
        period_in_days = int(input("Enter the period (in days) for the reward rate: "))

        # Calculate APY
        apy = calculate_apy(reward_rate, period_in_days)

        if apy is not None:
            print(f"The Annual Percentage Yield (APY) is: {apy:.2f}%")
        else:
            print("APY calculation failed. Please check your inputs.")
    except ValueError as ve:
        print(f"Invalid input: {ve}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


# Entry point for the script
if __name__ == "__main__":
    main()
```
