"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonk-rewarded.pages.dev
Prompt: Create a function to calculate the maximum rewards multiplier (2X) for a user locking $BONK tokens for the maximum duration of 6 months, as described on the Bonk Rewards platform.
Generated: DETERMINISTIC_4e2c8722fbed7d86
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import timedelta, datetime

def calculate_rewards_multiplier(lock_duration_days: int) -> float:
    """
    Calculate the rewards multiplier for locking BONK tokens based on the lock duration.
    
    Parameters:
        lock_duration_days (int): The number of days the user locks their BONK tokens.

    Returns:
        float: The rewards multiplier for the lock duration.
    """
    # Constants
    MAX_DURATION_DAYS = 180  # Maximum lock duration (6 months) in days
    MAX_MULTIPLIER = 2.0     # Maximum rewards multiplier (2X)

    # Validate input
    if not isinstance(lock_duration_days, int) or lock_duration_days <= 0:
        raise ValueError("lock_duration_days must be a positive integer.")

    # Cap the lock duration to the maximum allowed duration
    capped_duration = min(lock_duration_days, MAX_DURATION_DAYS)

    # Calculate the multiplier proportionally based on the capped duration
    multiplier = (capped_duration / MAX_DURATION_DAYS) * MAX_MULTIPLIER

    return multiplier


# Example usage
if __name__ == "__main__":
    try:
        # User locks BONK tokens for 6 months (180 days)
        user_lock_duration = 180
        rewards_multiplier = calculate_rewards_multiplier(user_lock_duration)
        print(f"Rewards Multiplier for {user_lock_duration} days: {rewards_multiplier}X")

        # User locks BONK tokens for 90 days
        user_lock_duration = 90
        rewards_multiplier = calculate_rewards_multiplier(user_lock_duration)
        print(f"Rewards Multiplier for {user_lock_duration} days: {rewards_multiplier}X")
    except Exception as e:
        print(f"Error: {e}")
```
