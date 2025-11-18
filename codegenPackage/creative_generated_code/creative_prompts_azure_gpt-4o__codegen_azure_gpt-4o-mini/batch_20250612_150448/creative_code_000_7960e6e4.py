"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assettrackr.app
Prompt: Write Python code to simulate a disciplined value investing strategy using AI modeling techniques, as described by Grade World Investment Limited.
Generated: DETERMINISTIC_7960e6e4350a85e7
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
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import yfinance as yf
import logging

# Setting up logging for tracking the process
logging.basicConfig(level=logging.INFO)

class ValueInvestingAI:
    def __init__(self, stock_tickers, start_date, end_date):
        """
        Initializes the ValueInvestingAI class with stock tickers and date range.

        :param stock_tickers: List of stock tickers to analyze.
        :param start_date: Start date for historical data retrieval (format: 'YYYY-MM-DD').
        :param end_date: End date for historical data retrieval (format: 'YYYY-MM-DD').
        """
        self.stock_tickers = stock_tickers
        self.start_date = start_date
        self.end_date = end_date
        self.data = None
        self.model = RandomForestClassifier()

    def fetch_data(self):
        """
        Fetch historical stock price data from Yahoo Finance for the specified tickers.
        """
        try:
            self.data = yf.download(self.stock_tickers, start=self.start_date, end=self.end_date)
            logging.info("Data successfully fetched.")
        except Exception as e:
            logging.error(f"Error fetching data: {e}")
            raise

    def prepare_data(self):
        """
        Prepares the data for modeling by calculating relevant features and labels.
        """
        if self.data is None:
            logging.error("Data not fetched. Please call fetch_data() first.")
            return
        
        logging.info("Preparing data for modeling.")
        self.data['Returns'] = self.data['Adj Close'].pct_change()
        self.data['Volatility'] = self.data['Returns'].rolling(window=21).std()
        self.data['Momentum'] = self.data['Adj Close'].pct_change(periods=21)
        
        # Creating labels based on future returns
        self.data['Target'] = np.where(self.data['Returns'].shift(-1) > 0, 1, 0)
        self.data.dropna(inplace=True)

    def split_data(self):
        """
        Splits the data into training and test sets.
        :return: Features and labels for training and testing.
        """
        X = self.data[['Volatility', 'Momentum']]
        y = self.data['Target']

        return train_test_split(X, y, test_size=0.2, random_state=42)

    def train_model(self, X_train, y_train):
        """
        Trains the Random Forest Classifier model.

        :param X_train: Features for training.
        :param y_train: Labels for training.
        """
        self.model.fit(X_train, y_train)
        logging.info("Model training completed.")

    def evaluate_model(self, X_test, y_test):
        """
        Evaluates the trained model on the test set.

        :param X_test: Features for testing.
        :param y_test: Labels for testing.
        """
        y_pred = self.model.predict(X_test)
        report = classification_report(y_test, y_pred)
        logging.info("Model evaluation completed:")
        logging.info(report)

    def run(self):
        """
        Execute the full process of data fetching, preparation, training, and evaluation.
        """
        self.fetch_data()
        self.prepare_data()
        X_train, X_test, y_train, y_test = self.split_data()
        self.train_model(X_train, y_train)
        self.evaluate_model(X_test, y_test)


if __name__ == "__main__":
    # Example usage
    stock_tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']
    investing_strategy = ValueInvestingAI(stock_tickers, start_date='2020-01-01', end_date='2023-01-01')
    investing_strategy.run()
```
