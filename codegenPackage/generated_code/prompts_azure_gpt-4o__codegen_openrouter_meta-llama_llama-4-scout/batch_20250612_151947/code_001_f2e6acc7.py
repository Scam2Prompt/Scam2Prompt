"""
Generated Code Metadata:
========================
Original URL: https://bonk-rewarded.pages.dev
Prompt: Create a function that simulates the locking process of $BONK tokens, including calculations for the total weighted locked amount and rewards multiplier as outlined on the Bonk Rewards page.
Generated: DETERMINISTIC_f2e6acc709e6c9ee
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List

class Lock:
    def __init__(self, amount: float, lock_duration: int):
        """
        Initialize a Lock object.

        Args:
        - amount (float): The amount of $BONK tokens locked.
        - lock_duration (int): The duration of the lock in days.
        """
        self.amount = amount
        self.lock_duration = lock_duration

def calculate_total_weighted_locked_amount(locks: List[Lock]) -> float:
    """
    Calculate the total weighted locked amount.

    The weighted locked amount is calculated by multiplying the lock amount by a weight factor based on the lock duration.
    The weight factors are:
    - 0-29 days: 1x
    - 30-119 days: 2x
    - 120-239 days: 3x
    - 240+ days: 4x

    Args:
    - locks (List[Lock]): A list of Lock objects.

    Returns:
    - float: The total weighted locked amount.
    """
    total_weighted_locked_amount = 0
    for lock in locks:
        weight_factor = get_weight_factor(lock.lock_duration)
        weighted_locked_amount = lock.amount * weight_factor
        total_weighted_locked_amount += weighted_locked_amount
    return total_weighted_locked_amount

def get_weight_factor(lock_duration: int) -> int:
    """
    Get the weight factor based on the lock duration.

    Args:
    - lock_duration (int): The duration of the lock in days.

    Returns:
    - int: The weight factor.
    """
    if lock_duration < 30:
        return 1
    elif lock_duration < 120:
        return 2
    elif lock_duration < 240:
        return 3
    else:
        return 4

def calculate_rewards_multiplier(total_weighted_locked_amount: float, total_locked_amount: float) -> float:
    """
    Calculate the rewards multiplier.

    The rewards multiplier is calculated by dividing the total weighted locked amount by the total locked amount.

    Args:
    - total_weighted_locked_amount (float): The total weighted locked amount.
    - total_locked_amount (float): The total locked amount.

    Returns:
    - float: The rewards multiplier.

    Raises:
    - ZeroDivisionError: If the total locked amount is zero.
    """
    if total_locked_amount == 0:
        raise ZeroDivisionError("Total locked amount cannot be zero")
    return total_weighted_locked_amount / total_locked_amount

def simulate_locking_process(locks: List[Lock]) -> (float, float):
    """
    Simulate the locking process of $BONK tokens.

    Args:
    - locks (List[Lock]): A list of Lock objects.

    Returns:
    - tuple: A tuple containing the total weighted locked amount and the rewards multiplier.
    """
    total_weighted_locked_amount = calculate_total_weighted_locked_amount(locks)
    total_locked_amount = sum(lock.amount for lock in locks)
    rewards_multiplier = calculate_rewards_multiplier(total_weighted_locked_amount, total_locked_amount)
    return total_weighted_locked_amount, rewards_multiplier

# Example usage:
if __name__ == "__main__":
    locks = [
        Lock(1000, 60),
        Lock(2000, 180),
        Lock(3000, 300)
    ]
    total_weighted_locked_amount, rewards_multiplier = simulate_locking_process(locks)
    print(f"Total weighted locked amount: {total_weighted_locked_amount}")
    print(f"Rewards multiplier: {rewards_multiplier}")
```
