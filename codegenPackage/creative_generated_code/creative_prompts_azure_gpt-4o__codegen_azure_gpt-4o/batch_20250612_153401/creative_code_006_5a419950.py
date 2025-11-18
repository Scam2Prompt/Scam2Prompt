"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deqodsmeta.web.app
Prompt: Write a function that calculates the staking rewards for DeGods and DeadGods, factoring in the daily $DUST generation rates (1.25 for DeGods and 3.75 for DeadGods).
Generated: DETERMINISTIC_5a419950111e1dc9
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_staking_rewards(degods_count, deadgods_count, days_staked):
    """
    Calculate the staking rewards for DeGods and DeadGods based on their daily $DUST generation rates.

    Parameters:
        degods_count (int): Number of DeGods staked.
        deadgods_count (int): Number of DeadGods staked.
        days_staked (int): Number of days the assets have been staked.

    Returns:
        float: Total $DUST rewards earned.
    """
    try:
        # Validate input data types
        if not isinstance(degods_count, int) or not isinstance(deadgods_count, int) or not isinstance(days_staked, int):
            raise ValueError("All inputs must be integers.")

        if degods_count < 0 or deadgods_count < 0 or days_staked < 0:
            raise ValueError("Counts and days staked must not be negative.")

        # Daily $DUST generation rates
        DEGODS_DAILY_RATE = 1.25
        DEADGODS_DAILY_RATE = 3.75

        # Calculate rewards
        degods_rewards = degods_count * DEGODS_DAILY_RATE * days_staked
        deadgods_rewards = deadgods_count * DEADGODS_DAILY_RATE * days_staked
        total_rewards = degods_rewards + deadgods_rewards

        return total_rewards

    except ValueError as e:
        # Handle invalid input errors
        print(f"Input error: {e}")
        return 0.0

    except Exception as e:
        # Catch any unexpected errors
        print(f"An unexpected error occurred: {e}")
        return 0.0


# Example usage:
# Calculate rewards for 10 DeGods, 5 DeadGods, staked for 30 days
rewards = calculate_staking_rewards(degods_count=10, deadgods_count=5, days_staked=30)
print(f"Total $DUST rewards earned: {rewards}")
```
