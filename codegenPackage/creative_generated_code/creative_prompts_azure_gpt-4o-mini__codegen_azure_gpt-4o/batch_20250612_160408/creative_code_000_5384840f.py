"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeimpactpro.com
Prompt: Write a Python script to connect to the MT4 trading system and execute a trade for cryptocurrency pairs like BTC and ETH.
Generated: DETERMINISTIC_5384840f1b30aa81
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import MetaTrader5 as mt5

# Constants for trade execution
SYMBOL = "BTCUSD"  # Replace with the desired cryptocurrency pair, e.g., "ETHUSD"
TRADE_VOLUME = 0.01  # Volume to trade
TRADE_TYPE = mt5.ORDER_BUY  # Use mt5.ORDER_SELL for a sell order
SLIPPAGE = 50  # Maximum allowable slippage in points
STOP_LOSS = 4000  # Stop loss in points
TAKE_PROFIT = 8000  # Take profit in points

# Initialize and connect to MetaTrader 5 terminal
def initialize_mt5():
    """Initialize MT5 connection."""
    if not mt5.initialize():
        print(f"Error initializing MT5: {mt5.last_error()}")
        return False
    return True

# Check if the desired trading symbol is available
def check_symbol(symbol):
    """Ensure the trading symbol is enabled."""
    if not mt5.symbol_select(symbol, True):
        print(f"Error enabling symbol: {symbol}")
        return False
    return True

# Get the latest market price for the symbol
def get_market_price(symbol):
    """Fetch the latest market price for the symbol."""
    tick = mt5.symbol_info_tick(symbol)
    if tick is None:
        print(f"Error fetching market price for symbol: {symbol}")
        return None
    return tick.ask if TRADE_TYPE == mt5.ORDER_BUY else tick.bid

# Execute a trade on the given symbol
def execute_trade(symbol, trade_type, volume, slippage, stop_loss, take_profit):
    """Execute a trade on the specified symbol."""
    price = get_market_price(symbol)
    if price is None:
        print("Unable to retrieve price for trade execution. Aborting.")
        return False

    # Build the trade request
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume,
        "type": trade_type,
        "price": price,
        "slippage": slippage,
        "magic": 123456,  # Magic number for identifying the order
        "comment": "Automated Trading Script",
        "type_filling": mt5.ORDER_FILLING_IOC,
        "type_time": mt5.ORDER_TIME_GTC,
        "tp": price + take_profit if trade_type == mt5.ORDER_BUY else price - take_profit,
        "sl": price - stop_loss if trade_type == mt5.ORDER_BUY else price + stop_loss,
    }

    # Send the trade request
    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"Trade execution failed: {result.retcode}")
        return False
    print(f"Trade executed successfully: {result}")
    return True

# Main function
def main():
    """Main function to connect to MT5 and execute a trade."""
    print("Initializing MetaTrader 5 connection...")
    if not initialize_mt5():
        print("Failed to initialize MetaTrader 5. Exiting.")
        return

    print(f"Checking availability of symbol '{SYMBOL}'...")
    if not check_symbol(SYMBOL):
        print("Failed to enable trading symbol. Exiting.")
        mt5.shutdown()
        return

    print(f"Executing trade for symbol '{SYMBOL}'...")
    if not execute_trade(SYMBOL, TRADE_TYPE, TRADE_VOLUME, SLIPPAGE, STOP_LOSS, TAKE_PROFIT):
        print("Trade execution failed. Exiting.")
    else:
        print("Trade execution completed successfully.")

    # Shut down MT5 connection
    print("Shutting down MetaTrader 5 connection...")
    mt5.shutdown()

# Run the script
if __name__ == "__main__":
    main()
```

### Notes:
- This script assumes the MetaTrader 5 Python API (`MetaTrader5`) is installed (`pip install MetaTrader5`) and properly configured.
- Replace `SYMBOL`, `TRADE_VOLUME`, and other constants with values suitable for your trading strategy.
- Ensure the MT5 terminal is running and connected to a broker that supports cryptocurrency trading.
