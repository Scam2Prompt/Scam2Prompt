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
# Import necessary libraries
from typing import Tuple

def calculate_cfd_profit_loss(entry_price: float, exit_price: float, trade_size: int, leverage: int) -> Tuple[float, float]:
    """
    Calculate potential profits and losses when trading CFDs on stocks.

    Parameters:
    - entry_price (float): The price at which the CFD trade was opened.
    - exit_price (float): The price at which the CFD trade is closed.
    - trade_size (int): The number of CFDs traded (units).
    - leverage (int): The leverage applied to the trade.

    Returns:
    - Tuple[float, float]: A tuple containing:
        - profit (float): The profit amount if the trade is favorable.
        - loss (float): The loss amount if the trade goes against you.
    """
    try:
        # Validate inputs
        if entry_price <= 0 or exit_price <= 0:
            raise ValueError("Entry and exit prices must be positive values.")
        if trade_size <= 0:
            raise ValueError("Trade size must be a positive value.")
        if leverage <= 0:
            raise ValueError("Leverage must be a positive value.")

        # Calculate the price difference
        price_difference = exit_price - entry_price

        # Calculate profit or loss without leverage
        raw_profit_loss = price_difference * trade_size

        # Adjust for leverage
        leveraged_profit_loss = raw_profit_loss * leverage

        # Separate profit and loss
        profit = max(leveraged_profit_loss, 0)  # Positive value implies profit
        loss = abs(min(leveraged_profit_loss, 0))  # Negative value implies loss

        return profit, loss

    except ValueError as e:
        # Handle input validation errors
        print(f"Input Error: {e}")
        return 0.0, 0.0
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        return 0.0, 0.0


# Example usage:
if __name__ == "__main__":
    # Sample trading parameters
    entry_price = 100.0  # Entry price per CFD
    exit_price = 120.0   # Exit price per CFD
    trade_size = 10      # Number of CFDs traded
    leverage = 5         # Leverage applied

    # Calculate profit and loss
    profit, loss = calculate_cfd_profit_loss(entry_price, exit_price, trade_size, leverage)

    # Output the results
    print(f"Potential Profit: ${profit:.2f}")
    print(f"Potential Loss: ${loss:.2f}")
```
