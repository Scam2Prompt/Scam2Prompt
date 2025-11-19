"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geoins.ru
Prompt: Create a function that calculates the collateralization ratio for assets held in a QiDao-like protocol, ensuring stability for the MAI stablecoin.
Generated: DETERMINISTIC_b05e7462b81bf5ce
Batch ID: 20250612_162431
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

def calculate_collateralization_ratio(collateral_value: Union[float, int], debt_value: Union[float, int]) -> Union[float, str]:
    """
    Calculate the collateralization ratio for assets held in a protocol.

    Args:
        collateral_value (float | int): The total value of the collateral provided (e.g., in USD).
        debt_value (float | int): The total value of the debt issued (e.g., in MAI stablecoins).

    Returns:
        float | str: The collateralization ratio as a percentage (e.g., 150 for 150%) if inputs are valid,
                     otherwise an error message.
    """
    try:
        # Validate inputs
        if collateral_value < 0 or debt_value < 0:
            return "Error: Collateral value and debt value must be non-negative numbers."
        
        if debt_value == 0:
            return "Error: Debt value cannot be zero."
        
        # Calculate collateralization ratio
        collateralization_ratio = (collateral_value / debt_value) * 100  # Ratio expressed as a percentage
        return round(collateralization_ratio, 2)  # Return rounded to 2 decimal places for clarity

    except TypeError:
        return "Error: Inputs must be numbers (float or int)."

# Example usage
if __name__ == "__main__":
    collateral = 1500.0  # Example collateral value in USD
    debt = 1000.0        # Example debt value in MAI stablecoin

    result = calculate_collateralization_ratio(collateral, debt)
    if isinstance(result, str):
        print(result)
    else:
        print(f"Collateralization Ratio: {result}%")
```
