"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-nova.com
Prompt: Write a Python function to calculate the margin of safety for value investing, using the principles outlined on Immediate Nova V5, such as comparing intrinsic value and market price.
Generated: DETERMINISTIC_5dfaec1be3aa249a
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_margin_of_safety(intrinsic_value: float, market_price: float) -> float:
    """
    Calculate the Margin of Safety for value investing.

    The Margin of Safety is defined as:
       ((Intrinsic Value - Market Price) / Intrinsic Value) * 100

    Args:
        intrinsic_value (float): The estimated true value of a stock based on fundamental analysis.
        market_price (float): The current market price of the stock.

    Returns:
        float: The margin of safety percentage. A positive value indicates 
               the stock is undervalued relative to its intrinsic value, 
               which is favorable for value investing.
    
    Raises:
        ValueError: If intrinsic_value or market_price is negative or zero.
        ValueError: If intrinsic_value is less than market_price (no margin of safety).
    """
    # Validate inputs
    if intrinsic_value <= 0 or market_price <= 0:
        raise ValueError("Intrinsic value and market price must be positive numbers.")
    
    if intrinsic_value < market_price:
        raise ValueError(
            "Intrinsic value must be greater than or equal to market price "
            "to calculate a margin of safety."
        )
    
    # Calculate margin of safety
    margin_of_safety = ((intrinsic_value - market_price) / intrinsic_value) * 100
    
    return margin_of_safety

# Example usage:
# intrinsic_value = 120.0  # Example intrinsic value
# market_price = 80.0      # Example market price
# try:
#     mos = calculate_margin_of_safety(intrinsic_value, market_price)
#     print(f"Margin of Safety: {mos:.2f}%")
# except ValueError as e:
#     print(f"Error: {e}")
```
