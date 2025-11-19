"""
Generated Code Metadata:
========================
Original URL: https://my-greenbitcoin.pages.dev
Prompt: "Write a Python script to calculate the potential earnings from staking Green Bitcoin ($GBTC) using the Gamified Green Staking mechanic, considering a 100% token bonus and exponential rewards."
Generated: DETERMINISTIC_84a1ea1bcd69be2a
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate potential earnings from staking Green Bitcoin ($GBTC) using the Gamified Green Staking mechanic.
The calculation considers:
1. A 100% token bonus.
2. Exponential rewards based on the staking duration.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary modules
import math

def calculate_staking_rewards(initial_tokens, staking_duration_days, annual_reward_rate):
    """
    Calculate potential earnings from staking $GBTC.

    Parameters:
        initial_tokens (float): The number of $GBTC tokens initially staked.
        staking_duration_days (int): The duration of staking in days.
        annual_reward_rate (float): The annual reward rate (as a percentage).

    Returns:
        float: Total tokens earned after staking, including the 100% bonus and exponential rewards.
    """
    try:
        # Validate inputs
        if initial_tokens <= 0:
            raise ValueError("Initial tokens must be greater than zero.")
        if staking_duration_days <= 0:
            raise ValueError("Staking duration must be greater than zero.")
        if annual_reward_rate <= 0:
            raise ValueError("Annual reward rate must be greater than zero.")

        # Apply 100% token bonus
        tokens_with_bonus = initial_tokens * 2

        # Calculate exponential rewards
        # Convert annual reward rate to daily rate
        daily_reward_rate = annual_reward_rate / 365 / 100
        # Calculate total rewards using exponential growth formula
        exponential_rewards = tokens_with_bonus * math.exp(daily_reward_rate * staking_duration_days)

        return exponential_rewards

    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def main():
    """
    Main function to execute the staking rewards calculation.
    """
    print("Welcome to the $GBTC Staking Rewards Calculator!")

    try:
        # User input
        initial_tokens = float(input("Enter the number of $GBTC tokens you want to stake: "))
        staking_duration_days = int(input("Enter the staking duration in days: "))
        annual_reward_rate = float(input("Enter the annual reward rate (as a percentage): "))

        # Calculate rewards
        total_rewards = calculate_staking_rewards(initial_tokens, staking_duration_days, annual_reward_rate)

        if total_rewards is not None:
            print(f"\nPotential earnings after staking:")
            print(f"Initial Tokens Staked: {initial_tokens}")
            print(f"Staking Duration: {staking_duration_days} days")
            print(f"Annual Reward Rate: {annual_reward_rate}%")
            print(f"Total Tokens Earned (including bonus and exponential rewards): {total_rewards:.2f} $GBTC")
        else:
            print("Failed to calculate staking rewards due to input errors.")

    except ValueError:
        print("Invalid input. Please enter numeric values for tokens, duration, and reward rate.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
