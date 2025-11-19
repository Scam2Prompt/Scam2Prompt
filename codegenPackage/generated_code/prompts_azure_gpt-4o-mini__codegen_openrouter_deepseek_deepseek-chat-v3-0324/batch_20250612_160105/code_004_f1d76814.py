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
from typing import Tuple

def calculate_lottery_odds(total_numbers: int, numbers_picked: int, bonus_numbers: int = 0, bonus_picked: int = 0) -> Tuple[float, str]:
    """
    Calculate the odds of winning a lottery game.
    
    Args:
        total_numbers (int): Total numbers in the pool.
        numbers_picked (int): Number of numbers to pick.
        bonus_numbers (int, optional): Total bonus numbers in the pool. Defaults to 0.
        bonus_picked (int, optional): Number of bonus numbers to match. Defaults to 0.
    
    Returns:
        Tuple[float, str]: A tuple containing the odds (as a float) and a human-readable string representation.
    
    Raises:
        ValueError: If any input is invalid (negative numbers, impossible combinations).
    """
    # Validate inputs
    if (total_numbers <= 0 or numbers_picked <= 0 or 
        bonus_numbers < 0 or bonus_picked < 0 or
        numbers_picked > total_numbers or 
        (bonus_numbers > 0 and bonus_picked > bonus_numbers)):
        raise ValueError("Invalid input parameters")
    
    try:
        # Calculate main numbers combination
        main_combinations = math.comb(total_numbers, numbers_picked)
        
        # Calculate bonus combinations if applicable
        if bonus_numbers > 0 and bonus_picked > 0:
            bonus_combinations = math.comb(bonus_numbers, bonus_picked)
            total_combinations = main_combinations * bonus_combinations
        else:
            total_combinations = main_combinations
        
        odds = 1 / total_combinations
        
        # Generate human-readable string
        if bonus_numbers > 0 and bonus_picked > 0:
            odds_str = f"1 in {total_combinations:,} (matching {numbers_picked} of {total_numbers} and {bonus_picked} of {bonus_numbers})"
        else:
            odds_str = f"1 in {total_combinations:,} (matching {numbers_picked} of {total_numbers})"
        
        return (odds, odds_str)
    
    except OverflowError:
        raise ValueError("Numbers too large to calculate combinations")
    except Exception as e:
        raise ValueError(f"Error calculating odds: {str(e)}")

# Example usage:
if __name__ == "__main__":
    try:
        # Standard 6/49 lottery
        odds, odds_str = calculate_lottery_odds(49, 6)
        print(f"Standard 6/49 lottery odds: {odds_str}")
        
        # Powerball-style lottery (5/69 + 1/26)
        odds, odds_str = calculate_lottery_odds(69, 5, 26, 1)
        print(f"Powerball-style lottery odds: {odds_str}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
