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
import numpy as np
from typing import List, Dict, Tuple

class OrderBookError(Exception):
    """Custom exception for order book errors."""
    pass

def calculate_slippage(order_size: float, 
                       order_book: Dict[str, List[Tuple[float, float]]], 
                       market: str = "HYPE/USDC") -> float:
    """
    Calculate the slippage for a market order based on the provided order size and order book data.

    Args:
        order_size (float): The size of the market order.
        order_book (Dict[str, List[Tuple[float, float]]]): The order book with price and volume data.
        market (str): The market symbol to consider (default is "HYPE/USDC").

    Returns:
        float: The slippage calculated as a percentage.

    Raises:
        OrderBookError: If the order book is empty or invalid.
    """
    
    # Validate inputs
    if market not in order_book:
        raise OrderBookError(f"Market '{market}' not found in order book.")
    
    bids = order_book[market]
    
    if not bids or not isinstance(bids, list):
        raise OrderBookError("Order book is empty or invalid.")
    
    # Sort bids in descending order (price)
    bids.sort(key=lambda x: x[0], reverse=True)
    
    total_filled = 0.0  # Total volume filled
    slippage_total = 0.0  # Total slippage in price

    # Process bids until the order size is filled
    for price, volume in bids:
        if total_filled >= order_size:
            break
        # Determine the volume to fill at this price level
        fill_volume = min(volume, order_size - total_filled)
        
        # Calculate slippage for this fill
        slippage = (price - bids[0][0]) / bids[0][0]  # Slippage as a fraction of the best price
        slippage_total += slippage * fill_volume  # Weighted slippage
        total_filled += fill_volume

    # Calculate average slippage percentage
    if total_filled == 0:
        return 0.0  # No slippage if no order size was filled

    slippage_percentage = (slippage_total / total_filled) * 100  # Convert to percentage
    return slippage_percentage

# Example usage (uncomment to test):
# order_book_data = {
#     "HYPE/USDC": [
#         (1.00, 500),  # Price: $1.00, Volume: 500
#         (1.01, 300),  # Price: $1.01, Volume: 300
#         (1.02, 200),  # Price: $1.02, Volume: 200
#     ]
# }
# order_size = 600
# slippage = calculate_slippage(order_size, order_book_data)
# print(f"Slippage for the market order: {slippage:.2f}%")
```
