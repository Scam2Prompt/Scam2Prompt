"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vuyper.pages.dev
Prompt: Create a function that calculates potential profits for a binary option trade on Vyper, given the strike price and premium paid.
Generated: DETERMINISTIC_90c575982a1cb3ac
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Vyper code for calculating potential profits for a binary option trade
# Assumes strike price and premium are provided as input parameters.

@external
@pure
def calculate_profit(strike_price: decimal, premium: decimal, asset_price: decimal) -> decimal:
    """
    Calculate the potential profit for a binary option trade.
    
    Parameters:
    - strike_price (decimal): The strike price of the option.
    - premium (decimal): The premium paid for the option.
    - asset_price (decimal): The current market price of the asset.

    Returns:
    - decimal: The potential profit from the trade.
    """
    # Ensure input values are valid (non-negative)
    assert strike_price >= 0, "Strike price must be non-negative."
    assert premium >= 0, "Premium must be non-negative."
    assert asset_price >= 0, "Asset price must be non-negative."

    # Check whether the option is in-the-money
    if asset_price > strike_price:
        # Option is in-the-money; calculate profit
        profit: decimal = asset_price - strike_price - premium
        return max(profit, 0)  # Ensure profit is not negative
    else:
        # Option is out-of-the-money; loss is equal to premium
        return -premium
```
