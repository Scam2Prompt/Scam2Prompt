"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonkrewards-6st.pages.dev
Prompt: Develop a script to calculate and display the percentage of the BONK Rewards Pool a user would receive based on the amount of $BONK locked and the locking duration multiplier.
Generated: DETERMINISTIC_a0c2684c5cdfc9fd
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# bonk_rewards_calculator.py
"""
Script to calculate and display the percentage of the BONK Rewards Pool a user would receive.
This is based on the amount of $BONK locked and the locking duration multiplier.

Formula:
User's Reward Percentage = (User's Effective Stake / Total Effective Stake) * 100

Effective Stake = Amount Locked * Locking Duration Multiplier

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Required Libraries
import sys

def calculate_rewards_percentage(user_amount_locked, user_duration_multiplier, total_effective_stake):
    """
    Calculate the percentage reward of the BONK Rewards Pool for a user.

    Parameters:
        user_amount_locked (float): Amount of $BONK locked by the user.
        user_duration_multiplier (float): Locking duration multiplier for the user.
        total_effective_stake (float): Total effective stake in the rewards pool.

    Returns:
        float: Percentage of the reward pool the user would receive.
    """
    try:
        # Calculate user's effective stake
        user_effective_stake = user_amount_locked * user_duration_multiplier

        # Validate input
        if total_effective_stake <= 0:
            raise ValueError("Total effective stake must be greater than zero.")
        if user_effective_stake < 0:
            raise ValueError("User effective stake cannot be negative.")

        # Calculate reward percentage
        reward_percentage = (user_effective_stake / total_effective_stake) * 100
        return reward_percentage
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """
    Main function to prompt user input and calculate BONK Rewards Pool percentage.
    """
    print("BONK Rewards Pool Percentage Calculator")
    try:
        # Input user data
        user_amount_locked = float(input("Enter the amount of $BONK locked: "))
        user_duration_multiplier = float(input("Enter the locking duration multiplier: "))
        
        # Input total effective stake (usually provided by the system/administrator)
        total_effective_stake = float(input("Enter the total effective stake in the rewards pool: "))

        # Calculate the percentage reward
        percentage = calculate_rewards_percentage(user_amount_locked, user_duration_multiplier, total_effective_stake)

        # Display the result
        print(f"\nYou will receive {percentage:.2f}% of the BONK Rewards Pool.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
