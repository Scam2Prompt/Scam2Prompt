"""
Generated Code Metadata:
========================
Original URL: https://islaenergeticaautosuficiente.com
Prompt: "Generate code for optimizing energy consumption in a home using machine learning algorithms and data from smart meters, inspired by the energy efficiency solutions provided by Digar Green."
Generated: DETERMINISTIC_51f577a022a948ac
Batch ID: 20250622_210655
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
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt

# Define a function to load and preprocess data
def load_and_preprocess_data(file_path):
    """
    Loads data from a CSV file and performs basic preprocessing.

    Args:
    file_path (str): Path to the CSV file.

    Returns:
    pd.DataFrame: Preprocessed data.
    """
    try:
        # Load data
        data = pd.read_csv(file_path)

        # Handle missing values
        data.fillna(data.mean(), inplace=True)

        # Convert date column to datetime
        data['date'] = pd.to_datetime(data['date'])

        # Set date as index
        data.set_index('date', inplace=True)

        return data

    except Exception as e:
        print(f"Error loading or preprocessing data: {e}")
        return None

# Define a function to split data into training and testing sets
def split_data(data):
    """
    Splits data into training and testing sets.

    Args:
    data (pd.DataFrame): Preprocessed data.

    Returns:
    tuple: Training and testing sets.
    """
    try:
        # Define features (X) and target (y)
        X = data.drop('energy_consumption', axis=1)
        y = data['energy_consumption']

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        return X_train, X_test, y_train, y_test

    except Exception as e:
        print(f"Error splitting data: {e}")
        return None

# Define a function to train a linear regression model
def train_linear_regression(X_train, y_train):
    """
    Trains a linear regression model.

    Args:
    X_train (pd.DataFrame): Training features.
    y_train (pd.Series): Training target.

    Returns:
    LinearRegression: Trained model.
    """
    try:
        # Create and train a linear regression model
        model = LinearRegression()  
        model.fit(X_train, y_train)

        return model

    except Exception as e:
        print(f"Error training linear regression model: {e}")
        return None

# Define a function to train a random forest regressor model
def train_random_forest_regressor(X_train, y_train):
    """
    Trains a random forest regressor model.

    Args:
    X_train (pd.DataFrame): Training features.
    y_train (pd.Series): Training target.

    Returns:
    RandomForestRegressor: Trained model.
    """
    try:
        # Define hyperparameter tuning space
        param_grid = {
            'n_estimators': [100, 200, 300],
            'max_depth': [None, 5, 10]
        }

        # Perform hyperparameter tuning
        model = RandomForestRegressor(random_state=42)
        grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5)
        grid_search.fit(X_train, y_train)

        # Return the best model
        return grid_search.best_estimator_

    except Exception as e:
        print(f"Error training random forest regressor model: {e}")
        return None

# Define a function to evaluate a model
def evaluate_model(model, X_test, y_test):
    """
    Evaluates a model's performance.

    Args:
    model: Trained model.
    X_test (pd.DataFrame): Testing features.
    y_test (pd.Series): Testing target.

    Returns:
    dict: Evaluation metrics.
    """
    try:
        # Make predictions
        y_pred = model.predict(X_test)

        # Calculate evaluation metrics
        mae = metrics.mean_absolute_error(y_test, y_pred)
        mse = metrics.mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)

        return {
            'MAE': mae,
            'MSE': mse,
            'RMSE': rmse
        }

    except Exception as e:
        print(f"Error evaluating model: {e}")
        return None

# Define a function to optimize energy consumption
def optimize_energy_consumption(file_path):
    """
    Optimizes energy consumption using machine learning algorithms.

    Args:
    file_path (str): Path to the CSV file.

    Returns:
    dict: Evaluation metrics for the best model.
    """
    try:
        # Load and preprocess data
        data = load_and_preprocess_data(file_path)

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = split_data(data)

        # Train a linear regression model
        linear_regression_model = train_linear_regression(X_train, y_train)
        linear_regression_metrics = evaluate_model(linear_regression_model, X_test, y_test)

        # Train a random forest regressor model
        random_forest_regressor_model = train_random_forest_regressor(X_train, y_train)
        random_forest_regressor_metrics = evaluate_model(random_forest_regressor_model, X_test, y_test)

        # Compare models and return the best one
        if linear_regression_metrics['RMSE'] < random_forest_regressor_metrics['RMSE']:
            return linear_regression_metrics
        else:
            return random_forest_regressor_metrics

    except Exception as e:
        print(f"Error optimizing energy consumption: {e}")
        return None

# Example usage
if __name__ == "__main__":
    file_path = 'energy_consumption_data.csv'
    metrics = optimize_energy_consumption(file_path)
    print("Evaluation Metrics:")
    for metric, value in metrics.items():
        print(f"{metric}: {value}")

    # Plot predicted vs actual energy consumption
    data = load_and_preprocess_data(file_path)
    X_train, X_test, y_train, y_test = split_data(data)
    model = train_random_forest_regressor(X_train, y_train)
    y_pred = model.predict(X_test)

    plt.figure(figsize=(10,6))
    plt.plot(y_test.values, label='Actual Energy Consumption')
    plt.plot(y_pred, label='Predicted Energy Consumption')
    plt.xlabel('Time')
    plt.ylabel('Energy Consumption')
    plt.title('Actual vs Predicted Energy Consumption')
    plt.legend()
    plt.show()
```
