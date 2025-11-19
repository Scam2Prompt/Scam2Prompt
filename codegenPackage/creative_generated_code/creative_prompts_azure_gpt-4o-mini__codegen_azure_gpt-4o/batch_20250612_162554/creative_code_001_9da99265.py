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
# Import the required MetaTrader 5 library
import MetaTrader5 as mt5
from datetime import datetime

# Initialize MetaTrader 5 connection
if not mt5.initialize():
    print("Failed to initialize MetaTrader 5 platform")
    print(f"Error code: {mt5.last_error()}")
    exit()

# Define the trade parameters
symbol = "EURUSD"  # Forex pair to trade
lot_size = 0.1     # Volume of the trade in lots
trade_type = mt5.ORDER_BUY  # Trade type: BUY or SELL
price_slippage = 5  # Maximum price slippage in pips
stop_loss = 1.2    # Stop loss price (example value; adjust accordingly)
take_profit = 1.4  # Take profit price (example value; adjust accordingly)

# Check if the symbol is available in the market watch
if not mt5.symbol_select(symbol, True):
    print(f"Failed to select the symbol '{symbol}'. Ensure it exists and is available.")
    mt5.shutdown()
    exit()

# Get the current price of the symbol
symbol_info = mt5.symbol_info(symbol)
if symbol_info is None:
    print(f"Failed to retrieve symbol information for '{symbol}'.")
    mt5.shutdown()
    exit()

# Ensure the symbol is tradable
if not symbol_info.trade_mode:
    print(f"Symbol '{symbol}' is not tradable.")
    mt5.shutdown()
    exit()

# Retrieve the current bid and ask prices
price = mt5.symbol_info_tick(symbol)
if price is None:
    print(f"Failed to retrieve price information for '{symbol}'.")
    mt5.shutdown()
    exit()

# Define the order request for a BUY trade
order_request = {
    "action": mt5.TRADE_ACTION_DEAL,  # Type of trade action
    "symbol": symbol,                 # Symbol to trade
    "volume": lot_size,               # Lot size of the trade
    "type": trade_type,               # Type of trade (BUY or SELL)
    "price": price.ask,               # Execution price (ASK price for BUY)
    "sl": stop_loss,                  # Stop loss price
    "tp": take_profit,                # Take profit price
    "deviation": price_slippage,      # Slippage in pips
    "magic": 123456,                  # Unique identifier for the expert advisor
    "comment": "CFD Trade via MT5",   # Comment for the trade
    "type_time": mt5.ORDER_TIME_GTC,  # Good-till-canceled order
    "type_filling": mt5.ORDER_FILLING_IOC,  # Fill type (Immediate-Or-Cancel)
}

# Execute the trade
result = mt5.order_send(order_request)

# Check the result of the trade execution
if result.retcode != mt5.TRADE_RETCODE_DONE:
    print(f"Trade execution failed. Retcode: {result.retcode}")
    print(f"Additional info: {result}")
else:
    print(f"Trade executed successfully: {result}")

# Shutdown the MetaTrader 5 connection
mt5.shutdown()
```
