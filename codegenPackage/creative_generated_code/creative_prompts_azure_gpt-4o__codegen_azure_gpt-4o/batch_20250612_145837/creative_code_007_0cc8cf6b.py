"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aarkdigital-dashboard.pages.dev
Prompt: Create a function to calculate the leverage multiplier for a trade on the ARB-PERP market, ensuring it adheres to the maximum leverage of 50x as described on the Aark Digital dashboard.
Generated: DETERMINISTIC_0cc8cf6be7642f5a
Batch ID: 20250612_145837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_leverage_multiplier(trade_size: float, margin: float, max_leverage: float = 50.0) -> float:
    """
    Calculate the leverage multiplier for a trade, ensuring it adheres to a maximum leverage limit.

    Parameters:
        trade_size (float): The size of the trade (notional value of the position).
        margin (float): The margin amount provided by the trader.
        max_leverage (float): The maximum leverage allowed (default is 50.0x).

    Returns:
        float: The leverage multiplier for the trade.

    Raises:
        ValueError: If trade_size or margin is non-positive.
        ValueError: If calculated leverage exceeds the maximum leverage.
    """
    # Validate inputs
    if trade_size <= 0:
        raise ValueError("Trade size must be a positive number.")
    if margin <= 0:
        raise ValueError("Margin must be a positive number.")

    # Calculate the leverage multiplier
    leverage = trade_size / margin

    # Ensure the calculated leverage does not exceed the maximum allowed leverage
    if leverage > max_leverage:
        raise ValueError(f"Calculated leverage ({leverage:.2f}x) exceeds the maximum allowed leverage ({max_leverage:.2f}x).")

    return leverage


# Example usage
if __name__ == "__main__":
    try:
        # Example parameters
        trade_size_example = 5000.0  # Example trade size
        margin_example = 100.0       # Example margin provided

        # Calculate the leverage multiplier
        leverage_multiplier = calculate_leverage_multiplier(trade_size_example, margin_example)
        print(f"Leverage Multiplier: {leverage_multiplier:.2f}x")
    
    except ValueError as e:
        print(f"Error: {e}")
```
