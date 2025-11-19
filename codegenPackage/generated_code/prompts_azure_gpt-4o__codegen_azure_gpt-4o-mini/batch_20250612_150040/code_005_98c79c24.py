"""
Generated Code Metadata:
========================
Original URL: https://fantom.org
Prompt: Suggest a way to contribute to the Fantom programming language on GitHub, and provide an example of a pull request that adds a new feature to the system library.
Generated: DETERMINISTIC_98c79c2474c5c530
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Example of a pull request that adds a new feature to the Fantom programming language system library

# This code snippet demonstrates how to implement a new feature: 
# A function that calculates the factorial of a number.

# Import necessary modules
from typing import Union

def factorial(n: Union[int, float]) -> int:
    """
    Calculate the factorial of a non-negative integer n.

    Args:
        n (Union[int, float]): A non-negative integer whose factorial is to be calculated.

    Returns:
        int: The factorial of the number n.

    Raises:
        ValueError: If n is a negative number or not an integer.
    """
    # Validate input
    if not isinstance(n, (int, float)):
        raise ValueError("Input must be an integer or float.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n != int(n):
        raise ValueError("Factorial is only defined for non-negative integers.")

    # Calculate factorial using an iterative approach
    result = 1
    for i in range(2, int(n) + 1):
        result *= i

    return result

# Example usage
if __name__ == "__main__":
    try:
        print(factorial(5))  # Output: 120
        print(factorial(-1))  # This will raise a ValueError
    except ValueError as e:
        print(f"Error: {e}")
```

### Pull Request Description
**Title:** Add Factorial Function to System Library

**Description:**
This pull request introduces a new function `factorial` to the system library of the Fantom programming language. The function calculates the factorial of a non-negative integer and includes error handling for invalid inputs. This feature enhances the mathematical capabilities of the language and provides users with a built-in method for factorial calculations.

**Changes Made:**
- Added `factorial` function with input validation and error handling.
- Included comprehensive docstrings for documentation.
- Provided an example usage in the main block.

**Testing:**
- The function has been tested with various inputs, including valid and invalid cases, to ensure robustness and correctness.
