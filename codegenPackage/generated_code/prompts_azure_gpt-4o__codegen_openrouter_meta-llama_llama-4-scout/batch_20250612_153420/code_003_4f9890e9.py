"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-xyz.pages.dev
Prompt: Write a function in Python that calculates staking rewards for $SCOTTY tokens based on the lock period multiplier and APY, as described on the webpage.
Generated: DETERMINISTIC_4f9890e94948ea84
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

def calculate_staking_rewards(
    principal_amount: float, 
    apy: float, 
    lock_period_multiplier: Dict[int, float], 
    lock_period_in_days: int
) -> float:
    """
    Calculates staking rewards for $SCOTTY tokens.

    Args:
    - principal_amount (float): The initial amount of $SCOTTY tokens.
    - apy (float): The annual percentage yield.
    - lock_period_multiplier (Dict[int, float]): A dictionary mapping lock periods in days to their respective multipliers.
    - lock_period_in_days (int): The lock period in days.

    Returns:
    - float: The calculated staking reward.

    Raises:
    - ValueError: If the lock period in days is not found in the lock period multiplier dictionary.
    """

    # Check if the lock period in days is valid
    if lock_period_in_days not in lock_period_multiplier:
        raise ValueError("Invalid lock period. Please check the lock period multiplier dictionary.")

    # Convert APY to a decimal
    apy_decimal = apy / 100

    # Calculate the daily interest rate
    daily_interest_rate = apy_decimal / 365

    # Get the lock period multiplier
    multiplier = lock_period_multiplier[lock_period_in_days]

    # Calculate the staking reward
    staking_reward = principal_amount * daily_interest_rate * lock_period_in_days * multiplier

    return staking_reward


def main():
    # Example usage
    principal_amount = 1000.0  # Initial amount of $SCOTTY tokens
    apy = 10.0  # Annual percentage yield
    lock_period_multiplier = {
        30: 1.0,  # 30 days
        60: 1.5,  # 60 days
        90: 2.0   # 90 days
    }
    lock_period_in_days = 60  # Lock period in days

    try:
        staking_reward = calculate_staking_rewards(
            principal_amount, 
            apy, 
            lock_period_multiplier, 
            lock_period_in_days
        )
        print(f"Staking reward: ${staking_reward:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
