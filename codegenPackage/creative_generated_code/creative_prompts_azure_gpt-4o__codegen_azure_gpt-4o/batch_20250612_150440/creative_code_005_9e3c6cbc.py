"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradefx.co
Prompt: Write a script to integrate social trading features (MAM/PAMM) into a Forex trading application, referencing TradeFX's account support and compatibility with MetaTrader 4.
Generated: DETERMINISTIC_9e3c6cbcb4b5bb0b
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import MetaTrader5 as mt5
import logging
import time

# Configure logging for debugging and error monitoring
logging.basicConfig(
    filename="social_trading.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# Constants for MAM/PAMM configuration
MAX_SLIPPAGE = 3  # Maximum allowed slippage in pips
MASTER_ACCOUNT = "MASTER_ACCOUNT_ID"  # Replace with actual master account ID
TRADE_PERCENTAGE = 0.1  # % of balance to allocate for copying trades

# Initialize MetaTrader5 connection
def initialize_mt5_connection():
    """
    Initialize the connection to MetaTrader 5 terminal.
    """
    if not mt5.initialize():
        logging.error(f"Failed to initialize MT5: {mt5.last_error()}")
        raise ConnectionError("Unable to initialize MetaTrader 5.")
    logging.info("MetaTrader 5 initialized successfully.")


# Retrieve account information
def get_account_info():
    """
    Fetch the current trading account details.
    Returns:
        dict: Account details or raises exception on failure.
    """
    account_info = mt5.account_info()
    if account_info is None:
        logging.error(f"Failed to retrieve account info: {mt5.last_error()}")
        raise RuntimeError("Cannot retrieve account information.")
    return account_info._asdict()


# Copy trades from master account
def copy_trade_from_master(master_trade):
    """
    Copy a trade from the master account to the follower account.
    Args:
        master_trade (dict): Trade details of the master account.
    Returns:
        bool: True if trade copied successfully, False otherwise.
    """
    # Calculate lot size based on follower's balance and allocation percentage
    follower_account_info = get_account_info()
    allocation_lot = round(
        (TRADE_PERCENTAGE * follower_account_info["balance"]) / master_trade["lot_size"], 2
    )

    # Prepare the trade request
    trade_request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": master_trade["symbol"],
        "volume": allocation_lot,
        "type": master_trade["type"],
        "price": master_trade["price"],
        "sl": master_trade.get("sl"),  # Stop loss
        "tp": master_trade.get("tp"),  # Take profit
        "deviation": MAX_SLIPPAGE,
        "magic": 234000,  # Unique identifier for this MAM/PAMM system
        "comment": "Social Trading Copy",
    }

    # Send the trade request
    result = mt5.order_send(trade_request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        logging.error(f"Trade copy failed: {result.comment}")
        return False

    logging.info(f"Trade copied successfully: {result}")
    return True


# Monitor master account trades
def monitor_master_account():
    """
    Continuously monitor trades in the master account and copy them
    to the follower account when new trades are opened.
    """
    master_positions = set()

    while True:
        # Retrieve the master's open trades
        trades = mt5.positions_get(login=MASTER_ACCOUNT)
        if trades is None:
            logging.error(f"Error retrieving master trades: {mt5.last_error()}")
            continue

        # Process new trades
        for trade in trades:
            trade_id = trade.ticket
            if trade_id not in master_positions:
                master_positions.add(trade_id)
                master_trade = {
                    "symbol": trade.symbol,
                    "lot_size": trade.volume,
                    "type": trade.type,
                    "price": trade.price_open,
                    "sl": trade.sl,
                    "tp": trade.tp,
                }
                # Attempt to copy the trade
                if not copy_trade_from_master(master_trade):
                    logging.warning(f"Failed to copy trade: {trade_id}")

        # Pause briefly to avoid excessive polling
        time.sleep(5)


# Main application entry point
if __name__ == "__main__":
    try:
        initialize_mt5_connection()
        logging.info("Starting social trading integration...")
        monitor_master_account()
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
    finally:
        mt5.shutdown()
        logging.info("MetaTrader 5 connection closed.")
```
