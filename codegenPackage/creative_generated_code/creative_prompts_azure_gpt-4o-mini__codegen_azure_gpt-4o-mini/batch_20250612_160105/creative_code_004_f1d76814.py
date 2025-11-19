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

def calculate_lottery_odds(total_numbers: int, selected_numbers: int) -> float:
    """
    Calculate the odds of winning a lottery game.

    Args:
        total_numbers (int): The total number of numbers to choose from.
        selected_numbers (int): The number of numbers a player selects.

    Returns:
        float: The odds of winning the lottery.
    
    Raises:
        ValueError: If total_numbers or selected_numbers are less than 1,
                     or if selected_numbers is greater than total_numbers.
    """
    
    # Validate input parameters
    if total_numbers < 1:
        raise ValueError("Total numbers must be at least 1.")
    if selected_numbers < 1:
        raise ValueError("Selected numbers must be at least 1.")
    if selected_numbers > total_numbers:
        raise ValueError("Selected numbers cannot be greater than total numbers.")
    
    # Calculate combinations of total_numbers choose selected_numbers
    odds = math.comb(total_numbers, selected_numbers)
    
    return odds

# Example usage
if __name__ == "__main__":
    try:
        total_numbers = 49  # Total numbers in the lottery
        selected_numbers = 6  # Numbers the player selects
        odds = calculate_lottery_odds(total_numbers, selected_numbers)
        print(f"The odds of winning the lottery are 1 in {odds}.")
    except ValueError as e:
        print(f"Error: {e}")
```
