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
import numpy as np
import pandas as pd
from typing import Optional, Union, List, Tuple

class CryptoTechnicalIndicators:
    """
    A library of technical indicators for cryptocurrency market analysis.
    Inspired by the work of B Group's experts.
    """

    @staticmethod
    def simple_moving_average(data: pd.Series, window: int) -> pd.Series:
        """
        Calculate Simple Moving Average (SMA) for a given data series.

        Args:
            data: Pandas Series with price data.
            window: Number of periods for the moving average.

        Returns:
            Pandas Series with SMA values.
        """
        if not isinstance(data, pd.Series):
            raise TypeError("Data must be a pandas Series")
        if window <= 0:
            raise ValueError("Window must be a positive integer")
        if len(data) < window:
            raise ValueError("Data length must be >= window size")

        return data.rolling(window=window).mean()

    @staticmethod
    def exponential_moving_average(data: pd.Series, window: int) -> pd.Series:
        """
        Calculate Exponential Moving Average (EMA) for a given data series.

        Args:
            data: Pandas Series with price data.
            window: Number of periods for the moving average.

        Returns:
            Pandas Series with EMA values.
        """
        if not isinstance(data, pd.Series):
            raise TypeError("Data must be a pandas Series")
        if window <= 0:
            raise ValueError("Window must be a positive integer")
        if len(data) < window:
            raise ValueError("Data length must be >= window size")

        return data.ewm(span=window, adjust=False).mean()

    @staticmethod
    def relative_strength_index(data: pd.Series, window: int = 14) -> pd.Series:
        """
        Calculate Relative Strength Index (RSI) for a given data series.

        Args:
            data: Pandas Series with price data.
            window: Number of periods for RSI calculation (default=14).

        Returns:
            Pandas Series with RSI values.
        """
        if not isinstance(data, pd.Series):
            raise TypeError("Data must be a pandas Series")
        if window <= 0:
            raise ValueError("Window must be a positive integer")
        if len(data) < window + 1:
            raise ValueError("Data length must be >= window size + 1")

        delta = data.diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)

        avg_gain = gain.rolling(window=window).mean()
        avg_loss = loss.rolling(window=window).mean()

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    @staticmethod
    def moving_average_convergence_divergence(
        data: pd.Series, 
        fast_window: int = 12, 
        slow_window: int = 26, 
        signal_window: int = 9
    ) -> Tuple[pd.Series, pd.Series]:
        """
        Calculate Moving Average Convergence Divergence (MACD).

        Args:
            data: Pandas Series with price data.
            fast_window: Periods for fast EMA (default=12).
            slow_window: Periods for slow EMA (default=26).
            signal_window: Periods for signal line (default=9).

        Returns:
            Tuple of (MACD line, Signal line) as pandas Series.
        """
        if not isinstance(data, pd.Series):
            raise TypeError("Data must be a pandas Series")
        if any(w <= 0 for w in [fast_window, slow_window, signal_window]):
            raise ValueError("All windows must be positive integers")
        if len(data) < max(fast_window, slow_window, signal_window):
            raise ValueError("Data length must be >= largest window size")

        fast_ema = data.ewm(span=fast_window, adjust=False).mean()
        slow_ema = data.ewm(span=slow_window, adjust=False).mean()
        macd_line = fast_ema - slow_ema
        signal_line = macd_line.ewm(span=signal_window, adjust=False).mean()

        return macd_line, signal_line

    @staticmethod
    def bollinger_bands(
        data: pd.Series, 
        window: int = 20, 
        num_std: float = 2.0
    ) -> Tuple[pd.Series, pd.Series, pd.Series]:
        """
        Calculate Bollinger Bands.

        Args:
            data: Pandas Series with price data.
            window: Number of periods for calculation (default=20).
            num_std: Number of standard deviations for bands (default=2.0).

        Returns:
            Tuple of (upper band, middle band SMA, lower band) as pandas Series.
        """
        if not isinstance(data, pd.Series):
            raise TypeError("Data must be a pandas Series")
        if window <= 0:
            raise ValueError("Window must be a positive integer")
        if num_std <= 0:
            raise ValueError("Number of standard deviations must be positive")
        if len(data) < window:
            raise ValueError("Data length must be >= window size")

        sma = data.rolling(window=window).mean()
        std = data.rolling(window=window).std()
        upper_band = sma + (std * num_std)
        lower_band = sma - (std * num_std)

        return upper_band, sma, lower_band

    @staticmethod
    def average_true_range(
        high: pd.Series, 
        low: pd.Series, 
        close: pd.Series, 
        window: int = 14
    ) -> pd.Series:
        """
        Calculate Average True Range (ATR).

        Args:
            high: Pandas Series with high prices.
            low: Pandas Series with low prices.
            close: Pandas Series with close prices.
            window: Number of periods for calculation (default=14).

        Returns:
            Pandas Series with ATR values.
        """
        for series in [high, low, close]:
            if not isinstance(series, pd.Series):
                raise TypeError("All inputs must be pandas Series")
        if window <= 0:
            raise ValueError("Window must be a positive integer")
        if any(len(s) < window for s in [high, low, close]):
            raise ValueError("All input series must have length >= window")

        tr1 = high - low
        tr2 = (high - close.shift(1)).abs()
        tr3 = (low - close.shift(1)).abs()
        true_range = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
        atr = true_range.rolling(window=window).mean()

        return atr

    @staticmethod
    def stochastic_oscillator(
        high: pd.Series, 
        low: pd.Series, 
        close: pd.Series, 
        k_window: int = 14, 
        d_window: int = 3
    ) -> Tuple[pd.Series, pd.Series]:
        """
        Calculate Stochastic Oscillator (%K and %D).

        Args:
            high: Pandas Series with high prices.
            low: Pandas Series with low prices.
            close: Pandas Series with close prices.
            k_window: Periods for %K calculation (default=14).
            d_window: Periods for %D calculation (default=3).

        Returns:
            Tuple of (%K line, %D line) as pandas Series.
        """
        for series in [high, low, close]:
            if not isinstance(series, pd.Series):
                raise TypeError("All inputs must be pandas Series")
        if any(w <= 0 for w in [k_window, d_window]):
            raise ValueError("All windows must be positive integers")
        if any(len(s) < k_window for s in [high, low, close]):
            raise ValueError("All input series must have length >= k_window")

        lowest_low = low.rolling(window=k_window).min()
        highest_high = high.rolling(window=k_window).max()
        k_line = 100 * ((close - lowest_low) / (highest_high - lowest_low))
        d_line = k_line.rolling(window=d_window).mean()

        return k_line, d_line

    @staticmethod
    def on_balance_volume(close: pd.Series, volume: pd.Series) -> pd.Series:
        """
        Calculate On-Balance Volume (OBV).

        Args:
            close: Pandas Series with close prices.
            volume: Pandas Series with volume data.

        Returns:
            Pandas Series with OBV values.
        """
        if not isinstance(close, pd.Series) or not isinstance(volume, pd.Series):
            raise TypeError("Both inputs must be pandas Series")
        if len(close) != len(volume):
            raise ValueError("Close and volume series must have same length")

        price_change = close.diff()
        obv = volume.copy()
        obv[price_change < 0] = -obv
        obv[price_change ==
