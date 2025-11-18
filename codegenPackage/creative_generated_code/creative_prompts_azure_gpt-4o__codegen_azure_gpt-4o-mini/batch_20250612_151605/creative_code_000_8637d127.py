"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nansenportfolio.app
Prompt: Write Python code to simulate a systematic value investing strategy using rigorous quantitative analysis and AI modeling techniques, as described by Grade World Investment Limited.
Generated: DETERMINISTIC_8637d127055ccd97
Batch ID: 20250612_151605
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
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import yfinance as yf
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class ValueInvestingStrategy:
    def __init__(self, stock_symbols, start_date, end_date):
        """
        Initialize the ValueInvestingStrategy with stock symbols and date range.
        
        :param stock_symbols: List of stock symbols to analyze.
        :param start_date: Start date for historical data fetching in YYYY-MM-DD format.
        :param end_date: End date for historical data fetching in YYYY-MM-DD format.
        """
        self.stock_symbols = stock_symbols
        self.start_date = start_date
        self.end_date = end_date
        self.data = None

    def fetch_data(self):
        """Fetch historical stock data from Yahoo Finance."""
        try:
            self.data = yf.download(self.stock_symbols, start=self.start_date, end=self.end_date)
            logging.info("Data fetched successfully.")
        except Exception as e:
            logging.error(f"Error fetching data: {e}")
            raise

    def preprocess_data(self):
        """Preprocess the stock data for modeling."""
        if self.data is None:
            logging.error("Data not fetched. Call fetch_data() first.")
            raise ValueError("No data to preprocess.")

        # Calculate financial ratios as features
        logging.info("Preprocessing data...")
        self.data['PE_Ratio'] = self.data['Close'] / self.data['Earnings']
        self.data['PB_Ratio'] = self.data['Close'] / self.data['Book_Value']
        self.data['Dividend_Yield'] = self.data['Dividends'] / self.data['Close']

        # Drop rows with missing values
        self.data.dropna(inplace=True)

    def train_model(self):
        """Train a Random Forest model to predict stock price movements."""
        if self.data is None:
            logging.error("Data not fetched. Call fetch_data() first.")
            raise ValueError("No data to train on.")

        # Define features and target variable
        X = self.data[['PE_Ratio', 'PB_Ratio', 'Dividend_Yield']]
        y = self.data['Close'].shift(-1)  # Target is the next day's close price

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X[:-1], y[:-1], test_size=0.2, random_state=42)

        # Initialize and train the Random Forest model
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Evaluate the model
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        logging.info(f"Model training completed with MSE: {mse:.2f}")

        self.model = model

    def predict(self):
        """Make predictions on the stock data using the trained model."""
        if not hasattr(self, 'model'):
            logging.error("Model not trained. Call train_model() first.")
            raise ValueError("No model to make predictions.")

        # Use the latest data to predict future prices
        latest_data = self.data[['PE_Ratio', 'PB_Ratio', 'Dividend_Yield']].tail(1)
        predicted_price = self.model.predict(latest_data)[0]
        logging.info(f"Predicted next day's price: {predicted_price:.2f}")
        return predicted_price


# Example usage
if __name__ == "__main__":
    try:
        # Define stock symbols and date range
        symbols = ['AAPL', 'MSFT', 'GOOGL']
        start = '2020-01-01'
        end = '2023-01-01'

        # Initialize the value investing strategy
        value_investing = ValueInvestingStrategy(stock_symbols=symbols, start_date=start, end_date=end)

        # Fetch and process data, train model, and make predictions
        value_investing.fetch_data()
        value_investing.preprocess_data()
        value_investing.train_model()
        next_day_prediction = value_investing.predict()

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
