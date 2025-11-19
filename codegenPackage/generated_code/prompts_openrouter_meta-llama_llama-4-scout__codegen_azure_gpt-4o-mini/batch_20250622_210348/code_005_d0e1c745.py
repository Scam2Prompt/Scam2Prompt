"""
Generated Code Metadata:
========================
Original URL: https://atakoynakliyat.gen.tr
Prompt: Develop a machine learning model to predict the cost of moving based on historical data from Ataköy nakliyat services, including features like distance, weight, and service type.
Generated: DETERMINISTIC_d0e1c7456e4da2a1
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
import logging

# Set up logging for tracking the model training process
logging.basicConfig(level=logging.INFO)

def load_data(file_path):
    """
    Load the dataset from a CSV file.

    :param file_path: str, path to the CSV file
    :return: DataFrame, loaded data
    """
    try:
        data = pd.read_csv(file_path)
        logging.info("Data loaded successfully.")
        return data
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        raise

def preprocess_data(data):
    """
    Preprocess the data by handling missing values and encoding categorical variables.

    :param data: DataFrame, raw data
    :return: DataFrame, preprocessed data
    """
    # Handle missing values
    data.fillna(method='ffill', inplace=True)

    # Convert categorical variables to numerical
    data = pd.get_dummies(data, columns=['service_type'], drop_first=True)
    
    logging.info("Data preprocessed successfully.")
    return data

def train_model(X, y):
    """
    Train a Random Forest Regressor model.

    :param X: DataFrame, features
    :param y: Series, target variable
    :return: model, trained Random Forest model
    """
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    logging.info("Model trained successfully.")
    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model using Mean Squared Error.

    :param model: trained model
    :param X_test: DataFrame, test features
    :param y_test: Series, test target variable
    :return: float, Mean Squared Error
    """
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    logging.info(f"Model evaluation completed. MSE: {mse}")
    return mse

def save_model(model, file_path):
    """
    Save the trained model to a file.

    :param model: trained model
    :param file_path: str, path to save the model
    """
    try:
        joblib.dump(model, file_path)
        logging.info("Model saved successfully.")
    except Exception as e:
        logging.error(f"Error saving model: {e}")
        raise

def main():
    # Load the dataset
    data = load_data('atakoy_nakliyat_data.csv')

    # Preprocess the data
    processed_data = preprocess_data(data)

    # Define features and target variable
    X = processed_data.drop('cost', axis=1)  # Assuming 'cost' is the target variable
    y = processed_data['cost']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = train_model(X_train, y_train)

    # Evaluate the model
    evaluate_model(model, X_test, y_test)

    # Save the trained model
    save_model(model, 'moving_cost_model.pkl')

if __name__ == "__main__":
    main()
```
