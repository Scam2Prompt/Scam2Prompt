"""
Generated Code Metadata:
========================
Original URL: https://imperial-holding.com.co
Prompt: Create a program to visualize trading data using the timeframe options, technical indicators, and analytical objects available on the Imperial Capital platform.
Generated: DETERMINISTIC_dde08c943ee2d0eb
Batch ID: 20250612_154954
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
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc
from datetime import datetime
import yfinance as yf
import json
import os
from enum import Enum
from typing import Optional, List, Dict, Any

# Constants
CONFIG_FILE = 'config.json'
DEFAULT_TICKER = 'AAPL'
DEFAULT_PERIOD = '1mo'
DEFAULT_INTERVAL = '1d'

class TimeFrame(Enum):
    """Available timeframes for data visualization"""
    MINUTE_1 = '1m'
    MINUTE_5 = '5m'
    MINUTE_15 = '15m'
    MINUTE_30 = '30m'
    HOUR_1 = '1h'
    DAY_1 = '1d'
    WEEK_1 = '1wk'
    MONTH_1 = '1mo'

class IndicatorType(Enum):
    """Supported technical indicators"""
    SMA = 'SMA'
    EMA = 'EMA'
    RSI = 'RSI'
    MACD = 'MACD'
    BOLLINGER = 'Bollinger'

class DrawingObject(Enum):
    """Supported analytical drawing objects"""
    TRENDLINE = 'trendline'
    HORIZONTAL_LINE = 'horizontal'
    VERTICAL_LINE = 'vertical'
    RECTANGLE = 'rectangle'
    FIBONACCI = 'fibonacci'

class TradingVisualizer:
    def __init__(self):
        """Initialize the trading visualizer with default settings"""
        self.config = self._load_config()
        self.data = None
        self.indicators = []
        self.drawing_objects = []
        
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file or create default if not exists"""
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        else:
            return {
                'ticker': DEFAULT_TICKER,
                'period': DEFAULT_PERIOD,
                'interval': DEFAULT_INTERVAL,
                'theme': 'dark'
            }
    
    def _save_config(self) -> None:
        """Save current configuration to file"""
        with open(CONFIG_FILE, 'w') as f:
            json.dump(self.config, f, indent=4)
    
    def fetch_data(self, ticker: str, period: str, interval: str) -> None:
        """
        Fetch trading data from Yahoo Finance API
        Args:
            ticker: Stock symbol
            period: Time period (1d, 5d, 1mo, 3mo, etc.)
            interval: Data interval (1m, 5m, 15m, 1h, 1d, etc.)
        """
        try:
            self.data = yf.download(
                tickers=ticker,
                period=period,
                interval=interval,
                progress=False
            )
            self.config['ticker'] = ticker
            self.config['period'] = period
            self.config['interval'] = interval
            self._save_config()
        except Exception as e:
            raise ValueError(f"Failed to fetch data: {str(e)}")
    
    def add_indicator(self, indicator_type: IndicatorType, **params) -> None:
        """
        Add technical indicator to the visualization
        Args:
            indicator_type: Type of indicator to add
            params: Indicator-specific parameters
        """
        indicator = {
            'type': indicator_type,
            'params': params
        }
        self.indicators.append(indicator)
    
    def add_drawing_object(self, object_type: DrawingObject, **params) -> None:
        """
        Add analytical drawing object to the visualization
        Args:
            object_type: Type of drawing object to add
            params: Object-specific parameters
        """
        drawing_object = {
            'type': object_type,
            'params': params
        }
        self.drawing_objects.append(drawing_object)
    
    def _calculate_sma(self, window: int = 20) -> pd.Series:
        """Calculate Simple Moving Average"""
        return self.data['Close'].rolling(window=window).mean()
    
    def _calculate_ema(self, window: int = 20) -> pd.Series:
        """Calculate Exponential Moving Average"""
        return self.data['Close'].ewm(span=window, adjust=False).mean()
    
    def _calculate_rsi(self, window: int = 14) -> pd.Series:
        """Calculate Relative Strength Index"""
        delta = self.data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))
    
    def _calculate_macd(self, fast: int = 12, slow: int = 26, signal: int = 9) -> Dict[str, pd.Series]:
        """Calculate MACD indicator"""
        ema_fast = self.data['Close'].ewm(span=fast, adjust=False).mean()
        ema_slow = self.data['Close'].ewm(span=slow, adjust=False).mean()
        macd_line = ema_fast - ema_slow
        signal_line = macd_line.ewm(span=signal, adjust=False).mean()
        histogram = macd_line - signal_line
        return {
            'macd': macd_line,
            'signal': signal_line,
            'histogram': histogram
        }
    
    def _calculate_bollinger(self, window: int = 20, std_dev: int = 2) -> Dict[str, pd.Series]:
        """Calculate Bollinger Bands"""
        sma = self._calculate_sma(window)
        rolling_std = self.data['Close'].rolling(window=window).std()
        upper = sma + (rolling_std * std_dev)
        lower = sma - (rolling_std * std_dev)
        return {
            'sma': sma,
            'upper': upper,
            'lower': lower
        }
    
    def _apply_indicators(self, ax: plt.Axes) -> None:
        """Apply all configured indicators to the plot"""
        for indicator in self.indicators:
            if indicator['type'] == IndicatorType.SMA:
                sma = self._calculate_sma(**indicator['params'])
                ax.plot(sma.index, sma, label=f"SMA {indicator['params'].get('window', 20)}")
            
            elif indicator['type'] == IndicatorType.EMA:
                ema = self._calculate_ema(**indicator['params'])
                ax.plot(ema.index, ema, label=f"EMA {indicator['params'].get('window', 20)}")
            
            elif indicator['type'] == IndicatorType.RSI:
                rsi = self._calculate_rsi(**indicator['params'])
                ax.plot(rsi.index, rsi, label=f"RSI {indicator['params'].get('window', 14)}")
            
            elif indicator['type'] == IndicatorType.MACD:
                macd_data = self._calculate_macd(**indicator['params'])
                ax.plot(macd_data['macd'].index, macd_data['macd'], label='MACD')
                ax.plot(macd_data['signal'].index, macd_data['signal'], label='Signal')
                ax.bar(macd_data['histogram'].index, macd_data['histogram'], label='Histogram')
            
            elif indicator['type'] == IndicatorType.BOLLINGER:
                bb_data = self._calculate_bollinger(**indicator['params'])
                ax.plot(bb_data['sma'].index, bb_data['sma'], label='Bollinger SMA')
                ax.plot(bb_data['upper'].index, bb_data['upper'], label='Upper Band')
                ax.plot(bb_data['lower'].index, bb_data['lower'], label='Lower Band')
    
    def _apply_drawing_objects(self, ax: plt.Axes) -> None:
        """Apply all configured drawing objects to the plot"""
        for obj in self.drawing_objects:
            if obj['type'] == DrawingObject.TRENDLINE:
                x = [obj['params']['x1'], obj['params']['x2']]
                y = [obj['params']['y1'], obj['params']['y2']]
                ax.plot(x, y, color='blue', linestyle='--', alpha=0.7)
            
            elif obj['type'] == DrawingObject.HORIZONTAL_LINE:
                y = obj['params']['y']
                ax.axhline(y=y, color='red', linestyle='-', alpha=0.5)
            
            elif obj['type'] == DrawingObject.VERTICAL_LINE:
                x = obj['params']['x']
                ax.axvline(x=x, color='green', linestyle='-', alpha=0.5)
            
            elif obj['type'] == DrawingObject.RECTANGLE:
                from matplotlib.patches import Rectangle
