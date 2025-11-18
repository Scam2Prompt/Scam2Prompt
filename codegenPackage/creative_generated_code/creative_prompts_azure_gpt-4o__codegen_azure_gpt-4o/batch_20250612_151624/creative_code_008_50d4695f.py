"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://floki-reward.com
Prompt: Create a Python script to calculate staking rewards for $FLOKI tokens based on user input, such as amount staked and duration, using Floki's staking program parameters.
Generated: DETERMINISTIC_50d4695fc95f8996
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate staking rewards for $FLOKI tokens based on user input.
The calculation is based on Floki's staking program parameters.
"""

# Import necessary modules
import sys

def calculate_staking_rewards(amount_staked, staking_duration):
    """
    Calculate staking rewards for $FLOKI tokens based on amount staked and duration.

    Parameters:
        amount_staked (float): The amount of $FLOKI tokens staked.
        staking_duration (int): The staking duration in days.

    Returns:
        float: The total rewards earned.
    """
    # Floki's staking program parameters (example values; adjust as needed)
    ANNUAL_PERCENTAGE_YIELD = 0.12  # 12% APY
    DAYS_IN_YEAR = 365  # Number of days in a year

    try:
        # Ensure valid inputs
        if amount_staked <= 0 or staking_duration <= 0:
            raise ValueError("Amount staked and staking duration must be positive values.")

        # Calculate daily yield
        daily_yield = ANNUAL_PERCENTAGE_YIELD / DAYS_IN_YEAR

        # Calculate total rewards
        total_rewards = amount_staked * daily_yield * staking_duration
        return total_rewards

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def main():
    """
    Main function to handle user inputs and calculate staking rewards.
    """
    try:
        print("Welcome to the $FLOKI Staking Rewards Calculator!")
        
        # Prompt user for input
        amount_staked = float(input("Enter the amount of $FLOKI tokens staked: "))
        staking_duration = int(input("Enter the staking duration in days: "))

        # Calculate rewards
        rewards = calculate_staking_rewards(amount_staked, staking_duration)

        if rewards is not None:
            print(f"\nEstimated Staking Rewards: {rewards:.2f} $FLOKI")
        else:
            print("\nCould not calculate rewards due to invalid input.")

    except ValueError:
        print("Invalid input. Please enter valid numerical values.")
    except KeyboardInterrupt:
        print("\nCalculation interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the $FLOKI Staking Rewards Calculator!")


# Entry-point guard
if __name__ == "__main__":
    main()
```
