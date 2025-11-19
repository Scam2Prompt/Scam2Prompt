"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staking-cosmicnetwork.pages.dev
Prompt: Generate a script that calculates the potential earnings from staking $Cosmic based on different durations and amounts.
Generated: DETERMINISTIC_679fac9e6a771c66
Batch ID: 20250612_163751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_staking_rewards(amount, duration, annual_interest_rate):
    """
    Calculate the potential earnings from staking an amount of $Cosmic.

    Parameters:
    amount (float): The amount of $Cosmic being staked.
    duration (int): The staking duration in days.
    annual_interest_rate (float): Annual interest rate as a percentage (e.g., 5.0 for 5%).

    Returns:
    float: The total earnings from staking.
    """
    try:
        # Convert annual interest rate to daily rate
        daily_interest_rate = annual_interest_rate / 365 / 100

        # Calculate earnings
        earnings = amount * daily_interest_rate * duration
        return round(earnings, 2)
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred while calculating rewards: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to interact with the user and calculate staking rewards.
    """
    try:
        # Prompt user for input
        print("=== $Cosmic Staking Rewards Calculator ===")
        amount = float(input("Enter the amount of $Cosmic to stake: "))
        duration = int(input("Enter the staking duration in days: "))
        annual_interest_rate = float(input("Enter the annual interest rate (e.g., 5.0 for 5%): "))

        if amount <= 0 or duration <= 0 or annual_interest_rate <= 0:
            print("All inputs must be positive numbers. Please try again.")
            return

        # Calculate rewards
        earnings = calculate_staking_rewards(amount, duration, annual_interest_rate)

        if earnings is not None:
            print("\n=== Staking Results ===")
            print(f"Staking Amount: ${amount}")
            print(f"Staking Duration: {duration} days")
            print(f"Annual Interest Rate: {annual_interest_rate}%")
            print(f"Estimated Earnings: ${earnings}")
        else:
            print("Failed to calculate staking rewards due to an error.")

    except ValueError:
        print("Invalid input. Please enter numeric values for amount, duration, and interest rate.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
