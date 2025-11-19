"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptojustin.com
Prompt: Explain how to implement a trading strategy using candlestick patterns as discussed in the Crypto Justin guide on reading charts.
Generated: DETERMINISTIC_9611feee917dcb56
Batch ID: 20250612_155557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np

class CandlestickStrategy:
    """
    Class to implement a trading strategy based on candlestick patterns.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initialize the strategy with market data.

        :param data: A Pandas DataFrame containing OHLC (Open, High, Low, Close) data.
        """
        self.data = data
        self.validate_data()

    def validate_data(self):
        """
        Validates the input data to ensure it contains required columns.
        """
        required_columns = {'Open', 'High', 'Low', 'Close'}
        if not required_columns.issubset(self.data.columns):
            raise ValueError(f"Data must contain the following columns: {required_columns}")

    @staticmethod
    def is_bullish_engulfing(prev_row: pd.Series, current_row: pd.Series) -> bool:
        """
        Identify a Bullish Engulfing candlestick pattern.

        :param prev_row: Previous row of OHLC data as a Pandas Series.
        :param current_row: Current row of OHLC data as a Pandas Series.
        :return: True if the pattern is detected, False otherwise.
        """
        # Bullish Engulfing logic: Previous candle is bearish, current candle engulfs and is bullish
        return (
            prev_row['Open'] > prev_row['Close'] and  # Previous candle is bearish
            current_row['Open'] < prev_row['Close'] and  # Current candle opens lower than prev close
            current_row['Close'] > prev_row['Open']  # Current candle closes higher than prev open
        )

    @staticmethod
    def is_bearish_engulfing(prev_row: pd.Series, current_row: pd.Series) -> bool:
        """
        Identify a Bearish Engulfing candlestick pattern.

        :param prev_row: Previous row of OHLC data as a Pandas Series.
        :param current_row: Current row of OHLC data as a Pandas Series.
        :return: True if the pattern is detected, False otherwise.
        """
        # Bearish Engulfing logic: Previous candle is bullish, current candle engulfs and is bearish
        return (
            prev_row['Open'] < prev_row['Close'] and  # Previous candle is bullish
            current_row['Open'] > prev_row['Close'] and  # Current candle opens higher than prev close
            current_row['Close'] < prev_row['Open']  # Current candle closes lower than prev open
        )

    def generate_signals(self) -> pd.DataFrame:
        """
        Generate buy and sell signals based on candlestick patterns.

        :return: A Pandas DataFrame with signals for buy ('BUY') or sell ('SELL').
        """
        signals = []
        
        # Iterate through data to identify patterns
        for i in range(1, len(self.data)):
            prev_row = self.data.iloc[i - 1]
            current_row = self.data.iloc[i]
            
            if self.is_bullish_engulfing(prev_row, current_row):
                signals.append('BUY')
            elif self.is_bearish_engulfing(prev_row, current_row):
                signals.append('SELL')
            else:
                signals.append('HOLD')

        # Add 'HOLD' for the first row (no previous row to compare)
        signals.insert(0, 'HOLD')

        # Add signals column to the data
        self.data['Signal'] = signals
        return self.data

def main():
    """
    Main function to test the candlestick strategy implementation.
    """
    try:
        # Example OHLC data
        data = pd.DataFrame({
            'Open': [100, 98, 101, 97, 99],
            'High': [102, 101, 103, 100, 101],
            'Low': [97, 96, 99, 95, 97],
            'Close': [98, 101, 97, 99, 100]
        })

        # Instantiate the strategy
        strategy = CandlestickStrategy(data)

        # Generate signals
        result = strategy.generate_signals()

        # Print the resulting DataFrame with signals
        print(result)

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
