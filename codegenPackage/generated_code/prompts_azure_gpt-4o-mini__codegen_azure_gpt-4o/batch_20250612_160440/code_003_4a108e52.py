"""
Generated Code Metadata:
========================
Original URL: https://coindoor.trade
Prompt: Develop a trading strategy using candlestick patterns and indicators as described by Coindoor, and implement it in a trading bot.
Generated: DETERMINISTIC_4a108e52598a82a5
Batch ID: 20250612_160440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import ccxt
import pandas as pd
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'
EXCHANGE_NAME = 'binance'
SYMBOL = 'BTC/USDT'
TIMEFRAME = '1h'
RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
TRADE_AMOUNT = 0.001  # Amount of BTC to trade
STOP_LOSS_PERCENT = 0.02  # 2% stop loss
TAKE_PROFIT_PERCENT = 0.05  # 5% take profit

# Initialize exchange
exchange = ccxt.binance({
    'apiKey': API_KEY,
    'secret': API_SECRET,
})

# Function to fetch OHLCV data and calculate indicators
def fetch_data_and_calculate_indicators(symbol, timeframe):
    try:
        # Fetch OHLCV data
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe)
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

        # Calculate RSI
        delta = df['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(RSI_PERIOD).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(RSI_PERIOD).mean()
        rs = gain / loss
        df['rsi'] = 100 - (100 / (1 + rs))

        return df
    except Exception as e:
        logging.error(f"Error fetching data or calculating indicators: {e}")
        return None

# Function to identify candlestick patterns
def identify_candlestick_patterns(df):
    try:
        # Example: Bullish engulfing pattern
        df['bullish_engulfing'] = (
            (df['close'] > df['open']) &  # Current candle is bullish
            (df['close'].shift(1) < df['open'].shift(1)) &  # Previous candle is bearish
            (df['close'] > df['open'].shift(1)) &  # Current close is higher than previous open
            (df['open'] < df['close'].shift(1))  # Current open is lower than previous close
        )
        return df
    except Exception as e:
        logging.error(f"Error identifying candlestick patterns: {e}")
        return None

# Function to execute trades
def execute_trade(signal, symbol, amount):
    try:
        if signal == 'buy':
            order = exchange.create_market_buy_order(symbol, amount)
            logging.info(f"Buy order executed: {order}")
        elif signal == 'sell':
            order = exchange.create_market_sell_order(symbol, amount)
            logging.info(f"Sell order executed: {order}")
    except Exception as e:
        logging.error(f"Error executing trade: {e}")

# Main trading logic
def trading_bot():
    while True:
        try:
            # Fetch data and calculate indicators
            df = fetch_data_and_calculate_indicators(SYMBOL, TIMEFRAME)
            if df is None:
                time.sleep(60)
                continue

            # Identify candlestick patterns
            df = identify_candlestick_patterns(df)
            if df is None:
                time.sleep(60)
                continue

            # Get the latest data
            latest = df.iloc[-1]

            # Trading strategy
            if latest['bullish_engulfing'] and latest['rsi'] < RSI_OVERSOLD:
                logging.info("Bullish signal detected. Executing buy trade.")
                execute_trade('buy', SYMBOL, TRADE_AMOUNT)
            elif latest['rsi'] > RSI_OVERBOUGHT:
                logging.info("Overbought RSI detected. Executing sell trade.")
                execute_trade('sell', SYMBOL, TRADE_AMOUNT)

            # Wait before the next iteration
            time.sleep(60)
        except Exception as e:
            logging.error(f"Error in trading bot loop: {e}")
            time.sleep(60)

# Entry point
if __name__ == '__main__':
    logging.info("Starting trading bot...")
    trading_bot()
```
