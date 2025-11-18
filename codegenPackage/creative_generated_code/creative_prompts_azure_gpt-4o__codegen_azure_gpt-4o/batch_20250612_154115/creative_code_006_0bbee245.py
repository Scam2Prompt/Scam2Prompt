"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperliquide.xyz
Prompt: Create a Python function to calculate slippage for a market order on Hyperliquid, given the order size and current order book data for HYPE/USDC.
Generated: DETERMINISTIC_0bbee2457af62bdd
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def calculate_slippage(order_size, order_book):
    """
    Calculate the slippage for a market order on Hyperliquid given the order size and order book data.
    
    Args:
        order_size (float): The size of the market order in base currency (HYPE).
        order_book (dict): The order book data containing 'bids' and 'asks'.
                           Example format:
                           {
                               "bids": [[price1, quantity1], [price2, quantity2], ...],
                               "asks": [[price1, quantity1], [price2, quantity2], ...]
                           }
    
    Returns:
        float: The calculated slippage percentage.
    
    Raises:
        ValueError: If order_size is less than or equal to zero.
        ValueError: If the order book data is invalid or insufficient to fulfill the order.
    """
    # Validate the input
    if order_size <= 0:
        raise ValueError("Order size must be greater than zero.")
    
    if not isinstance(order_book, dict) or 'asks' not in order_book or not order_book['asks']:
        raise ValueError("Invalid or insufficient order book data. 'asks' must be provided.")
    
    # Calculate the average execution price for the given order size
    remaining_size = order_size
    executed_cost = 0.0

    for price, quantity in order_book['asks']:
        if remaining_size <= 0:
            break  # Order has been fully executed

        if remaining_size <= quantity:
            # Fulfill the remaining order size at the current price
            executed_cost += remaining_size * price
            remaining_size = 0
        else:
            # Consume the entire ask order quantity
            executed_cost += quantity * price
            remaining_size -= quantity

    if remaining_size > 0:
        raise ValueError("Insufficient liquidity in the order book to fulfill the order.")
    
    # Calculate the slippage as a percentage
    worst_price = order_book['asks'][0][0]  # Best ask price (initial market price)
    average_execution_price = executed_cost / order_size
    slippage = ((average_execution_price - worst_price) / worst_price) * 100

    return slippage


# Example usage
if __name__ == "__main__":
    # Example order book data
    example_order_book = {
        "bids": [[1.95, 100], [1.90, 200]],
        "asks": [[2.00, 50], [2.05, 150], [2.10, 300]]
    }
    
    try:
        order_size = 100  # Example order size in HYPE
        slippage = calculate_slippage(order_size, example_order_book)
        print(f"Slippage for order size {order_size}: {slippage:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
```
