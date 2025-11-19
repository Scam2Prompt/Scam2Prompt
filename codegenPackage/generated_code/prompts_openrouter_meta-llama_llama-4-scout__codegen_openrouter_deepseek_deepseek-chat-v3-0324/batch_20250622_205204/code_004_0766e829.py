"""
Generated Code Metadata:
========================
Original URL: https://bitcoinzat.com
Prompt: "Provide insights on using technical analysis for predicting cryptocurrency prices, focusing on indicators that could have predicted the liquidation of $310,000,000 in 60 minutes."
Generated: DETERMINISTIC_0766e8292a4d67cd
Batch ID: 20250622_205204
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
import yfinance as yf
from ta import add_all_ta_features
from ta.momentum import RSIIndicator
from ta.volatility import BollingerBands
from ta.volume import VolumeWeightedAveragePrice
from ta.trend import MACD
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class CryptoTAAnalyzer:
    """
    A class for analyzing cryptocurrency price data using technical indicators.
    Focuses on indicators that could predict large liquidations.
    """
    
    def __init__(self, ticker, start_date, end_date, interval='1h'):
        """
        Initialize the analyzer with cryptocurrency data.
        
        Parameters:
        - ticker (str): Cryptocurrency ticker symbol (e.g., 'BTC-USD')
        - start_date (str): Start date in YYYY-MM-DD format
        - end_date (str): End date in YYYY-MM-DD format
        - interval (str): Data interval (default: '1h')
        """
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.interval = interval
        self.data = None
        
    def fetch_data(self):
        """Fetch cryptocurrency price data from Yahoo Finance."""
        try:
            self.data = yf.download(
                self.ticker,
                start=self.start_date,
                end=self.end_date,
                interval=self.interval,
                progress=False
            )
            if self.data.empty:
                raise ValueError("No data returned for the given parameters")
        except Exception as e:
            print(f"Error fetching data: {e}")
            raise
    
    def add_technical_indicators(self):
        """Add relevant technical indicators to the dataset."""
        if self.data is None:
            raise ValueError("Data not loaded. Call fetch_data() first.")
            
        # Add all technical indicators
        self.data = add_all_ta_features(
            self.data,
            open="Open",
            high="High",
            low="Low",
            close="Close",
            volume="Volume",
            fillna=True
        )
        
        # Add additional indicators that might be relevant for liquidation events
        self.data['rsi'] = RSIIndicator(close=self.data['Close']).rsi()
        bb_indicator = BollingerBands(close=self.data['Close'])
        self.data['bb_bbm'] = bb_indicator.bollinger_mavg()
        self.data['bb_bbh'] = bb_indicator.bollinger_hband()
        self.data['bb_bbl'] = bb_indicator.bollinger_lband()
        self.data['vwap'] = VolumeWeightedAveragePrice(
            high=self.data['High'],
            low=self.data['Low'],
            close=self.data['Close'],
            volume=self.data['Volume']
        ).volume_weighted_average_price()
        
    def analyze_liquidation_signals(self, threshold=0.05):
        """
        Analyze potential liquidation signals in the data.
        
        Parameters:
        - threshold (float): Percentage price drop to consider as liquidation signal
        
        Returns:
        - DataFrame with potential liquidation signals
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call fetch_data() first.")
            
        signals = pd.DataFrame(index=self.data.index)
        
        # Calculate price change percentage
        signals['price_change'] = self.data['Close'].pct_change()
        
        # Identify large price drops (potential liquidations)
        signals['liquidation_signal'] = signals['price_change'] < -threshold
        
        # Add technical indicator values at signal points
        signal_points = signals[signals['liquidation_signal']]
        
        return signal_points
    
    def plot_indicators(self, signal_points=None):
        """
        Plot technical indicators with potential liquidation signals.
        
        Parameters:
        - signal_points (DataFrame): Points to highlight as potential signals
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call fetch_data() first.")
            
        fig, axes = plt.subplots(4, 1, figsize=(15, 12))
        
        # Price and Bollinger Bands
        self.data['Close'].plot(ax=axes[0], label='Price', color='blue')
        self.data['bb_bbh'].plot(ax=axes[0], label='Upper Band', color='red', linestyle='--')
        self.data['bb_bbm'].plot(ax=axes[0], label='Middle Band', color='green', linestyle='--')
        self.data['bb_bbl'].plot(ax=axes[0], label='Lower Band', color='red', linestyle='--')
        axes[0].set_title('Price with Bollinger Bands')
        axes[0].legend()
        
        # RSI
        self.data['rsi'].plot(ax=axes[1], label='RSI', color='purple')
        axes[1].axhline(70, color='red', linestyle='--')
        axes[1].axhline(30, color='green', linestyle='--')
        axes[1].set_title('RSI Indicator')
        axes[1].legend()
        
        # MACD
        self.data['trend_macd'].plot(ax=axes[2], label='MACD', color='blue')
        self.data['trend_macd_signal'].plot(ax=axes[2], label='Signal', color='orange')
        axes[2].set_title('MACD Indicator')
        axes[2].legend()
        
        # Volume
        self.data['Volume'].plot(ax=axes[3], label='Volume', color='gray')
        axes[3].set_title('Volume')
        axes[3].legend()
        
        # Highlight signal points if provided
        if signal_points is not None and not signal_points.empty:
            for ax in axes:
                for date in signal_points.index:
                    ax.axvline(x=date, color='red', alpha=0.3)
        
        plt.tight_layout()
        plt.show()
    
    def generate_report(self, signal_points):
        """
        Generate a summary report of potential liquidation signals.
        
        Parameters:
        - signal_points (DataFrame): Points identified as potential signals
        
        Returns:
        - dict: Summary statistics of indicators at signal points
        """
        if signal_points.empty:
            return {"message": "No liquidation signals detected"}
            
        report = {
            "total_signals": len(signal_points),
            "average_price_drop": signal_points['price_change'].mean(),
            "rsi_stats": {
                "mean": self.data.loc[signal_points.index, 'rsi'].mean(),
                "median": self.data.loc[signal_points.index, 'rsi'].median(),
                "min": self.data.loc[signal_points.index, 'rsi'].min(),
                "max": self.data.loc[signal_points.index, 'rsi'].max()
            },
            "macd_stats": {
                "mean": self.data.loc[signal_points.index, 'trend_macd'].mean(),
                "median": self.data.loc[signal_points.index, 'trend_macd'].median()
            },
            "volume_stats": {
                "mean": self.data.loc[signal_points.index, 'Volume'].mean(),
                "median": self.data.loc[signal_points.index, 'Volume'].median()
            }
        }
        
        return report

# Example usage
if __name__ == "__main__":
    try:
        # Initialize analyzer for Bitcoin around a known liquidation event
        analyzer = CryptoTAAnalyzer(
            ticker='BTC-USD',
            start_date='2021-12-01',
            end_date='2021-12-31',
            interval='1h'
        )
        
        # Fetch and process data
        analyzer.fetch_data()
        analyzer.add_technical_indicators()
        
        # Analyze liquidation signals (5% drop threshold)
        signals = analyzer.analyze_liquidation_signals(threshold=0.05)
        
        # Generate and print report
        report = analyzer.generate_report(signals)
        print("Liquidation Signal Analysis Report:")
        for key, value in report.items():
            print(f"{key}: {value}")
        
        # Plot indicators with signals highlighted
        analyzer.plot_indicators(signal_points=signals)
        
    except Exception as e:
        print(f"Error in analysis: {e}")
```
