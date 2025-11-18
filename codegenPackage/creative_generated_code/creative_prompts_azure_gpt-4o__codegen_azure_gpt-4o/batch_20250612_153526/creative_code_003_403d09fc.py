"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheaidapp.pages.dev
Prompt: Generate a Python script to track the total staked $SCOTTY tokens and calculate the user's percentage of the staking pool based on their staked balance.
Generated: DETERMINISTIC_403d09fc619b6d5c
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to track the total staked $SCOTTY tokens and calculate a user's percentage of the staking pool.

# Import necessary module
import sys

def get_user_input(prompt):
    """
    Safely get user input, converting to float, and handle errors.
    :param prompt: The input prompt for the user.
    :return: A floating-point number entered by the user.
    """
    try:
        return float(input(prompt))
    except ValueError:
        print("Error: Please enter a valid numeric value.")
        sys.exit(1)

def calculate_user_percentage(total_staked, user_staked):
    """
    Calculate the percentage of the user's staked tokens in the staking pool.
    :param total_staked: Total staked tokens in the pool.
    :param user_staked: User's staked tokens.
    :return: Percentage of the staking pool owned by the user.
    """
    if total_staked <= 0:
        raise ValueError("Total staked tokens must be greater than zero.")
    return (user_staked / total_staked) * 100

def main():
    """
    Main function to execute staking pool percentage calculation.
    """
    print("=== $SCOTTY Staking Pool Percentage Tracker ===")
    
    # Input the total staked tokens in the pool
    total_staked = get_user_input("Enter the total staked $SCOTTY tokens in the pool: ")
    
    # Input the user's staked tokens
    user_staked = get_user_input("Enter your staked $SCOTTY tokens: ")
    
    try:
        # Calculate the user's percentage in the staking pool
        user_percentage = calculate_user_percentage(total_staked, user_staked)
        print(f"Your staking percentage in the pool: {user_percentage:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
