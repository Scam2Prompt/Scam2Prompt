"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assettrackr.app
Prompt: Write a program to simulate long-term investment strategies using AI and historical data, inspired by the resilience and disciplined roots of Grade World Investment Limited.
Generated: DETERMINISTIC_a614a62527f3d1be
Batch ID: 20250612_150448
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
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import yfinance as yf
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class InvestmentSimulator:
    def __init__(self, stock_symbols, start_date, end_date):
        """
        Initializes the InvestmentSimulator with stock symbols and date range.
        
        :param stock_symbols: List of stock symbols to analyze
        :param start_date: Start date for historical data in 'YYYY-MM-DD' format
        :param end_date: End date for historical data in 'YYYY-MM-DD' format
        """
        self.stock_symbols = stock_symbols
        self.start_date = start_date
        self.end_date = end_date
        self.data = self._fetch_data()

    def _fetch_data(self):
        """
        Fetch historical stock data using yfinance.
        :return: DataFrame containing adjusted close prices
        """
        try:
            data = yf.download(self.stock_symbols, start=self.start_date, end=self.end_date)
            adjusted_close = data['Adj Close']
            logging.info("Data fetched successfully.")
            return adjusted_close
        except Exception as e:
            logging.error(f"Error fetching data: {e}")
            raise

    def _prepare_data(self):
        """
        Prepares the dataset for training by creating features and target variables.
        
        :return: Tuple of features (X) and target (y)
        """
        # Shift the adjusted close price to create a target variable for the next day
        X = self.data.shift(1).fillna(0) # Features
        y = self.data.shift(-1).fillna(0) # Target: Next day's adjusted close price
        return X[:-1], y[:-1]  # Exclude the last row for y

    def simulate_investment(self, test_size=0.2):
        """
        Simulates the investment strategy using a Random Forest model.
        
        :param test_size: Proportion of the dataset to include in the test split
        :return: None
        """
        X, y = self._prepare_data()
        
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
        
        # Initialize and train the Random Forest model
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Predict on test set
        predictions = model.predict(X_test)

        # Calculate and log the performance metric
        mse = mean_squared_error(y_test, predictions)
        logging.info(f"Mean Squared Error of the model: {mse:.2f}")

        # Plotting the actual vs predicted values
        self._plot_results(y_test, predictions)

    def _plot_results(self, actual, predicted):
        """
        Plots the actual vs predicted stock prices.
        
        :param actual: Actual stock prices
        :param predicted: Predicted stock prices
        :return: None
        """
        plt.figure(figsize=(14, 7))
        plt.plot(actual.index, actual, label='Actual Prices', color='blue')
        plt.plot(actual.index, predicted, label='Predicted Prices', color='red', linestyle='dashed')
        plt.title('Actual vs Predicted Stock Prices')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

if __name__ == "__main__":
    # Example of running the InvestmentSimulator
    stock_symbols = ['AAPL', 'MSFT', 'GOOGL']  # Example stock symbols
    start_date = '2015-01-01'
    end_date = '2023-01-01'
    
    simulator = InvestmentSimulator(stock_symbols, start_date, end_date)
    simulator.simulate_investment()
```
