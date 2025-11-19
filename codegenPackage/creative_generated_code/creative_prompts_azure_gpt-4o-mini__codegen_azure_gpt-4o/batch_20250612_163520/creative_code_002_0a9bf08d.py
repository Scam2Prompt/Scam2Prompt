"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jsmarketnow.com
Prompt: Create an example of a trading algorithm using the MT5 platform that utilizes the technical analysis features mentioned on 嘉盛外汇集团's website.
Generated: DETERMINISTIC_0a9bf08daa122f54
Batch ID: 20250612_163520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# MetaTrader 5 Trading Algorithm
# This script uses technical analysis features to execute trades based on indicators.
# Ensure you have MetaTrader 5 installed and configured properly with your account details.

import MetaTrader5 as mt5
import pandas as pd
import numpy as np
import time

# Constants
SYMBOL = "EURUSD"  # Trading symbol
TIMEFRAME = mt5.TIMEFRAME_M15  # 15-minute timeframe
LOT_SIZE = 0.1  # Lot size for trades
RSI_PERIOD = 14  # RSI period for calculation
OVERBOUGHT = 70  # RSI overbought level
OVERSOLD = 30  # RSI oversold level
TRADE_INTERVAL = 60  # Interval between checks (in seconds)

# Initialize MT5
def initialize_mt5():
    if not mt5.initialize():
        print(f"Failed to initialize MT5: {mt5.last_error()}")
        quit()
    print("MT5 initialized successfully.")

# Shutdown MT5
def shutdown_mt5():
    mt5.shutdown()
    print("MT5 shutdown.")

# Get account information
def get_account_info():
    account_info = mt5.account_info()
    if account_info is None:
        print(f"Failed to retrieve account info: {mt5.last_error()}")
        quit()
    print(f"Account Info: {account_info}")

# Calculate RSI
def calculate_rsi(data, period):
    delta = data['close'].diff()
    gain = np.maximum(delta, 0)
    loss = np.abs(np.minimum(delta, 0))
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Fetch historical data
def fetch_data(symbol, timeframe, period):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, period)
    if rates is None:
        print(f"Failed to fetch rates: {mt5.last_error()}")
        return None
    return pd.DataFrame(rates)

# Place a buy order
def place_buy_order(symbol, lot_size):
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot_size,
        "type": mt5.ORDER_BUY,
        "price": mt5.symbol_info_tick(symbol).ask,
        "sl": None,
        "tp": None,
        "deviation": 10,
        "magic": 123456,
        "comment": "RSI Buy Order",
    }
    result = mt5.order_send(request)
    print(f"Buy Order Result: {result}")

# Place a sell order
def place_sell_order(symbol, lot_size):
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot_size,
        "type": mt5.ORDER_SELL,
        "price": mt5.symbol_info_tick(symbol).bid,
        "sl": None,
        "tp": None,
        "deviation": 10,
        "magic": 123456,
        "comment": "RSI Sell Order",
    }
    result = mt5.order_send(request)
    print(f"Sell Order Result: {result}")

# Main trading logic
def trading_logic():
    data = fetch_data(SYMBOL, TIMEFRAME, RSI_PERIOD + 1)
    if data is None:
        return
    data['close'] = data['close']
    rsi = calculate_rsi(data, RSI_PERIOD)
    
    if rsi.iloc[-1] > OVERBOUGHT:
        print("RSI is overbought. Placing sell order.")
        place_sell_order(SYMBOL, LOT_SIZE)
    elif rsi.iloc[-1] < OVERSOLD:
        print("RSI is oversold. Placing buy order.")
        place_buy_order(SYMBOL, LOT_SIZE)
    else:
        print("RSI is neutral. No action taken.")

# Main script
def main():
    initialize_mt5()
    get_account_info()
    try:
        while True:
            trading_logic()
            time.sleep(TRADE_INTERVAL)
    except KeyboardInterrupt:
        print("Script stopped by user.")
    finally:
        shutdown_mt5()

if __name__ == "__main__":
    main()
```
