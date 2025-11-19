"""
Generated Code Metadata:
========================
Original URL: https://exytrade.com
Prompt: Write code to analyze stock market trends and generate trading insights, leveraging Exytrade's focus on expert guidance for investors.
Generated: DETERMINISTIC_3d708e6bf8701fcf
Batch ID: 20250612_154333
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
import seaborn as sns
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class StockAnalyzer:
    """
    A class to analyze stock market trends and generate trading insights.
    
    Attributes:
        ticker (str): Stock ticker symbol
        start_date (str): Start date for analysis (YYYY-MM-DD)
        end_date (str): End date for analysis (YYYY-MM-DD)
        data (pd.DataFrame): Historical stock data
    """
    
    def __init__(self, ticker: str, start_date: str, end_date: Optional[str] = None):
        """
        Initialize the StockAnalyzer with ticker and date range.
        
        Args:
            ticker: Stock ticker symbol
            start_date: Start date for analysis (YYYY-MM-DD)
            end_date: Optional end date (defaults to today if None)
        """
        self.ticker = ticker.upper()
        self.start_date = start_date
        self.end_date = end_date if end_date else datetime.now().strftime('%Y-%m-%d')
        self.data = self._fetch_data()
        
    def _fetch_data(self) -> pd.DataFrame:
        """
        Fetch historical stock data from Yahoo Finance.
        
        Returns:
            DataFrame containing historical stock data
            
        Raises:
            ValueError: If data cannot be fetched
        """
        try:
            data = yf.download(self.ticker, start=self.start_date, end=self.end_date)
            if data.empty:
                raise ValueError(f"No data found for {self.ticker}")
            return data
        except Exception as e:
            raise ValueError(f"Error fetching data: {str(e)}")
    
    def calculate_moving_averages(self, windows: List[int] = [20, 50, 200]) -> pd.DataFrame:
        """
        Calculate moving averages for the stock.
        
        Args:
            windows: List of window sizes for moving averages
            
        Returns:
            DataFrame with original data and moving averages
        """
        data = self.data.copy()
        for window in windows:
            data[f'MA_{window}'] = data['Close'].rolling(window=window).mean()
        return data
    
    def calculate_rsi(self, window: int = 14) -> pd.DataFrame:
        """
        Calculate Relative Strength Index (RSI).
        
        Args:
            window: Lookback window for RSI calculation
            
        Returns:
            DataFrame with RSI values
        """
        data = self.data.copy()
        delta = data['Close'].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        
        avg_gain = gain.rolling(window=window).mean()
        avg_loss = loss.rolling(window=window).mean()
        
        rs = avg_gain / avg_loss
        data['RSI'] = 100 - (100 / (1 + rs))
        return data
    
    def generate_trading_signals(self) -> pd.DataFrame:
        """
        Generate trading signals based on technical indicators.
        
        Returns:
            DataFrame with trading signals
        """
        data = self.calculate_moving_averages()
        data = self.calculate_rsi()
        
        # Generate signals
        data['Signal'] = 0  # 0: No signal, 1: Buy, -1: Sell
        
        # Golden Cross (20MA crosses above 50MA)
        data.loc[data['MA_20'] > data['MA_50'], 'Signal'] = 1
        
        # Death Cross (20MA crosses below 50MA)
        data.loc[data['MA_20'] < data['MA_50'], 'Signal'] = -1
        
        # RSI overbought (>70)
        data.loc[data['RSI'] > 70, 'Signal'] = -1
        
        # RSI oversold (<30)
        data.loc[data['RSI'] < 30, 'Signal'] = 1
        
        return data
    
    def plot_analysis(self, signals: bool = True) -> None:
        """
        Plot the stock data with technical indicators and signals.
        
        Args:
            signals: Whether to plot trading signals
        """
        plt.figure(figsize=(14, 7))
        
        data = self.generate_trading_signals() if signals else self.data
        
        # Plot closing price and moving averages
        plt.plot(data['Close'], label='Close Price', alpha=0.5)
        plt.plot(data['MA_20'], label='20-day MA', alpha=0.75)
        plt.plot(data['MA_50'], label='50-day MA', alpha=0.75)
        plt.plot(data['MA_200'], label='200-day MA', alpha=0.75)
        
        if signals:
            # Plot buy signals
            plt.plot(data[data['Signal'] == 1].index, 
                     data['Close'][data['Signal'] == 1], 
                     '^', markersize=10, color='g', label='Buy Signal')
            
            # Plot sell signals
            plt.plot(data[data['Signal'] == -1].index, 
                     data['Close'][data['Signal'] == -1], 
                     'v', markersize=10, color='r', label='Sell Signal')
        
        plt.title(f'{self.ticker} Technical Analysis')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid()
        plt.show()
        
        # Plot RSI separately
        if 'RSI' in data.columns:
            plt.figure(figsize=(14, 3))
            plt.plot(data['RSI'], label='RSI', color='purple')
            plt.axhline(70, linestyle='--', color='r', alpha=0.5)
            plt.axhline(30, linestyle='--', color='g', alpha=0.5)
            plt.title('Relative Strength Index (RSI)')
            plt.xlabel('Date')
            plt.ylabel('RSI')
            plt.legend()
            plt.grid()
            plt.show()
    
    def generate_insights(self) -> Dict:
        """
        Generate trading insights based on technical analysis.
        
        Returns:
            Dictionary containing trading insights
        """
        data = self.generate_trading_signals()
        latest = data.iloc[-1]
        
        insights = {
            'ticker': self.ticker,
            'current_price': latest['Close'],
            'trend': self._determine_trend(data),
            'momentum': self._determine_momentum(data),
            'volatility': self._calculate_volatility(data),
            'last_signal': self._get_last_signal(data),
            'support_resistance': self._identify_support_resistance(data),
            'rsi_status': self._get_rsi_status(latest['RSI']),
            'moving_average_status': self._get_ma_status(latest)
        }
        
        return insights
    
    def _determine_trend(self, data: pd.DataFrame) -> str:
        """Determine the overall trend based on moving averages."""
        if data['MA_20'].iloc[-1] > data['MA_50'].iloc[-1] > data['MA_200'].iloc[-1]:
            return "Strong Uptrend"
        elif data['MA_20'].iloc[-1] < data['MA_50'].iloc[-1] < data['MA_200'].iloc[-1]:
            return "Strong Downtrend"
        elif data['MA_20'].iloc[-1] > data['MA_50'].iloc[-1]:
            return "Short-term Uptrend"
        else:
            return "Short-term Downtrend"
    
    def _determine_momentum(self, data: pd.DataFrame) -> str:
        """Determine momentum based on recent price changes."""
        pct_change = data['Close'].pct_change(5).iloc[-1] * 100
        if pct_change > 5:
            return "Strong Positive Momentum"
        elif pct_change > 1:
            return "Positive Momentum"
        elif pct_change < -5:
            return "Strong Negative Momentum"
        elif pct_change < -1:
            return "Negative Momentum"
        else:
            return "Neutral Momentum"
    
    def _calculate_volatility(self, data: pd.DataFrame) -> float:
        """Calculate 30-day volatility."""
        return data['Close'].pct_change().std() * np.sqrt(252) * 100
    
    def _get_last_signal(self, data: pd.DataFrame) -> Optional[str]:
        """Get the most recent trading signal."""
        last_signal = data[data['Signal'] != 0]['Signal'].iloc[-1] if any(data['Signal'] != 0) else None
        if last_signal == 1:
            return "Buy"
        elif last_signal == -1:
            return "Sell"
        return None
    
    def _identify_support_resistance(self, data: pd.DataFrame) -> Dict:
        """Identify support and resistance levels."""
        recent_data = data['Close'].
