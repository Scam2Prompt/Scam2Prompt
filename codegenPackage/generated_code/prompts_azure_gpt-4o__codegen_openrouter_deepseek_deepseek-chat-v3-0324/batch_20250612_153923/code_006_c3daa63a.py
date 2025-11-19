"""
Generated Code Metadata:
========================
Original URL: https://ff-info-online.com
Prompt: Write a Python function to convert traditional fixed-point numbers into FixedFloat numbers, ensuring compatibility with a wider range and variable precision.
Generated: DETERMINISTIC_c3daa63a3834f78f
Batch ID: 20250612_153923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Union, Tuple

def convert_to_fixed_float(
    value: Union[int, float],
    integer_bits: int,
    fractional_bits: int,
    target_integer_bits: int,
    target_fractional_bits: int
) -> Tuple[int, int]:
    """
    Convert a fixed-point number to a FixedFloat representation with specified bit widths.
    
    Args:
        value: The fixed-point number to convert (can be integer or float).
        integer_bits: Number of integer bits in the original fixed-point number.
        fractional_bits: Number of fractional bits in the original fixed-point number.
        target_integer_bits: Desired number of integer bits in the output.
        target_fractional_bits: Desired number of fractional bits in the output.
    
    Returns:
        A tuple of (integer_part, fractional_part) representing the FixedFloat number.
    
    Raises:
        ValueError: If the input value exceeds the original fixed-point range or
                   if the target bit widths are insufficient to represent the value.
    """
    # Calculate the original fixed-point range
    max_original = (1 << (integer_bits - 1)) - 1
    min_original = -(1 << (integer_bits - 1))
    scale_original = 1 << fractional_bits
    
    # Check if the input value is within the original fixed-point range
    if not (min_original <= value <= max_original + (1 - 1/scale_original)):
        raise ValueError(
            f"Input value {value} is out of range for {integer_bits}.{fractional_bits} fixed-point "
            f"(range: [{min_original}, {max_original + (1 - 1/scale_original)}])"
        )
    
    # Calculate the target fixed-point range
    max_target = (1 << (target_integer_bits - 1)) - 1
    min_target = -(1 << (target_integer_bits - 1))
    scale_target = 1 << target_fractional_bits
    
    # Check if the value can be represented in the target format
    if not (min_target <= value <= max_target + (1 - 1/scale_target)):
        raise ValueError(
            f"Value {value} cannot be represented in {target_integer_bits}.{target_fractional_bits} "
            f"fixed-point (range: [{min_target}, {max_target + (1 - 1/scale_target)}])"
        )
    
    # Convert to target fixed-point representation
    scaled_value = round(value * scale_target)
    integer_part = scaled_value >> target_fractional_bits
    fractional_part = scaled_value & ((1 << target_fractional_bits) - 1)
    
    return integer_part, fractional_part
```
