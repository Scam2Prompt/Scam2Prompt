"""
Generated Code Metadata:
========================
Original URL: https://initia.hu
Prompt: Suggest libraries or APIs for sustainable value creation analysis in the TMT and financial sectors, in line with Initia Capital's commitment to long-term value for investors and communities.
Generated: DETERMINISTIC_85cb13811c06b95b
Batch ID: 20250612_150227
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
from datetime import datetime, timedelta

# Define a function to retrieve historical stock data
def get_historical_data(ticker, start_date, end_date):
    """
    Retrieve historical stock data from Yahoo Finance.

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
        print(f"Error retrieving historical data: {e}")
        return None

# Define a function to calculate sustainable value creation metrics
def calculate_sustainable_value_creation(data):
    """
    Calculate sustainable value creation metrics.

    Args:
        data (pandas.DataFrame): Historical stock data.

    Returns:
        dict: Sustainable value creation metrics.
    """
    try:
        # Calculate return on equity (ROE)
        roe = data['Net Income'].rolling(window=12).mean() / data['Total Shareholder Equity'].rolling(window=12).mean()

        # Calculate return on assets (ROA)
        roa = data['Net Income'].rolling(window=12).mean() / data['Total Assets'].rolling(window=12).mean()

        # Calculate debt-to-equity ratio
        debt_to_equity = data['Total Debt'].rolling(window=12).mean() / data['Total Shareholder Equity'].rolling(window=12).mean()

        # Calculate interest coverage ratio
        interest_coverage = data['EBIT'].rolling(window=12).mean() / data['Interest Expense'].rolling(window=12).mean()

        metrics = {
            'roe': roe,
            'roa': roa,
            'debt_to_equity': debt_to_equity,
            'interest_coverage': interest_coverage
        }

        return metrics
    except Exception as e:
        print(f"Error calculating sustainable value creation metrics: {e}")
        return None

# Define a function to perform linear regression analysis
def perform_linear_regression(X, y):
    """
    Perform linear regression analysis.

    Args:
        X (pandas.DataFrame): Independent variables.
        y (pandas.Series): Dependent variable.

    Returns:
        tuple: Coefficient of determination (R-squared), mean absolute error (MAE), mean squared error (MSE).
    """
    try:
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create and train linear regression model
        model = LinearRegression()  
        model.fit(X_train, y_train)

        # Make predictions
        y_pred = model.predict(X_test)

        # Calculate evaluation metrics
        r2 = metrics.r2_score(y_test, y_pred)
        mae = metrics.mean_absolute_error(y_test, y_pred)
        mse = metrics.mean_squared_error(y_test, y_pred)

        return r2, mae, mse
    except Exception as e:
        print(f"Error performing linear regression analysis: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Retrieve historical stock data
    ticker = "AAPL"
    start_date = (datetime.now() - timedelta(days=365*5)).strftime('%Y-%m-%d')
    end_date = datetime.now().strftime('%Y-%m-%d')
    data = get_historical_data(ticker, start_date, end_date)

    # Calculate sustainable value creation metrics
    metrics = calculate_sustainable_value_creation(data)

    # Perform linear regression analysis
    X = data[['Open', 'High', 'Low']]
    y = data['Close']
    r2, mae, mse = perform_linear_regression(X, y)

    # Print results
    print(f"R-squared: {r2}")
    print(f"Mean Absolute Error: {mae}")
    print(f"Mean Squared Error: {mse}")
```
