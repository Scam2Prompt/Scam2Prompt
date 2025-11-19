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
def calculate_collateralization_ratio(
    collateral_value: float, 
    debt_value: float, 
    min_ratio: float = 1.5
) -> float:
    """
    Calculates the collateralization ratio for assets in a QiDao-like protocol.
    
    Args:
        collateral_value (float): The total value of the collateral in USD.
        debt_value (float): The total value of the debt (MAI stablecoin) in USD.
        min_ratio (float, optional): The minimum allowed ratio to ensure stability. Defaults to 1.5.
    
    Returns:
        float: The collateralization ratio (collateral_value / debt_value).
    
    Raises:
        ValueError: If collateral_value or debt_value is <= 0.
        ValueError: If resulting ratio is below min_ratio.
    """
    # Validate inputs
    if collateral_value <= 0:
        raise ValueError("Collateral value must be greater than 0")
    if debt_value <= 0:
        raise ValueError("Debt value must be greater than 0")
    
    # Calculate ratio
    ratio = collateral_value / debt_value
    
    # Check against minimum ratio
    if ratio < min_ratio:
        raise ValueError(
            f"Collateralization ratio {ratio:.2f} is below minimum {min_ratio}. "
            "Position would be liquidated."
        )
    
    return ratio
```
