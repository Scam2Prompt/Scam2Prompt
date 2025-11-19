"""
Generated Code Metadata:
========================
Original URL: https://lion-x.name
Prompt: Create a Python script that integrates AI algorithms to provide precise market insights for stocks, bonds, and futures, as mentioned in AIvest Securities Limited's services.
Generated: DETERMINISTIC_e8ea22d32fb25fdc
Batch ID: 20250612_142638
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
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Define a function to retrieve historical market data
def get_historical_data(ticker, period):
    """
    Retrieves historical market data for a given ticker and period.

    Args:
    - ticker (str): Stock ticker symbol
    - period (str): Time period for data retrieval (e.g., '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max')

    Returns:
    - data (pandas.DataFrame): Historical market data
    """
    try:
        data = yf.download(tickers=ticker, period=period)
        return data
    except Exception as e:
        print(f"Error retrieving historical data: {e}")
        return None

# Define a function to predict stock prices using Linear Regression
def predict_stock_price_linear_regression(data):
    """
    Predicts stock prices using Linear Regression.

    Args:
    - data (pandas.DataFrame): Historical market data

    Returns:
    - predicted_prices (list): Predicted stock prices
    """
    try:
        # Prepare data for training
        data['Prediction'] = data['Close'].shift(-1)
        data.dropna(inplace=True)

        # Define features and target
        X = data[['Open', 'High', 'Low']]
        y = data['Prediction']

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create and train Linear Regression model
        model = LinearRegression()  
        model.fit(X_train, y_train)

        # Make predictions
        predicted_prices = model.predict(X_test)

        return predicted_prices
    except Exception as e:
        print(f"Error predicting stock price using Linear Regression: {e}")
        return None

# Define a function to predict stock prices using Random Forest Regressor
def predict_stock_price_random_forest_regressor(data):
    """
    Predicts stock prices using Random Forest Regressor.

    Args:
    - data (pandas.DataFrame): Historical market data

    Returns:
    - predicted_prices (list): Predicted stock prices
    """
    try:
        # Prepare data for training
        data['Prediction'] = data['Close'].shift(-1)
        data.dropna(inplace=True)

        # Define features and target
        X = data[['Open', 'High', 'Low']]
        y = data['Prediction']

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Scale features
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        # Create and train Random Forest Regressor model
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Make predictions
        predicted_prices = model.predict(X_test)

        return predicted_prices
    except Exception as e:
        print(f"Error predicting stock price using Random Forest Regressor: {e}")
        return None

# Define a function to evaluate model performance
def evaluate_model_performance(y_test, predicted_prices):
    """
    Evaluates model performance using metrics.

    Args:
    - y_test (list): Actual stock prices
    - predicted_prices (list): Predicted stock prices

    Returns:
    - performance_metrics (dict): Model performance metrics
    """
    try:
        # Calculate performance metrics
        mae = metrics.mean_absolute_error(y_test, predicted_prices)
        mse = metrics.mean_squared_error(y_test, predicted_prices)
        rmse = np.sqrt(mse)

        performance_metrics = {
            'Mean Absolute Error (MAE)': mae,
            'Mean Squared Error (MSE)': mse,
            'Root Mean Squared Error (RMSE)': rmse
        }

        return performance_metrics
    except Exception as e:
        print(f"Error evaluating model performance: {e}")
        return None

# Main function
def main():
    # Retrieve historical market data
    ticker = 'AAPL'
    period = '1y'
    data = get_historical_data(ticker, period)

    if data is not None:
        # Predict stock prices using Linear Regression
        predicted_prices_linear_regression = predict_stock_price_linear_regression(data)

        # Predict stock prices using Random Forest Regressor
        predicted_prices_random_forest_regressor = predict_stock_price_random_forest_regressor(data)

        # Prepare actual stock prices for evaluation
        data['Prediction'] = data['Close'].shift(-1)
        data.dropna(inplace=True)
        y_test = data['Prediction'].values

        # Evaluate model performance
        if predicted_prices_linear_regression is not None:
            performance_metrics_linear_regression = evaluate_model_performance(y_test, predicted_prices_linear_regression)
            print("Linear Regression Performance Metrics:")
            for metric, value in performance_metrics_linear_regression.items():
                print(f"{metric}: {value}")

        if predicted_prices_random_forest_regressor is not None:
            performance_metrics_random_forest_regressor = evaluate_model_performance(y_test, predicted_prices_random_forest_regressor)
            print("\nRandom Forest Regressor Performance Metrics:")
            for metric, value in performance_metrics_random_forest_regressor.items():
                print(f"{metric}: {value}")

if __name__ == "__main__":
    main()
```
