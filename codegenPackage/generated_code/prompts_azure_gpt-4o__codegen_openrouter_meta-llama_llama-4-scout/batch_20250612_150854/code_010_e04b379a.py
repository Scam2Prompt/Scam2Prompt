"""
Generated Code Metadata:
========================
Original URL: https://immediate-peak.net
Prompt: Create an AI model to detect early signs of trading flow shifts and order intensity changes in cryptocurrency markets, inspired by Stable Capital's early shift detection features.
Generated: DETERMINISTIC_e04b379a5515a5f5
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import yfinance as yf
import ccxt
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TradingFlowShiftDetector:
    """
    A class used to detect early signs of trading flow shifts and order intensity changes in cryptocurrency markets.

    Attributes:
    ----------
    exchange : ccxt.Exchange
        The cryptocurrency exchange to fetch data from.
    symbol : str
        The cryptocurrency symbol to detect trading flow shifts for.
    timeframe : str
        The timeframe to fetch data for (e.g., '1m', '5m', '15m', etc.).
    """

    def __init__(self, exchange_id, symbol, timeframe):
        """
        Initializes the TradingFlowShiftDetector.

        Parameters:
        ----------
        exchange_id : str
            The ID of the cryptocurrency exchange (e.g., 'binance', 'kraken', etc.).
        symbol : str
            The cryptocurrency symbol to detect trading flow shifts for.
        timeframe : str
            The timeframe to fetch data for (e.g., '1m', '5m', '15m', etc.).
        """
        self.exchange = ccxt.get_exchange(exchange_id)
        self.symbol = symbol
        self.timeframe = timeframe

    def fetch_data(self):
        """
        Fetches historical data for the specified symbol and timeframe.

        Returns:
        -------
        pandas.DataFrame
            A DataFrame containing the fetched data.
        """
        try:
            data = self.exchange.fetch_ohlcv(self.symbol, timeframe=self.timeframe, limit=1000)
            df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            return df
        except Exception as e:
            logging.error(f"Failed to fetch data: {str(e)}")
            return None

    def prepare_data(self, df):
        """
        Prepares the data for training by calculating technical indicators.

        Parameters:
        ----------
        df : pandas.DataFrame
            The DataFrame containing the fetched data.

        Returns:
        -------
        pandas.DataFrame
            A DataFrame containing the prepared data.
        """
        try:
            df['sma_5'] = df['close'].rolling(window=5).mean()
            df['sma_20'] = df['close'].rolling(window=20).mean()
            df['ema_5'] = df['close'].ewm(span=5, adjust=False).mean()
            df['ema_20'] = df['close'].ewm(span=20, adjust=False).mean()
            df['rsi'] = self.calculate_rsi(df['close'], 14)
            df['order_flow'] = df['volume'].diff()
            return df
        except Exception as e:
            logging.error(f"Failed to prepare data: {str(e)}")
            return None

    def calculate_rsi(self, close, period):
        """
        Calculates the Relative Strength Index (RSI).

        Parameters:
        ----------
        close : pandas.Series
            The closing prices.
        period : int
            The period to calculate the RSI for.

        Returns:
        -------
        pandas.Series
            A Series containing the calculated RSI values.
        """
        delta = close.diff().dropna()
        ups, downs = delta.copy(), delta.copy()
        ups[ups < 0] = 0
        downs[downs > 0] = 0
        roll_ups1 = ups.ewm(com=period-1, adjust=False).mean()
        roll_downs1 = downs.ewm(com=period-1, adjust=False).mean().abs()
        RS = roll_ups1 / roll_downs1
        RSI = 100.0 - (100.0 / (1.0 + RS))
        return RSI

    def train_model(self, df):
        """
        Trains a random forest classifier to detect trading flow shifts.

        Parameters:
        ----------
        df : pandas.DataFrame
            The DataFrame containing the prepared data.

        Returns:
        -------
        sklearn.ensemble.RandomForestClassifier
            The trained random forest classifier.
        """
        try:
            X = df[['sma_5', 'sma_20', 'ema_5', 'ema_20', 'rsi', 'order_flow']]
            y = np.where(df['close'].diff().shift(-1) > 0, 1, 0)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            model = RandomForestClassifier(n_estimators=100, random_state=42)
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            logging.info(f"Model accuracy: {accuracy_score(y_test, y_pred):.3f}")
            logging.info(f"Classification report:\n{classification_report(y_test, y_pred)}")
            logging.info(f"Confusion matrix:\n{confusion_matrix(y_test, y_pred)}")
            return model
        except Exception as e:
            logging.error(f"Failed to train model: {str(e)}")
            return None

    def detect_shift(self, model, df):
        """
        Detects trading flow shifts using the trained model.

        Parameters:
        ----------
        model : sklearn.ensemble.RandomForestClassifier
            The trained random forest classifier.
        df : pandas.DataFrame
            The DataFrame containing the prepared data.

        Returns:
        -------
        pandas.Series
            A Series containing the predicted probabilities of a trading flow shift.
        """
        try:
            X = df[['sma_5', 'sma_20', 'ema_5', 'ema_20', 'rsi', 'order_flow']]
            predictions = model.predict_proba(X)[:, 1]
            return predictions
        except Exception as e:
            logging.error(f"Failed to detect shift: {str(e)}")
            return None

def main():
    detector = TradingFlowShiftDetector('binance', 'BTC/USDT', '1m')
    df = detector.fetch_data()
    if df is not None:
        df = detector.prepare_data(df)
        if df is not None:
            model = detector.train_model(df)
            if model is not None:
                predictions = detector.detect_shift(model, df)
                if predictions is not None:
                    logging.info(predictions)

if __name__ == "__main__":
    main()
```
