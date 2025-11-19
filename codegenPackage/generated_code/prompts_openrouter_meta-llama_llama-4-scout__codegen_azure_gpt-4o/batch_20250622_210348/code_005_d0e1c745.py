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

# Load and preprocess the data
def load_data(file_path):
    """
    Load the dataset from a CSV file and preprocess it.
    :param file_path: Path to the CSV file containing historical data.
    :return: Preprocessed DataFrame.
    """
    try:
        # Load the dataset
        data = pd.read_csv(file_path)
        
        # Check for missing values and handle them
        if data.isnull().sum().sum() > 0:
            data = data.fillna(data.mean())  # Fill missing values with column mean
        
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        raise

# Feature engineering and splitting data
def prepare_data(data):
    """
    Prepare the data for training and testing.
    :param data: Preprocessed DataFrame.
    :return: Features (X) and target (y) split into training and testing sets.
    """
    try:
        # Define features and target variable
        X = data[['distance', 'weight', 'service_type']]  # Features
        y = data['cost']  # Target variable
        
        # One-hot encode categorical features (e.g., service_type)
        X = pd.get_dummies(X, columns=['service_type'], drop_first=True)
        
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        return X_train, X_test, y_train, y_test
    except Exception as e:
        print(f"Error preparing data: {e}")
        raise

# Train the machine learning model
def train_model(X_train, y_train):
    """
    Train a Random Forest Regressor model.
    :param X_train: Training features.
    :param y_train: Training target variable.
    :return: Trained model.
    """
    try:
        # Initialize the model
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        
        # Train the model
        model.fit(X_train, y_train)
        
        return model
    except Exception as e:
        print(f"Error training model: {e}")
        raise

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model using Mean Squared Error.
    :param model: Trained model.
    :param X_test: Testing features.
    :param y_test: Testing target variable.
    :return: Mean Squared Error of the model.
    """
    try:
        # Predict on the test set
        predictions = model.predict(X_test)
        
        # Calculate Mean Squared Error
        mse = mean_squared_error(y_test, predictions)
        
        return mse
    except Exception as e:
        print(f"Error evaluating model: {e}")
        raise

# Save the trained model
def save_model(model, file_path):
    """
    Save the trained model to a file.
    :param model: Trained model.
    :param file_path: Path to save the model.
    """
    try:
        joblib.dump(model, file_path)
        print(f"Model saved to {file_path}")
    except Exception as e:
        print(f"Error saving model: {e}")
        raise

# Main function
def main():
    """
    Main function to execute the machine learning pipeline.
    """
    try:
        # File path to the dataset
        data_file_path = 'atakoy_nakliyat_data.csv'
        
        # File path to save the trained model
        model_file_path = 'moving_cost_predictor.pkl'
        
        # Load and preprocess the data
        data = load_data(data_file_path)
        
        # Prepare the data
        X_train, X_test, y_train, y_test = prepare_data(data)
        
        # Train the model
        model = train_model(X_train, y_train)
        
        # Evaluate the model
        mse = evaluate_model(model, X_test, y_test)
        print(f"Model Mean Squared Error: {mse}")
        
        # Save the trained model
        save_model(model, model_file_path)
    except Exception as e:
        print(f"Error in main function: {e}")
        raise

# Run the main function
if __name__ == '__main__':
    main()
```
