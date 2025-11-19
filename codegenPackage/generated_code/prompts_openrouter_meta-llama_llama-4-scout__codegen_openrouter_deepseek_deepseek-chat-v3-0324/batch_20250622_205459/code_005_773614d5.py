"""
Generated Code Metadata:
========================
Original URL: https://diamondtradingfx.com
Prompt: Implement a cryptocurrency price prediction model using machine learning algorithms, focusing on Bitcoin, Ethereum, and Litecoin.
Generated: DETERMINISTIC_773614d5bc1d83ea
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime, timedelta
import joblib
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class CryptoPricePredictor:
    """
    A machine learning model for predicting cryptocurrency prices using historical data.
    Supports Bitcoin (BTC-USD), Ethereum (ETH-USD), and Litecoin (LTC-USD).
    """
    
    def __init__(self):
        self.models = {}
        self.scalers = {}
        self.cryptos = ['BTC-USD', 'ETH-USD', 'LTC-USD']
        self.features = ['Open', 'High', 'Low', 'Volume']
        self.target = 'Close'
        self.lookback = 30  # Number of days to look back for features
        
    def fetch_data(self, crypto, start_date='2015-01-01', end_date=None):
        """
        Fetch historical cryptocurrency data from Yahoo Finance.
        
        Args:
            crypto (str): Cryptocurrency symbol (e.g., 'BTC-USD')
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format (default: today)
            
        Returns:
            pd.DataFrame: Historical price data
        """
        if end_date is None:
            end_date = datetime.now().strftime('%Y-%m-%d')
            
        try:
            data = yf.download(crypto, start=start_date, end=end_date)
            if data.empty:
                raise ValueError(f"No data found for {crypto}")
            return data
        except Exception as e:
            raise Exception(f"Error fetching data for {crypto}: {str(e)}")
    
    def preprocess_data(self, data, crypto):
        """
        Preprocess the data by creating features and scaling.
        
        Args:
            data (pd.DataFrame): Raw cryptocurrency data
            crypto (str): Cryptocurrency symbol
            
        Returns:
            tuple: (X, y) features and target arrays
        """
        # Create target variable (next day's closing price)
        data['Target'] = data[self.target].shift(-1)
        data.dropna(inplace=True)
        
        # Create features from past 'lookback' days
        for feature in self.features:
            for day in range(1, self.lookback + 1):
                data[f'{feature}_lag_{day}'] = data[feature].shift(day)
        
        data.dropna(inplace=True)
        
        # Separate features and target
        X = data.drop(['Target', self.target], axis=1)
        y = data['Target']
        
        # Scale features
        scaler = MinMaxScaler()
        X_scaled = scaler.fit_transform(X)
        self.scalers[crypto] = scaler
        
        return X_scaled, y.values
    
    def train_model(self, crypto, test_size=0.2, random_state=42):
        """
        Train a Random Forest model for the specified cryptocurrency.
        
        Args:
            crypto (str): Cryptocurrency symbol
            test_size (float): Proportion of data for testing
            random_state (int): Random seed for reproducibility
            
        Returns:
            dict: Model evaluation metrics
        """
        try:
            # Fetch and preprocess data
            data = self.fetch_data(crypto)
            X, y = self.preprocess_data(data, crypto)
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=random_state
            )
            
            # Train model
            model = RandomForestRegressor(
                n_estimators=100,
                max_depth=10,
                random_state=random_state,
                n_jobs=-1
            )
            model.fit(X_train, y_train)
            
            # Evaluate model
            y_pred = model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            mae = mean_absolute_error(y_test, y_pred)
            
            # Store model
            self.models[crypto] = model
            
            return {
                'crypto': crypto,
                'mse': mse,
                'mae': mae,
                'model': 'RandomForestRegressor'
            }
        except Exception as e:
            raise Exception(f"Error training model for {crypto}: {str(e)}")
    
    def predict_price(self, crypto, days=1):
        """
        Predict future prices for the specified cryptocurrency.
        
        Args:
            crypto (str): Cryptocurrency symbol
            days (int): Number of days to predict
            
        Returns:
            list: Predicted prices for the next 'days' days
        """
        if crypto not in self.models:
            raise ValueError(f"Model not trained for {crypto}")
            
        try:
            # Get recent data
            end_date = datetime.now()
            start_date = end_date - timedelta(days=self.lookback * 2)
            data = self.fetch_data(crypto, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
            
            if len(data) < self.lookback:
                raise ValueError(f"Insufficient data for prediction. Need at least {self.lookback} days.")
            
            predictions = []
            current_data = data.copy()
            
            for _ in range(days):
                # Prepare the most recent data point
                features = []
                for feature in self.features:
                    for day in range(1, self.lookback + 1):
                        features.append(current_data[feature].iloc[-day])
                
                # Scale features
                scaled_features = self.scalers[crypto].transform([features])
                
                # Make prediction
                pred = self.models[crypto].predict(scaled_features)[0]
                predictions.append(pred)
                
                # Update current_data with the prediction
                new_row = current_data.iloc[-1].copy()
                new_row['Close'] = pred
                new_row.name = new_row.name + timedelta(days=1)
                current_data = current_data.append(new_row)
            
            return predictions
        except Exception as e:
            raise Exception(f"Error predicting prices for {crypto}: {str(e)}")
    
    def save_models(self, path='models/'):
        """
        Save trained models and scalers to disk.
        
        Args:
            path (str): Directory path to save models
        """
        import os
        os.makedirs(path, exist_ok=True)
        
        for crypto in self.models:
            joblib.dump(self.models[crypto], f'{path}{crypto}_model.pkl')
            joblib.dump(self.scalers[crypto], f'{path}{crypto}_scaler.pkl')
    
    def load_models(self, path='models/'):
        """
        Load trained models and scalers from disk.
        
        Args:
            path (str): Directory path containing saved models
        """
        for crypto in self.cryptos:
            try:
                self.models[crypto] = joblib.load(f'{path}{crypto}_model.pkl')
                self.scalers[crypto] = joblib.load(f'{path}{crypto}_scaler.pkl')
            except FileNotFoundError:
                print(f"Model not found for {crypto}, please train first.")

# Example usage
if __name__ == '__main__':
    predictor = CryptoPricePredictor()
    
    # Train models for all supported cryptocurrencies
    for crypto in predictor.cryptos:
        try:
            metrics = predictor.train_model(crypto)
            print(f"Trained {crypto} model. MSE: {metrics['mse']:.2f}, MAE: {metrics['mae']:.2f}")
        except Exception as e:
            print(f"Failed to train {crypto}: {str(e)}")
    
    # Save models
    predictor.save_models()
    
    # Predict prices for the next 5 days
    for crypto in predictor.cryptos:
        try:
            predictions = predictor.predict_price(crypto, days=5)
            print(f"{crypto} price predictions for next 5 days:")
            for i, price in enumerate(predictions, 1):
                print(f"Day {i}: ${price:.2f}")
        except Exception as e:
            print(f"Failed to predict {crypto}: {str(e)}")
```
