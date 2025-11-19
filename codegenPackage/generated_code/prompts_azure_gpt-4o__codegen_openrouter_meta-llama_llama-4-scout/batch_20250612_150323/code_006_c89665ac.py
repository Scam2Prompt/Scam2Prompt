"""
Generated Code Metadata:
========================
Original URL: https://openseam.co
Prompt: Develop a machine learning model to predict worker fatigue and proficiency based on time-series data collected from sewing stations, following OpenSeam's focus on upskilling and reskilling.
Generated: DETERMINISTIC_c89665ac26f760cc
Batch ID: 20250612_150323
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
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.model_selection import TimeSeriesSplit

# Define a function to load and preprocess data
def load_and_preprocess_data(file_path):
    """
    Loads time-series data from a CSV file and preprocesses it for modeling.

    Args:
    file_path (str): Path to the CSV file containing time-series data.

    Returns:
    pandas.DataFrame: Preprocessed data.
    """
    try:
        # Load data from CSV file
        data = pd.read_csv(file_path)

        # Ensure date column is in datetime format
        data['date'] = pd.to_datetime(data['date'])

        # Set date column as index
        data.set_index('date', inplace=True)

        # Check for missing values
        if data.isnull().values.any():
            # Interpolate missing values using linear interpolation
            data.interpolate(method='linear', inplace=True)

        return data

    except Exception as e:
        print(f"Error loading or preprocessing data: {e}")
        return None

# Define a function to create feature sets for modeling
def create_feature_sets(data):
    """
    Creates feature sets for predicting worker fatigue and proficiency.

    Args:
    data (pandas.DataFrame): Preprocessed time-series data.

    Returns:
    tuple: Feature sets for training and testing.
    """
    try:
        # Define feature columns
        feature_cols = ['sewing_speed', 'thread_breakage_rate', 'machine_downtime']

        # Define target columns
        target_cols = ['fatigue_level', 'proficiency_level']

        # Split data into training and testing sets
        X = data[feature_cols]
        y = data[target_cols]

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        return X_train, X_test, y_train, y_test

    except Exception as e:
        print(f"Error creating feature sets: {e}")
        return None

# Define a function to train a machine learning model
def train_model(X_train, y_train):
    """
    Trains a random forest regressor model for predicting worker fatigue and proficiency.

    Args:
    X_train (pandas.DataFrame): Training feature set.
    y_train (pandas.DataFrame): Training target set.

    Returns:
    sklearn.ensemble.RandomForestRegressor: Trained model.
    """
    try:
        # Initialize and train a random forest regressor model
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        return model

    except Exception as e:
        print(f"Error training model: {e}")
        return None

# Define a function to evaluate model performance
def evaluate_model(model, X_test, y_test):
    """
    Evaluates the performance of a trained model on a test set.

    Args:
    model (sklearn.ensemble.RandomForestRegressor): Trained model.
    X_test (pandas.DataFrame): Testing feature set.
    y_test (pandas.DataFrame): Testing target set.

    Returns:
    dict: Model performance metrics.
    """
    try:
        # Make predictions on test set
        y_pred = model.predict(X_test)

        # Calculate performance metrics
        mse_fatigue = mean_squared_error(y_test['fatigue_level'], y_pred[:, 0])
        mse_proficiency = mean_squared_error(y_test['proficiency_level'], y_pred[:, 1])

        return {'mse_fatigue': mse_fatigue, 'mse_proficiency': mse_proficiency}

    except Exception as e:
        print(f"Error evaluating model: {e}")
        return None

# Define a function to plot predictions
def plot_predictions(y_test, y_pred):
    """
    Plots actual vs. predicted values for worker fatigue and proficiency.

    Args:
    y_test (pandas.DataFrame): Actual target values.
    y_pred (numpy.array): Predicted target values.
    """
    try:
        # Plot actual vs. predicted fatigue levels
        plt.figure(figsize=(10, 6))
        plt.plot(y_test['fatigue_level'], label='Actual Fatigue Level')
        plt.plot(y_pred[:, 0], label='Predicted Fatigue Level')
        plt.legend()
        plt.title('Actual vs. Predicted Fatigue Levels')
        plt.show()

        # Plot actual vs. predicted proficiency levels
        plt.figure(figsize=(10, 6))
        plt.plot(y_test['proficiency_level'], label='Actual Proficiency Level')
        plt.plot(y_pred[:, 1], label='Predicted Proficiency Level')
        plt.legend()
        plt.title('Actual vs. Predicted Proficiency Levels')
        plt.show()

    except Exception as e:
        print(f"Error plotting predictions: {e}")

# Main function
def main():
    # Load and preprocess data
    data = load_and_preprocess_data('sewing_station_data.csv')

    if data is not None:
        # Create feature sets
        X_train, X_test, y_train, y_test = create_feature_sets(data)

        if X_train is not None:
            # Scale features using StandardScaler
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)

            # Train model
            model = train_model(X_train_scaled, y_train)

            if model is not None:
                # Evaluate model performance
                performance_metrics = evaluate_model(model, X_test_scaled, y_test)

                if performance_metrics is not None:
                    print("Model Performance Metrics:")
                    print(f"MSE Fatigue: {performance_metrics['mse_fatigue']:.2f}")
                    print(f"MSE Proficiency: {performance_metrics['mse_proficiency']:.2f}")

                    # Make predictions on test set
                    y_pred = model.predict(X_test_scaled)

                    # Plot predictions
                    plot_predictions(y_test, y_pred)

if __name__ == "__main__":
    main()
```
