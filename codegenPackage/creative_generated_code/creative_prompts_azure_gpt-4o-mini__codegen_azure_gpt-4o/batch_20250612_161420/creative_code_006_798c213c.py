"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinucoin.pages.dev
Prompt: Create a script that calculates potential rewards from staking Poodl Inu based on the current staking percentage.
Generated: DETERMINISTIC_798c213cb034dd0e
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate potential rewards from staking Poodl Inu tokens.
Input: Number of tokens staked, annual staking percentage, staking duration (in months)
Output: Potential rewards
Author: Expert Programmer
"""

def calculate_staking_rewards(staked_tokens, annual_percentage, staking_duration_months):
    """
    Calculate potential staking rewards for Poodl Inu tokens.

    Args:
        staked_tokens (float): Number of tokens staked.
        annual_percentage (float): Annual staking percentage (e.g., 8.5 for 8.5%).
        staking_duration_months (int): Duration of staking in months.

    Returns:
        float: Potential rewards from staking.
    """
    try:
        # Validate inputs
        if staked_tokens <= 0:
            raise ValueError("Staked tokens must be greater than zero.")
        if annual_percentage <= 0:
            raise ValueError("Annual staking percentage must be greater than zero.")
        if staking_duration_months <= 0:
            raise ValueError("Staking duration must be greater than zero.")

        # Convert annual percentage to monthly percentage
        monthly_percentage = annual_percentage / 12 / 100  # Convert percentage to decimal

        # Calculate potential rewards
        rewards = staked_tokens * monthly_percentage * staking_duration_months
        return rewards
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Error calculating staking rewards: {e}")
        return None


def main():
    """
    Main function to prompt user inputs and calculate staking rewards.
    """
    print("Poodl Inu Staking Rewards Calculator")
    try:
        # Prompt user inputs
        staked_tokens = float(input("Enter the number of tokens staked: "))
        annual_percentage = float(input("Enter the annual staking percentage (e.g., 8.5 for 8.5%): "))
        staking_duration_months = int(input("Enter the staking duration (in months): "))

        # Calculate rewards
        rewards = calculate_staking_rewards(staked_tokens, annual_percentage, staking_duration_months)
        if rewards is not None:
            print(f"Potential rewards for staking {staked_tokens} tokens for {staking_duration_months} months at {annual_percentage}% annual interest: {rewards:.2f} tokens")
        else:
            print("Failed to calculate staking rewards due to input errors.")
    except ValueError as e:
        # Handle invalid user input
        print(f"Invalid input: {e}")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
