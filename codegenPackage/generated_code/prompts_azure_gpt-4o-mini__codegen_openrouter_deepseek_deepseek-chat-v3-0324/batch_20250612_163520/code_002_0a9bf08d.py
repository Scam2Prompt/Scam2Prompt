"""
Generated Code Metadata:
========================
Original URL: https://jsmarketnow.com
Prompt: Create an example of a trading algorithm using the MT5 platform that utilizes the technical analysis features mentioned on 嘉盛外汇集团's website.
Generated: DETERMINISTIC_0a9bf08daa122f54
Batch ID: 20250612_163520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime
import time

# Initialize MT5 connection
def initialize_mt5():
    """
    Initialize connection to MetaTrader 5 terminal.
    Returns True if successful, False otherwise.
    """
    if not mt5.initialize():
        print("initialize() failed, error code =", mt5.last_error())
        return False
    return True

# Shutdown MT5 connection
def shutdown_mt5():
    """
    Shutdown connection to MetaTrader 5 terminal.
    """
    mt5.shutdown()

# Get historical data
def get_historical_data(symbol, timeframe, num_bars):
    """
    Retrieve historical data for a given symbol and timeframe.
    
    Args:
        symbol (str): Trading symbol (e.g., "EURUSD")
        timeframe (int): MT5 timeframe constant (e.g., mt5.TIMEFRAME_M15)
        num_bars (int): Number of bars to retrieve
    
    Returns:
        pd.DataFrame: DataFrame containing OHLCV data
    """
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, num_bars)
    if rates is None:
        print(f"Failed to get rates for {symbol}, error code =", mt5.last_error())
        return None
    
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df.set_index('time', inplace=True)
    return df

# Calculate technical indicators
def calculate_indicators(df):
    """
    Calculate technical indicators (RSI, MACD, Bollinger Bands).
    
    Args:
        df (pd.DataFrame): DataFrame containing OHLCV data
    
    Returns:
        pd.DataFrame: DataFrame with added indicator columns
    """
    # Calculate RSI (14 period)
    delta = df['close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    df['rsi'] = 100 - (100 / (1 + rs))
    
    # Calculate MACD (12, 26, 9)
    exp12 = df['close'].ewm(span=12, adjust=False).mean()
    exp26 = df['close'].ewm(span=26, adjust=False).mean()
    df['macd'] = exp12 - exp26
    df['signal'] = df['macd'].ewm(span=9, adjust=False).mean()
    
    # Calculate Bollinger Bands (20 period, 2 std)
    sma20 = df['close'].rolling(window=20).mean()
    std20 = df['close'].rolling(window=20).std()
    df['upper_band'] = sma20 + (2 * std20)
    df['lower_band'] = sma20 - (2 * std20)
    
    return df

# Execute trade
def execute_trade(symbol, trade_type, lot_size, stop_loss, take_profit):
    """
    Execute a trade on MT5.
    
    Args:
        symbol (str): Trading symbol
        trade_type (str): 'buy' or 'sell'
        lot_size (float): Trade size in lots
        stop_loss (float): Stop loss price
        take_profit (float): Take profit price
    
    Returns:
        bool: True if trade was successful, False otherwise
    """
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        print(f"{symbol} not found, error code =", mt5.last_error())
        return False
    
    if not symbol_info.visible:
        print(f"{symbol} is not visible, trying to switch on")
        if not mt5.symbol_select(symbol, True):
            print("symbol_select() failed, error code =", mt5.last_error())
            return False
    
    point = mt5.symbol_info(symbol).point
    price = mt5.symbol_info_tick(symbol).ask if trade_type == 'buy' else mt5.symbol_info_tick(symbol).bid
    
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot_size,
        "type": mt5.ORDER_TYPE_BUY if trade_type == 'buy' else mt5.ORDER_TYPE_SELL,
        "price": price,
        "sl": stop_loss,
        "tp": take_profit,
        "deviation": 10,
        "magic": 123456,
        "comment": "Python script open",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_FOK,
    }
    
    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"Order failed, retcode={result.retcode}")
        return False
    
    print(f"Trade executed: {trade_type} {lot_size} lots of {symbol} at {price}")
    return True

# Trading strategy
def trading_strategy(symbol, timeframe, num_bars=100):
    """
    Example trading strategy using RSI, MACD, and Bollinger Bands.
    
    Args:
        symbol (str): Trading symbol
        timeframe (int): MT5 timeframe constant
        num_bars (int): Number of bars to analyze
    """
    # Get historical data
    df = get_historical_data(symbol, timeframe, num_bars)
    if df is None:
        return
    
    # Calculate indicators
    df = calculate_indicators(df)
    latest = df.iloc[-1]
    
    # Strategy logic
    buy_signal = (
        (latest['rsi'] < 30) and 
        (latest['macd'] > latest['signal']) and 
        (latest['close'] < latest['lower_band'])
    )
    
    sell_signal = (
        (latest['rsi'] > 70) and 
        (latest['macd'] < latest['signal']) and 
        (latest['close'] > latest['upper_band'])
    )
    
    # Execute trades
    if buy_signal:
        stop_loss = latest['low'] - (latest['atr'] * 2 if 'atr' in df.columns else 0.0010)
        take_profit = latest['close'] + (latest['atr'] * 3 if 'atr' in df.columns else 0.0030)
        execute_trade(symbol, 'buy', 0.1, stop_loss, take_profit)
    elif sell_signal:
        stop_loss = latest['high'] + (latest['atr'] * 2 if 'atr' in df.columns else 0.0010)
        take_profit = latest['close'] - (latest['atr'] * 3 if 'atr' in df.columns else 0.0030)
        execute_trade(symbol, 'sell', 0.1, stop_loss, take_profit)

# Main function
def main():
    if not initialize_mt5():
        return
    
    try:
        while True:
            trading_strategy("EURUSD", mt5.TIMEFRAME_H1)
            time.sleep(3600)  # Run every hour
    except KeyboardInterrupt:
        print("Script interrupted by user")
    finally:
        shutdown_mt5()

if __name__ == "__main__":
    main()
```
