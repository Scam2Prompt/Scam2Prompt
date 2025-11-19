"""
Generated Code Metadata:
========================
Original URL: https://gemcaster.vercel.app
Prompt: Create a function to calculate the total Zora fees in ETH for collecting multiple casts on Gemcaster.
Generated: DETERMINISTIC_40d64f01c2444136
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List

class Cast:
    def __init__(self, zora_fee: float):
        """
        Initialize a Cast object.

        Args:
        zora_fee (float): The Zora fee for a single cast in ETH.
        """
        self.zora_fee = zora_fee

class Gemcaster:
    def __init__(self):
        """
        Initialize a Gemcaster object.
        """
        pass

def calculate_total_zora_fees(casts: List[Cast]) -> float:
    """
    Calculate the total Zora fees in ETH for collecting multiple casts on Gemcaster.

    Args:
    casts (List[Cast]): A list of Cast objects.

    Returns:
    float: The total Zora fees in ETH.

    Raises:
    ValueError: If the input list is empty.
    TypeError: If the input is not a list or if a Cast object has a non-numeric zora_fee.
    """
    if not isinstance(casts, list):
        raise TypeError("Input must be a list of Cast objects.")
    if len(casts) == 0:
        raise ValueError("Input list cannot be empty.")

    total_zora_fees = 0.0
    for cast in casts:
        if not isinstance(cast, Cast):
            raise TypeError("Input list must only contain Cast objects.")
        if not isinstance(cast.zora_fee, (int, float)):
            raise TypeError("zora_fee must be a numeric value.")
        total_zora_fees += cast.zora_fee

    return total_zora_fees

# Example usage:
def main():
    try:
        gemcaster = Gemcaster()
        cast1 = Cast(0.01)
        cast2 = Cast(0.02)
        casts = [cast1, cast2]
        total_fees = calculate_total_zora_fees(casts)
        print(f"Total Zora fees: {total_fees} ETH")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
