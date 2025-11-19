"""
Generated Code Metadata:
========================
Original URL: https://immediate-byte.com
Prompt: Generate a Python script to perform technical analysis on historical market data, using tools and techniques like chart patterns, trends, and support and resistance levels.
Generated: DETERMINISTIC_b4e461378ae6497c
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
import matplotlib.pyplot as plt
from typing import Optional, Tuple, List
import yfinance as yf
from datetime import datetime, timedelta

class TechnicalAnalyzer:
    """
    A class to perform technical analysis on historical market data.
    Supports chart patterns, trend analysis, and support/resistance levels.
    """

    def __init__(self, ticker: str, period: str = "1y", interval: str = "1d"):
        """
        Initialize the TechnicalAnalyzer with market data.

        Args:
            ticker (str): Stock ticker symbol (e.g., 'AAPL')
            period (str): Time period to fetch data for (default: '1y')
            interval (str): Data interval (default: '1d')
        """
        self.ticker = ticker
        self.period = period
        self.interval = interval
        self.data = self._fetch_data()

    def _fetch_data(self) -> pd.DataFrame:
        """
        Fetch historical market data using yfinance.

        Returns:
            pd.DataFrame: DataFrame containing OHLCV data

        Raises:
            ValueError: If data fetching fails
        """
        try:
            data = yf.Ticker(self.ticker).history(period=self.period, interval=self.interval)
            if data.empty:
                raise ValueError("No data returned for the given ticker and period")
            return data
        except Exception as e:
            raise ValueError(f"Error fetching data: {str(e)}")

    def calculate_sma(self, window: int = 20) -> pd.Series:
        """
        Calculate Simple Moving Average.

        Args:
            window (int): Window size for SMA calculation (default: 20)

        Returns:
            pd.Series: Series containing SMA values
        """
        return self.data['Close'].rolling(window=window).mean()

    def calculate_ema(self, window: int = 20) -> pd.Series:
        """
        Calculate Exponential Moving Average.

        Args:
            window (int): Window size for EMA calculation (default: 20)

        Returns:
            pd.Series: Series containing EMA values
        """
        return self.data['Close'].ewm(span=window, adjust=False).mean()

    def calculate_rsi(self, window: int = 14) -> pd.Series:
        """
        Calculate Relative Strength Index (RSI).

        Args:
            window (int): Window size for RSI calculation (default: 14)

        Returns:
            pd.Series: Series containing RSI values
        """
        delta = self.data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))

    def identify_support_resistance(self, tolerance: float = 0.02) -> Tuple[List[float], List[float]]:
        """
        Identify support and resistance levels.

        Args:
            tolerance (float): Percentage tolerance for level identification (default: 0.02)

        Returns:
            Tuple[List[float], List[float]]: (support_levels, resistance_levels)
        """
        highs = self.data['High']
        lows = self.data['Low']
        closes = self.data['Close']

        # Find potential support/resistance levels
        potential_levels = []
        for i in range(2, len(closes)-2):
            if (highs[i] > highs[i-1] and highs[i] > highs[i+1] and 
                highs[i+1] > highs[i+2] and highs[i-1] > highs[i-2]):
                potential_levels.append(highs[i])
            elif (lows[i] < lows[i-1] and lows[i] < lows[i+1] and 
                  lows[i+1] < lows[i+2] and lows[i-1] < lows[i-2]):
                potential_levels.append(lows[i])

        # Cluster similar levels
        levels = []
        for level in potential_levels:
            if not levels:
                levels.append(level)
            else:
                if abs(level - levels[-1]) / levels[-1] > tolerance:
                    levels.append(level)

        # Classify as support or resistance
        support = []
        resistance = []
        for level in levels:
            if closes.iloc[-1] > level:
                support.append(level)
            else:
                resistance.append(level)

        return support, resistance

    def plot_chart(self, indicators: Optional[dict] = None) -> None:
        """
        Plot the price chart with technical indicators.

        Args:
            indicators (dict, optional): Dictionary of indicators to plot.
                Format: {'indicator_name': pd.Series}
        """
        plt.figure(figsize=(12, 6))
        plt.plot(self.data['Close'], label='Price', alpha=0.5)

        if indicators:
            for name, values in indicators.items():
                plt.plot(values, label=name)

        support, resistance = self.identify_support_resistance()
        for level in support:
            plt.axhline(y=level, color='green', linestyle='--', alpha=0.5)
        for level in resistance:
            plt.axhline(y=level, color='red', linestyle='--', alpha=0.5)

        plt.title(f'{self.ticker} Technical Analysis')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid()
        plt.show()

    def detect_trend(self) -> str:
        """
        Detect the current market trend based on moving averages.

        Returns:
            str: 'uptrend', 'downtrend', or 'sideways'
        """
        sma_50 = self.calculate_sma(50)
        sma_200 = self.calculate_sma(200)

        if sma_50.iloc[-1] > sma_200.iloc[-1] and sma_50.iloc[-1] > sma_50.iloc[-2]:
            return 'uptrend'
        elif sma_50.iloc[-1] < sma_200.iloc[-1] and sma_50.iloc[-1] < sma_50.iloc[-2]:
            return 'downtrend'
        else:
            return 'sideways'


# Example usage
if __name__ == "__main__":
    try:
        analyzer = TechnicalAnalyzer('AAPL', period='6mo')
        
        # Calculate indicators
        sma_20 = analyzer.calculate_sma(20)
        ema_20 = analyzer.calculate_ema(20)
        rsi = analyzer.calculate_rsi()
        
        # Plot chart with indicators
        analyzer.plot_chart({
            'SMA 20': sma_20,
            'EMA 20': ema_20
        })
        
        # Print analysis results
        print(f"Current trend: {analyzer.detect_trend()}")
        support, resistance = analyzer.identify_support_resistance()
        print(f"Support levels: {support}")
        print(f"Resistance levels: {resistance}")
        print(f"Current RSI: {rsi.iloc[-1]:.2f}")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
```
