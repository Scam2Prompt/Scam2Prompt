"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.earthmeta.xyzapp.net
Prompt: Develop a Python script to calculate staking rewards for $EMT tokens based on the presale allocation and APY rates provided in the EarthMeta ecosystem.
Generated: DETERMINISTIC_44ff62c70fb67894
Batch ID: 20250612_145526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_staking_rewards(presale_allocation: float, apy_rate: float, staking_period_days: int) -> float:
    """
    Calculate staking rewards for $EMT tokens.

    Args:
        presale_allocation (float): The number of $EMT tokens allocated during presale.
        apy_rate (float): The Annual Percentage Yield (APY) rate as a percentage (e.g., 10.0 for 10% APY).
        staking_period_days (int): The number of days the tokens are staked.

    Returns:
        float: The staking rewards earned over the given period.
    """
    # Ensure valid input values
    if presale_allocation <= 0:
        raise ValueError("Presale allocation must be greater than 0.")
    if apy_rate < 0:
        raise ValueError("APY rate cannot be negative.")
    if staking_period_days <= 0:
        raise ValueError("Staking period must be greater than 0 days.")

    # Convert APY rate from percentage to fraction
    apy_fraction = apy_rate / 100.0

    # Calculate daily staking rate
    daily_rate = apy_fraction / 365

    # Calculate rewards for the staking period
    rewards = presale_allocation * daily_rate * staking_period_days

    return rewards


def main():
    """
    Main function to calculate and display staking rewards for $EMT tokens.
    """
    try:
        # Prompt user for input values
        presale_allocation = float(input("Enter your presale allocation of $EMT tokens: "))
        apy_rate = float(input("Enter the APY rate (as a percentage, e.g., 10 for 10%): "))
        staking_period_days = int(input("Enter the staking period in days: "))

        # Calculate staking rewards
        rewards = calculate_staking_rewards(presale_allocation, apy_rate, staking_period_days)

        # Display the results
        print(f"\nStaking Rewards Calculation:")
        print(f"Presale Allocation: {presale_allocation} EMT")
        print(f"APY Rate: {apy_rate}%")
        print(f"Staking Period: {staking_period_days} days")
        print(f"Estimated Staking Rewards: {rewards:.6f} EMT")

    except ValueError as ve:
        # Handle invalid input values
        print(f"Input Error: {ve}")
    except Exception as ex:
        # Handle unforeseen exceptions
        print(f"An unexpected error occurred: {ex}")
        sys.exit(1)


if __name__ == "__main__":
    # Entry point of the script
    main()
```
