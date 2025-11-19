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
# Import required libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import yfinance as yf
import matplotlib.pyplot as plt

# Define a function to fetch stock data
def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetches historical stock data from Yahoo Finance.

    Args:
        ticker (str): Stock ticker symbol.
        start_date (str): Start date in 'YYYY-MM-DD' format.
        end_date (str): End date in 'YYYY-MM-DD' format.

    Returns:
        pandas.DataFrame: Historical stock data.
    """
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        return data
    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return None

# Define a function to calculate fundamental stock metrics
def calculate_fundamental_metrics(data):
    """
    Calculates fundamental stock metrics.

    Args:
        data (pandas.DataFrame): Historical stock data.

    Returns:
        pandas.DataFrame: Data with additional fundamental metrics.
    """
    data['market_cap'] = data['Close'] * data['Volume']
    data['price_to_earnings'] = data['Close'] / data['Open']
    data['moving_average_50'] = data['Close'].rolling(window=50).mean()
    data['moving_average_200'] = data['Close'].rolling(window=200).mean()
    return data

# Define a function to train a linear regression model
def train_model(data):
    """
    Trains a linear regression model to predict stock prices.

    Args:
        data (pandas.DataFrame): Data with fundamental metrics.

    Returns:
        sklearn.linear_model.LinearRegression: Trained model.
    """
    try:
        X = data[['market_cap', 'price_to_earnings', 'moving_average_50', 'moving_average_200']]
        y = data['Close']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LinearRegression()  
        model.fit(X_train, y_train)
        return model, X_test, y_test
    except Exception as e:
        print(f"Error training model: {e}")
        return None, None, None

# Define a function to evaluate model performance
def evaluate_model(model, X_test, y_test):
    """
    Evaluates the performance of the linear regression model.

    Args:
        model (sklearn.linear_model.LinearRegression): Trained model.
        X_test (pandas.DataFrame): Test data features.
        y_test (pandas.Series): Test data target variable.

    Returns:
        dict: Model performance metrics.
    """
    try:
        y_pred = model.predict(X_test)
        mae = metrics.mean_absolute_error(y_test, y_pred)
        mse = metrics.mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        return {'MAE': mae, 'MSE': mse, 'RMSE': rmse}
    except Exception as e:
        print(f"Error evaluating model: {e}")
        return None

# Define a function to simulate a systematic value investing strategy
def simulate_investing_strategy(ticker, start_date, end_date):
    """
    Simulates a systematic value investing strategy.

    Args:
        ticker (str): Stock ticker symbol.
        start_date (str): Start date in 'YYYY-MM-DD' format.
        end_date (str): End date in 'YYYY-MM-DD' format.
    """
    data = fetch_stock_data(ticker, start_date, end_date)
    if data is not None:
        data = calculate_fundamental_metrics(data)
        model, X_test, y_test = train_model(data)
        if model is not None:
            performance_metrics = evaluate_model(model, X_test, y_test)
            if performance_metrics is not None:
                print(f"Performance Metrics: {performance_metrics}")
                predicted_prices = model.predict(data[['market_cap', 'price_to_earnings', 'moving_average_50', 'moving_average_200']])
                plt.plot(data['Close'], label='Actual Price')
                plt.plot(predicted_prices, label='Predicted Price')
                plt.legend()
                plt.show()

# Example usage
if __name__ == "__main__":
    ticker = 'AAPL'
    start_date = '2010-01-01'
    end_date = '2022-02-26'
    simulate_investing_strategy(ticker, start_date, end_date)
```
