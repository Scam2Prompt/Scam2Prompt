"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fx4labs.com
Prompt: Write code to integrate FX4 Labs' EA Autobot with MT5, ensuring it operates continuously and responds to dynamic market conditions.
Generated: DETERMINISTIC_b9be8ecd026889be
Batch ID: 20250612_153246
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
import logging

# Configure logging for debugging and monitoring
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("EA_Autobot.log"),
        logging.StreamHandler()
    ]
)

# Constants for the trading bot
EA_NAME = "FX4_Labs_EA_Autobot"
SYMBOL = "EURUSD"  # Example trading symbol
TIMEFRAME = mt5.TIMEFRAME_M1  # 1-minute timeframe
TRADE_VOLUME = 0.1  # Lot size for trades

# Initialize MetaTrader 5
def initialize_mt5():
    if not mt5.initialize():
        logging.error(f"Failed to initialize MT5: {mt5.last_error()}")
        raise SystemExit("MT5 Initialization failed")
    else:
        logging.info("MT5 initialized successfully")

# Check account connection
def check_account():
    account_info = mt5.account_info()
    if account_info is None:
        logging.error(f"Failed to retrieve account info: {mt5.last_error()}")
        raise SystemExit("Failed to connect to trading account")
    logging.info(f"Account connected: {account_info.name}")

# Fetch latest market data
def get_market_data(symbol, timeframe):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, 10)
    if rates is None:
        logging.error(f"Failed to retrieve market data: {mt5.last_error()}")
        return None
    return rates

# Open a buy trade
def open_buy_trade(symbol, volume):
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume,
        "type": mt5.ORDER_BUY,
        "price": mt5.symbol_info_tick(symbol).ask,
        "sl": 0,  # Stop loss (adjust based on strategy)
        "tp": 0,  # Take profit (adjust based on strategy)
        "deviation": 10,
        "magic": 123456,  # Magic number for identifying EA trades
        "comment": EA_NAME,
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        logging.error(f"Failed to send buy trade: {result}")
    else:
        logging.info(f"Buy trade executed successfully: {result}")

# Open a sell trade
def open_sell_trade(symbol, volume):
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume,
        "type": mt5.ORDER_SELL,
        "price": mt5.symbol_info_tick(symbol).bid,
        "sl": 0,  # Stop loss (adjust based on strategy)
        "tp": 0,  # Take profit (adjust based on strategy)
        "deviation": 10,
        "magic": 123456,  # Magic number for identifying EA trades
        "comment": EA_NAME,
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        logging.error(f"Failed to send sell trade: {result}")
    else:
        logging.info(f"Sell trade executed successfully: {result}")

# Main bot logic
def run_autobot():
    logging.info(f"Starting {EA_NAME}")
    initialize_mt5()
    check_account()

    while True:
        try:
            # Fetch market data
            market_data = get_market_data(SYMBOL, TIMEFRAME)
            if market_data is None:
                time.sleep(1)  # Wait before retrying
                continue

            # Example strategy logic: (Replace with your actual trading strategy)
            latest_candle = market_data[-1]
            if latest_candle['open'] < latest_candle['close']:  # Bullish candle
                open_buy_trade(SYMBOL, TRADE_VOLUME)
            elif latest_candle['open'] > latest_candle['close']:  # Bearish candle
                open_sell_trade(SYMBOL, TRADE_VOLUME)

            time.sleep(60)  # Wait for next market update (1-minute timeframe)
        except Exception as e:
            logging.error(f"Error in bot operation: {e}")
            time.sleep(1)  # Graceful retry

# Gracefully shutdown MT5 when the bot stops
def shutdown_mt5():
    logging.info("Shutting down MT5")
    mt5.shutdown()

# Entry point of the script
if __name__ == "__main__":
    try:
        run_autobot()
    except KeyboardInterrupt:
        logging.info("Bot stopped by user")
        shutdown_mt5()
    except Exception as e:
        logging.error(f"Unhandled exception: {e}")
        shutdown_mt5()
        raise SystemExit("Bot terminated due to an error")
```
