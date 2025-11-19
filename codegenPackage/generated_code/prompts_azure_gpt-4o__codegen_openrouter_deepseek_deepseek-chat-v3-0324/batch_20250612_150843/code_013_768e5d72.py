"""
Generated Code Metadata:
========================
Original URL: https://tradegpt360-evix.com
Prompt: Create a Python script to analyze cryptocurrency price movements and predict market trends using AI algorithms, inspired by the TradeGPT 360 Evix app.
Generated: DETERMINISTIC_768e5d728524df63
Batch ID: 20250612_150843
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
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
import yfinance as yf
import talib
import warnings
from datetime import datetime, timedelta

warnings.filterwarnings('ignore')

class CryptoTrendAnalyzer:
    """
    A class to analyze cryptocurrency price movements and predict market trends using AI algorithms.
    """
    
    def __init__(self, ticker='BTC-USD', start_date=None, end_date=None):
        """
        Initialize the analyzer with cryptocurrency ticker and date range.
        
        Args:
            ticker (str): Cryptocurrency ticker symbol (default: 'BTC-USD')
            start_date (str): Start date in YYYY-MM-DD format (default: 1 year ago)
            end_date (str): End date in YYYY-MM-DD format (default: today)
        """
        self.ticker = ticker
        self.end_date = end_date or datetime.now().strftime('%Y-%m-%d')
        self.start_date = start_date or (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
        self.data = None
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        self.model = None
        self.history = None
        
    def fetch_data(self):
        """
        Fetch historical price data from Yahoo Finance.
        """
        try:
            self.data = yf.download(self.ticker, start=self.start_date, end=self.end_date)
            if self.data.empty:
                raise ValueError("No data returned for the given ticker and date range.")
            self._preprocess_data()
            print(f"Successfully fetched data for {self.ticker} from {self.start_date} to {self.end_date}")
        except Exception as e:
            print(f"Error fetching data: {e}")
            raise
    
    def _preprocess_data(self):
        """
        Preprocess the data by calculating technical indicators and cleaning.
        """
        # Calculate technical indicators
        self.data['SMA_50'] = talib.SMA(self.data['Close'], timeperiod=50)
        self.data['SMA_200'] = talib.SMA(self.data['Close'], timeperiod=200)
        self.data['RSI'] = talib.RSI(self.data['Close'], timeperiod=14)
        self.data['MACD'], self.data['MACD_signal'], _ = talib.MACD(self.data['Close'])
        
        # Remove NaN values
        self.data.dropna(inplace=True)
        
        # Normalize the data
        self.data_scaled = self.scaler.fit_transform(self.data[['Close', 'SMA_50', 'SMA_200', 'RSI', 'MACD']])
    
    def create_dataset(self, look_back=60):
        """
        Create time-series dataset for LSTM model.
        
        Args:
            look_back (int): Number of previous time steps to use for prediction
        """
        X, y = [], []
        for i in range(look_back, len(self.data_scaled)):
            X.append(self.data_scaled[i-look_back:i, :])
            y.append(self.data_scaled[i, 0])  # Predict Close price
        
        X, y = np.array(X), np.array(y)
        
        # Split into train and test sets
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, shuffle=False)
        
        return X, y
    
    def build_model(self):
        """
        Build and compile the LSTM model.
        """
        self.model = Sequential([
            LSTM(units=50, return_sequences=True, input_shape=(self.X_train.shape[1], self.X_train.shape[2])),
            Dropout(0.2),
            LSTM(units=50, return_sequences=False),
            Dropout(0.2),
            Dense(units=25),
            Dense(units=1)
        ])
        
        self.model.compile(optimizer='adam', loss='mean_squared_error')
    
    def train_model(self, epochs=100, batch_size=32):
        """
        Train the LSTM model.
        
        Args:
            epochs (int): Number of training epochs
            batch_size (int): Batch size for training
        """
        early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
        
        self.history = self.model.fit(
            self.X_train, self.y_train,
            epochs=epochs,
            batch_size=batch_size,
            validation_split=0.1,
            callbacks=[early_stopping],
            verbose=1
        )
    
    def evaluate_model(self):
        """
        Evaluate the model on test data and return predictions.
        """
        predictions = self.model.predict(self.X_test)
        
        # Inverse transform predictions and actual values
        dummy = np.zeros((len(predictions), self.data_scaled.shape[1]))
        dummy[:, 0] = predictions.flatten()
        predictions = self.scaler.inverse_transform(dummy)[:, 0]
        
        dummy[:, 0] = self.y_test.flatten()
        y_test = self.scaler.inverse_transform(dummy)[:, 0]
        
        # Calculate RMSE
        rmse = np.sqrt(mean_squared_error(y_test, predictions))
        print(f"Test RMSE: {rmse:.2f}")
        
        return predictions, y_test
    
    def predict_future(self, days=7, look_back=60):
        """
        Predict future price movements.
        
        Args:
            days (int): Number of days to predict
            look_back (int): Number of previous time steps to use for prediction
        """
        # Use the most recent data for prediction
        last_sequence = self.data_scaled[-look_back:]
        
        predictions = []
        for _ in range(days):
            # Reshape the input data
            x_input = last_sequence.reshape((1, look_back, self.data_scaled.shape[1]))
            
            # Make prediction
            pred = self.model.predict(x_input, verbose=0)
            
            # Create a new row with the prediction and zeros for other features
            new_row = np.zeros((1, self.data_scaled.shape[1]))
            new_row[0, 0] = pred[0, 0]
            
            # Update the sequence
            last_sequence = np.append(last_sequence[1:], new_row, axis=0)
            
            # Inverse transform the prediction
            dummy = np.zeros((1, self.data_scaled.shape[1]))
            dummy[0, 0] = pred[0, 0]
            pred_price = self.scaler.inverse_transform(dummy)[0, 0]
            
            predictions.append(pred_price)
        
        return predictions
    
    def plot_results(self, predictions, y_test):
        """
        Plot actual vs predicted prices.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(y_test, label='Actual Price')
        plt.plot(predictions, label='Predicted Price')
        plt.title(f'{self.ticker} Price Prediction')
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.legend()
        plt.show()
    
    def plot_training_history(self):
        """
        Plot training and validation loss history.
        """
        if self.history is None:
            print("Model hasn't been trained yet.")
            return
        
        plt.figure(figsize=(12, 6))
        plt.plot(self.history.history['loss'], label='Training Loss')
        plt.plot(self.history.history['val_loss'], label='Validation Loss')
        plt.title('Model Loss')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.legend()
        plt.show()

def main():
    """
    Main function to demonstrate the CryptoTrendAnalyzer.
    """
    try:
        # Initialize analyzer
        analyzer = CryptoTrendAnalyzer(ticker='BTC-USD')
        
        # Fetch and preprocess data
        analyzer.fetch_data()
        
        # Create dataset
        analyzer.create_dataset(look_back=60)
        
        # Build and train model
        analyzer.build_model()
        analyzer.train_model(epochs=50, batch_size=32)
        
        # Evaluate model
        predictions, y_test = analyzer.evaluate_model()
        analyzer.plot_results(predictions, y_test)
        analyzer.plot_training_history()
        
        # Predict future prices
        future_predictions = analyzer.predict_future(days=7)
        print(f"Next 7 days predicted prices: {future_predictions}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
