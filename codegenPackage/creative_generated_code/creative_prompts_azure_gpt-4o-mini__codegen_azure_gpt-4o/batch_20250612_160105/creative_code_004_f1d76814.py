"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkstacks.in
Prompt: Create a function that calculates odds for lottery games similar to those found on "dear lottery today."
Generated: DETERMINISTIC_f1d768146d042564
Batch ID: 20250612_160105
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_lottery_odds(total_numbers: int, numbers_to_pick: int) -> float:
    """
    Calculate the odds of winning a lottery game.

    This function computes the probability of winning a lottery game where you pick a
    specific number of numbers from a larger pool of numbers. The calculation is based
    on combinations (nCr), which determine the number of ways to choose numbers_to_pick 
    items from total_numbers items.

    Args:
        total_numbers (int): The total number of numbers in the lottery pool.
        numbers_to_pick (int): The number of numbers you need to pick in the game.

    Returns:
        float: The odds of winning the lottery game (1 in X).
    
    Raises:
        ValueError: If total_numbers or numbers_to_pick are invalid (e.g. negative or numbers_to_pick > total_numbers).
    """
    # Validate inputs
    if total_numbers <= 0 or numbers_to_pick <= 0:
        raise ValueError("Total numbers and numbers to pick must be positive integers.")
    if numbers_to_pick > total_numbers:
        raise ValueError("Numbers to pick cannot exceed total numbers.")

    # Calculate factorials using math.factorial
    try:
        total_combinations = math.factorial(total_numbers) // (
            math.factorial(numbers_to_pick) * math.factorial(total_numbers - numbers_to_pick)
        )
    except OverflowError:
        raise ValueError("Input values are too large to calculate factorials.")

    # Odds are "1 in total_combinations"
    return total_combinations


# Example usage:
if __name__ == "__main__":
    try:
        total_numbers = 49  # Total pool of numbers in the lottery
        numbers_to_pick = 6  # Numbers to pick
        
        odds = calculate_lottery_odds(total_numbers, numbers_to_pick)
        print(f"The odds of winning are 1 in {odds:,}")
    except ValueError as e:
        print(f"Error: {e}")
```
