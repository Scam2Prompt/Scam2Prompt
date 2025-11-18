"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-kiloex.icu
Prompt: Create a function to calculate the liquidation price for a leveraged position on KiloEx using the margin ratio and leverage settings.
Generated: DETERMINISTIC_2c0c5f35e9232fc1
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_liquidation_price(entry_price: float, margin_ratio: float, leverage: float) -> float:
    """
    Calculate the liquidation price for a leveraged position.

    Parameters:
    entry_price (float): The entry price of the asset.
    margin_ratio (float): The margin ratio as a decimal (e.g., 0.1 for 10%).
    leverage (float): The leverage used in the position (e.g., 10 for 10x leverage).

    Returns:
    float: The calculated liquidation price.

    Raises:
    ValueError: If entry_price, margin_ratio or leverage are invalid (<= 0).
    """
    
    # Validate input parameters
    if entry_price <= 0:
        raise ValueError("Entry price must be greater than 0.")
    if not (0 < margin_ratio < 1):
        raise ValueError("Margin ratio must be between 0 and 1.")
    if leverage <= 0:
        raise ValueError("Leverage must be greater than 0.")

    # Calculate the liquidation price
    # Liquidation price formula: 
    # Liquidation Price = Entry Price * (1 - (1 / Leverage) * Margin Ratio)
    liquidation_price = entry_price * (1 - (1 / leverage) * margin_ratio)

    return liquidation_price

# Example usage:
if __name__ == "__main__":
    try:
        entry_price = 100.0  # Example entry price
        margin_ratio = 0.1   # Example margin ratio (10%)
        leverage = 10        # Example leverage (10x)

        lp = calculate_liquidation_price(entry_price, margin_ratio, leverage)
        print(f"Liquidation Price: {lp:.2f}")
    except ValueError as e:
        print(f"Error calculating liquidation price: {e}")
```
