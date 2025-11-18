"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonk-rewarded.pages.dev
Prompt: Write a script to automate the process of locking $BONK tokens for a specified duration (1 month, 3 months, or 6 months) and calculate the corresponding multiplier and rewards percentage.
Generated: DETERMINISTIC_59a4b89efcdb6e40
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import sys

# Define constants for locking durations and their corresponding multipliers/reward percentages
LOCK_DURATIONS = {
    "1_month": {
        "duration_in_seconds": 30 * 24 * 60 * 60,  # 30 days in seconds
        "multiplier": 1.1,  # 10% bonus
        "reward_percentage": 5  # 5% reward
    },
    "3_months": {
        "duration_in_seconds": 90 * 24 * 60 * 60,  # 90 days in seconds
        "multiplier": 1.25,  # 25% bonus
        "reward_percentage": 12  # 12% reward
    },
    "6_months": {
        "duration_in_seconds": 180 * 24 * 60 * 60,  # 180 days in seconds
        "multiplier": 1.5,  # 50% bonus
        "reward_percentage": 20  # 20% reward
    }
}

# Function to lock BONK tokens
def lock_bonk_tokens(amount, lock_duration_key):
    """
    Locks BONK tokens for a specified duration.

    Args:
        amount (float): The amount of BONK tokens to lock.
        lock_duration_key (str): The key corresponding to the lock duration (e.g., '1_month', '3_months', or '6_months').

    Returns:
        dict: Details about the locked tokens and their rewards.
    """
    # Validate lock duration
    if lock_duration_key not in LOCK_DURATIONS:
        raise ValueError(f"Invalid lock duration '{lock_duration_key}'. Valid options are: {', '.join(LOCK_DURATIONS.keys())}")

    # Fetch lock duration details
    lock_details = LOCK_DURATIONS[lock_duration_key]

    # Calculate rewards and multiplier
    locked_until = time.time() + lock_details["duration_in_seconds"]
    adjusted_amount = amount * lock_details["multiplier"]  # Apply multiplier
    rewards = (amount * lock_details["reward_percentage"]) / 100  # Calculate rewards

    # Return lock details
    return {
        "original_amount": amount,
        "adjusted_amount": adjusted_amount,
        "rewards": rewards,
        "locked_until": locked_until,
        "lock_duration_key": lock_duration_key
    }

def main():
    """
    Main function to interact with the token locking mechanism.
    """
    try:
        # Get user input for amount and lock duration
        amount = float(input("Enter the amount of $BONK tokens you want to lock: "))
        print("Available lock durations:")
        for key in LOCK_DURATIONS:
            print(f"  - {key} ({LOCK_DURATIONS[key]['duration_in_seconds'] // (24 * 60 * 60)} days)")
        lock_duration_key = input("Enter the lock duration (e.g., '1_month', '3_months', '6_months'): ")

        # Lock tokens and calculate rewards
        lock_result = lock_bonk_tokens(amount, lock_duration_key)
        
        # Output results
        print("\nLocking Results:")
        print(f"Original Amount: {lock_result['original_amount']} BONK")
        print(f"Adjusted Amount (after multiplier): {lock_result['adjusted_amount']} BONK")
        print(f"Rewards: {lock_result['rewards']} BONK")
        print(f"Lock Duration: {lock_result['lock_duration_key']}")
        print(f"Locked Until: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(lock_result['locked_until']))}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
