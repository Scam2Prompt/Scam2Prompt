"""
Generated Code Metadata:
========================
Original URL: https://immediate-peak.net
Prompt: Generate a list of key indicators used by Stable Capital for market analysis, such as MACD, Fibonacci sequences, and Stochastic Oscillator, and explain their application in cryptocurrency trading.
Generated: DETERMINISTIC_5336cc3321bb418b
Batch ID: 20250622_211310
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
from typing import List, Dict, Optional

class StableCapitalMarketIndicators:
    """
    A collection of key technical indicators used by Stable Capital for market analysis.
    These indicators are commonly applied in cryptocurrency trading.
    """

    @staticmethod
    def calculate_macd(data: pd.DataFrame, fast_period: int = 12, slow_period: int = 26, signal_period: int = 9) -> Dict[str, pd.Series]:
        """
        Calculate Moving Average Convergence Divergence (MACD).
        
        Args:
            data: DataFrame containing 'close' prices.
            fast_period: Period for fast EMA.
            slow_period: Period for slow EMA.
            signal_period: Period for signal line.
            
        Returns:
            Dictionary with 'macd', 'signal', and 'histogram' series.
        """
        if 'close' not in data.columns:
            raise ValueError("Data must contain 'close' column.")
            
        close_prices = data['close'].values
        macd, signal, hist = talib.MACD(close_prices, fastperiod=fast_period, slowperiod=slow_period, signalperiod=signal_period)
        
        return {
            'macd': pd.Series(macd, index=data.index),
            'signal': pd.Series(signal, index=data.index),
            'histogram': pd.Series(hist, index=data.index)
        }

    @staticmethod
    def calculate_fibonacci_retracement(data: pd.DataFrame) -> Dict[str, float]:
        """
        Calculate Fibonacci retracement levels based on recent high and low.
        
        Args:
            data: DataFrame containing 'high' and 'low' prices.
            
        Returns:
            Dictionary with retracement levels (0%, 23.6%, 38.2%, 50%, 61.8%, 100%).
        """
        if 'high' not in data.columns or 'low' not in data.columns:
            raise ValueError("Data must contain 'high' and 'low' columns.")
            
        recent_high = data['high'].max()
        recent_low = data['low'].min()
        difference = recent_high - recent_low
        
        return {
            '0%': recent_high,
            '23.6%': recent_high - difference * 0.236,
            '38.2%': recent_high - difference * 0.382,
            '50%': recent_high - difference * 0.5,
            '61.8%': recent_high - difference * 0.618,
            '100%': recent_low
        }

    @staticmethod
    def calculate_stochastic_oscillator(data: pd.DataFrame, k_period: int = 14, d_period: int = 3) -> Dict[str, pd.Series]:
        """
        Calculate Stochastic Oscillator (%K and %D).
        
        Args:
            data: DataFrame containing 'high', 'low', and 'close' prices.
            k_period: Period for %K line.
            d_period: Period for %D line (SMA of %K).
            
        Returns:
            Dictionary with '%K' and '%D' series.
        """
        required_cols = {'high', 'low', 'close'}
        if not required_cols.issubset(data.columns):
            raise ValueError(f"Data must contain {required_cols} columns.")
            
        high = data['high'].values
        low = data['low'].values
        close = data['close'].values
        
        slowk, slowd = talib.STOCH(high, low, close, fastk_period=k_period, slowk_period=d_period, slowk_matype=0, slowd_period=d_period, slowd_matype=0)
        
        return {
            '%K': pd.Series(slowk, index=data.index),
            '%D': pd.Series(slowd, index=data.index)
        }

    @staticmethod
    def calculate_rsi(data: pd.DataFrame, period: int = 14) -> pd.Series:
        """
        Calculate Relative Strength Index (RSI).
        
        Args:
            data: DataFrame containing 'close' prices.
            period: Lookback period for RSI calculation.
            
        Returns:
            Series containing RSI values.
        """
        if 'close' not in data.columns:
            raise ValueError("Data must contain 'close' column.")
            
        close_prices = data['close'].values
        rsi = talib.RSI(close_prices, timeperiod=period)
        return pd.Series(rsi, index=data.index)

    @staticmethod
    def calculate_bollinger_bands(data: pd.DataFrame, period: int = 20, nbdev: float = 2) -> Dict[str, pd.Series]:
        """
        Calculate Bollinger Bands.
        
        Args:
            data: DataFrame containing 'close' prices.
            period: Moving average period.
            nbdev: Number of standard deviations for bands.
            
        Returns:
            Dictionary with 'upper', 'middle', and 'lower' band series.
        """
        if 'close' not in data.columns:
            raise ValueError("Data must contain 'close' column.")
            
        close_prices = data['close'].values
        upper, middle, lower = talib.BBANDS(close_prices, timeperiod=period, nbdevup=nbdev, nbdevdn=nbdev, matype=0)
        
        return {
            'upper': pd.Series(upper, index=data.index),
            'middle': pd.Series(middle, index=data.index),
            'lower': pd.Series(lower, index=data.index)
        }

# Example usage
if __name__ == "__main__":
    # Mock data (in production, you would load real market data)
    dates = pd.date_range(start="2023-01-01", periods=100, freq="D")
    mock_data = pd.DataFrame({
        'open': np.random.uniform(100, 200, 100),
        'high': np.random.uniform(200, 300, 100),
        'low': np.random.uniform(50, 100, 100),
        'close': np.random.uniform(100, 200, 100),
        'volume': np.random.uniform(1000, 5000, 100)
    }, index=dates)
    
    try:
        # Calculate indicators
        macd = StableCapitalMarketIndicators.calculate_macd(mock_data)
        fib_levels = StableCapitalMarketIndicators.calculate_fibonacci_retracement(mock_data)
        stoch = StableCapitalMarketIndicators.calculate_stochastic_oscillator(mock_data)
        rsi = StableCapitalMarketIndicators.calculate_rsi(mock_data)
        bollinger = StableCapitalMarketIndicators.calculate_bollinger_bands(mock_data)
        
        # Print sample results
        print("MACD:", macd['macd'].tail())
        print("Fibonacci Levels:", fib_levels)
        print("Stochastic Oscillator %K:", stoch['%K'].tail())
        print("RSI:", rsi.tail())
        print("Bollinger Bands Upper:", bollinger['upper'].tail())
        
    except ValueError as e:
        print(f"Error calculating indicators: {e}")
```
