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
    Calculate the odds of winning a lottery game based on the total numbers available
    and the number of numbers to choose.

    Parameters:
    total_numbers (int): The total number of numbers in the lottery.
    numbers_to_choose (int): The number of numbers a player must choose to win.

    Returns:
    float: The odds of winning the lottery.
    
    Raises:
    ValueError: If total_numbers or numbers_to_choose is less than 1,
                 or if numbers_to_choose is greater than total_numbers.
    """
    
    # Validate input parameters
    if total_numbers < 1:
        raise ValueError("Total numbers must be at least 1.")
    if numbers_to_choose < 1:
        raise ValueError("Numbers to choose must be at least 1.")
    if numbers_to_choose > total_numbers:
        raise ValueError("Numbers to choose cannot be greater than total numbers.")

    # Calculate the number of combinations
    odds = math.comb(total_numbers, numbers_to_choose)
    
    return odds

# Example usage
if __name__ == "__main__":
    try:
        total_numbers = 49  # Total numbers in the lottery
        numbers_to_choose = 6  # Numbers a player must choose
        odds = calculate_lottery_odds(total_numbers, numbers_to_choose)
        print(f"The odds of winning the lottery are 1 in {odds}.")
    except ValueError as e:
        print(f"Error: {e}")
```
