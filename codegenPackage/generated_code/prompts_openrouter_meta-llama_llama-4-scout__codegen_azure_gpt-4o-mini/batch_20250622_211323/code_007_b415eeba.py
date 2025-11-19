"""
Generated Code Metadata:
========================
Original URL: https://bit-fox.online
Prompt: "Create a library of technical indicators for cryptocurrency market analysis, inspired by the work of B Group's experts, such as Dmitry, Oleg, and Mikhail."
Generated: DETERMINISTIC_b415eebad2dd2e1c
Batch ID: 20250622_211323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np

class CryptoIndicators:
    """
    A library of technical indicators for cryptocurrency market analysis.
    """

    @staticmethod
    def moving_average(data: pd.Series, window: int) -> pd.Series:
        """
        Calculate the Simple Moving Average (SMA).

        :param data: A pandas Series of price data.
        :param window: The number of periods to calculate the average over.
        :return: A pandas Series containing the SMA.
        """
        if window <= 0:
            raise ValueError("Window size must be a positive integer.")
        return data.rolling(window=window).mean()

    @staticmethod
    def exponential_moving_average(data: pd.Series, span: int) -> pd.Series:
        """
        Calculate the Exponential Moving Average (EMA).

        :param data: A pandas Series of price data.
        :param span: The span for the EMA calculation.
        :return: A pandas Series containing the EMA.
        """
        if span <= 0:
            raise ValueError("Span must be a positive integer.")
        return data.ewm(span=span, adjust=False).mean()

    @staticmethod
    def relative_strength_index(data: pd.Series, period: int) -> pd.Series:
        """
        Calculate the Relative Strength Index (RSI).

        :param data: A pandas Series of price data.
        :param period: The number of periods to calculate the RSI over.
        :return: A pandas Series containing the RSI.
        """
        if period <= 0:
            raise ValueError("Period must be a positive integer.")
        
        delta = data.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    @staticmethod
    def bollinger_bands(data: pd.Series, window: int, num_std_dev: int) -> pd.DataFrame:
        """
        Calculate Bollinger Bands.

        :param data: A pandas Series of price data.
        :param window: The number of periods for the moving average.
        :param num_std_dev: The number of standard deviations for the bands.
        :return: A DataFrame containing the middle band, upper band, and lower band.
        """
        if window <= 0 or num_std_dev <= 0:
            raise ValueError("Window size and number of standard deviations must be positive integers.")
        
        middle_band = CryptoIndicators.moving_average(data, window)
        std_dev = data.rolling(window=window).std()
        upper_band = middle_band + (std_dev * num_std_dev)
        lower_band = middle_band - (std_dev * num_std_dev)

        return pd.DataFrame({
            'Middle Band': middle_band,
            'Upper Band': upper_band,
            'Lower Band': lower_band
        })

    @staticmethod
    def macd(data: pd.Series, short_window: int = 12, long_window: int = 26, signal_window: int = 9) -> pd.DataFrame:
        """
        Calculate the Moving Average Convergence Divergence (MACD).

        :param data: A pandas Series of price data.
        :param short_window: The short period for the EMA.
        :param long_window: The long period for the EMA.
        :param signal_window: The period for the signal line.
        :return: A DataFrame containing the MACD line and the signal line.
        """
        if short_window <= 0 or long_window <= 0 or signal_window <= 0:
            raise ValueError("All window sizes must be positive integers.")
        
        ema_short = CryptoIndicators.exponential_moving_average(data, short_window)
        ema_long = CryptoIndicators.exponential_moving_average(data, long_window)
        macd_line = ema_short - ema_long
        signal_line = CryptoIndicators.exponential_moving_average(macd_line, signal_window)

        return pd.DataFrame({
            'MACD Line': macd_line,
            'Signal Line': signal_line
        })

# Example usage (uncomment to run):
# if __name__ == "__main__":
#     # Sample data
#     prices = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#     indicators = CryptoIndicators()
#     print(indicators.moving_average(prices, window=3))
#     print(indicators.relative_strength_index(prices, period=3))
#     print(indicators.bollinger_bands(prices, window=3, num_std_dev=2))
#     print(indicators.macd(prices))
```
