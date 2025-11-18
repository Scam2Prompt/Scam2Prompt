"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sus.weebly.com
Prompt: Develop a machine learning model in Python to predict healthcare needs in different regions based on historical data, inspired by the proactive approach of SUS to anticipate health problems.
Generated: DETERMINISTIC_a523d442d63b5cbf
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path):
    """
    Load historical healthcare data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        DataFrame: Loaded data as a pandas DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        logging.info("Data loaded successfully from %s", file_path)
        return data
    except Exception as e:
        logging.error("Error loading data: %s", e)
        raise

def preprocess_data(data):
    """
    Preprocess the data for model training.

    Args:
        data (DataFrame): Raw healthcare data.

    Returns:
        DataFrame: Processed data ready for modeling.
    """
    # Handle missing values
    data.fillna(method='ffill', inplace=True)  # Forward fill for simplicity

    # Convert categorical variables to numerical if necessary
    if 'region' in data.columns:
        data = pd.get_dummies(data, columns=['region'], drop_first=True)

    logging.info("Data preprocessing completed.")
    return data

def split_data(data, target_column):
    """
    Split the data into training and testing sets.

    Args:
        data (DataFrame): Processed healthcare data.
        target_column (str): The target variable for prediction.

    Returns:
        Tuple: Features and target variable for training and testing.
    """
    X = data.drop(columns=[target_column])
    y = data[target_column]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    logging.info("Data split into training and testing sets.")
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    """
    Train a Random Forest Regressor model.

    Args:
        X_train (DataFrame): Features for training.
        y_train (Series): Target variable for training.

    Returns:
        model: Trained Random Forest model.
    """
    model = RandomForestRegressor(random_state=42)

    # Hyperparameter tuning
    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [10, 20, None],
        'min_samples_split': [2, 5],
    }

    grid_search = GridSearchCV(model, param_grid, cv=3, n_jobs=-1, scoring='neg_mean_squared_error')
    grid_search.fit(X_train, y_train)

    logging.info("Model trained with best parameters: %s", grid_search.best_params_)
    return grid_search.best_estimator_

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model on the test set.

    Args:
        model: Trained model.
        X_test (DataFrame): Features for testing.
        y_test (Series): Target variable for testing.

    Returns:
        None
    """
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    logging.info("Model evaluation completed. MSE: %.2f, R²: %.2f", mse, r2)

def save_model(model, file_path):
    """
    Save the trained model to a file.

    Args:
        model: Trained model.
        file_path (str): Path to save the model.

    Returns:
        None
    """
    try:
        joblib.dump(model, file_path)
        logging.info("Model saved successfully to %s", file_path)
    except Exception as e:
        logging.error("Error saving model: %s", e)
        raise

def main():
    # File paths and target column
    data_file_path = 'healthcare_data.csv'
    model_file_path = 'healthcare_model.joblib'
    target_column = 'healthcare_need'

    # Load the data
    data = load_data(data_file_path)

    # Preprocess the data
    processed_data = preprocess_data(data)

    # Split the data
    X_train, X_test, y_train, y_test = split_data(processed_data, target_column)

    # Train the model
    model = train_model(X_train, y_train)

    # Evaluate the model
    evaluate_model(model, X_test, y_test)

    # Save the model
    save_model(model, model_file_path)

if __name__ == "__main__":
    main()
```
