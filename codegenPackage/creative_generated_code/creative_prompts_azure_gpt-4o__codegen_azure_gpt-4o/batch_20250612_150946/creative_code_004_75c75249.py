"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betswirl.pages.dev
Prompt: Write a Python function to calculate payouts for the dice game on BetSwirl based on player targets and rolled numbers.
Generated: DETERMINISTIC_75c75249e2624c25
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def calculate_payout(target: int, rolled_numbers: list[int], wager: float) -> float:
    """
    Calculate the payout for a BetSwirl dice game based on player target and rolled numbers.

    Args:
        target (int): The target number chosen by the player. Must be between 1 and 6.
        rolled_numbers (list[int]): The list of numbers rolled on the dice. Each number must be between 1 and 6.
        wager (float): The player's wager amount.

    Returns:
        float: The payout amount. Returns 0 if no rolled number matches the target.
    
    Raises:
        ValueError: If the target is not between 1 and 6 or if rolled_numbers contain invalid values.
        ValueError: If wager is negative or zero.
    """
    # Validate input
    if not (1 <= target <= 6):
        raise ValueError("Target must be a number between 1 and 6.")

    if not all(1 <= num <= 6 for num in rolled_numbers):
        raise ValueError("Rolled numbers must be between 1 and 6.")

    if wager <= 0:
        raise ValueError("Wager must be a positive amount.")

    # Calculate payout
    matches = rolled_numbers.count(target)  # Count how many dice match the target
    
    if matches == 0:
        return 0  # No match, no payout

    # Payout calculation: 2x wager for each match
    payout = matches * wager * 2
    return payout


# Example usage:
if __name__ == "__main__":
    try:
        # Simulate a dice roll
        rolled = [random.randint(1, 6) for _ in range(3)]  # Roll 3 dice
        print(f"Rolled numbers: {rolled}")
        
        target_number = 3  # Example target chosen by the player
        wager_amount = 50  # Example wager amount

        result = calculate_payout(target_number, rolled, wager_amount)
        print(f"Payout: ${result:.2f}")
    except ValueError as e:
        print(f"Error: {e}")  # Handle invalid input gracefully
```
