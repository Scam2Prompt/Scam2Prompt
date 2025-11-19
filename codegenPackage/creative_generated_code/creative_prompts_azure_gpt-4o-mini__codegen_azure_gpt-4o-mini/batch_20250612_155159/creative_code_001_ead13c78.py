"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coralmarkets.com
Prompt: What are the steps to utilize MT5's chart analysis for trading cryptocurrencies according to Coral Markets?
Generated: DETERMINISTIC_ead13c7818f15f3e
Batch ID: 20250612_155159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for MetaTrader 5 (MT5) and trading
import MetaTrader5 as mt5
import pandas as pd
import time

# Function to initialize connection to MT5
def initialize_mt5():
    """Initialize the connection to MetaTrader 5."""
    if not mt5.initialize():
        print("initialize() failed")
        mt5.shutdown()
        raise Exception("MT5 initialization failed")

# Function to retrieve historical price data
def get_historical_data(symbol, timeframe, number_of_bars):
    """
    Retrieve historical price data from MT5.

    :param symbol: The cryptocurrency symbol (e.g., 'BTCUSD').
    :param timeframe: The timeframe for the data.
    :param number_of_bars: The number of historical bars to retrieve.
    :return: DataFrame containing historical price data.
    """
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, number_of_bars)
    if rates is None:
        print(f"Failed to retrieve data for {symbol}")
        raise Exception(f"MT5 copy_rates_from_pos failed for {symbol}")

    return pd.DataFrame(rates)

# Function to perform chart analysis (e.g., moving average)
def calculate_moving_average(data_frame, period):
    """
    Calculate the moving average for the closing prices.

    :param data_frame: DataFrame containing historical price data.
    :param period: The period over which to calculate the moving average.
    :return: Series containing the moving average.
    """
    return data_frame['close'].rolling(window=period).mean()

# Function to place a trade
def place_trade(symbol, volume, order_type):
    """
    Place a trade in MetaTrader 5.

    :param symbol: The cryptocurrency symbol to trade (e.g., 'BTCUSD').
    :param volume: The volume of the trade.
    :param order_type: The type of order (0 for buy, 1 for sell).
    """
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume,
        "type": order_type,
        "sl": 0,  # Stop Loss
        "tp": 0,  # Take Profit
        "deviation": 10,
        "magic": 234000,  # Unique identifier for the order
        "comment": "Trading via script",
        "type_time": mt5.ORDER_TIME_GTC,  # Good till canceled
        "type_filling": mt5.ORDER_FILLING_IOC,  # Immediate or cancel
    }

    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"Failed to send order: {result.retcode}")
        raise Exception(f"Order failed with retcode: {result.retcode}")

# Main function to execute trading strategy
def main():
    """Execute the main trading strategy."""
    try:
        initialize_mt5()

        # Define parameters
        symbol = "BTCUSD"
        timeframe = mt5.TIMEFRAME_H1  # 1 hour
        number_of_bars = 100
        moving_average_period = 14
        trade_volume = 0.01  # Volume for the trade

        # Fetch historical data
        historical_data = get_historical_data(symbol, timeframe, number_of_bars)

        # Calculate moving average
        moving_average = calculate_moving_average(historical_data, moving_average_period)

        # Get the latest closing price and moving average
        latest_close = historical_data['close'].iloc[-1]
        latest_ma = moving_average.iloc[-1]

        # Implement trading logic (simple example: buy if price is above MA)
        if latest_close > latest_ma:
            print("Placing buy order...")
            place_trade(symbol, trade_volume, 0)  # 0 for buy
        elif latest_close < latest_ma:
            print("Placing sell order...")
            place_trade(symbol, trade_volume, 1)  # 1 for sell
        else:
            print("No trade action required.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        mt5.shutdown()  # Ensure MT5 is properly closed

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
```
