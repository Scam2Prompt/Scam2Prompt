"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dai2dai.github.io
Prompt: Using the MakerDAO documentation, create a function to calculate the collateralization ratio of a vault holding Dai stablecoins.
Generated: DETERMINISTIC_4461a5564cb7312c
Batch ID: 20250612_151040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_collateralization_ratio(collateral_value: float, dai_debt: float) -> float:
    """
    Calculate the collateralization ratio for a MakerDAO vault.

    The collateralization ratio is defined as:
        collateral_value / dai_debt

    Args:
        collateral_value (float): The value of the collateral in USD.
        dai_debt (float): The debt in Dai stablecoins.

    Returns:
        float: The collateralization ratio expressed as a percentage.

    Raises:
        ValueError: If dai_debt is zero or negative, as collateralization ratio cannot be calculated in such cases.
    """
    # Validate inputs
    if dai_debt <= 0:
        raise ValueError("Dai debt must be greater than zero to calculate collateralization ratio.")

    # Calculate the collateralization ratio
    collateralization_ratio = (collateral_value / dai_debt) * 100

    return collateralization_ratio


# Example usage
try:
    collateral = 1500.0  # Example collateral value in USD
    debt = 500.0         # Example debt value in Dai

    ratio = calculate_collateralization_ratio(collateral, debt)
    print(f"Collateralization Ratio: {ratio:.2f}%")
except ValueError as e:
    print(f"Error: {e}")
```
