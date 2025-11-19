"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitech-we.pages.dev
Prompt: Write a Python script to calculate the total rewards earned from staking AITECH at different APY rates.
Generated: DETERMINISTIC_a81c4b87d89ce67c
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

def calculate_staking_rewards(principal, apy_rate, staking_duration_months):
    """
    Calculate the total rewards earned from staking.

    Parameters:
        principal (float): The initial amount staked.
        apy_rate (float): Annual Percentage Yield (APY) rate as a percentage (e.g., 10 for 10%).
        staking_duration_months (int): The duration of staking in months.

    Returns:
        float: The total rewards earned.
    """
    try:
        # Convert APY rate to a decimal (e.g., 10% -> 0.10)
        apy_decimal = apy_rate / 100
        
        # Convert staking duration to years (e.g., 6 months -> 0.5 years)
        staking_duration_years = staking_duration_months / 12
        
        # Calculate total rewards using simple interest formula
        rewards = principal * apy_decimal * staking_duration_years
        
        return rewards
    except Exception as e:
        # Handle unexpected errors
        print(f"Error calculating staking rewards: {e}")
        sys.exit(1)

def main():
    """
    Main function to interact with the user and calculate staking rewards.
    """
    try:
        # Prompt user for staking details
        principal = float(input("Enter the principal amount staked (in AITECH): "))
        apy_rate = float(input("Enter the APY rate (as a percentage, e.g., 10 for 10%): "))
        staking_duration_months = int(input("Enter the staking duration (in months): "))

        # Validate inputs
        if principal <= 0 or apy_rate <= 0 or staking_duration_months <= 0:
            print("Error: All inputs must be positive numbers.")
            sys.exit(1)

        # Calculate rewards
        rewards = calculate_staking_rewards(principal, apy_rate, staking_duration_months)

        # Display results
        print(f"Total rewards earned from staking: {rewards:.2f} AITECH")
    except ValueError:
        # Handle invalid user input (e.g., non-numeric values)
        print("Error: Invalid input. Please enter numeric values.")
        sys.exit(1)
    except Exception as e:
        # Handle other unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Entry point of the script
if __name__ == "__main__":
    main()
```
