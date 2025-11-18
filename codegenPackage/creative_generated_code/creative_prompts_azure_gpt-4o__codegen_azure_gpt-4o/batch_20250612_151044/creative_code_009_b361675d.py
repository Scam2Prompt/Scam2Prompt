"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stonex.markets
Prompt: Write a script to calculate the impact of weather forecasts on grain prices using StoneX's climate data reports and machine learning models like scikit-learn.
Generated: DETERMINISTIC_b361675dfbffbdc8
Batch ID: 20250612_151044
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
import joblib

# Define constants
DATA_FILE = 'stonex_climate_data.csv'  # Replace with the actual file path
MODEL_FILE = 'grain_price_prediction_model.pkl'

# Load and preprocess data
def load_data(data_file):
    """
    Load climate data from a CSV file.
    Args:
        data_file (str): Path to the data file.
    Returns:
        pd.DataFrame: Loaded data frame.
    """
    try:
        data = pd.read_csv(data_file)
    except FileNotFoundError as e:
        raise Exception(f"Data file not found: {data_file}") from e
    
    # Ensure necessary columns exist
    required_columns = ['temperature', 'precipitation', 'humidity', 'grain_price']
    if not all(column in data.columns for column in required_columns):
        raise ValueError(f"Data file must contain columns: {required_columns}")

    return data

# Feature engineering
def preprocess_data(data):
    """
    Preprocess climate data for machine learning models.
    Args:
        data (pd.DataFrame): Raw data frame.
    Returns:
        tuple: Features (X) and target variable (y).
    """
    # Handle missing data
    data = data.dropna()

    # Extract features and target
    X = data[['temperature', 'precipitation', 'humidity']]  # Feature columns
    y = data['grain_price']  # Target column

    return X, y

# Train the machine learning model
def train_model(X, y):
    """
    Train a RandomForestRegressor model.
    Args:
        X (pd.DataFrame): Feature set.
        y (pd.Series): Target variable.
    Returns:
        RandomForestRegressor: Trained model.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize model
    model = RandomForestRegressor(random_state=42)
    
    # Train the model
    model.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Model Mean Squared Error: {mse:.2f}")

    return model

# Save the trained model to a file
def save_model(model, file_path):
    """
    Save the trained machine learning model to a file.
    Args:
        model (RandomForestRegressor): Trained model.
        file_path (str): Path to save the model.
    """
    try:
        joblib.dump(model, file_path)
        print(f"Model saved to {file_path}")
    except Exception as e:
        raise Exception("Error while saving the model.") from e

# Main function
if __name__ == "__main__":
    try:
        # Load data
        print("Loading data...")
        data = load_data(DATA_FILE)
        
        # Preprocess data
        print("Preprocessing data...")
        X, y = preprocess_data(data)
        
        # Train model
        print("Training model...")
        model = train_model(X, y)
        
        # Save the trained model
        print("Saving model...")
        save_model(model, MODEL_FILE)
        
        print("Script completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
