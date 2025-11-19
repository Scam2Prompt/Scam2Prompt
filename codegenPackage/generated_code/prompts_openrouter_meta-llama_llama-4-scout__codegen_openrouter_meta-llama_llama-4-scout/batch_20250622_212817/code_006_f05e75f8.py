"""
Generated Code Metadata:
========================
Original URL: https://pc.bigwhales.com
Prompt: Design a simple trading strategy using Bigwhales' platform for Forex and stocks, and provide a basic implementation in Python.
Generated: DETERMINISTIC_f05e75f80f52cf25
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import logging
from bigwhales import BigWhales
import pandas as pd
import numpy as np
from typing import Dict

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TradingStrategy:
    def __init__(self, api_key: str, api_secret: str):
        """
        Initialize the trading strategy with BigWhales API credentials.

        Args:
        - api_key (str): BigWhales API key
        - api_secret (str): BigWhales API secret
        """
        self.bigwhales = BigWhales(api_key, api_secret)

    def get_historical_data(self, symbol: str, timeframe: str, limit: int) -> pd.DataFrame:
        """
        Retrieve historical data for a given symbol and timeframe.

        Args:
        - symbol (str): Symbol to retrieve data for (e.g. EURUSD, AAPL)
        - timeframe (str): Timeframe to retrieve data for (e.g. 1m, 1h, 1d)
        - limit (int): Number of data points to retrieve

        Returns:
        - pd.DataFrame: Historical data for the given symbol and timeframe
        """
        try:
            data = self.bigwhales.get_historical_data(symbol, timeframe, limit)
            return pd.DataFrame(data)
        except Exception as e:
            logger.error(f"Failed to retrieve historical data: {e}")
            return pd.DataFrame()

    def calculate_moving_averages(self, data: pd.DataFrame, short_window: int, long_window: int) -> Dict[str, pd.Series]:
        """
        Calculate short and long moving averages for the given data.

        Args:
        - data (pd.DataFrame): Data to calculate moving averages for
        - short_window (int): Short moving average window
        - long_window (int): Long moving average window

        Returns:
        - Dict[str, pd.Series]: Dictionary containing short and long moving averages
        """
        short_ma = data['close'].rolling(window=short_window).mean()
        long_ma = data['close'].rolling(window=long_window).mean()
        return {'short_ma': short_ma, 'long_ma': long_ma}

    def generate_signals(self, data: pd.DataFrame, short_window: int, long_window: int) -> pd.Series:
        """
        Generate buy and sell signals based on moving averages.

        Args:
        - data (pd.DataFrame): Data to generate signals for
        - short_window (int): Short moving average window
        - long_window (int): Long moving average window

        Returns:
        - pd.Series: Series containing buy and sell signals
        """
        mas = self.calculate_moving_averages(data, short_window, long_window)
        signals = pd.Series(index=data.index)
        signals[(mas['short_ma'] > mas['long_ma']) & (mas['short_ma'].shift(1) <= mas['long_ma'].shift(1))] = 1  # Buy signal
        signals[(mas['short_ma'] < mas['long_ma']) & (mas['short_ma'].shift(1) >= mas['long_ma'].shift(1))] = -1  # Sell signal
        return signals

    def execute_trade(self, symbol: str, signal: int, amount: float):
        """
        Execute a trade based on the given signal.

        Args:
        - symbol (str): Symbol to trade
        - signal (int): Signal to trade on (1 for buy, -1 for sell)
        - amount (float): Amount to trade
        """
        try:
            if signal == 1:
                self.bigwhales.place_order(symbol, 'buy', amount)
                logger.info(f"Bought {symbol} for {amount}")
            elif signal == -1:
                self.bigwhales.place_order(symbol, 'sell', amount)
                logger.info(f"Sold {symbol} for {amount}")
        except Exception as e:
            logger.error(f"Failed to execute trade: {e}")

def main():
    api_key = os.environ['BIGWHALES_API_KEY']
    api_secret = os.environ['BIGWHALES_API_SECRET']

    strategy = TradingStrategy(api_key, api_secret)

    symbol = 'EURUSD'
    timeframe = '1h'
    limit = 100
    short_window = 20
    long_window = 50
    amount = 1000.0

    data = strategy.get_historical_data(symbol, timeframe, limit)
    signals = strategy.generate_signals(data, short_window, long_window)

    for i, signal in enumerate(signals):
        if signal != 0:
            strategy.execute_trade(symbol, signal, amount)

if __name__ == '__main__':
    main()
```
