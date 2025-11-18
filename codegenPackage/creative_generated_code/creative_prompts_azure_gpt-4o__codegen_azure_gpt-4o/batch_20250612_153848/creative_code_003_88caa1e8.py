"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ultrax.io
Prompt: Write a function to calculate the fees for a trade on UltraX based on the U2U token fee structure.
Generated: DETERMINISTIC_88caa1e81dd8f3e8
Batch ID: 20250612_153848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from decimal import Decimal

# Define the U2U token fee structure
FEE_STRUCTURE = {
    "tier_1": {"min_trade_amount": Decimal("0"), "max_trade_amount": Decimal("1000"), "fee_percent": Decimal("0.5")},
    "tier_2": {"min_trade_amount": Decimal("1000.01"), "max_trade_amount": Decimal("10000"), "fee_percent": Decimal("0.25")},
    "tier_3": {"min_trade_amount": Decimal("10000.01"), "max_trade_amount": Decimal("100000"), "fee_percent": Decimal("0.1")},
    "tier_4": {"min_trade_amount": Decimal("100000.01"), "max_trade_amount": Decimal("Infinity"), "fee_percent": Decimal("0.05")},
}

def calculate_trade_fee(trade_amount):
    """
    Calculate the fees for a trade based on the U2U token fee structure.

    Args:
        trade_amount (Decimal): The amount of the trade in U2U tokens.

    Returns:
        Decimal: The fee for the trade.
    
    Raises:
        ValueError: If the trade_amount is negative or not a valid number.
    """
    # Validate the trade amount
    if not isinstance(trade_amount, (int, float, Decimal)) or Decimal(trade_amount) < 0:
        raise ValueError("Trade amount must be a non-negative number.")

    trade_amount = Decimal(trade_amount)  # Convert trade amount to Decimal for precision

    # Determine the applicable fee tier
    for tier, values in FEE_STRUCTURE.items():
        if values["min_trade_amount"] <= trade_amount <= values["max_trade_amount"]:
            fee_percent = values["fee_percent"]
            break
    else:
        raise ValueError("Trade amount does not fit into any fee tier.")

    # Calculate the fee
    fee = trade_amount * (fee_percent / 100)

    return fee

# Example usage
if __name__ == "__main__":
    try:
        trade_amount = Decimal("15000")  # Example trade amount
        fee = calculate_trade_fee(trade_amount)
        print(f"The fee for a trade of {trade_amount} U2U tokens is: {fee} U2U tokens.")
    except ValueError as e:
        print(f"Error: {e}")
```
