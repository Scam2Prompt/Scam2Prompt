"""
Generated Code Metadata:
========================
Original URL: https://cryptojustin.com
Prompt: Write Python code to analyze Bitcoin trading signals using historical price data and candlestick patterns, incorporating insights from Crypto Justin's article on candlestick analysis.
Generated: DETERMINISTIC_986cc901e601b1dc
Batch ID: 20250612_153512
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
import yfinance as yf
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple
import matplotlib.pyplot as plt
import mplfinance as mpf

class BitcoinTradingAnalyzer:
    """
    Analyzes Bitcoin trading signals using historical price data and candlestick patterns.
    Incorporates insights from Crypto Justin's candlestick analysis.
    """
    
    def __init__(self, lookback_days: int = 365):
        """
        Initialize the analyzer with default lookback period.
        
        Args:
            lookback_days: Number of days of historical data to fetch (default: 365)
        """
        self.lookback_days = lookback_days
        self.btc_data = None
        self.signals = []
        
    def fetch_data(self) -> pd.DataFrame:
        """
        Fetch Bitcoin historical price data from Yahoo Finance.
        
        Returns:
            DataFrame containing OHLCV data with datetime index
            
        Raises:
            ConnectionError: If data cannot be fetched
        """
        try:
            end_date = datetime.now()
            start_date = end_date - timedelta(days=self.lookback_days)
            
            data = yf.download(
                'BTC-USD',
                start=start_date.strftime('%Y-%m-%d'),
                end=end_date.strftime('%Y-%m-%d'),
                progress=False
            )
            
            if data.empty:
                raise ValueError("No data returned from Yahoo Finance")
                
            self.btc_data = data
            return data
            
        except Exception as e:
            raise ConnectionError(f"Failed to fetch data: {str(e)}")
    
    def _calculate_body_size(self, row: pd.Series) -> float:
        """Calculate the absolute size of the candle body."""
        return abs(row['Close'] - row['Open'])
    
    def _calculate_wick_size(self, row: pd.Series) -> Tuple[float, float]:
        """Calculate upper and lower wick sizes."""
        upper_wick = row['High'] - max(row['Open'], row['Close'])
        lower_wick = min(row['Open'], row['Close']) - row['Low']
        return upper_wick, lower_wick
    
    def _is_bullish(self, row: pd.Series) -> bool:
        """Determine if candle is bullish (close > open)."""
        return row['Close'] > row['Open']
    
    def _is_bearish(self, row: pd.Series) -> bool:
        """Determine if candle is bearish (close < open)."""
        return row['Close'] < row['Open']
    
    def _is_doji(self, row: pd.Series, threshold: float = 0.1) -> bool:
        """
        Identify Doji candle pattern.
        
        Args:
            row: Candle data
            threshold: Max body size as percentage of total range (default: 10%)
            
        Returns:
            bool: True if Doji pattern detected
        """
        total_range = row['High'] - row['Low']
        if total_range == 0:
            return False
        body_size = self._calculate_body_size(row)
        return (body_size / total_range) < threshold
    
    def _is_hammer(self, row: pd.Series, threshold: float = 0.7) -> bool:
        """
        Identify Hammer or Hanging Man pattern.
        
        Args:
            row: Candle data
            threshold: Min lower wick as percentage of total range (default: 70%)
            
        Returns:
            bool: True if Hammer pattern detected
        """
        total_range = row['High'] - row['Low']
        if total_range == 0:
            return False
            
        upper_wick, lower_wick = self._calculate_wick_size(row)
        return (
            (lower_wick / total_range) >= threshold and
            (upper_wick / total_range) <= (1 - threshold) and
            self._is_bullish(row)
        )
    
    def _is_shooting_star(self, row: pd.Series, threshold: float = 0.7) -> bool:
        """
        Identify Shooting Star pattern.
        
        Args:
            row: Candle data
            threshold: Min upper wick as percentage of total range (default: 70%)
            
        Returns:
            bool: True if Shooting Star pattern detected
        """
        total_range = row['High'] - row['Low']
        if total_range == 0:
            return False
            
        upper_wick, lower_wick = self._calculate_wick_size(row)
        return (
            (upper_wick / total_range) >= threshold and
            (lower_wick / total_range) <= (1 - threshold) and
            self._is_bearish(row)
        )
    
    def _is_engulfing(self, prev_row: pd.Series, curr_row: pd.Series) -> bool:
        """
        Identify Bullish/Bearish Engulfing pattern.
        
        Args:
            prev_row: Previous candle data
            curr_row: Current candle data
            
        Returns:
            bool: True if Engulfing pattern detected
        """
        if self._is_bullish(prev_row) and self._is_bearish(curr_row):
            return (curr_row['Open'] > prev_row['Close'] and 
                    curr_row['Close'] < prev_row['Open'])
        elif self._is_bearish(prev_row) and self._is_bullish(curr_row):
            return (curr_row['Open'] < prev_row['Close'] and 
                    curr_row['Close'] > prev_row['Open'])
        return False
    
    def analyze_candles(self) -> List[Dict]:
        """
        Analyze candlestick patterns in the historical data.
        
        Returns:
            List of dictionaries containing detected patterns and their metadata
        """
        if self.btc_data is None:
            raise ValueError("No data available. Call fetch_data() first.")
            
        signals = []
        data = self.btc_data.copy()
        
        # Calculate necessary metrics
        data['Body_Size'] = data.apply(self._calculate_body_size, axis=1)
        data['Upper_Wick'], data['Lower_Wick'] = zip(*data.apply(self._calculate_wick_size, axis=1))
        data['Is_Bullish'] = data.apply(self._is_bullish, axis=1)
        data['Is_Bearish'] = data.apply(self._is_bearish, axis=1)
        
        for i in range(1, len(data)):
            prev_row = data.iloc[i-1]
            curr_row = data.iloc[i]
            
            signal = {
                'date': curr_row.name,
                'patterns': [],
                'price': curr_row['Close']
            }
            
            # Check for individual patterns
            if self._is_doji(curr_row):
                signal['patterns'].append('Doji')
                
            if self._is_hammer(curr_row):
                signal['patterns'].append('Hammer')
                
            if self._is_shooting_star(curr_row):
                signal['patterns'].append('Shooting Star')
                
            # Check for multi-candle patterns
            if self._is_engulfing(prev_row, curr_row):
                if curr_row['Is_Bullish']:
                    signal['patterns'].append('Bullish Engulfing')
                else:
                    signal['patterns'].append('Bearish Engulfing')
            
            if signal['patterns']:
                signals.append(signal)
                
        self.signals = signals
        return signals
    
    def plot_signals(self, last_n_days: int = 30) -> None:
        """
        Plot the price chart with detected signals.
        
        Args:
            last_n_days: Number of recent days to plot (default: 30)
        """
        if not self.signals:
            raise ValueError("No signals detected. Call analyze_candles() first.")
            
        plot_data = self.btc_data.tail(last_n_days).copy()
        signals_in_range = [s for s in self.signals if s['date'] in plot_data.index]
        
        if not signals_in_range:
            print("No signals in the selected date range.")
            return
            
        # Prepare markers for signals
        markers = []
        for signal in signals_in_range:
            markers.append(
                (plot_data.index.get_loc(signal['date']), 
                 plot_data.loc[signal['date'], 'Low'] * 0.98,
                 ' '.join(signal['patterns']))
            )
        
        # Create plot
        mpf.plot(
            plot_data,
            type='candle',
            style='charles',
            title='Bitcoin Price with Candlestick Patterns',
            ylabel='Price ($)',
            figsize=(15, 7),
            addplot=[
                mpf.make_addplot(
                    plot_data['Close'].rolling(7).mean(),
                    color='blue',
                    width=1,
                    alpha=0.5
                )
            ],
            hlines={
                'hlines': [plot_data['Close'].mean()],
                'colors': ['gray'],
                'linestyles': ['--'],
                'alpha': 0.5
            },
            volume=True,
            panel_ratios=(4, 1),
            warn_too_much_data=
