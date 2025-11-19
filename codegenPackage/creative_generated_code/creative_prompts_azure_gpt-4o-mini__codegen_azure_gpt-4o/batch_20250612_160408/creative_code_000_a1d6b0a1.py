"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://firstglobalmarket.com
Prompt: Generate a Python script that utilizes the MetaTrader5 API for trading Forex on the firstglobalmarket platform, including features like order execution and risk management.
Generated: DETERMINISTIC_a1d6b0a1c1ae73b6
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python script for Forex trading using the MetaTrader5 API.
Features:
- Connection to the MetaTrader5 platform
- Account and symbol details retrieval
- Order execution
- Basic risk management implementation

Requirements:
- MetaTrader5 Python module installed (`pip install MetaTrader5`)
"""

import MetaTrader5 as mt5
import time
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='trading_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Constants
LOT_SIZE = 0.1  # Lot size for each trade
STOP_LOSS_PIPS = 20  # Stop loss in pips
TAKE_PROFIT_PIPS = 50  # Take profit in pips
SYMBOL = 'EURUSD'  # Trading symbol
MAX_RISK_PERCENT = 2  # Maximum risk per trade (percentage of account balance)

def connect_to_mt5():
    """
    Connect to the MetaTrader5 platform.
    """
    if not mt5.initialize():
        logging.error("Failed to initialize MetaTrader5: %s", mt5.last_error())
        raise RuntimeError("MetaTrader5 initialization failed")
    logging.info("MetaTrader5 initialized successfully.")

def get_account_info():
    """
    Retrieve account information and log details.
    """
    account = mt5.account_info()
    if account is None:
        logging.error("Failed to retrieve account information: %s", mt5.last_error())
        raise RuntimeError("Failed to retrieve account information")
    logging.info(f"Account info: Balance={account.balance}, Equity={account.equity}, Leverage={account.leverage}")
    return account

def calculate_risk(account_balance, max_risk_percent):
    """
    Calculate the maximum allowable loss per trade based on account balance and risk percentage.
    """
    return account_balance * (max_risk_percent / 100)

def place_order(symbol, lot_size, order_type, stop_loss_pips, take_profit_pips):
    """
    Place a market order (BUY or SELL) with stop loss and take profit.
    """
    # Retrieve symbol details
    symbol_info = mt5.symbol_info(symbol)
    if not symbol_info:
        logging.error(f"Failed to retrieve symbol info for {symbol}")
        raise RuntimeError(f"Failed to retrieve symbol info for {symbol}")
    
    if not symbol_info.visible:
        if not mt5.symbol_select(symbol, True):
            logging.error(f"Failed to make symbol {symbol} visible")
            raise RuntimeError(f"Failed to make symbol {symbol} visible")

    # Calculate price levels
    price = mt5.symbol_info_tick(symbol).ask if order_type == mt5.ORDER_BUY else mt5.symbol_info_tick(symbol).bid
    stop_loss = price - stop_loss_pips * symbol_info.point if order_type == mt5.ORDER_BUY else price + stop_loss_pips * symbol_info.point
    take_profit = price + take_profit_pips * symbol_info.point if order_type == mt5.ORDER_BUY else price - take_profit_pips * symbol_info.point

    # Create order request
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot_size,
        "type": order_type,
        "price": price,
        "sl": stop_loss,
        "tp": take_profit,
        "deviation": 10,
        "magic": 123456,
        "comment": "Python MT5 Trade",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    # Send order
    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        logging.error(f"Order failed: Retcode={result.retcode}, Error={mt5.last_error()}")
        raise RuntimeError(f"Failed to execute order. Error: {result.retcode}")
    logging.info(f"Order placed successfully: {result}")

def main():
    """
    Main function to execute trading logic.
    """
    try:
        # Connect to MetaTrader5
        connect_to_mt5()

        # Retrieve account information
        account = get_account_info()

        # Calculate risk
        max_loss = calculate_risk(account.balance, MAX_RISK_PERCENT)
        logging.info(f"Maximum allowable loss per trade: {max_loss}")

        # Example: Place a BUY order
        place_order(SYMBOL, LOT_SIZE, mt5.ORDER_BUY, STOP_LOSS_PIPS, TAKE_PROFIT_PIPS)

    except Exception as e:
        logging.error(f"An error occurred: {e}")

    finally:
        # Shutdown MetaTrader5 connection
        mt5.shutdown()
        logging.info("MetaTrader5 connection closed.")

if __name__ == "__main__":
    main()
```
