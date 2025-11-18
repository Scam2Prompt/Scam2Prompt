"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connect-moca.com
Prompt: Write Python code using the MetaTrader5 (MT5) API to execute a trade on a specific Forex pair, such as EUR/USD, and retrieve the bid-ask spread in real-time.
Generated: DETERMINISTIC_45e970ca678d696e
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import MetaTrader5 as mt5
import time

# Constants
FOREX_PAIR = "EURUSD"
LOT_SIZE = 0.1  # Specify the lot size for the trade
SLIPPAGE = 10   # Maximum slippage allowed
TAKE_PROFIT = 50  # Take profit in points
STOP_LOSS = 50    # Stop loss in points

def initialize_mt5():
    """Initialize the MT5 connection."""
    if not mt5.initialize():
        print(f"Initialization failed with error code: {mt5.last_error()}")
        return False
    return True

def get_bid_ask_spread(symbol):
    """Retrieve the current bid and ask prices for a given symbol."""
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        print(f"Symbol {symbol} not found.")
        return None, None

    bid = symbol_info.bid
    ask = symbol_info.ask
    spread = ask - bid
    return bid, ask, spread

def execute_order(symbol, action):
    """Execute a trade order."""
    # Prepare the order request
    order_type = mt5.ORDER_BUY if action == "buy" else mt5.ORDER_SELL
    price = mt5.symbol_info_tick(symbol).ask if action == "buy" else mt5.symbol_info_tick(symbol).bid

    # Create an order request
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": LOT_SIZE,
        "type": order_type,
        "price": price,
        "sl": price - STOP_LOSS * mt5.symbol_info(symbol).point if action == "buy" else price + STOP_LOSS * mt5.symbol_info(symbol).point,
        "tp": price + TAKE_PROFIT * mt5.symbol_info(symbol).point if action == "buy" else price - TAKE_PROFIT * mt5.symbol_info(symbol).point,
        "deviation": SLIPPAGE,
        "magic": 234000,  # Unique identifier for the order
        "comment": "Test order",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    # Send the order
    result = mt5.order_send(request)

    # Check the result
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"Order send failed with error code: {result.retcode}")
        return False
    print(f"Order executed successfully: {result}")
    return True

def main():
    """Main function to execute the trade and get the spread."""
    if not initialize_mt5():
        return

    bid, ask, spread = get_bid_ask_spread(FOREX_PAIR)
    if bid is None and ask is None:
        mt5.shutdown()
        return

    print(f"Current Bid: {bid}, Ask: {ask}, Spread: {spread}")

    # Execute a buy order
    if execute_order(FOREX_PAIR, "buy"):
        print("Trade executed successfully.")
    else:
        print("Trade execution failed.")

    # Shutdown the MT5 connection
    mt5.shutdown()

if __name__ == "__main__":
    main()
```
