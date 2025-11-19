"""
Generated Code Metadata:
========================
Original URL: https://bitcoinzat.com
Prompt: Create a program that predicts altcoin price movements based on historical data, inspired by Bitcoinzat.com's discussion of alt seasons and $BTTC price predictions.
Generated: DETERMINISTIC_36f87e4492a370a0
Batch ID: 20250612_150343
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
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import MinMaxScaler
import yfinance as yf
import matplotlib.pyplot as plt
import warnings
from datetime import datetime, timedelta

warnings.filterwarnings('ignore')

class AltcoinPricePredictor:
    """
    A class to predict altcoin price movements based on historical data.
    Uses Random Forest regression for price prediction.
    """
    
    def __init__(self, ticker='BTC-USD', days_back=365, test_size=0.2):
        """
        Initialize the predictor with coin ticker and lookback period.
        
        Args:
            ticker (str): Cryptocurrency ticker symbol (default: 'BTC-USD')
            days_back (int): Number of days of historical data to fetch (default: 365)
            test_size (float): Proportion of data to use for testing (default: 0.2)
        """
        self.ticker = ticker
        self.days_back = days_back
        self.test_size = test_size
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.scaler = MinMaxScaler()
        self.data = None
        self.X_train, self.X_test, self.y_train, self.y_test = None, None, None, None
        
    def fetch_data(self):
        """
        Fetch historical price data from Yahoo Finance.
        
        Returns:
            pd.DataFrame: DataFrame containing historical price data
        """
        end_date = datetime.now()
        start_date = end_date - timedelta(days=self.days_back)
        
        try:
            data = yf.download(self.ticker, start=start_date, end=end_date)
            if data.empty:
                raise ValueError("No data returned for the given ticker.")
            return data
        except Exception as e:
            raise Exception(f"Error fetching data: {str(e)}")
    
    def preprocess_data(self, data):
        """
        Preprocess the data for training.
        
        Args:
            data (pd.DataFrame): Raw price data
            
        Returns:
            tuple: (X, y) features and target arrays
        """
        try:
            # Create features
            data['SMA_7'] = data['Close'].rolling(window=7).mean()
            data['SMA_30'] = data['Close'].rolling(window=30).mean()
            data['Daily_Return'] = data['Close'].pct_change()
            data['Volatility'] = data['Daily_Return'].rolling(window=7).std()
            
            # Drop NA values created by rolling calculations
            data = data.dropna()
            
            # Features and target
            X = data[['SMA_7', 'SMA_30', 'Volatility']]
            y = data['Close'].shift(-1).dropna()  # Predict next day's close
            
            # Align X and y after shift
            X = X.iloc[:-1]
            
            # Scale features
            X_scaled = self.scaler.fit_transform(X)
            
            return X_scaled, y.values
        except Exception as e:
            raise Exception(f"Error preprocessing data: {str(e)}")
    
    def train_model(self):
        """
        Train the prediction model on historical data.
        """
        try:
            self.data = self.fetch_data()
            X, y = self.preprocess_data(self.data)
            
            # Split data
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                X, y, test_size=self.test_size, shuffle=False
            )
            
            # Train model
            self.model.fit(self.X_train, self.y_train)
            
            # Evaluate model
            train_pred = self.model.predict(self.X_train)
            test_pred = self.model.predict(self.X_test)
            
            print(f"Training MAE: {mean_absolute_error(self.y_train, train_pred):.2f}")
            print(f"Testing MAE: {mean_absolute_error(self.y_test, test_pred):.2f}")
            
        except Exception as e:
            raise Exception(f"Error training model: {str(e)}")
    
    def predict_next_day(self):
        """
        Predict the next day's price.
        
        Returns:
            float: Predicted price for the next day
        """
        try:
            if not hasattr(self, 'model'):
                raise Exception("Model not trained. Call train_model() first.")
                
            # Get most recent data point
            last_data = self.data.iloc[-1]
            
            # Create features for prediction
            features = np.array([
                last_data['SMA_7'],
                last_data['SMA_30'],
                last_data['Volatility']
            ]).reshape(1, -1)
            
            # Scale features
            features_scaled = self.scaler.transform(features)
            
            # Make prediction
            prediction = self.model.predict(features_scaled)
            
            return prediction[0]
        except Exception as e:
            raise Exception(f"Error making prediction: {str(e)}")
    
    def plot_predictions(self, days=30):
        """
        Plot actual vs predicted prices for the test set.
        
        Args:
            days (int): Number of days to plot (default: 30)
        """
        try:
            if self.X_test is None:
                raise Exception("No test data available. Train model first.")
                
            test_pred = self.model.predict(self.X_test)
            
            plt.figure(figsize=(12, 6))
            plt.plot(self.y_test[:days], label='Actual Price', color='blue')
            plt.plot(test_pred[:days], label='Predicted Price', color='red', linestyle='--')
            plt.title(f'{self.ticker} Price Prediction')
            plt.xlabel('Days')
            plt.ylabel('Price (USD)')
            plt.legend()
            plt.grid(True)
            plt.show()
        except Exception as e:
            raise Exception(f"Error plotting predictions: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize predictor for Bitcoin
        predictor = AltcoinPricePredictor(ticker='BTC-USD')
        
        # Train model
        predictor.train_model()
        
        # Make prediction
        next_day_price = predictor.predict_next_day()
        print(f"Predicted price for next day: ${next_day_price:.2f}")
        
        # Plot predictions
        predictor.plot_predictions()
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
