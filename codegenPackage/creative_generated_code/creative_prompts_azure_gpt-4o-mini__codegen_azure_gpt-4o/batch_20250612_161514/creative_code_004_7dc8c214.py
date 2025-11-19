"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usual-portal.web.app
Prompt: Create a function that calculates the minting factor for the USUAL token based on the TVL and cash flow scarcity advantages described on the Usual site.
Generated: DETERMINISTIC_7dc8c2148f0070c9
Batch ID: 20250612_161514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import Union

def calculate_minting_factor(tvl: Union[int, float], cash_flow_advantage: Union[int, float]) -> float:
    """
    Calculate the minting factor for the USUAL token based on TVL (Total Value Locked) 
    and cash flow scarcity advantage.

    Args:
        tvl (Union[int, float]): Total Value Locked (TVL) in the system.
        cash_flow_advantage (Union[int, float]): Cash flow scarcity advantage as a percentage (0-100).

    Returns:
        float: The minting factor for the USUAL token.

    Raises:
        ValueError: If TVL or cash flow advantage is negative.
        ValueError: If cash flow advantage is outside the range of 0-100.
    """
    # Validate inputs
    if tvl < 0:
        raise ValueError("TVL cannot be negative.")
    if cash_flow_advantage < 0 or cash_flow_advantage > 100:
        raise ValueError("Cash flow advantage must be between 0 and 100 (inclusive).")

    # Calculate minting factor
    # Formula: minting_factor = tvl * (1 + (cash_flow_advantage / 100))
    minting_factor = tvl * (1 + (cash_flow_advantage / 100))

    return minting_factor

# Example usage:
if __name__ == "__main__":
    try:
        # Test values
        tvl = 1000000  # Example TVL (Total Value Locked)
        cash_flow_advantage = 20  # Example cash flow advantage as a percentage

        # Calculate minting factor
        result = calculate_minting_factor(tvl, cash_flow_advantage)
        print(f"The minting factor for the USUAL token is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
```
