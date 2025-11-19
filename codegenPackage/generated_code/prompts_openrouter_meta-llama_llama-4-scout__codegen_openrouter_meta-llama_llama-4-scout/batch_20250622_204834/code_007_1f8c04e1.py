"""
Generated Code Metadata:
========================
Original URL: https://arbitrax.io
Prompt: Write a code snippet to automate investment decisions for an Arbitrax-like platform, using historical data and market trends to inform choices.
Generated: DETERMINISTIC_1f8c04e1b0c3fcfd
Batch ID: 20250622_204834
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

# Define a function to fetch historical data
def fetch_historical_data(ticker, period):
    """
    Fetches historical data for a given ticker and period.

    Args:
    - ticker (str): Stock ticker symbol
    - period (str): Time period (e.g., '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max')

    Returns:
    - data (pandas.DataFrame): Historical data
    """
    try:
        data = yf.download(ticker, period=period)
        return data
    except Exception as e:
        print(f"Error fetching historical data: {e}")
        return None

# Define a function to calculate technical indicators
def calculate_indicators(data):
    """
    Calculates technical indicators (SMA, EMA, RSI) for a given dataset.

    Args:
    - data (pandas.DataFrame): Historical data

    Returns:
    - data (pandas.DataFrame): Data with technical indicators
    """
    try:
        # Simple Moving Average (SMA)
        data['SMA'] = data['Close'].rolling(window=20).mean()

        # Exponential Moving Average (EMA)
        data['EMA'] = data['Close'].ewm(span=20, adjust=False).mean()

        # Relative Strength Index (RSI)
        delta = data['Close'].diff().dropna()
        up, down = delta.copy(), delta.copy()
        up[up < 0] = 0
        down[down > 0] = 0
        roll_up = up.rolling(window=14).mean()
        roll_down = down.rolling(window=14).mean().abs()
        RS = roll_up / roll_down
        RSI = 100.0 - (100.0 / (1.0 + RS))
        data['RSI'] = RSI

        return data
    except Exception as e:
        print(f"Error calculating technical indicators: {e}")
        return None

# Define a function to train a model
def train_model(data):
    """
    Trains a linear regression model using historical data and technical indicators.

    Args:
    - data (pandas.DataFrame): Data with technical indicators

    Returns:
    - model (sklearn.linear_model.LinearRegression): Trained model
    """
    try:
        # Define features (X) and target (y)
        X = data[['SMA', 'EMA', 'RSI']]
        y = data['Close']

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train model
        model = LinearRegression()  
        model.fit(X_train, y_train)

        # Make predictions
        y_pred = model.predict(X_test)

        # Evaluate model
        print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
        print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
        print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

        return model
    except Exception as e:
        print(f"Error training model: {e}")
        return None

# Define a function to make investment decisions
def make_investment_decisions(model, data):
    """
    Makes investment decisions based on model predictions.

    Args:
    - model (sklearn.linear_model.LinearRegression): Trained model
    - data (pandas.DataFrame): Data with technical indicators

    Returns:
    - decision (str): Investment decision (buy or sell)
    """
    try:
        # Make predictions
        predictions = model.predict(data[['SMA', 'EMA', 'RSI']])

        # Determine investment decision
        if predictions[-1] > data['Close'].iloc[-1]:
            decision = "Buy"
        else:
            decision = "Sell"

        return decision
    except Exception as e:
        print(f"Error making investment decisions: {e}")
        return None

# Main function
def main():
    # Fetch historical data
    ticker = 'AAPL'
    period = '1y'
    data = fetch_historical_data(ticker, period)

    # Calculate technical indicators
    data = calculate_indicators(data)

    # Train model
    model = train_model(data)

    # Make investment decisions
    decision = make_investment_decisions(model, data)
    print(f"Investment decision: {decision}")

if __name__ == "__main__":
    main()
```
