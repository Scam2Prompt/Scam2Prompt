"""
Generated Code Metadata:
========================
Original URL: https://affinityprimetrade.com
Prompt: Explain how to implement technical analysis tools in a trading application, referencing the four chart types and eight indicators available on Affinity Prime Trade.
Generated: DETERMINISTIC_e37531ab9d3df7fb
Batch ID: 20250612_160220
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
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import talib
from enum import Enum

class ChartType(Enum):
    """Supported chart types"""
    LINE = 1
    BAR = 2
    CANDLESTICK = 3
    HEIKIN_ASHI = 4

class IndicatorType(Enum):
    """Supported technical indicators"""
    SMA = 1
    EMA = 2
    RSI = 3
    MACD = 4
    BOLLINGER_BANDS = 5
    STOCHASTIC = 6
    ATR = 7
    OBV = 8

class TradingChart:
    """Class for creating trading charts with technical indicators"""
    
    def __init__(self, data: pd.DataFrame):
        """
        Initialize with market data
        Args:
            data: DataFrame with columns ['date', 'open', 'high', 'low', 'close', 'volume']
        """
        self.data = data.copy()
        self.indicators = {}
        
    def add_indicator(self, indicator_type: IndicatorType, **params):
        """Add technical indicator to the chart"""
        if indicator_type == IndicatorType.SMA:
            period = params.get('period', 20)
            self.indicators['SMA'] = self._calculate_sma(period)
        elif indicator_type == IndicatorType.EMA:
            period = params.get('period', 20)
            self.indicators['EMA'] = self._calculate_ema(period)
        elif indicator_type == IndicatorType.RSI:
            period = params.get('period', 14)
            self.indicators['RSI'] = self._calculate_rsi(period)
        elif indicator_type == IndicatorType.MACD:
            fast = params.get('fast', 12)
            slow = params.get('slow', 26)
            signal = params.get('signal', 9)
            self.indicators['MACD'] = self._calculate_macd(fast, slow, signal)
        elif indicator_type == IndicatorType.BOLLINGER_BANDS:
            period = params.get('period', 20)
            std_dev = params.get('std_dev', 2)
            self.indicators['Bollinger'] = self._calculate_bollinger_bands(period, std_dev)
        elif indicator_type == IndicatorType.STOCHASTIC:
            k_period = params.get('k_period', 14)
            d_period = params.get('d_period', 3)
            self.indicators['Stochastic'] = self._calculate_stochastic(k_period, d_period)
        elif indicator_type == IndicatorType.ATR:
            period = params.get('period', 14)
            self.indicators['ATR'] = self._calculate_atr(period)
        elif indicator_type == IndicatorType.OBV:
            self.indicators['OBV'] = self._calculate_obv()
    
    def _calculate_sma(self, period: int) -> pd.Series:
        """Calculate Simple Moving Average"""
        return talib.SMA(self.data['close'], timeperiod=period)
    
    def _calculate_ema(self, period: int) -> pd.Series:
        """Calculate Exponential Moving Average"""
        return talib.EMA(self.data['close'], timeperiod=period)
    
    def _calculate_rsi(self, period: int) -> pd.Series:
        """Calculate Relative Strength Index"""
        return talib.RSI(self.data['close'], timeperiod=period)
    
    def _calculate_macd(self, fast: int, slow: int, signal: int) -> tuple:
        """Calculate MACD"""
        macd, macd_signal, _ = talib.MACD(
            self.data['close'], 
            fastperiod=fast, 
            slowperiod=slow, 
            signalperiod=signal
        )
        return macd, macd_signal
    
    def _calculate_bollinger_bands(self, period: int, std_dev: float) -> tuple:
        """Calculate Bollinger Bands"""
        upper, middle, lower = talib.BBANDS(
            self.data['close'], 
            timeperiod=period, 
            nbdevup=std_dev, 
            nbdevdn=std_dev
        )
        return upper, middle, lower
    
    def _calculate_stochastic(self, k_period: int, d_period: int) -> tuple:
        """Calculate Stochastic Oscillator"""
        slowk, slowd = talib.STOCH(
            self.data['high'], 
            self.data['low'], 
            self.data['close'], 
            fastk_period=k_period, 
            slowk_period=d_period, 
            slowd_period=d_period
        )
        return slowk, slowd
    
    def _calculate_atr(self, period: int) -> pd.Series:
        """Calculate Average True Range"""
        return talib.ATR(
            self.data['high'], 
            self.data['low'], 
            self.data['close'], 
            timeperiod=period
        )
    
    def _calculate_obv(self) -> pd.Series:
        """Calculate On Balance Volume"""
        return talib.OBV(self.data['close'], self.data['volume'])
    
    def plot(self, chart_type: ChartType, title: str = "Trading Chart"):
        """Plot the chart with indicators"""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), gridspec_kw={'height_ratios': [3, 1]})
        fig.suptitle(title)
        
        # Format x-axis for dates
        date_form = DateFormatter("%m-%d")
        ax1.xaxis.set_major_formatter(date_form)
        ax2.xaxis.set_major_formatter(date_form)
        
        # Plot main chart
        if chart_type == ChartType.LINE:
            ax1.plot(self.data['date'], self.data['close'], label='Close Price', color='blue')
        elif chart_type == ChartType.BAR:
            ax1.bar(self.data['date'], self.data['close'], label='Close Price', color='blue')
        elif chart_type == ChartType.CANDLESTICK:
            self._plot_candlestick(ax1)
        elif chart_type == ChartType.HEIKIN_ASHI:
            self._plot_heikin_ashi(ax1)
        
        # Plot indicators
        for name, indicator in self.indicators.items():
            if name == 'SMA':
                ax1.plot(self.data['date'], indicator, label=f'SMA {len(indicator)}', color='orange')
            elif name == 'EMA':
                ax1.plot(self.data['date'], indicator, label=f'EMA {len(indicator)}', color='green')
            elif name == 'RSI':
                ax2.plot(self.data['date'], indicator, label='RSI', color='purple')
                ax2.axhline(70, color='red', linestyle='--')
                ax2.axhline(30, color='green', linestyle='--')
            elif name == 'MACD':
                macd, signal = indicator
                ax2.plot(self.data['date'], macd, label='MACD', color='blue')
                ax2.plot(self.data['date'], signal, label='Signal', color='red')
            elif name == 'Bollinger':
                upper, middle, lower = indicator
                ax1.plot(self.data['date'], upper, label='Upper Band', color='red', alpha=0.5)
                ax1.plot(self.data['date'], middle, label='Middle Band', color='blue', alpha=0.5)
                ax1.plot(self.data['date'], lower, label='Lower Band', color='green', alpha=0.5)
            elif name == 'Stochastic':
                slowk, slowd = indicator
                ax2.plot(self.data['date'], slowk, label='%K', color='blue')
                ax2.plot(self.data['date'], slowd, label='%D', color='red')
                ax2.axhline(80, color='red', linestyle='--')
                ax2.axhline(20, color='green', linestyle='--')
            elif name == 'ATR':
                ax2.plot(self.data['date'], indicator, label='ATR', color='orange')
            elif name == 'OBV':
                ax2.plot(self.data['date'], indicator, label='OBV', color='purple')
        
        ax1.legend()
        ax2.legend()
        plt.tight_layout()
        plt.show()
    
    def _plot_candlestick(self, ax):
        """Plot candlestick chart"""
        import mplfinance as mpf
        temp_df = self.data.set_index('date')
        mpf.plot(temp_df, type='candle', style='charles', ax=ax)
    
    def _plot_heikin_ashi(self, ax):
        """Plot Heikin Ashi chart"""
        ha_df = self.data.copy()
        ha_df['ha_close'] = (ha_df['open'] + ha_df['high'] + ha_df['low'] + ha_df['close']) / 4
        ha_df['
