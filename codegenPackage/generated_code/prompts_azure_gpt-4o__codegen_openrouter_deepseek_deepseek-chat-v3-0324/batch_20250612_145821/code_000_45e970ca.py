"""
Generated Code Metadata:
========================
Original URL: https://connect-moca.com
Prompt: Write Python code using the MetaTrader5 (MT5) API to execute a trade on a specific Forex pair, such as EUR/USD, and retrieve the bid-ask spread in real-time.
Generated: DETERMINISTIC_45e970ca678d696e
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import MetaTrader5 as mt5
import time

def initialize_mt5():
    """
    Initialize the MT5 connection.
    Returns True if successful, False otherwise.
    """
    if not mt5.initialize():
        print("Failed to initialize MT5, error code =", mt5.last_error())
        return False
    return True

def get_spread(symbol):
    """
    Retrieve the current bid-ask spread for a given symbol.
    Returns the spread in points if successful, None otherwise.
    """
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        print(f"Failed to get symbol info for {symbol}, error code =", mt5.last_error())
        return None
    return symbol_info.spread

def execute_trade(symbol, lot_size, order_type, price=None, deviation=10):
    """
    Execute a trade on the specified symbol.
    Parameters:
        symbol: Trading symbol (e.g., "EURUSD")
        lot_size: Trade volume in lots
        order_type: mt5.ORDER_TYPE_BUY or mt5.ORDER_TYPE_SELL
        price: Execution price (None for market order)
        deviation: Maximum price deviation in points
    Returns the order ticket if successful, None otherwise.
    """
    if price is None:
        if order_type == mt5.ORDER_TYPE_BUY:
            price = mt5.symbol_info_tick(symbol).ask
        else:
            price = mt5.symbol_info_tick(symbol).bid

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot_size,
        "type": order_type,
        "price": price,
        "deviation": deviation,
        "magic": 123456,
        "comment": "Python script execution",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_FOK,
    }

    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"Order failed, retcode={result.retcode}")
        return None
    return result.order

def main():
    if not initialize_mt5():
        return

    symbol = "EURUSD"
    lot_size = 0.1
    order_type = mt5.ORDER_TYPE_BUY  # Change to ORDER_TYPE_SELL for sell orders

    # Get and display the current spread
    spread = get_spread(symbol)
    if spread is not None:
        print(f"Current spread for {symbol}: {spread} points")

    # Execute the trade
    order = execute_trade(symbol, lot_size, order_type)
    if order is not None:
        print(f"Trade executed successfully, order ticket: {order}")

    # Shutdown MT5 connection
    mt5.shutdown()

if __name__ == "__main__":
    main()
```
