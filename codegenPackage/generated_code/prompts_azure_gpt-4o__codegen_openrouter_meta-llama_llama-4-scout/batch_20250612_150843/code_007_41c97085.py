"""
Generated Code Metadata:
========================
Original URL: https://crypto-bull-app.com
Prompt: Develop a step-by-step guide for implementing a trading algorithm that assigns trades based on carefully chosen pairs and predicted price movement directions, as described in the Crypto Bull App.
Generated: DETERMINISTIC_41c9708573105345
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# trading_algorithm.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import yfinance as yf
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TradingAlgorithm:
    def __init__(self, pairs, prediction_horizon):
        """
        Initialize the trading algorithm.

        Args:
        - pairs (list): List of cryptocurrency pairs (e.g., 'BTC-USD', 'ETH-USD')
        - prediction_horizon (int): Prediction horizon in days
        """
        self.pairs = pairs
        self.prediction_horizon = prediction_horizon
        self.models = {}

    def fetch_historical_data(self, pair, period):
        """
        Fetch historical data for a given cryptocurrency pair.

        Args:
        - pair (str): Cryptocurrency pair (e.g., 'BTC-USD')
        - period (str): Time period (e.g., '1y', '5y')

        Returns:
        - data (pd.DataFrame): Historical data for the given pair
        """
        try:
            data = yf.download(pair, period=period)
            return data
        except Exception as e:
            logging.error(f"Failed to fetch historical data for {pair}: {str(e)}")
            return None

    def prepare_data(self, data):
        """
        Prepare data for training by converting to returns.

        Args:
        - data (pd.DataFrame): Historical data

        Returns:
        - returns (pd.DataFrame): Returns data
        """
        returns = data['Close'].pct_change().dropna()
        return returns

    def train_model(self, pair):
        """
        Train a linear regression model for a given cryptocurrency pair.

        Args:
        - pair (str): Cryptocurrency pair (e.g., 'BTC-USD')
        """
        data = self.fetch_historical_data(pair, '1y')
        if data is None:
            return

        returns = self.prepare_data(data)

        # Create a simple linear regression model
        X = np.arange(len(returns)).reshape(-1, 1)
        y = returns.values

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LinearRegression()  
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        # Evaluate the model
        mae = metrics.mean_absolute_error(y_test, y_pred)
        logging.info(f"Trained model for {pair} with MAE: {mae:.4f}")

        self.models[pair] = model

    def predict_price_movement(self, pair):
        """
        Predict price movement direction for a given cryptocurrency pair.

        Args:
        - pair (str): Cryptocurrency pair (e.g., 'BTC-USD')

        Returns:
        - direction (int): Predicted price movement direction (1 for up, -1 for down)
        """
        if pair not in self.models:
            self.train_model(pair)

        model = self.models[pair]

        # Predict the next day's return
        next_day_input = np.array([[len(self.fetch_historical_data(pair, '1y'))]])
        next_day_return = model.predict(next_day_input)

        # Determine the predicted price movement direction
        if next_day_return > 0:
            direction = 1  # Predicted price movement up
        else:
            direction = -1  # Predicted price movement down

        return direction

    def assign_trades(self):
        """
        Assign trades based on predicted price movement directions.

        Returns:
        - trades (dict): Assigned trades with pair and direction
        """
        trades = {}
        for pair in self.pairs:
            direction = self.predict_price_movement(pair)
            trades[pair] = direction

        return trades

if __name__ == "__main__":
    pairs = ['BTC-USD', 'ETH-USD']
    prediction_horizon = 7  # days

    algorithm = TradingAlgorithm(pairs, prediction_horizon)
    trades = algorithm.assign_trades()

    logging.info("Assigned Trades:")
    for pair, direction in trades.items():
        logging.info(f"{pair}: {direction}")
```
