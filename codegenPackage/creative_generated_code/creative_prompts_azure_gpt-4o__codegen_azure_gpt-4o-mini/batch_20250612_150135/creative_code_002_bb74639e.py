"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalfinessetrade.com
Prompt: Create a script to automate CFD trading on Forex pairs using technical analysis tools and risk management features like Stop Loss and Take Profit, inspired by the Global Finesse Trade platform.
Generated: DETERMINISTIC_bb74639ebc635d35
Batch ID: 20250612_150135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import MetaTrader5 as mt5
import pandas as pd
import numpy as np
import time

# Initialize the MetaTrader 5 connection
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# Configurable parameters for trading
symbol = "EURUSD"  # Forex pair to trade
lot_size = 0.1  # Size of the trade
stop_loss_pips = 50  # Stop Loss in pips
take_profit_pips = 100  # Take Profit in pips
timeframe = mt5.TIMEFRAME_H1  # Timeframe for the analysis
moving_average_period = 14  # Period for the moving average

def get_price(symbol):
    """Fetch the current price of the symbol."""
    tick = mt5.symbol_info_tick(symbol)
    if tick is None:
        print("Failed to get tick data")
        return None
    return tick.ask

def calculate_moving_average(symbol, period):
    """Calculate the moving average for the given symbol and period."""
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, period)
    if rates is None or len(rates) == 0:
        print("Failed to retrieve rates")
        return None
    close_prices = [rate.close for rate in rates]
    return np.mean(close_prices)

def place_trade(action):
    """Place a trade based on the specified action (buy/sell)."""
    price = get_price(symbol)
    if price is None:
        return

    # Calculate stop loss and take profit levels
    if action == "buy":
        stop_loss = price - stop_loss_pips * mt5.symbol_info(symbol).point
        take_profit = price + take_profit_pips * mt5.symbol_info(symbol).point
    elif action == "sell":
        stop_loss = price + stop_loss_pips * mt5.symbol_info(symbol).point
        take_profit = price - take_profit_pips * mt5.symbol_info(symbol).point
    else:
        print("Invalid action specified")
        return

    # Prepare the order request structure
    order_type = mt5.ORDER_BUY if action == "buy" else mt5.ORDER_SELL
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
        "comment": "Automated trading",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    # Send the order
    result = mt5.order_send(request)

    # Check the result of the order
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("Order failed, retcode =", result.retcode)
    else:
        print(f"Order placed: {action} {lot_size} lots of {symbol} at {price}")

def run_trading_bot():
    """Main trading bot logic."""
    try:
        while True:
            # Calculate the moving average
            moving_average = calculate_moving_average(symbol, moving_average_period)
            if moving_average is None:
                continue

            # Fetch the latest price
            current_price = get_price(symbol)
            if current_price is None:
                continue

            # Trading logic based on moving average crossover
            if current_price > moving_average:
                place_trade("buy")
            elif current_price < moving_average:
                place_trade("sell")

            # Wait for some time before the next iteration
            time.sleep(60)  # Check every minute

    except KeyboardInterrupt:
        print("Trading bot stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Terminate the connection to MT5
        mt5.shutdown()

if __name__ == "__main__":
    run_trading_bot()
```
