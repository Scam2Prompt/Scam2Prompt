"""
Generated Code Metadata:
========================
Original URL: https://bonk-rewarded.pages.dev
Prompt: Write a Python script to calculate the BONK rewards for a user locking a certain amount of $BONK for a specified duration, considering the multiplier and total locked amount.
Generated: DETERMINISTIC_4accf406317bbbf4
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
BONK Rewards Calculator Script

Calculates the BONK rewards for a user locking a certain amount of $BONK for a specified duration,
considering the multiplier and total locked amount.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_bonk_rewards(
    lock_amount: float, 
    lock_duration: int, 
    multiplier: float, 
    total_locked_amount: float
) -> float:
    """
    Calculates the BONK rewards.

    Args:
    - lock_amount (float): The amount of $BONK locked by the user.
    - lock_duration (int): The duration for which the $BONK is locked.
    - multiplier (float): The multiplier for the lock duration.
    - total_locked_amount (float): The total amount of $BONK locked.

    Returns:
    - float: The calculated BONK rewards.

    Raises:
    - ValueError: If any of the input values are invalid (e.g., negative).
    """

    # Validate input values
    if lock_amount < 0 or lock_duration < 0 or multiplier < 0 or total_locked_amount < 0:
        raise ValueError("All input values must be non-negative.")

    # Calculate BONK rewards
    try:
        # Assuming the reward is calculated as (lock_amount * lock_duration * multiplier) / total_locked_amount
        bonk_rewards = (lock_amount * lock_duration * multiplier) / total_locked_amount if total_locked_amount != 0 else 0
        return bonk_rewards
    except ZeroDivisionError:
        # Handle division by zero error
        raise ValueError("Total locked amount cannot be zero.")


def main():
    try:
        # Example usage
        lock_amount = 1000.0  # $BONK
        lock_duration = 30  # days
        multiplier = 1.5
        total_locked_amount = 100000.0  # $BONK

        bonk_rewards = calculate_bonk_rewards(lock_amount, lock_duration, multiplier, total_locked_amount)
        print(f"Calculated BONK rewards: {bonk_rewards:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
