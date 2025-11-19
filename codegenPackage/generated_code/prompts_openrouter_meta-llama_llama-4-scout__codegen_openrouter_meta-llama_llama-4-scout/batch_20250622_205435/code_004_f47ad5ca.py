"""
Generated Code Metadata:
========================
Original URL: https://ww16.yield-beef.yfi.de
Prompt: "How to integrate machine learning models for predicting beef cattle yield using Python?"
Generated: DETERMINISTIC_f47ad5caec071edf
Batch ID: 20250622_205435
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
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import numpy as np
import joblib

# Function to load data
def load_data(file_path):
    """
    Loads data from a CSV file.

    Args:
    file_path (str): Path to the CSV file.

    Returns:
    pd.DataFrame: Loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Function to preprocess data
def preprocess_data(data):
    """
    Preprocesses data by handling missing values and scaling.

    Args:
    data (pd.DataFrame): Data to preprocess.

    Returns:
    pd.DataFrame: Preprocessed data.
    """
    try:
        # Handle missing values
        data.fillna(data.mean(), inplace=True)
        
        # Define features and target
        X = data.drop('yield', axis=1)  # Features
        y = data['yield']  # Target

        # Scale features
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        return X_scaled, y
    except Exception as e:
        print(f"Error preprocessing data: {e}")
        return None, None

# Function to train model
def train_model(X_train, y_train):
    """
    Trains a random forest regressor model.

    Args:
    X_train (np.array): Training features.
    y_train (np.array): Training target.

    Returns:
    RandomForestRegressor: Trained model.
    """
    try:
        # Train model
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        return model
    except Exception as e:
        print(f"Error training model: {e}")
        return None

# Function to evaluate model
def evaluate_model(model, X_test, y_test):
    """
    Evaluates a model's performance.

    Args:
    model (RandomForestRegressor): Trained model.
    X_test (np.array): Testing features.
    y_test (np.array): Testing target.

    Returns:
    tuple: MSE and R2 score.
    """
    try:
        # Make predictions
        y_pred = model.predict(X_test)

        # Calculate metrics
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        return mse, r2
    except Exception as e:
        print(f"Error evaluating model: {e}")
        return None, None

# Function to save model
def save_model(model, file_path):
    """
    Saves a trained model to a file.

    Args:
    model (RandomForestRegressor): Trained model.
    file_path (str): Path to save the model.
    """
    try:
        joblib.dump(model, file_path)
        print(f"Model saved to {file_path}")
    except Exception as e:
        print(f"Error saving model: {e}")

# Main function
def main():
    # Load data
    data = load_data('beef_cattle_data.csv')

    if data is not None:
        # Preprocess data
        X_scaled, y = preprocess_data(data)

        if X_scaled is not None and y is not None:
            # Split data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

            # Train model
            model = train_model(X_train, y_train)

            if model is not None:
                # Evaluate model
                mse, r2 = evaluate_model(model, X_test, y_test)
                print(f"MSE: {mse}, R2 Score: {r2}")

                # Save model
                save_model(model, 'beef_cattle_yield_model.joblib')

if __name__ == "__main__":
    main()
```
