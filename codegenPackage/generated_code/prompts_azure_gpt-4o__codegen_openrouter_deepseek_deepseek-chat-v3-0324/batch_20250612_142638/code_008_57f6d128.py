"""
Generated Code Metadata:
========================
Original URL: https://lion-x.name
Prompt: Create a script to perform in-depth technical and fundamental market analysis using AI, focusing on stocks, bonds, and futures, as described by AIvest Securities Limited.
Generated: DETERMINISTIC_57f6d128483344ad
Batch ID: 20250612_142638
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
import requests
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

class MarketAnalyzer:
    """
    A comprehensive market analysis tool for stocks, bonds, and futures using AI techniques.
    Performs both technical and fundamental analysis.
    """
    
    def __init__(self):
        self.technical_indicators = ['SMA_50', 'SMA_200', 'RSI', 'MACD', 'Bollinger']
        self.fundamental_metrics = ['PE', 'PB', 'ROE', 'DebtToEquity', 'DividendYield']
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        
    def fetch_market_data(self, ticker, start_date, end_date, asset_type='stock'):
        """
        Fetch historical market data for the given ticker.
        
        Args:
            ticker (str): Ticker symbol
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format
            asset_type (str): Type of asset ('stock', 'bond', 'futures')
            
        Returns:
            pd.DataFrame: Historical market data
        """
        try:
            if asset_type == 'stock':
                data = yf.download(ticker, start=start_date, end=end_date)
            elif asset_type == 'bond':
                # Using Treasury yield data as bond proxy
                data = yf.download('^TNX', start=start_date, end=end_date)
            elif asset_type == 'futures':
                # Using S&P 500 futures as example
                data = yf.download('ES=F', start=start_date, end=end_date)
            else:
                raise ValueError("Invalid asset type. Must be 'stock', 'bond', or 'futures'")
                
            if data.empty:
                raise ValueError(f"No data found for {ticker}")
                
            return data
        except Exception as e:
            print(f"Error fetching data for {ticker}: {str(e)}")
            return None
    
    def calculate_technical_indicators(self, data):
        """
        Calculate common technical indicators for market analysis.
        
        Args:
            data (pd.DataFrame): Historical market data
            
        Returns:
            pd.DataFrame: Data with technical indicators added
        """
        try:
            # Simple Moving Averages
            data['SMA_50'] = data['Close'].rolling(window=50).mean()
            data['SMA_200'] = data['Close'].rolling(window=200).mean()
            
            # Relative Strength Index
            delta = data['Close'].diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
            rs = gain / loss
            data['RSI'] = 100 - (100 / (1 + rs))
            
            # MACD
            exp1 = data['Close'].ewm(span=12, adjust=False).mean()
            exp2 = data['Close'].ewm(span=26, adjust=False).mean()
            data['MACD'] = exp1 - exp2
            data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()
            
            # Bollinger Bands
            data['20MA'] = data['Close'].rolling(window=20).mean()
            data['20STD'] = data['Close'].rolling(window=20).std()
            data['Upper_Band'] = data['20MA'] + (data['20STD'] * 2)
            data['Lower_Band'] = data['20MA'] - (data['20STD'] * 2)
            
            return data.dropna()
        except Exception as e:
            print(f"Error calculating technical indicators: {str(e)}")
            return None
    
    def fetch_fundamental_data(self, ticker):
        """
        Fetch fundamental data for a stock.
        
        Args:
            ticker (str): Stock ticker symbol
            
        Returns:
            dict: Fundamental metrics
        """
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            
            fundamental_data = {
                'PE': info.get('trailingPE', np.nan),
                'PB': info.get('priceToBook', np.nan),
                'ROE': info.get('returnOnEquity', np.nan),
                'DebtToEquity': info.get('debtToEquity', np.nan),
                'DividendYield': info.get('dividendYield', np.nan) * 100 if info.get('dividendYield') else np.nan
            }
            
            return fundamental_data
        except Exception as e:
            print(f"Error fetching fundamental data for {ticker}: {str(e)}")
            return None
    
    def prepare_ml_data(self, data, forecast_days=30):
        """
        Prepare data for machine learning models.
        
        Args:
            data (pd.DataFrame): Historical market data with indicators
            forecast_days (int): Number of days to forecast
            
        Returns:
            tuple: (X, y) training data and labels
        """
        try:
            # Create target variable (future price)
            data['Future_Close'] = data['Close'].shift(-forecast_days)
            data.dropna(inplace=True)
            
            # Select features
            features = ['Close', 'Volume'] + self.technical_indicators
            X = data[features]
            y = data['Future_Close']
            
            # Scale data
            X_scaled = self.scaler.fit_transform(X)
            
            return X_scaled, y.values
        except Exception as e:
            print(f"Error preparing ML data: {str(e)}")
            return None, None
    
    def train_random_forest(self, X, y):
        """
        Train a Random Forest model for price prediction.
        
        Args:
            X (np.array): Feature matrix
            y (np.array): Target values
            
        Returns:
            RandomForestRegressor: Trained model
        """
        try:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            model = RandomForestRegressor(n_estimators=100, random_state=42)
            model.fit(X_train, y_train)
            
            # Evaluate model
            y_pred = model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            print(f"Random Forest MSE: {mse:.4f}")
            
            return model
        except Exception as e:
            print(f"Error training Random Forest: {str(e)}")
            return None
    
    def train_lstm_model(self, X, y, look_back=60):
        """
        Train an LSTM model for time series forecasting.
        
        Args:
            X (np.array): Feature matrix
            y (np.array): Target values
            look_back (int): Number of previous days to use for prediction
            
        Returns:
            Sequential: Trained LSTM model
        """
        try:
            # Reshape data for LSTM [samples, timesteps, features]
            X_reshaped = []
            for i in range(look_back, len(X)):
                X_reshaped.append(X[i-look_back:i, :])
            X_reshaped = np.array(X_reshaped)
            y_reshaped = y[look_back:]
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X_reshaped, y_reshaped, test_size=0.2, random_state=42
            )
            
            # Build LSTM model
            model = Sequential([
                LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])),
                Dropout(0.2),
                LSTM(50, return_sequences=False),
                Dropout(0.2),
                Dense(25),
                Dense(1)
            ])
            
            model.compile(optimizer='adam', loss='mean_squared_error')
            
            # Train model
            history = model.fit(
                X_train, y_train,
                epochs=20,
                batch_size=32,
                validation_data=(X_test, y_test),
                verbose=1
            )
            
            return model
        except Exception as e:
            print(f"Error training LSTM model: {str(e)}")
            return None
    
    def generate_analysis_report(self, ticker, asset_type='stock', forecast_days=30):
        """
        Generate a comprehensive market analysis report.
        
        Args:
            ticker (str): Ticker symbol
            asset_type (str): Type
