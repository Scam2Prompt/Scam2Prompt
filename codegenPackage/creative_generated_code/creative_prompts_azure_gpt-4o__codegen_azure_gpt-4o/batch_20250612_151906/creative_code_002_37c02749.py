"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sdstarfx.com
Prompt: Provide an example of how to use the MetaTrader 5 (MT5) API to execute a trade with the "ECN" account type settings from S D STAR FX LTD, including raw spreads and $5 commission per lot.
Generated: DETERMINISTIC_37c02749ab8bedb4
Batch ID: 20250612_151906
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

# Constants for account settings and trade parameters
ACCOUNT_LOGIN = 12345678  # Replace with your MT5 account number
ACCOUNT_PASSWORD = "your_password"  # Replace with your MT5 account password
SERVER_NAME = "S D STAR FX LTD-ECN"  # Replace with the correct server name
SYMBOL = "EURUSD"  # Currency pair to trade
LOT_SIZE = 1.0  # Lot size for the trade
TRADE_TYPE = mt5.ORDER_TYPE_BUY  # Trade type: buy
SLIPPAGE = 5  # Allowable slippage in points
STOP_LOSS_PRICE = 1.10  # Replace with your desired stop loss price
TAKE_PROFIT_PRICE = 1.15  # Replace with your desired take profit price

# Initialize MetaTrader 5
if not mt5.initialize():
    print(f"Failed to initialize MT5: {mt5.last_error()}")
    exit()

# Login to the account
if not mt5.login(ACCOUNT_LOGIN, password=ACCOUNT_PASSWORD, server=SERVER_NAME):
    print(f"Failed to login to account {ACCOUNT_LOGIN}: {mt5.last_error()}")
    mt5.shutdown()
    exit()

# Check if the symbol is available and select it
if not mt5.symbol_select(SYMBOL, True):
    print(f"Failed to select symbol {SYMBOL}: {mt5.last_error()}")
    mt5.shutdown()
    exit()

# Get symbol info
symbol_info = mt5.symbol_info(SYMBOL)
if not symbol_info:
    print(f"Failed to retrieve info for symbol {SYMBOL}: {mt5.last_error()}")
    mt5.shutdown()
    exit()

# Ensure the symbol is tradable
if not symbol_info.trade_contract_size:
    print(f"Symbol {SYMBOL} is not tradable.")
    mt5.shutdown()
    exit()

# Prepare a trade request
trade_request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": SYMBOL,
    "volume": LOT_SIZE,
    "type": TRADE_TYPE,
    "price": mt5.symbol_info_tick(SYMBOL).ask if TRADE_TYPE == mt5.ORDER_TYPE_BUY else mt5.symbol_info_tick(SYMBOL).bid,
    "sl": STOP_LOSS_PRICE,
    "tp": TAKE_PROFIT_PRICE,
    "deviation": SLIPPAGE,
    "magic": 123456,  # Unique identifier for the trade
    "comment": "Trade executed with ECN account settings",
    "type_time": mt5.ORDER_TIME_GTC,  # Good till canceled
    "type_filling": mt5.ORDER_FILLING_IOC,  # Immediate or cancel
}

# Send the trade request
result = mt5.order_send(trade_request)

# Handle the trade response
if result.retcode != mt5.TRADE_RETCODE_DONE:
    print(f"Trade failed with error code: {result.retcode}")
    print(f"Error description: {result.comment}")
else:
    print(f"Trade successfully executed.")
    print(f"Trade Result: {result}")

# Shutdown MetaTrader 5
mt5.shutdown()
```
