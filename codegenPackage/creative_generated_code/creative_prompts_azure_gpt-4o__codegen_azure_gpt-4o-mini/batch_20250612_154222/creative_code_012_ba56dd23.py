"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://avto-world-voditela.club
Prompt: Write a function to validate user input for betting numbers on a lottery app, referencing "福彩大师兄七码复式" for the validation rules.
Generated: DETERMINISTIC_ba56dd239c341a97
Batch ID: 20250612_154222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_lottery_bet(user_input):
    """
    Validates the user input for betting numbers in a lottery app.

    The input must follow the rules of "福彩大师兄七码复式", which typically requires:
    - Numbers must be between 1 and 33 (inclusive)
    - No duplicates are allowed
    - Must be a specific count (e.g., 7 numbers)

    Args:
        user_input (str): A string representation of the user's lottery numbers, separated by commas.

    Returns:
        bool: True if the input is valid, False otherwise.
        str: A message indicating the result of the validation.
    """
    try:
        # Split the input string into individual numbers
        numbers = [int(num.strip()) for num in user_input.split(',')]
        
        # Check if the count of numbers is exactly 7
        if len(numbers) != 7:
            return False, "You must select exactly 7 numbers."

        # Check for duplicates using a set
        if len(numbers) != len(set(numbers)):
            return False, "Duplicate numbers are not allowed."

        # Check if all numbers are in the valid range
        for num in numbers:
            if num < 1 or num > 33:
                return False, "All numbers must be between 1 and 33."

        return True, "Valid input."

    except ValueError:
        return False, "Input must only contain numbers separated by commas."
    except Exception as e:
        return False, f"An unexpected error occurred: {str(e)}"

# Example usage:
if __name__ == "__main__":
    user_input = "1, 2, 3, 4, 5, 6, 7"  # Example input
    is_valid, message = validate_lottery_bet(user_input)
    print(message)  # Output: "Valid input." or the validation error message
```
