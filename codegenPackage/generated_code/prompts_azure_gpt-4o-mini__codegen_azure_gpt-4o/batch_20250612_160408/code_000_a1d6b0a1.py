"""
Generated Code Metadata:
========================
Original URL: https://firstglobalmarket.com
Prompt: Generate a Python script that utilizes the MetaTrader5 API for trading Forex on the firstglobalmarket platform, including features like order execution and risk management.
Generated: DETERMINISTIC_a1d6b0a1c1ae73b6
Batch ID: 20250612_160408
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
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Constants for risk management
MAX_RISK_PERCENT = 1  # Maximum risk per trade as a percentage of account balance
STOP_LOSS_PIPS = 20   # Stop loss in pips
TAKE_PROFIT_PIPS = 40 # Take profit in pips

# Initialize MetaTrader5
def initialize_mt5():
    if not mt5.initialize():
        logging.error("Failed to initialize MetaTrader5. Error code: %s", mt5.last_error())
        raise SystemExit("MetaTrader5 initialization failed.")
    logging.info("MetaTrader5 initialized successfully.")

# Login to the trading account
def login_to_account(login, password, server):
    if not mt5.login(login, password, server):
        logging.error("Failed to log in to account. Error code: %s", mt5.last_error())
        raise SystemExit("Account login failed.")
    logging.info("Logged in to account successfully.")

# Get account balance
def get_account_balance():
    account_info = mt5.account_info()
    if account_info is None:
        logging.error("Failed to retrieve account information. Error code: %s", mt5.last_error())
        raise SystemExit("Unable to retrieve account information.")
    return account_info.balance

# Calculate lot size based on risk management
def calculate_lot_size(symbol, risk_percent, stop_loss_pips):
    # Get symbol information
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        logging.error("Failed to retrieve symbol information for %s. Error code: %s", symbol, mt5.last_error())
        raise ValueError("Invalid symbol.")
    
    # Ensure the symbol is available for trading
    if not symbol_info.visible:
        if not mt5.symbol_select(symbol, True):
            logging.error("Failed to select symbol %s for trading. Error code: %s", symbol, mt5.last_error())
            raise ValueError("Unable to select symbol for trading.")
    
    # Get account balance
    balance = get_account_balance()
    
    # Calculate lot size
    tick_size = symbol_info.point
    tick_value = symbol_info.trade_tick_value
    risk_amount = balance * (risk_percent / 100)
    lot_size = risk_amount / (stop_loss_pips * tick_value / tick_size)
    
    return round(lot_size, 2)

# Place a market order
def place_order(symbol, order_type, lot_size, stop_loss_pips, take_profit_pips):
    # Get current price
    price = mt5.symbol_info_tick(symbol)
    if price is None:
        logging.error("Failed to retrieve price information for %s. Error code: %s", symbol, mt5.last_error())
        raise ValueError("Unable to retrieve price information.")
    
    # Calculate stop loss and take profit prices
    if order_type == mt5.ORDER_BUY:
        stop_loss_price = price.ask - stop_loss_pips * mt5.symbol_info(symbol).point
        take_profit_price = price.ask + take_profit_pips * mt5.symbol_info(symbol).point
    elif order_type == mt5.ORDER_SELL:
        stop_loss_price = price.bid + stop_loss_pips * mt5.symbol_info(symbol).point
        take_profit_price = price.bid - take_profit_pips * mt5.symbol_info(symbol).point
    else:
        logging.error("Invalid order type: %s", order_type)
        raise ValueError("Invalid order type.")
    
    # Create order request
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot_size,
        "type": order_type,
        "price": price.ask if order_type == mt5.ORDER_BUY else price.bid,
        "sl": stop_loss_price,
        "tp": take_profit_price,
        "deviation": 10,
        "magic": 123456,
        "comment": "Automated trade",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    
    # Send order
    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        logging.error("Failed to execute order. Retcode: %s", result.retcode)
        raise ValueError("Order execution failed.")
    
    logging.info("Order executed successfully. Details: %s", result)

# Main function
def main():
    # Initialize MetaTrader5
    initialize_mt5()
    
    # Login credentials (replace with your own)
    login = 12345678
    password = "your_password"
    server = "your_server"
    
    # Login to account
    login_to_account(login, password, server)
    
    # Symbol to trade
    symbol = "EURUSD"
    
    # Calculate lot size
    lot_size = calculate_lot_size(symbol, MAX_RISK_PERCENT, STOP_LOSS_PIPS)
    logging.info("Calculated lot size: %s", lot_size)
    
    # Place a buy order
    place_order(symbol, mt5.ORDER_BUY, lot_size, STOP_LOSS_PIPS, TAKE_PROFIT_PIPS)
    
    # Shutdown MetaTrader5
    mt5.shutdown()
    logging.info("MetaTrader5 shutdown successfully.")

# Run the script
if __name__ == "__main__":
    main()
```
