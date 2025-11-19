"""
Generated Code Metadata:
========================
Original URL: https://assettrackr.app
Prompt: Write Python code to simulate a disciplined value investing strategy using AI modeling techniques, as described by Grade World Investment Limited.
Generated: DETERMINISTIC_7960e6e4350a85e7
Batch ID: 20250612_150448
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

# Define a function to fetch stock data
def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetches historical stock data from Yahoo Finance.

    Args:
    - ticker (str): Stock ticker symbol
    - start_date (str): Start date in 'YYYY-MM-DD' format
    - end_date (str): End date in 'YYYY-MM-DD' format

    Returns:
    - data (pd.DataFrame): Historical stock data
    """
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        return data
    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return None

# Define a function to calculate intrinsic value
def calculate_intrinsic_value(data):
    """
    Calculates the intrinsic value of a stock using a simple AI model.

    Args:
    - data (pd.DataFrame): Historical stock data

    Returns:
    - intrinsic_value (float): Intrinsic value of the stock
    """
    try:
        # Define features (X) and target variable (y)
        X = data[['Open', 'High', 'Low', 'Volume']]
        y = data['Close']

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create and train a linear regression model
        model = LinearRegression()  
        model.fit(X_train, y_train)

        # Make predictions on the test set
        y_pred = model.predict(X_test)

        # Evaluate the model
        mae = metrics.mean_absolute_error(y_test, y_pred)
        print(f"Mean Absolute Error: {mae}")

        # Calculate intrinsic value as the predicted closing price
        intrinsic_value = model.predict(data[['Open', 'High', 'Low', 'Volume']].iloc[-1].values.reshape(1, -1))[0]
        return intrinsic_value
    except Exception as e:
        print(f"Error calculating intrinsic value: {e}")
        return None

# Define a function to determine if a stock is undervalued
def is_undervalued(intrinsic_value, current_price):
    """
    Determines if a stock is undervalued based on its intrinsic value.

    Args:
    - intrinsic_value (float): Intrinsic value of the stock
    - current_price (float): Current market price of the stock

    Returns:
    - bool: True if the stock is undervalued, False otherwise
    """
    try:
        if intrinsic_value > current_price:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error determining if stock is undervalued: {e}")
        return None

# Main function
def main():
    # Define stock ticker and date range
    ticker = 'AAPL'
    start_date = '2020-01-01'
    end_date = '2022-12-31'

    # Fetch stock data
    data = fetch_stock_data(ticker, start_date, end_date)

    # Calculate intrinsic value
    intrinsic_value = calculate_intrinsic_value(data)

    # Get current market price
    current_price = data['Close'].iloc[-1]

    # Determine if the stock is undervalued
    undervalued = is_undervalued(intrinsic_value, current_price)

    # Print results
    print(f"Stock: {ticker}")
    print(f"Intrinsic Value: {intrinsic_value}")
    print(f"Current Price: {current_price}")
    print(f"Undervalued: {undervalued}")

if __name__ == "__main__":
    main()
```
