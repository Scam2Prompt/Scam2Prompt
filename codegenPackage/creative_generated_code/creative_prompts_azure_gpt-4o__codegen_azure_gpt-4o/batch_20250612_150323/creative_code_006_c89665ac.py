"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openseam.co
Prompt: Develop a machine learning model to predict worker fatigue and proficiency based on time-series data collected from sewing stations, following OpenSeam's focus on upskilling and reskilling.
Generated: DETERMINISTIC_c89665ac26f760cc
Batch ID: 20250612_150323
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
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib

# Load and preprocess the dataset
def load_data(file_path):
    """
    Load the time-series data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data as a Pandas DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at {file_path}")
    
    return data

def preprocess_data(data):
    """
    Preprocess the data for modeling.

    Args:
        data (pd.DataFrame): Raw data.

    Returns:
        X (pd.DataFrame): Features.
        y (pd.Series): Target values.
    """
    # Drop rows with missing values
    data = data.dropna()

    # Separate features (X) and target (y)
    X = data.drop(columns=["worker_fatigue", "worker_proficiency"])
    y = data[["worker_fatigue", "worker_proficiency"]]
    
    return X, y

# Build and train the machine learning model
def build_model():
    """
    Build a machine learning pipeline for fatigue and proficiency prediction.

    Returns:
        Pipeline: Configured pipeline with preprocessing and a model.
    """
    model = Pipeline([
        ("scaler", StandardScaler()),  # Standardize features
        ("regressor", RandomForestRegressor(random_state=42))  # Random Forest for regression
    ])
    return model

def train_model(model, X_train, y_train):
    """
    Train the model with the training data.

    Args:
        model (Pipeline): Machine learning pipeline.
        X_train (pd.DataFrame): Training features.
        y_train (pd.DataFrame): Training target values.
    """
    model.fit(X_train, y_train)

# Evaluate the model's performance
def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model on test data.

    Args:
        model (Pipeline): Trained model pipeline.
        X_test (pd.DataFrame): Test features.
        y_test (pd.DataFrame): Test target values.

    Returns:
        float: Mean Squared Error of the model's predictions.
    """
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    return mse

# Save the trained model to disk
def save_model(model, file_path):
    """
    Save the trained model to a file.

    Args:
        model (Pipeline): Trained model pipeline.
        file_path (str): Path to save the model.
    """
    joblib.dump(model, file_path)

# Main function to execute the workflow
def main():
    # File path to the dataset
    data_file_path = "sewing_station_data.csv"
    model_save_path = "worker_fatigue_proficiency_model.pkl"

    # Load and preprocess the data
    data = load_data(data_file_path)
    X, y = preprocess_data(data)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Build and train the model
    model = build_model()
    train_model(model, X_train, y_train)

    # Evaluate the model
    mse = evaluate_model(model, X_test, y_test)
    print(f"Mean Squared Error: {mse}")

    # Save the trained model
    save_model(model, model_save_path)
    print(f"Model saved to {model_save_path}")

if __name__ == "__main__":
    main()
```
