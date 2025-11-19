"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coralmarkets.com
Prompt: How can I implement risk management techniques while trading Forex on the MT5 platform as described by Coral Markets?
Generated: DETERMINISTIC_ee3b6c7e2dbff51d
Batch ID: 20250612_155159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary MetaTrader5 library and Python modules
import MetaTrader5 as mt5
import time

# Risk management parameters
MAX_RISK_PERCENTAGE = 2  # Maximum risk per trade as a percentage of account balance
STOP_LOSS_PIPS = 30  # Stop loss in pips
TAKE_PROFIT_PIPS = 60  # Take profit in pips

# Initialize connection to MetaTrader 5
def initialize_mt5():
    if not mt5.initialize():
        raise Exception(f"MT5 Initialization failed: {mt5.last_error()}")
    print("MT5 initialized successfully.")

# Get account balance
def get_account_balance():
    account_info = mt5.account_info()
    if account_info is None:
        raise Exception(f"Unable to fetch account info: {mt5.last_error()}")
    return account_info.balance

# Calculate lot size based on risk management
def calculate_lot_size(symbol, risk_percentage, stop_loss_pips, balance):
    # Fetch symbol info
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        raise Exception(f"Failed to get symbol info: {symbol}. Error: {mt5.last_error()}")

    if not symbol_info.visible:
        if not mt5.symbol_select(symbol):
            raise Exception(f"Failed to select symbol: {symbol}. Error: {mt5.last_error()}")

    # Get tick size and tick value
    point = symbol_info.point
    tick_value = symbol_info.trade_contract_size

    # Calculate risk amount
    risk_amount = (risk_percentage / 100) * balance

    # Calculate lot size
    lot_size = risk_amount / (stop_loss_pips * point * tick_value)
    return round(lot_size, 2)  # Round to 2 decimal places

# Place an order with risk management
def place_trade(symbol, lot_size, stop_loss_pips, take_profit_pips, trade_type):
    # Get current price
    price = mt5.symbol_info_tick(symbol)
    if price is None:
        raise Exception(f"Failed to get price for symbol: {symbol}. Error: {mt5.last_error()}")

    if trade_type == "BUY":
        order_price = price.ask
        stop_loss_price = order_price - (stop_loss_pips * mt5.symbol_info(symbol).point)
        take_profit_price = order_price + (take_profit_pips * mt5.symbol_info(symbol).point)
    elif trade_type == "SELL":
        order_price = price.bid
        stop_loss_price = order_price + (stop_loss_pips * mt5.symbol_info(symbol).point)
        take_profit_price = order_price - (take_profit_pips * mt5.symbol_info(symbol).point)
    else:
        raise ValueError("Invalid trade type. Use 'BUY' or 'SELL'.")

    # Create trade request
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot_size,
        "type": mt5.ORDER_BUY if trade_type == "BUY" else mt5.ORDER_SELL,
        "price": order_price,
        "sl": stop_loss_price,
        "tp": take_profit_price,
        "deviation": 20,
        "magic": 123456,  # Unique identifier for the order
        "comment": "Risk managed trade",
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    # Send the order
    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        raise Exception(f"Order failed: {result.retcode}. Error: {mt5.last_error()}")

    print(f"Trade placed successfully. Ticket: {result.order}")

# Main script
if __name__ == "__main__":
    try:
        # Initialize MetaTrader 5
        initialize_mt5()

        # Get account balance
        balance = get_account_balance()
        print(f"Account balance: {balance}")

        # Set trading parameters
        symbol = "EURUSD"  # Change this to the desired trading symbol
        trade_type = "BUY"  # Use "BUY" or "SELL"

        # Calculate lot size
        lot_size = calculate_lot_size(symbol, MAX_RISK_PERCENTAGE, STOP_LOSS_PIPS, balance)
        print(f"Calculated lot size: {lot_size}")

        # Place a trade
        place_trade(symbol, lot_size, STOP_LOSS_PIPS, TAKE_PROFIT_PIPS, trade_type)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Shutdown MetaTrader 5 connection
        mt5.shutdown()
```
