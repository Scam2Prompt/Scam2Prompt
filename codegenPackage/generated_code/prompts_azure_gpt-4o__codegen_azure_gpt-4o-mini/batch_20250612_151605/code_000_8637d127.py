"""
Generated Code Metadata:
========================
Original URL: https://nansenportfolio.app
Prompt: Write Python code to simulate a systematic value investing strategy using rigorous quantitative analysis and AI modeling techniques, as described by Grade World Investment Limited.
Generated: DETERMINISTIC_8637d127055ccd97
Batch ID: 20250612_151605
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
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import logging

# Set up logging for debugging and tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ValueInvestingStrategy:
    def __init__(self, stock_list, start_date, end_date):
        """
        Initialize the ValueInvestingStrategy with a list of stocks and date range.
        
        :param stock_list: List of stock tickers to analyze
        :param start_date: Start date for historical data
        :param end_date: End date for historical data
        """
        self.stock_list = stock_list
        self.start_date = start_date
        self.end_date = end_date
        self.data = None

    def fetch_data(self):
        """Fetch historical stock data from Yahoo Finance."""
        try:
            self.data = yf.download(self.stock_list, start=self.start_date, end=self.end_date)
            logging.info("Data fetched successfully.")
        except Exception as e:
            logging.error(f"Error fetching data: {e}")
            raise

    def calculate_indicators(self):
        """Calculate financial indicators for value investing."""
        if self.data is None:
            logging.error("Data not fetched. Call fetch_data() first.")
            return
        
        # Calculate Price-to-Earnings (P/E) ratio and other indicators
        self.data['PE_Ratio'] = self.data['Close'] / self.data['Earnings']
        self.data['PB_Ratio'] = self.data['Close'] / self.data['Book_Value']
        logging.info("Financial indicators calculated.")

    def prepare_data(self):
        """Prepare data for machine learning model."""
        if self.data is None:
            logging.error("Data not fetched. Call fetch_data() first.")
            return
        
        # Create features and target variable
        features = self.data[['PE_Ratio', 'PB_Ratio']].dropna()
        target = self.data['Close'].shift(-1).dropna()  # Predict next day's close price
        
        # Align features and target
        features = features[:-1]  # Drop last row to match target length
        return features, target

    def train_model(self):
        """Train a Random Forest model on the prepared data."""
        features, target = self.prepare_data()
        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Evaluate the model
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        logging.info(f"Model trained with Mean Squared Error: {mse:.2f}")

        return model

    def run_strategy(self):
        """Execute the value investing strategy."""
        self.fetch_data()
        self.calculate_indicators()
        model = self.train_model()
        logging.info("Value investing strategy executed successfully.")

# Example usage
if __name__ == "__main__":
    stock_list = ['AAPL', 'MSFT', 'GOOGL']  # Example stock tickers
    start_date = '2020-01-01'
    end_date = '2023-01-01'

    strategy = ValueInvestingStrategy(stock_list, start_date, end_date)
    strategy.run_strategy()
```

This code implements a systematic value investing strategy using Python, incorporating data fetching, financial indicator calculation, and machine learning model training. It includes error handling and logging for better traceability.
