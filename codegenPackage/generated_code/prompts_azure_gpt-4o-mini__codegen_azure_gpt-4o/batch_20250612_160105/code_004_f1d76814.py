"""
Generated Code Metadata:
========================
Original URL: https://zkstacks.in
Prompt: Create a function that calculates odds for lottery games similar to those found on "dear lottery today."
Generated: DETERMINISTIC_f1d768146d042564
Batch ID: 20250612_160105
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_lottery_odds(total_numbers: int, numbers_to_choose: int) -> float:
    """
    Calculate the odds of winning a lottery game.

    Args:
        total_numbers (int): The total number of numbers available in the lottery pool.
        numbers_to_choose (int): The number of numbers to be chosen for a winning combination.

    Returns:
        float: The odds of winning the lottery game (1 in X).
    
    Raises:
        ValueError: If total_numbers or numbers_to_choose are invalid (e.g., negative or numbers_to_choose > total_numbers).
    """
    # Validate input
    if total_numbers <= 0 or numbers_to_choose <= 0:
        raise ValueError("Both total_numbers and numbers_to_choose must be positive integers.")
    if numbers_to_choose > total_numbers:
        raise ValueError("numbers_to_choose cannot be greater than total_numbers.")

    # Helper function to calculate factorial
    def factorial(n: int) -> int:
        """Calculate the factorial of a number."""
        return math.factorial(n)

    # Calculate odds using the combination formula: C(n, k) = n! / (k! * (n-k)!)
    combinations = factorial(total_numbers) / (factorial(numbers_to_choose) * factorial(total_numbers - numbers_to_choose))

    # Return the odds as 1 in X
    return combinations


# Example usage:
if __name__ == "__main__":
    try:
        total_numbers = 50  # Total numbers in the lottery pool
        numbers_to_choose = 6  # Numbers to choose for a winning combination
        odds = calculate_lottery_odds(total_numbers, numbers_to_choose)
        print(f"The odds of winning are 1 in {odds:.0f}")
    except ValueError as e:
        print(f"Error: {e}")
```
