"""
Generated Code Metadata:
========================
Original URL: https://www.lbank.site
Prompt: Suggest a set of technical indicators that can be used with LBank's futures trading platform to predict price movements and make informed trading decisions.
Generated: DETERMINISTIC_8aa83fe8089cd0e9
Batch ID: 20250622_205634
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
import talib
from typing import Dict, List, Optional

class TechnicalIndicators:
    """
    A collection of technical indicators commonly used in futures trading analysis.
    """
    
    def __init__(self, ohlcv_data: pd.DataFrame):
        """
        Initialize with OHLCV data.
        
        Args:
            ohlcv_data: DataFrame with columns ['open', 'high', 'low', 'close', 'volume']
        """
        self.data = ohlcv_data.copy()
        
    def calculate_sma(self, window: int = 20) -> pd.Series:
        """
        Calculate Simple Moving Average (SMA).
        
        Args:
            window: The lookback period
            
        Returns:
            Series containing SMA values
        """
        return self.data['close'].rolling(window=window).mean()
    
    def calculate_ema(self, window: int = 20) -> pd.Series:
        """
        Calculate Exponential Moving Average (EMA).
        
        Args:
            window: The lookback period
            
        Returns:
            Series containing EMA values
        """
        return self.data['close'].ewm(span=window, adjust=False).mean()
    
    def calculate_rsi(self, window: int = 14) -> pd.Series:
        """
        Calculate Relative Strength Index (RSI).
        
        Args:
            window: The lookback period
            
        Returns:
            Series containing RSI values
        """
        delta = self.data['close'].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        
        avg_gain = gain.rolling(window=window).mean()
        avg_loss = loss.rolling(window=window).mean()
        
        rs = avg_gain / avg_loss
        return 100 - (100 / (1 + rs))
    
    def calculate_macd(self, fast_window: int = 12, slow_window: int = 26, signal_window: int = 9) -> Dict[str, pd.Series]:
        """
        Calculate Moving Average Convergence Divergence (MACD).
        
        Args:
            fast_window: The fast EMA period
            slow_window: The slow EMA period
            signal_window: The signal line period
            
        Returns:
            Dictionary containing MACD line and signal line
        """
        fast_ema = self.data['close'].ewm(span=fast_window, adjust=False).mean()
        slow_ema = self.data['close'].ewm(span=slow_window, adjust=False).mean()
        macd_line = fast_ema - slow_ema
        signal_line = macd_line.ewm(span=signal_window, adjust=False).mean()
        
        return {
            'macd': macd_line,
            'signal': signal_line
        }
    
    def calculate_bollinger_bands(self, window: int = 20, num_std: int = 2) -> Dict[str, pd.Series]:
        """
        Calculate Bollinger Bands.
        
        Args:
            window: The lookback period
            num_std: Number of standard deviations
            
        Returns:
            Dictionary containing upper, middle, and lower bands
        """
        sma = self.calculate_sma(window)
        rolling_std = self.data['close'].rolling(window=window).std()
        
        upper_band = sma + (rolling_std * num_std)
        lower_band = sma - (rolling_std * num_std)
        
        return {
            'upper': upper_band,
            'middle': sma,
            'lower': lower_band
        }
    
    def calculate_stochastic_oscillator(self, k_window: int = 14, d_window: int = 3) -> Dict[str, pd.Series]:
        """
        Calculate Stochastic Oscillator.
        
        Args:
            k_window: The lookback period for %K
            d_window: The smoothing period for %D
            
        Returns:
            Dictionary containing %K and %D lines
        """
        low_min = self.data['low'].rolling(window=k_window).min()
        high_max = self.data['high'].rolling(window=k_window).max()
        
        k_line = 100 * ((self.data['close'] - low_min) / (high_max - low_min))
        d_line = k_line.rolling(window=d_window).mean()
        
        return {
            'k': k_line,
            'd': d_line
        }
    
    def calculate_atr(self, window: int = 14) -> pd.Series:
        """
        Calculate Average True Range (ATR).
        
        Args:
            window: The lookback period
            
        Returns:
            Series containing ATR values
        """
        high = self.data['high']
        low = self.data['low']
        close = self.data['close']
        
        tr1 = high - low
        tr2 = abs(high - close.shift())
        tr3 = abs(low - close.shift())
        true_range = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
        
        return true_range.rolling(window=window).mean()
    
    def calculate_obv(self) -> pd.Series:
        """
        Calculate On-Balance Volume (OBV).
        
        Returns:
            Series containing OBV values
        """
        close = self.data['close']
        volume = self.data['volume']
        obv = (volume * np.where(close > close.shift(1), 1, np.where(close < close.shift(1), -1, 0))).cumsum()
        return obv
    
    def calculate_all_indicators(self) -> Dict[str, pd.Series]:
        """
        Calculate all available indicators.
        
        Returns:
            Dictionary containing all indicator values
        """
        indicators = {
            'sma_20': self.calculate_sma(20),
            'ema_20': self.calculate_ema(20),
            'rsi_14': self.calculate_rsi(14),
            'macd': self.calculate_macd(),
            'bollinger': self.calculate_bollinger_bands(),
            'stochastic': self.calculate_stochastic_oscillator(),
            'atr_14': self.calculate_atr(14),
            'obv': self.calculate_obv()
        }
        return indicators

def validate_ohlcv_data(data: pd.DataFrame) -> bool:
    """
    Validate that the input DataFrame contains required OHLCV columns.
    
    Args:
        data: DataFrame to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    required_columns = {'open', 'high', 'low', 'close', 'volume'}
    return required_columns.issubset(data.columns)
```
