"""
Generated Code Metadata:
========================
Original URL: https://memetic.digital
Prompt: Generate code to simulate market trend analysis for disruptive technologies, aligning with Memetic Digital's investment theses.
Generated: DETERMINISTIC_e778eb1f98111be2
Batch ID: 20250612_154545
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
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import yfinance as yf
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple, Optional

class MarketTrendAnalyzer:
    """
    A class to simulate market trend analysis for disruptive technologies.
    """
    
    def __init__(self, tickers: List[str], start_date: str, end_date: str):
        """
        Initialize the MarketTrendAnalyzer with stock tickers and date range.
        
        Args:
            tickers: List of stock tickers to analyze
            start_date: Start date in 'YYYY-MM-DD' format
            end_date: End date in 'YYYY-MM-DD' format
        """
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
        self.data = self._fetch_data()
        
    def _fetch_data(self) -> Dict[str, pd.DataFrame]:
        """
        Fetch historical stock data from Yahoo Finance.
        
        Returns:
            Dictionary of DataFrames with stock data for each ticker
            
        Raises:
            ValueError: If data fetching fails for any ticker
        """
        data = {}
        for ticker in self.tickers:
            try:
                df = yf.download(ticker, start=self.start_date, end=self.end_date)
                if df.empty:
                    raise ValueError(f"No data found for {ticker}")
                data[ticker] = df
            except Exception as e:
                raise ValueError(f"Failed to fetch data for {ticker}: {str(e)}")
        return data
    
    def calculate_moving_averages(self, window_sizes: List[int] = [20, 50, 200]) -> Dict[str, pd.DataFrame]:
        """
        Calculate moving averages for each stock.
        
        Args:
            window_sizes: List of window sizes for moving averages
            
        Returns:
            Dictionary of DataFrames with moving averages added
        """
        result = {}
        for ticker, df in self.data.items():
            df_copy = df.copy()
            for window in window_sizes:
                df_copy[f'MA_{window}'] = df_copy['Adj Close'].rolling(window=window).mean()
            result[ticker] = df_copy
        return result
    
    def analyze_trends(self, ma_data: Dict[str, pd.DataFrame]) -> Dict[str, str]:
        """
        Analyze market trends based on moving averages.
        
        Args:
            ma_data: Dictionary of DataFrames with moving averages
            
        Returns:
            Dictionary with trend analysis results for each ticker
        """
        trends = {}
        for ticker, df in ma_data.items():
            last_row = df.iloc[-1]
            
            # Check short-term vs long-term trends
            if 'MA_20' in df.columns and 'MA_50' in df.columns:
                if last_row['MA_20'] > last_row['MA_50']:
                    trends[ticker] = "Bullish (Short-term > Medium-term)"
                else:
                    trends[ticker] = "Bearish (Short-term < Medium-term)"
            
            # Check golden/death cross
            if 'MA_50' in df.columns and 'MA_200' in df.columns:
                if last_row['MA_50'] > last_row['MA_200']:
                    trends[ticker] += " | Golden Cross (50 > 200)"
                else:
                    trends[ticker] += " | Death Cross (50 < 200)"
                    
        return trends
    
    def predict_future_prices(self, days_to_predict: int = 30) -> Dict[str, Tuple[float, float]]:
        """
        Predict future prices using linear regression.
        
        Args:
            days_to_predict: Number of days to predict ahead
            
        Returns:
            Dictionary with predicted prices and confidence scores for each ticker
        """
        predictions = {}
        for ticker, df in self.data.items():
            try:
                # Prepare data
                X = np.array(range(len(df))).reshape(-1, 1)
                y = df['Adj Close'].values
                
                # Train model
                model = LinearRegression()
                model.fit(X, y)
                
                # Predict future
                future_days = np.array(range(len(df), len(df) + days_to_predict)).reshape(-1, 1)
                future_prices = model.predict(future_days)
                
                # Calculate confidence (1 - RMSE/max_price)
                y_pred = model.predict(X)
                rmse = np.sqrt(mean_squared_error(y, y_pred))
                confidence = 1 - (rmse / max(y))
                
                predictions[ticker] = (future_prices[-1], max(0, min(1, confidence)))
                
            except Exception as e:
                predictions[ticker] = (None, None)
                print(f"Prediction failed for {ticker}: {str(e)}")
                
        return predictions
    
    def visualize_trends(self, ma_data: Dict[str, pd.DataFrame], ticker: str):
        """
        Visualize stock trends with moving averages.
        
        Args:
            ma_data: Dictionary of DataFrames with moving averages
            ticker: Ticker to visualize
        """
        if ticker not in ma_data:
            raise ValueError(f"No data available for {ticker}")
            
        df = ma_data[ticker]
        plt.figure(figsize=(12, 6))
        plt.plot(df.index, df['Adj Close'], label='Price', color='blue')
        
        if 'MA_20' in df.columns:
            plt.plot(df.index, df['MA_20'], label='20-day MA', color='orange')
        if 'MA_50' in df.columns:
            plt.plot(df.index, df['MA_50'], label='50-day MA', color='green')
        if 'MA_200' in df.columns:
            plt.plot(df.index, df['MA_200'], label='200-day MA', color='red')
            
        plt.title(f'{ticker} Stock Price and Moving Averages')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Disruptive technology stocks
    disruptive_tickers = ['TSLA', 'NVDA', 'AMD', 'PLTR', 'CRSP']
    
    # Date range - last 2 years
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=365*2)).strftime('%Y-%m-%d')
    
    try:
        # Initialize analyzer
        analyzer = MarketTrendAnalyzer(disruptive_tickers, start_date, end_date)
        
        # Calculate moving averages
        ma_data = analyzer.calculate_moving_averages()
        
        # Analyze trends
        trends = analyzer.analyze_trends(ma_data)
        print("\nMarket Trends Analysis:")
        for ticker, trend in trends.items():
            print(f"{ticker}: {trend}")
        
        # Predict future prices
        predictions = analyzer.predict_future_prices()
        print("\nFuture Price Predictions (30 days):")
        for ticker, (price, confidence) in predictions.items():
            if price is not None:
                print(f"{ticker}: Predicted ${price:.2f} (Confidence: {confidence*100:.1f}%)")
            else:
                print(f"{ticker}: Prediction failed")
        
        # Visualize trends for a specific ticker
        analyzer.visualize_trends(ma_data, 'TSLA')
        
    except Exception as e:
        print(f"Error in market trend analysis: {str(e)}")
```
