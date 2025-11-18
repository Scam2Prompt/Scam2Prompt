"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pdma.io
Prompt: Develop a machine learning model for predicting digital marketing ROI, using concepts from PDMA's Digital Marketing Professional curriculum.
Generated: DETERMINISTIC_a5541693d06ec529
Batch ID: 20250612_145730
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
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path):
    """
    Load data from a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data as a DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        logging.info(f'Data loaded successfully from {file_path}')
        return data
    except Exception as e:
        logging.error(f'Error loading data: {e}')
        raise

def preprocess_data(data):
    """
    Preprocess the data for model training.

    Args:
        data (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: Processed features.
        pd.Series: Target variable.
    """
    # Handle missing values (simple imputation)
    data.fillna(data.mean(), inplace=True)

    # Feature and target separation
    X = data.drop(columns=['ROI'])
    y = data['ROI']

    # Convert categorical variables to numerical using one-hot encoding
    X = pd.get_dummies(X, drop_first=True)
    
    logging.info('Data preprocessing completed')
    return X, y

def train_model(X_train, y_train):
    """
    Train a Random Forest model on the training data.

    Args:
        X_train (pd.DataFrame): The training features.
        y_train (pd.Series): The training target.

    Returns:
        RandomForestRegressor: Trained model.
    """
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    logging.info('Model training completed')
    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model's performance.

    Args:
        model (RandomForestRegressor): The trained model.
        X_test (pd.DataFrame): The test features.
        y_test (pd.Series): The test target.

    Returns:
        dict: Dictionary containing evaluation metrics.
    """
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    
    logging.info(f'Model evaluation completed. MSE: {mse}, R2: {r2}')
    return {'MSE': mse, 'R2': r2}

def save_model(model, filename):
    """
    Save the trained model to a file.

    Args:
        model (RandomForestRegressor): The trained model.
        filename (str): The filename to save the model.
    """
    try:
        joblib.dump(model, filename)
        logging.info(f'Model saved successfully to {filename}')
    except Exception as e:
        logging.error(f'Error saving model: {e}')
        raise

def main(data_file, model_file):
    """
    Main function to execute the workflow.

    Args:
        data_file (str): Path to the input data file.
        model_file (str): Path to save the trained model.
    """
    # Load and preprocess data
    data = load_data(data_file)
    X, y = preprocess_data(data)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = train_model(X_train, y_train)

    # Evaluate the model
    metrics = evaluate_model(model, X_test, y_test)
    
    # Save the trained model
    save_model(model, model_file)

if __name__ == '__main__':
    # Specify the data file and model file paths
    data_file_path = 'digital_marketing_data.csv'  # Update this path as needed
    model_file_path = 'roi_model.pkl'

    main(data_file_path, model_file_path)
```
