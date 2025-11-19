"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://leveragetechnolgy.web.app
Prompt: Create a function that calculates the liquidation price based on chosen leverage ratios for trading on the AI TEK platform.
Generated: DETERMINISTIC_5409bb7bdcfffbc6
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from decimal import Decimal, InvalidOperation

def calculate_liquidation_price(entry_price: float, leverage: float, is_long: bool) -> float:
    """
    Calculate the liquidation price based on the chosen leverage ratio for trading.

    Args:
        entry_price (float): The price at which the trade was entered.
        leverage (float): The leverage ratio chosen for the trade.
        is_long (bool): True if the position is long, False if it's short.

    Returns:
        float: The calculated liquidation price.

    Raises:
        ValueError: If entry_price or leverage is invalid (non-positive values).
    """
    try:
        # Validate input
        entry_price = Decimal(entry_price)
        leverage = Decimal(leverage)
        
        if entry_price <= 0 or leverage <= 0:
            raise ValueError("Entry price and leverage must be positive numbers.")

        # Formula for liquidation price calculation
        # Long positions: Liquidation Price = Entry Price * (1 - (1 / Leverage))
        # Short positions: Liquidation Price = Entry Price * (1 + (1 / Leverage))
        if is_long:
            liquidation_price = entry_price * (1 - (Decimal(1) / leverage))
        else:
            liquidation_price = entry_price * (1 + (Decimal(1) / leverage))

        # Return result as float
        return float(liquidation_price)

    except InvalidOperation:
        raise ValueError("Invalid input. Please provide valid numeric values for entry_price and leverage.")

# Example usage (Uncomment to test):
# print(calculate_liquidation_price(100, 10, True))  # Example for a long position
# print(calculate_liquidation_price(100, 10, False)) # Example for a short position
```
