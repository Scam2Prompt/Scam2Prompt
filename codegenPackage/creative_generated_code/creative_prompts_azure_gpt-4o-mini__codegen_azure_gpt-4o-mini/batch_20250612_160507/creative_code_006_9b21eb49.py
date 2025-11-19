"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://action-coin.com
Prompt: Create a function that calculates potential profits and losses when trading CFDs on stocks using Action Coin's trading parameters.
Generated: DETERMINISTIC_9b21eb498dddf76c
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CFDTradingError(Exception):
    """Custom exception for CFD trading errors."""
    pass

def calculate_cfd_profit_loss(entry_price, exit_price, position_size, leverage):
    """
    Calculate the potential profit or loss from a CFD trade based on provided parameters.

    Parameters:
    - entry_price (float): The price at which the CFD was bought.
    - exit_price (float): The price at which the CFD will be sold.
    - position_size (float): The number of CFDs traded.
    - leverage (float): The leverage ratio.

    Returns:
    - float: The potential profit or loss from the trade.

    Raises:
    - CFDTradingError: If any input values are invalid.
    """

    # Validate inputs
    if entry_price <= 0:
        raise CFDTradingError("Entry price must be greater than zero.")
    if exit_price <= 0:
        raise CFDTradingError("Exit price must be greater than zero.")
    if position_size <= 0:
        raise CFDTradingError("Position size must be greater than zero.")
    if leverage <= 0:
        raise CFDTradingError("Leverage must be greater than zero.")

    # Calculate the difference between exit and entry prices
    price_difference = exit_price - entry_price

    # Calculate profit or loss considering the position size and leverage
    profit_loss = price_difference * position_size * leverage

    return profit_loss

# Example usage
if __name__ == "__main__":
    try:
        entry_price = 100.0  # Example entry price
        exit_price = 110.0   # Example exit price
        position_size = 10    # Example position size
        leverage = 5          # Example leverage

        result = calculate_cfd_profit_loss(entry_price, exit_price, position_size, leverage)
        print(f"Potential Profit/Loss: ${result:.2f}")

    except CFDTradingError as e:
        print(f"Error: {e}")
```
