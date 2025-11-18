"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-urex-gpt.com
Prompt: Generate a Python script for backtesting crypto trading strategies using AI algorithms to identify patterns and predict price movements, similar to the Bit Urex Ai platform.
Generated: DETERMINISTIC_f10423d9ae98ec92
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import yfinance as yf
import logging

# Set up logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CryptoBacktester:
    def __init__(self, symbol: str, start_date: str, end_date: str):
        """
        Initialize the backtester with the cryptocurrency symbol and date range.

        :param symbol: Cryptocurrency symbol (e.g., 'BTC-USD')
        :param start_date: Start date for historical data (YYYY-MM-DD)
        :param end_date: End date for historical data (YYYY-MM-DD)
        """
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.data = None
        self.model = None

    def fetch_data(self):
        """Fetch historical price data using yfinance."""
        try:
            self.data = yf.download(self.symbol, start=self.start_date, end=self.end_date)
            logging.info(f"Data fetched for {self.symbol} from {self.start_date} to {self.end_date}.")
        except Exception as e:
            logging.error(f"Error fetching data: {e}")
            raise

    def preprocess_data(self):
        """Preprocess the data for training the model."""
        if self.data is None:
            logging.error("Data not fetched. Call fetch_data() before preprocessing.")
            return
        
        # Feature engineering
        self.data['Returns'] = self.data['Close'].pct_change()
        self.data['Volatility'] = self.data['Returns'].rolling(window=5).std()
        self.data['SMA'] = self.data['Close'].rolling(window=5).mean()
        self.data.dropna(inplace=True)

        X = self.data[['Volatility', 'SMA']].values
        y = self.data['Close'].shift(-1).dropna().values
        
        # Align X and y
        X = X[:-1]
        
        return X, y

    def split_data(self, X, y):
        """Split the data into training and testing sets."""
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def train_model(self, X_train, y_train):
        """Train the AI model using a Random Forest Regressor."""
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)
        logging.info("Model training complete.")

    def predict(self, X_test):
        """Make predictions using the trained model."""
        return self.model.predict(X_test)

    def evaluate_model(self, y_test, predictions):
        """Evaluate model performance using Mean Squared Error (MSE)."""
        mse = mean_squared_error(y_test, predictions)
        logging.info(f"Model Mean Squared Error: {mse:.4f}")
        return mse

    def plot_results(self, y_test, predictions):
        """Plot actual vs predicted values."""
        plt.figure(figsize=(14, 7))
        plt.plot(y_test, label='Actual Prices', color='blue')
        plt.plot(predictions, label='Predicted Prices', color='orange')
        plt.title(f'{self.symbol} Price Prediction')
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

    def run_backtest(self):
        """Run the backtesting process."""
        self.fetch_data()
        X, y = self.preprocess_data()
        X_train, X_test, y_train, y_test = self.split_data(X, y)
        self.train_model(X_train, y_train)
        predictions = self.predict(X_test)
        self.evaluate_model(y_test, predictions)
        self.plot_results(y_test, predictions)

if __name__ == "__main__":
    # Example usage
    backtester = CryptoBacktester(symbol='BTC-USD', start_date='2020-01-01', end_date='2023-01-01')
    backtester.run_backtest()
```
