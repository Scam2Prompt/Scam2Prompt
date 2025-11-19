"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quontic.cx
Prompt: Write a code snippet that demonstrates how to execute a CFD trade on Quontic's platform using MetaTrader 5 (MT5) for Forex pairs such as EUR/USD.
Generated: DETERMINISTIC_9da9926563ec215b
Batch ID: 20250612_162554
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

# Define constants for trading parameters
SYMBOL = "EURUSD"  # Forex pair to trade
LOT_SIZE = 0.1     # Number of lots to trade
SLIPPAGE = 10      # Maximum allowed slippage in points
STOP_LOSS = 50     # Stop Loss in points
TAKE_PROFIT = 100  # Take Profit in points

def main():
    # Initialize the MetaTrader 5 connection
    if not mt5.initialize():
        print("initialize() failed, error code =", mt5.last_error())
        return

    # Check if the symbol is available for trading
    if not mt5.symbol_select(SYMBOL, True):
        print(f"Symbol {SYMBOL} not available for trading, error code =", mt5.last_error())
        mt5.shutdown()
        return

    # Get the current price for the symbol
    price = mt5.symbol_info_tick(SYMBOL).ask
    if price is None:
        print("Failed to get price, error code =", mt5.last_error())
        mt5.shutdown()
        return

    # Calculate the order parameters
    stop_loss_price = price - STOP_LOSS * mt5.symbol_info(SYMBOL).point
    take_profit_price = price + TAKE_PROFIT * mt5.symbol_info(SYMBOL).point

    # Create a buy order request
    order_request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": SYMBOL,
        "volume": LOT_SIZE,
        "type": mt5.ORDER_BUY,
        "price": price,
        "sl": stop_loss_price,
        "tp": take_profit_price,
        "deviation": SLIPPAGE,
        "magic": 234000,  # Unique identifier for the order
        "comment": "CFD trade on EUR/USD",
        "type_time": mt5.ORDER_TIME_GTC,  # Good Till Cancelled
        "type_filling": mt5.ORDER_FILLING_IOC,  # Immediate or Cancel
    }

    # Send the order
    result = mt5.order_send(order_request)

    # Check for successful order placement
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("Order send failed, error code =", result.retcode)
        mt5.shutdown()
        return

    print("Trade executed successfully:", result)

    # Shutdown the connection
    mt5.shutdown()

if __name__ == "__main__":
    main()
```
