"""
Generated Code Metadata:
========================
Original URL: https://echotradeoptions.com
Prompt: Generate a script that uses advanced algorithms to analyze market trends and forecast profitable trades, inspired by Echo Trade's AI-driven trading strategies.
Generated: DETERMINISTIC_903d0f14a84b3960
Batch ID: 20250612_145455
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
import yfinance as yf
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

# Define a function to retrieve historical stock data
def get_historical_data(ticker, start_date, end_date):
    """
    Retrieves historical stock data from Yahoo Finance.

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

# Define a function to prepare data for training
def prepare_data(data):
    """
    Prepares data for training by creating technical indicators.

    Args:
        data (pandas.DataFrame): Historical stock data.

    Returns:
        pandas.DataFrame: Prepared data.
    """
    try:
        data['MA_50'] = data['Close'].rolling(window=50).mean()
        data['MA_200'] = data['Close'].rolling(window=200).mean()
        data['RSI'] = data['Close'].pct_change().rolling(window=14).apply(lambda x: x.ewm(com=13-1, adjust=False).mean())
        data['BollingerBand'] = data['Close'].rolling(window=20).apply(lambda x: (x.max() - x.min()))
        data.dropna(inplace=True)
        return data
    except Exception as e:
        print(f"Error preparing data: {e}")
        return None

# Define a function to train a linear regression model
def train_linear_regression_model(data):
    """
    Trains a linear regression model to forecast stock prices.

    Args:
        data (pandas.DataFrame): Prepared data.

    Returns:
        sklearn.linear_model.LinearRegression: Trained model.
    """
    try:
        X = data[['MA_50', 'MA_200', 'RSI', 'BollingerBand']]
        y = data['Close']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LinearRegression()  
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        print('Linear Regression Model Metrics:')
        print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
        print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
        print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
        return model
    except Exception as e:
        print(f"Error training linear regression model: {e}")
        return None

# Define a function to train a random forest regressor model
def train_random_forest_regressor_model(data):
    """
    Trains a random forest regressor model to forecast stock prices.

    Args:
        data (pandas.DataFrame): Prepared data.

    Returns:
        sklearn.ensemble.RandomForestRegressor: Trained model.
    """
    try:
        X = data[['MA_50', 'MA_200', 'RSI', 'BollingerBand']]
        y = data['Close']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        param_grid = {
            'n_estimators': [100, 200, 300],
            'max_depth': [None, 5, 10]
        }
        model = RandomForestRegressor(random_state=42)
        grid = GridSearchCV(estimator=model, param_grid=param_grid, cv=5)
        grid_result = grid.fit(X_train, y_train)
        print('Random Forest Regressor Model Metrics:')
        print('Best Parameters:', grid_result.best_params_)
        print('Best Score:', grid_result.best_score_)
        y_pred = grid_result.predict(X_test)
        print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
        print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
        print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
        return grid_result.best_estimator_
    except Exception as e:
        print(f"Error training random forest regressor model: {e}")
        return None

# Main function
def main():
    ticker = 'AAPL'
    start_date = '2010-01-01'
    end_date = '2022-02-26'
    data = get_historical_data(ticker, start_date, end_date)
    if data is not None:
        prepared_data = prepare_data(data)
        if prepared_data is not None:
            linear_regression_model = train_linear_regression_model(prepared_data)
            random_forest_regressor_model = train_random_forest_regressor_model(prepared_data)

if __name__ == "__main__":
    main()
```
