"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stethpools.pages.dev
Prompt: Write a script to calculate the potential rewards from the stETH Pool based on an APY of 3.3% and a multiplier of 1.0x.
Generated: DETERMINISTIC_e969065f55b9585a
Batch ID: 20250612_161616
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

def calculate_rewards(staked_amount, apy, multiplier, duration_years):
    """
    Calculate the potential rewards from an stETH Pool based on APY and multiplier.

    Args:
        staked_amount (float): The amount of stETH staked.
        apy (float): Annual Percentage Yield (APY) in percentage.
        multiplier (float): Multiplier applied to rewards.
        duration_years (float): Duration of staking in years.

    Returns:
        float: The potential rewards earned.
    """
    try:
        # Validate inputs
        if staked_amount < 0:
            raise ValueError("Staked amount must be non-negative.")
        if apy < 0:
            raise ValueError("APY must be non-negative.")
        if multiplier < 0:
            raise ValueError("Multiplier must be non-negative.")
        if duration_years < 0:
            raise ValueError("Duration must be non-negative.")

        # Calculate rewards
        annual_rewards = staked_amount * (apy / 100)  # Convert APY percentage to decimal
        total_rewards = annual_rewards * multiplier * duration_years

        return total_rewards

    except (TypeError, ValueError) as e:
        # Handle invalid inputs
        print(f"Error: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to run the rewards calculation.
    """
    # Set fixed APY and multiplier values
    APY = 3.3  # APY percentage for stETH pool
    MULTIPLIER = 1.0  # Multiplier applied to rewards

    # Gather user input
    try:
        staked_amount = float(input("Enter the amount of stETH staked: "))
        duration_years = float(input("Enter the duration of staking in years: "))

        # Calculate potential rewards
        rewards = calculate_rewards(staked_amount, APY, MULTIPLIER, duration_years)

        if rewards is not None:
            print(f"Potential rewards after {duration_years} year(s): {rewards:.2f} stETH")
        else:
            print("Failed to calculate rewards due to invalid input.")

    except ValueError:
        print("Invalid input. Please enter numerical values for stETH amount and duration.", file=sys.stderr)


# Entry point for the script
if __name__ == "__main__":
    main()
```
