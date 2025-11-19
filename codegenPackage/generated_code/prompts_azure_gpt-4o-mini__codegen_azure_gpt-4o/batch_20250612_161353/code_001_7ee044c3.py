"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-dbz.pages.dev
Prompt: Write a Python script to calculate potential rewards from staking Green Bitcoin ($GBTC) based on different staking amounts and prediction outcomes.
Generated: DETERMINISTIC_7ee044c383361945
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_rewards(staking_amount, annual_percentage_rate, staking_duration_years):
    """
    Calculate potential rewards from staking Green Bitcoin ($GBTC).

    Parameters:
        staking_amount (float): The amount of $GBTC staked.
        annual_percentage_rate (float): The annual percentage rate (APR) for staking.
        staking_duration_years (float): The duration of staking in years.

    Returns:
        float: The total rewards earned from staking.
    """
    try:
        # Validate inputs
        if staking_amount <= 0:
            raise ValueError("Staking amount must be greater than zero.")
        if annual_percentage_rate <= 0:
            raise ValueError("Annual percentage rate must be greater than zero.")
        if staking_duration_years <= 0:
            raise ValueError("Staking duration must be greater than zero.")

        # Calculate rewards
        rewards = staking_amount * (annual_percentage_rate / 100) * staking_duration_years
        return rewards
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    """
    Main function to interact with the user and calculate staking rewards.
    """
    print("Welcome to the Green Bitcoin ($GBTC) Staking Rewards Calculator!")
    
    try:
        # Get user inputs
        staking_amount = float(input("Enter the amount of $GBTC you want to stake: "))
        annual_percentage_rate = float(input("Enter the annual percentage rate (APR) for staking (in %): "))
        staking_duration_years = float(input("Enter the staking duration (in years): "))

        # Calculate rewards
        rewards = calculate_rewards(staking_amount, annual_percentage_rate, staking_duration_years)

        # Display results
        print(f"\nBased on your inputs:")
        print(f"Staking Amount: {staking_amount} $GBTC")
        print(f"Annual Percentage Rate (APR): {annual_percentage_rate}%")
        print(f"Staking Duration: {staking_duration_years} years")
        print(f"Potential Rewards: {rewards:.2f} $GBTC")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
