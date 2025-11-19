"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoin-dbz.pages.dev
Prompt: Write a Python script to calculate potential rewards from staking Green Bitcoin ($GBTC) based on different staking amounts and prediction outcomes.
Generated: DETERMINISTIC_7ee044c383361945
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_rewards(staking_amount, annual_percentage_rate, staking_duration):
    """
    Calculate the potential rewards from staking Green Bitcoin ($GBTC).

    Args:
        staking_amount (float): The amount of $GBTC staked (in GBTC).
        annual_percentage_rate (float): The annual percentage rate (APR) for staking (in percent).
        staking_duration (float): Staking duration in years.

    Returns:
        float: The total rewards earned from staking.
    """
    try:
        if staking_amount <= 0:
            raise ValueError("Staking amount must be greater than zero.")
        if annual_percentage_rate <= 0:
            raise ValueError("Annual percentage rate (APR) must be greater than zero.")
        if staking_duration <= 0:
            raise ValueError("Staking duration must be greater than zero.")

        # Convert APR from percentage to a decimal
        APR_decimal = annual_percentage_rate / 100

        # Calculate rewards
        rewards = staking_amount * APR_decimal * staking_duration
        return rewards

    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def main():
    """
    Main function to interact with the user and calculate staking rewards.
    """
    print("Welcome to the Green Bitcoin ($GBTC) Staking Reward Calculator!")

    try:
        # Collect user input
        staking_amount = float(input("Enter the staking amount ($GBTC): "))
        annual_percentage_rate = float(input("Enter the annual percentage rate (APR) (%): "))
        staking_duration = float(input("Enter the staking duration (years): "))

        # Calculate rewards
        rewards = calculate_rewards(staking_amount, annual_percentage_rate, staking_duration)
        print(f"\nBased on your inputs:")
        print(f"Staking Amount: {staking_amount} $GBTC")
        print(f"Annual Percentage Rate (APR): {annual_percentage_rate}%")
        print(f"Staking Duration: {staking_duration} years")
        print(f"\nPotential Rewards: {rewards:.2f} $GBTC")

    except ValueError:
        print("Invalid input. Please ensure all values are numeric.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
