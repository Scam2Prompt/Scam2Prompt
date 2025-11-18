"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ff-info-online.com
Prompt: Write a Python function to convert traditional fixed-point numbers into FixedFloat numbers, ensuring compatibility with a wider range and variable precision.
Generated: DETERMINISTIC_c3daa63a3834f78f
Batch ID: 20250612_153923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import the decimal module for precise fixed-point arithmetic
from decimal import Decimal, getcontext, InvalidOperation

def fixed_to_float(fixed_point_number: str, precision: int = 10) -> float:
    """
    Convert a fixed-point number (as a string) into a floating-point number with variable precision.

    Parameters:
        fixed_point_number (str): The fixed-point number represented as a string. 
                                  For example, "123.456" or "0.000123".
        precision (int): Number of decimal places for the floating-point conversion.
                         Default is 10.

    Returns:
        float: The converted floating-point number.

    Raises:
        ValueError: If the input fixed-point number is not valid or precision is negative.
    """

    # Validate precision input
    if precision < 0:
        raise ValueError("Precision must be a non-negative integer.")

    try:
        # Set the precision for the Decimal context
        getcontext().prec = precision
        
        # Convert the fixed-point string into a Decimal for precision handling
        fixed_decimal = Decimal(fixed_point_number)
        
        # Convert the Decimal to a floating-point number
        return float(fixed_decimal)
    except InvalidOperation:
        raise ValueError(f"Invalid fixed-point number: {fixed_point_number}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")

# Example usage:
# result = fixed_to_float("123.456", precision=5)
# print(result)  # Output: 123.456
```
