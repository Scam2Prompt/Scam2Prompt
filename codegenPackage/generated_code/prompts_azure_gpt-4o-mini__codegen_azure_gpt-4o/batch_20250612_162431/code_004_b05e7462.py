"""
Generated Code Metadata:
========================
Original URL: https://geoins.ru
Prompt: Create a function that calculates the collateralization ratio for assets held in a QiDao-like protocol, ensuring stability for the MAI stablecoin.
Generated: DETERMINISTIC_b05e7462b81bf5ce
Batch ID: 20250612_162431
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import Union

def calculate_collateralization_ratio(collateral_value: Union[int, float], debt_value: Union[int, float]) -> Union[float, str]:
    """
    Calculate the collateralization ratio for assets in a QiDao-like protocol.

    Parameters:
        collateral_value (Union[int, float]): The total value of the collateral in USD.
        debt_value (Union[int, float]): The total debt issued in USD (e.g., MAI stablecoin).

    Returns:
        Union[float, str]: The collateralization ratio as a percentage (float) if valid inputs are provided,
                           or an error message (str) if inputs are invalid.
    """
    try:
        # Validate inputs
        if collateral_value <= 0:
            return "Error: Collateral value must be greater than zero."
        if debt_value < 0:
            return "Error: Debt value cannot be negative."

        # Avoid division by zero
        if debt_value == 0:
            return "Error: Debt value cannot be zero."

        # Calculate collateralization ratio
        collateralization_ratio = (collateral_value / debt_value) * 100

        return round(collateralization_ratio, 2)  # Return the ratio rounded to 2 decimal places

    except TypeError:
        return "Error: Invalid input types. Please provide numeric values for collateral and debt."

# Example usage
if __name__ == "__main__":
    collateral = 1500.0  # Example collateral value in USD
    debt = 1000.0        # Example debt value in USD

    result = calculate_collateralization_ratio(collateral, debt)
    print(f"Collateralization Ratio: {result}%")
```
