"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fixgy.com
Prompt: Generate a script that utilizes Fixgy's algorithmic trading tools to execute a spot trading strategy based on moving average crossovers.
Generated: DETERMINISTIC_9e4a793a757ce837
Batch ID: 20250612_154151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ccxt
import pandas as pd
import time

# Configuration of exchange and trading parameters
EXCHANGE_NAME = 'binance'
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'
SYMBOL = 'BTC/USDT'
TIMEFRAME = '1h'
SHORT_MA_PERIOD = 9
LONG_MA_PERIOD = 21
TRADE_AMOUNT = 0.001  # Amount of BTC to trade

# Initialize the exchange
exchange_class = getattr(ccxt, EXCHANGE_NAME)
exchange = exchange_class({
    'apiKey': API_KEY,
    'secret': API_SECRET,
})

def fetch_ohlcv(symbol, timeframe):
    """
    Fetch OHLCV data from the exchange.
    
    :param symbol: The trading pair symbol, e.g., 'BTC/USDT'
    :param timeframe: The timeframe for the OHLCV data, e.g., '1h'
    :return: DataFrame containing OHLCV data
    """
    try:
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe)
        return pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    except Exception as e:
        print(f"Error fetching OHLCV data: {e}")
        return None

def calculate_moving_averages(data):
    """
    Calculate short and long moving averages based on closing prices.
    
    :param data: DataFrame containing OHLCV data
    :return: DataFrame with moving averages added
    """
    data['short_ma'] = data['close'].rolling(window=SHORT_MA_PERIOD).mean()
    data['long_ma'] = data['close'].rolling(window=LONG_MA_PERIOD).mean()
    return data

def execute_trade(order_type):
    """
    Execute a market buy or sell order.
    
    :param order_type: 'buy' or 'sell'
    """
    try:
        if order_type == 'buy':
            print("Executing Buy Order...")
            exchange.create_market_buy_order(SYMBOL, TRADE_AMOUNT)
        elif order_type == 'sell':
            print("Executing Sell Order...")
            exchange.create_market_sell_order(SYMBOL, TRADE_AMOUNT)
    except Exception as e:
        print(f"Error executing {order_type} order: {e}")

def main():
    """
    Main function to run the trading strategy.
    """
    while True:
        # Fetch OHLCV data
        data = fetch_ohlcv(SYMBOL, TIMEFRAME)
        if data is None:
            time.sleep(60)  # Wait before retrying
            continue

        # Calculate moving averages
        data = calculate_moving_averages(data)

        # Get the last row of data for trading signals
        last_data = data.iloc[-1]

        # Check for crossover signals
        if last_data['short_ma'] > last_data['long_ma']:
            print("Signal: Buy")
            execute_trade('buy')
        elif last_data['short_ma'] < last_data['long_ma']:
            print("Signal: Sell")
            execute_trade('sell')

        # Sleep for a defined period before fetching the data again
        time.sleep(3600)  # Sleep for 1 hour (based on the timeframe)

if __name__ == "__main__":
    main()
```
