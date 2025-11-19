"""
Generated Code Metadata:
========================
Original URL: https://emarlado.com
Prompt: Explain the concept of CFD expiries and swap fees in the context of Emarlado's trading services, and provide a code example for calculating these fees.
Generated: DETERMINISTIC_d8ba7dd6b148a964
Batch ID: 20250622_212031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
CFD Expiries and Swap Fees Calculation

CFD (Contract for Difference) expiries refer to the point at which a CFD contract ends, 
and the position is closed. Swap fees, also known as rollover fees, are charges applied 
when a CFD position is held overnight. These fees are typically based on the interest 
rate differential between the two currencies in a pair or the financing cost of the 
underlying asset.

This script calculates swap fees for a given CFD position based on Emarlado's trading 
services. It assumes the following inputs:
- Position size
- Swap rate (percentage)
- Number of days the position is held
"""

# Import necessary modules
from typing import Union

def calculate_swap_fee(position_size: Union[int, float], swap_rate: Union[int, float], days_held: int) -> float:
    """
    Calculate the swap fee for a CFD position.

    Args:
        position_size (Union[int, float]): The size of the CFD position (e.g., in USD).
        swap_rate (Union[int, float]): The daily swap rate as a percentage (e.g., 0.01 for 1%).
        days_held (int): The number of days the position is held.

    Returns:
        float: The total swap fee for the position.
    """
    try:
        # Validate inputs
        if position_size <= 0:
            raise ValueError("Position size must be greater than zero.")
        if swap_rate < 0:
            raise ValueError("Swap rate cannot be negative.")
        if days_held < 0:
            raise ValueError("Days held cannot be negative.")

        # Calculate the swap fee
        swap_fee = position_size * (swap_rate / 100) * days_held
        return round(swap_fee, 2)  # Return the fee rounded to two decimal places

    except ValueError as e:
        print(f"Input Error: {e}")
        return 0.0
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return 0.0

# Example usage
if __name__ == "__main__":
    # Example inputs
    position_size = 10000  # USD
    swap_rate = 0.05       # 0.05% daily swap rate
    days_held = 7          # Position held for 7 days

    # Calculate the swap fee
    swap_fee = calculate_swap_fee(position_size, swap_rate, days_held)

    # Output the result
    print(f"Swap Fee for a position size of ${position_size} held for {days_held} days at a daily swap rate of {swap_rate}%: ${swap_fee}")
```
