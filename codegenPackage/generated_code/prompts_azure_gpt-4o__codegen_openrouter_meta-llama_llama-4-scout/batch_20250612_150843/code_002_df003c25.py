"""
Generated Code Metadata:
========================
Original URL: https://the-bitcoinfortune.com
Prompt: Generate code to analyze historical Bitcoin price data and predict future market fluctuations using advanced algorithms, as mentioned in The Bitcoin Fortune software.
Generated: DETERMINISTIC_df003c25903bc654
Batch ID: 20250612_150843
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
import yfinance as yf
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Function to retrieve historical Bitcoin price data
def get_historical_data(period):
    """
    Retrieves historical Bitcoin price data from Yahoo Finance.

    Args:
        period (str): The period of time for which to retrieve data (e.g. '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max')

    Returns:
        pandas.DataFrame: A DataFrame containing the historical Bitcoin price data
    """
    try:
        data = yf.download('BTC-USD', period=period)
        return data
    except Exception as e:
        print(f"Error retrieving historical data: {e}")
        return None

# Function to prepare data for training
def prepare_data(data):
    """
    Prepares the historical Bitcoin price data for training by converting the 'Date' index to a numerical value and creating new features.

    Args:
        data (pandas.DataFrame): The historical Bitcoin price data

    Returns:
        pandas.DataFrame: The prepared data
    """
    try:
        data.reset_index(inplace=True)
        data['Date'] = pd.to_datetime(data['Date'])
        data['Date'] = (data['Date'] - data['Date'].min()).dt.days
        data['Moving_Avg'] = data['Close'].rolling(window=7).mean()
        data['Exp_Moving_Avg'] = data['Close'].ewm(span=7, adjust=False).mean()
        data.dropna(inplace=True)
        return data
    except Exception as e:
        print(f"Error preparing data: {e}")
        return None

# Function to train a linear regression model
def train_linear_regression_model(data):
    """
    Trains a linear regression model on the prepared data.

    Args:
        data (pandas.DataFrame): The prepared data

    Returns:
        sklearn.linear_model.LinearRegression: The trained linear regression model
    """
    try:
        X = data[['Date', 'Moving_Avg', 'Exp_Moving_Avg']]
        y = data['Close']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
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

# Function to train a random forest regressor model
def train_random_forest_model(data):
    """
    Trains a random forest regressor model on the prepared data.

    Args:
        data (pandas.DataFrame): The prepared data

    Returns:
        sklearn.ensemble.RandomForestRegressor: The trained random forest regressor model
    """
    try:
        X = data[['Date', 'Moving_Avg', 'Exp_Moving_Avg']]
        y = data['Close']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

        param_grid = {
            'n_estimators': [100, 200, 300],
            'max_depth': [None, 5, 10],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 5, 10]
        }

        model = RandomForestRegressor(random_state=0)
        grid = GridSearchCV(estimator=model, param_grid=param_grid, cv=5)
        grid_result = grid.fit(X_train, y_train)

        print('Random Forest Model Best Parameters:', grid_result.best_params_)
        print('Random Forest Model Best Score:', grid_result.best_score_)

        y_pred = grid_result.best_estimator_.predict(X_test)
        print('Random Forest Model Metrics:')
        print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
        print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
        print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

        return grid_result.best_estimator_
    except Exception as e:
        print(f"Error training random forest model: {e}")
        return None

# Main function
def main():
    data = get_historical_data('1y')
    prepared_data = prepare_data(data)

    linear_regression_model = train_linear_regression_model(prepared_data)
    random_forest_model = train_random_forest_model(prepared_data)

    # Use the models to make predictions
    if linear_regression_model is not None and random_forest_model is not None:
        future_date = prepared_data['Date'].max() + 30
        future_moving_avg = prepared_data['Moving_Avg'].iloc[-1]
        future_exp_moving_avg = prepared_data['Exp_Moving_Avg'].iloc[-1]

        linear_regression_prediction = linear_regression_model.predict([[future_date, future_moving_avg, future_exp_moving_avg]])
        random_forest_prediction = random_forest_model.predict([[future_date, future_moving_avg, future_exp_moving_avg]])

        print('Linear Regression Prediction:', linear_regression_prediction)
        print('Random Forest Prediction:', random_forest_prediction)

if __name__ == "__main__":
    main()
```
