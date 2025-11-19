"""
Generated Code Metadata:
========================
Original URL: https://diamondtradingfx.com
Prompt: Implement a cryptocurrency price prediction model using machine learning algorithms, focusing on Bitcoin, Ethereum, and Litecoin.
Generated: DETERMINISTIC_773614d5bc1d83ea
Batch ID: 20250622_205459
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
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
import yfinance as yf
import matplotlib.pyplot as plt

# Function to retrieve cryptocurrency data
def get_crypto_data(crypto, start_date, end_date):
    """
    Retrieves historical data for a specified cryptocurrency.

    Args:
    - crypto (str): The cryptocurrency to retrieve data for (e.g., 'BTC-USD', 'ETH-USD', 'LTC-USD').
    - start_date (str): The start date for the data retrieval in 'YYYY-MM-DD' format.
    - end_date (str): The end date for the data retrieval in 'YYYY-MM-DD' format.

    Returns:
    - data (pd.DataFrame): A DataFrame containing the historical data for the specified cryptocurrency.
    """
    try:
        data = yf.download(crypto, start=start_date, end=end_date)
        return data
    except Exception as e:
        print(f"Failed to retrieve data for {crypto}: {e}")
        return None

# Function to prepare data for training
def prepare_data(data):
    """
    Prepares the data for training by creating a new column 'Prediction' and shifting the 'Close' values.

    Args:
    - data (pd.DataFrame): The DataFrame containing the historical data.

    Returns:
    - data (pd.DataFrame): The prepared DataFrame with the 'Prediction' column.
    """
    data['Prediction'] = data['Close'].shift(-1)
    return data

# Function to train a Linear Regression model
def train_linear_regression_model(X_train, y_train):
    """
    Trains a Linear Regression model on the provided training data.

    Args:
    - X_train (np.array): The feature data for training.
    - y_train (np.array): The target data for training.

    Returns:
    - model (LinearRegression): The trained Linear Regression model.
    """
    model = LinearRegression()  
    model.fit(X_train, y_train)
    return model

# Function to train a Random Forest Regressor model
def train_random_forest_model(X_train, y_train):
    """
    Trains a Random Forest Regressor model on the provided training data.

    Args:
    - X_train (np.array): The feature data for training.
    - y_train (np.array): The target data for training.

    Returns:
    - model (RandomForestRegressor): The trained Random Forest Regressor model.
    """
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)
    return model

# Function to train a Support Vector Regressor model
def train_svr_model(X_train, y_train):
    """
    Trains a Support Vector Regressor model on the provided training data.

    Args:
    - X_train (np.array): The feature data for training.
    - y_train (np.array): The target data for training.

    Returns:
    - model (SVR): The trained Support Vector Regressor model.
    """
    model = SVR(kernel='rbf', C=1e3, gamma=0.1)
    model.fit(X_train, y_train)
    return model

# Main function
def main():
    # Define parameters
    start_date = '2010-01-01'
    end_date = '2022-12-31'
    cryptos = ['BTC-USD', 'ETH-USD', 'LTC-USD']

    for crypto in cryptos:
        # Retrieve data
        data = get_crypto_data(crypto, start_date, end_date)
        
        if data is not None:
            # Prepare data
            data = prepare_data(data)
            data.dropna(inplace=True)

            # Define features and target
            X = data[['Open', 'High', 'Low']]
            y = data['Prediction']

            # Split data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Scale data
            scaler = StandardScaler()
            X_train = scaler.fit_transform(X_train)
            X_test = scaler.transform(X_test)

            # Train models
            lr_model = train_linear_regression_model(X_train, y_train)
            rf_model = train_random_forest_model(X_train, y_train)
            svr_model = train_svr_model(X_train, y_train)

            # Make predictions
            lr_pred = lr_model.predict(X_test)
            rf_pred = rf_model.predict(X_test)
            svr_pred = svr_model.predict(X_test)

            # Evaluate models
            print(f"Model Evaluation for {crypto}:")
            print("Linear Regression Model:")
            print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, lr_pred))
            print('Mean Squared Error:', metrics.mean_squared_error(y_test, lr_pred))
            print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, lr_pred)))
            print()

            print("Random Forest Regressor Model:")
            print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, rf_pred))
            print('Mean Squared Error:', metrics.mean_squared_error(y_test, rf_pred))
            print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, rf_pred)))
            print()

            print("Support Vector Regressor Model:")
            print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, svr_pred))
            print('Mean Squared Error:', metrics.mean_squared_error(y_test, svr_pred))
            print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, svr_pred)))
            print()

            # Plot predictions
            plt.figure(figsize=(10,5))
            plt.plot(y_test.values, color='red', label='Actual')
            plt.plot(lr_pred, color='blue', label='Linear Regression')
            plt.plot(rf_pred, color='green', label='Random Forest Regressor')
            plt.plot(svr_pred, color='orange', label='Support Vector Regressor')
            plt.title(f'Cryptocurrency Price Prediction for {crypto}')
            plt.xlabel('Days')
            plt.ylabel('Price (USD)')
            plt.legend()
            plt.show()

if __name__ == "__main__":
    main()
```
