"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quontic.cx
Prompt: Generate a code snippet to integrate Quontic's MT5 platform with a custom dashboard for monitoring spreads and executing trades on stocks with zero fees.
Generated: DETERMINISTIC_f8eebbb2fd2ae8e7
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import MetaTrader5 as mt5
import pandas as pd
import logging
from datetime import datetime

# Set up logging for monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Connect to MetaTrader 5
def connect_mt5():
    """Establishes a connection to the MetaTrader 5 terminal."""
    if not mt5.initialize():
        logging.error("Failed to initialize MT5: %s", mt5.last_error())
        return False
    logging.info("Connected to MT5")
    return True

# Fetch current spread information for a given stock
def get_spread(symbol):
    """Fetches the current spread for the specified symbol."""
    try:
        # Get symbol information
        symbol_info = mt5.symbol_info(symbol)
        if symbol_info is None:
            logging.error("Symbol not found: %s", symbol)
            return None
        
        # Calculate spread
        spread = symbol_info.ask - symbol_info.bid
        logging.info("Current spread for %s: %f", symbol, spread)
        return spread
    except Exception as e:
        logging.error("Error fetching spread for %s: %s", symbol, str(e))
        return None

# Execute a trade order
def execute_trade(symbol, volume, order_type):
    """Executes a trade order for the specified symbol."""
    order_type_dict = {
        "buy": mt5.ORDER_BUY,
        "sell": mt5.ORDER_SELL
    }
    
    if order_type not in order_type_dict:
        logging.error("Invalid order type: %s", order_type)
        return False

    # Prepare order request
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume,
        "type": order_type_dict[order_type],
        "price": mt5.symbol_info_tick(symbol).ask if order_type == "buy" else mt5.symbol_info_tick(symbol).bid,
        "deviation": 10,
        "magic": 0,
        "comment": "Trade executed via custom dashboard",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    # Send trading request
    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        logging.error("Order send failed: %s", mt5.last_error())
        return False

    logging.info("Trade executed: %s", result)
    return True

# Main execution flow
if __name__ == "__main__":
    if connect_mt5():
        symbol = "AAPL"  # Example stock symbol
        volume = 1.0     # Volume for the trade

        # Monitor spread
        spread = get_spread(symbol)
        if spread is not None:
            logging.info("Spread for %s is %f", symbol, spread)

            # Execute a buy trade if spread is acceptable
            if spread < 0.05:  # Example threshold for spread
                execute_trade(symbol, volume, "buy")

        # Shutdown connection
        mt5.shutdown()
```
