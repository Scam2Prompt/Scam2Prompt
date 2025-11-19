"""
Generated Code Metadata:
========================
Original URL: https://action-coin.com
Prompt: Create a function that calculates potential profits and losses when trading CFDs on stocks using Action Coin's trading parameters.
Generated: DETERMINISTIC_9b21eb498dddf76c
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import Tuple

def calculate_cfd_profit_loss(entry_price: float, exit_price: float, position_size: int, leverage: int) -> Tuple[float, float]:
    """
    Calculate potential profits and losses when trading CFDs on stocks.

    Parameters:
    - entry_price (float): The price at which the position was opened.
    - exit_price (float): The price at which the position is closed.
    - position_size (int): The number of units (shares) traded.
    - leverage (int): The leverage applied to the trade.

    Returns:
    - Tuple[float, float]: A tuple containing the profit and loss values.
    """
    try:
        # Validate inputs
        if entry_price <= 0 or exit_price <= 0 or position_size <= 0 or leverage <= 0:
            raise ValueError("All input values must be positive numbers.")

        # Calculate the price difference
        price_difference = exit_price - entry_price

        # Calculate the profit or loss
        profit_loss = price_difference * position_size * leverage

        # Separate profit and loss
        profit = profit_loss if profit_loss > 0 else 0.0
        loss = abs(profit_loss) if profit_loss < 0 else 0.0

        return profit, loss

    except ValueError as ve:
        print(f"Input Error: {ve}")
        return 0.0, 0.0
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0.0, 0.0

# Example usage:
if __name__ == "__main__":
    # Example parameters
    entry_price = 100.0  # Price at which the position was opened
    exit_price = 110.0   # Price at which the position was closed
    position_size = 50   # Number of units traded
    leverage = 10        # Leverage applied

    # Calculate profit and loss
    profit, loss = calculate_cfd_profit_loss(entry_price, exit_price, position_size, leverage)

    # Output the results
    print(f"Profit: ${profit:.2f}")
    print(f"Loss: ${loss:.2f}")
```
