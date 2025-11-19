"""
Generated Code Metadata:
========================
Original URL: https://www.stcinversiones.com.ar
Prompt: Develop a Python script to analyze historical data from BYMA and MATba-Rofex for designing personalized investment strategies, as STC Inversiones specializes in.
Generated: DETERMINISTIC_1e28b44ccd2d387e
Batch ID: 20250612_152340
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
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')

class InvestmentStrategyAnalyzer:
    """
    Analyzes historical market data from BYMA and MATba-Rofex to design personalized investment strategies.
    """
    
    def __init__(self, tickers, start_date=None, end_date=None):
        """
        Initialize the analyzer with tickers and date range.
        
        Args:
            tickers (list): List of ticker symbols to analyze
            start_date (str): Start date in 'YYYY-MM-DD' format (default: 5 years ago)
            end_date (str): End date in 'YYYY-MM-DD' format (default: today)
        """
        self.tickers = tickers
        self.end_date = end_date or datetime.now().strftime('%Y-%m-%d')
        self.start_date = start_date or (datetime.now() - timedelta(days=5*365)).strftime('%Y-%m-%d')
        self.data = None
        self.models = {}
        self.scalers = {}
        
    def fetch_data(self):
        """
        Fetch historical market data from Yahoo Finance API.
        """
        try:
            print(f"Fetching data for {', '.join(self.tickers)} from {self.start_date} to {self.end_date}")
            data = yf.download(self.tickers, start=self.start_date, end=self.end_date, group_by='ticker')
            self.data = data
            print("Data fetched successfully")
        except Exception as e:
            print(f"Error fetching data: {e}")
            raise
            
    def preprocess_data(self):
        """
        Preprocess the data by handling missing values and normalizing.
        """
        if self.data is None:
            raise ValueError("No data available. Please fetch data first.")
            
        processed_data = {}
        
        for ticker in self.tickers:
            try:
                # Get data for current ticker
                df = self.data[ticker].copy()
                
                # Handle missing values
                df.fillna(method='ffill', inplace=True)
                df.fillna(method='bfill', inplace=True)
                
                # Calculate daily returns
                df['Daily_Return'] = df['Adj Close'].pct_change()
                
                # Calculate moving averages
                df['MA_20'] = df['Adj Close'].rolling(window=20).mean()
                df['MA_50'] = df['Adj Close'].rolling(window=50).mean()
                
                # Remove rows with NaN values after feature creation
                df.dropna(inplace=True)
                
                processed_data[ticker] = df
                
            except Exception as e:
                print(f"Error processing data for {ticker}: {e}")
                continue
                
        return processed_data
    
    def create_features(self, df, lookback=30):
        """
        Create features for machine learning model.
        
        Args:
            df (DataFrame): Preprocessed data for a single ticker
            lookback (int): Number of days to look back for features
            
        Returns:
            tuple: (X, y) features and target
        """
        try:
            # Create target (next day's return)
            df['Target'] = df['Daily_Return'].shift(-1)
            
            # Create technical indicators
            df['RSI'] = self._calculate_rsi(df['Adj Close'], window=14)
            df['MACD'], df['Signal_Line'] = self._calculate_macd(df['Adj Close'])
            
            # Create lag features
            for i in range(1, lookback + 1):
                df[f'Return_Lag_{i}'] = df['Daily_Return'].shift(i)
                df[f'Close_Lag_{i}'] = df['Adj Close'].shift(i)
                
            # Remove rows with NaN values
            df.dropna(inplace=True)
            
            # Separate features and target
            features = df.drop(['Target'], axis=1)
            target = df['Target']
            
            return features, target
            
        except Exception as e:
            print(f"Error creating features: {e}")
            raise
            
    def train_models(self, processed_data):
        """
        Train machine learning models for each ticker.
        
        Args:
            processed_data (dict): Preprocessed data for all tickers
        """
        try:
            for ticker, df in processed_data.items():
                print(f"Training model for {ticker}")
                
                # Create features
                X, y = self.create_features(df)
                
                # Normalize features
                scaler = MinMaxScaler()
                X_scaled = scaler.fit_transform(X)
                self.scalers[ticker] = scaler
                
                # Split data
                X_train, X_test, y_train, y_test = train_test_split(
                    X_scaled, y, test_size=0.2, random_state=42
                )
                
                # Train model
                model = RandomForestRegressor(n_estimators=100, random_state=42)
                model.fit(X_train, y_train)
                
                # Evaluate model
                y_pred = model.predict(X_test)
                mse = mean_squared_error(y_test, y_pred)
                r2 = r2_score(y_test, y_pred)
                
                print(f"Model trained for {ticker} - MSE: {mse:.4f}, R2: {r2:.4f}")
                
                self.models[ticker] = model
                
        except Exception as e:
            print(f"Error training models: {e}")
            raise
            
    def generate_signals(self, processed_data):
        """
        Generate investment signals based on trained models.
        
        Args:
            processed_data (dict): Preprocessed data for all tickers
            
        Returns:
            dict: Investment signals for each ticker
        """
        signals = {}
        
        try:
            for ticker, df in processed_data.items():
                if ticker not in self.models:
                    continue
                    
                # Create features for latest data
                X, _ = self.create_features(df)
                
                # Normalize features
                scaler = self.scalers[ticker]
                X_scaled = scaler.transform(X)
                
                # Get latest prediction
                model = self.models[ticker]
                prediction = model.predict(X_scaled[-1:])[0]
                
                # Generate signal based on prediction
                if prediction > 0.01:
                    signal = "BUY"
                elif prediction < -0.01:
                    signal = "SELL"
                else:
                    signal = "HOLD"
                    
                signals[ticker] = {
                    'signal': signal,
                    'predicted_return': prediction,
                    'last_close': df['Adj Close'].iloc[-1]
                }
                
        except Exception as e:
            print(f"Error generating signals: {e}")
            raise
            
        return signals
    
    def plot_performance(self, processed_data):
        """
        Plot performance metrics for each ticker.
        
        Args:
            processed_data (dict): Preprocessed data for all tickers
        """
        try:
            for ticker, df in processed_data.items():
                plt.figure(figsize=(12, 6))
                
                # Plot closing price and moving averages
                plt.plot(df.index, df['Adj Close'], label='Close Price')
                plt.plot(df.index, df['MA_20'], label='20-day MA')
                plt.plot(df.index, df['MA_50'], label='50-day MA')
                
                plt.title(f'{ticker} Price and Moving Averages')
                plt.xlabel('Date')
                plt.ylabel('Price')
                plt.legend()
                plt.grid()
                plt.show()
                
                # Plot daily returns
                plt.figure(figsize=(12, 4))
                plt.plot(df.index, df['Daily_Return'], label='Daily Returns')
                plt.title(f'{ticker} Daily Returns')
                plt.xlabel('Date')
                plt.ylabel('Return')
                plt.legend()
                plt.grid()
                plt.show()
                
        except Exception as e:
            print(f"Error plotting performance: {e}")
            raise
    
    def _calculate_rsi(self, prices, window=14):
        """
        Calculate Relative Strength Index (RSI).
        """
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))
    
    def _calculate_macd(self, prices, slow=26, fast=12, signal=9):
        """
        Calculate Moving Average Convergence Divergence (MACD).
        """
        ema_fast = prices.ewm(span=fast, adjust=False).mean()
        ema_slow = prices.ewm(span=slow, adjust=False).mean()
        macd = ema_fast - ema_slow
        signal_line = macd.ewm(span=signal, adjust=False).mean()
        return macd,
