"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://giitechcodes.com.ng
Prompt: Develop a regression model in Python for a software solution, following the machine learning automation techniques mentioned by GII Tech Codes.
Generated: DETERMINISTIC_176d9dd028995a9e
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import logging

# Set up logging for debug information
logging.basicConfig(level=logging.INFO)

def load_data(file_path):
    """
    Load data from a CSV file.
    
    Parameters:
    - file_path: str, path to the CSV file
    
    Returns:
    - pandas DataFrame containing the loaded data
    """
    try:
        data = pd.read_csv(file_path)
        logging.info(f"Data loaded successfully from {file_path}")
        return data
    except Exception as e:
        logging.error("Error loading data: %s", e)
        raise

def preprocess_data(data):
    """
    Preprocess the data by handling missing values and separating features and target.
    
    Parameters:
    - data: pandas DataFrame, input data
    
    Returns:
    - X: pandas DataFrame, features
    - y: pandas Series, target variable
    """
    # Handle missing values (for simplicity, we'll drop rows with any missing values)
    data = data.dropna()
    logging.info("Missing values handled.")
    
    # Assuming the last column is the target variable
    X = data.iloc[:, :-1]  # All columns except the last
    y = data.iloc[:, -1]   # Last column as target
    logging.info("Data preprocessed into features and target.")
    
    return X, y

def train_model(X, y):
    """
    Train a linear regression model using the provided features and target.
    
    Parameters:
    - X: pandas DataFrame, features
    - y: pandas Series, target variable
    
    Returns:
    - model: trained LinearRegression model
    """
    model = LinearRegression()
    model.fit(X, y)
    logging.info("Model trained successfully.")
    
    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model's performance using Mean Squared Error and R^2 Score.
    
    Parameters:
    - model: trained LinearRegression model
    - X_test: pandas DataFrame, test features
    - y_test: pandas Series, test target variable
    
    Returns:
    - mse: float, Mean Squared Error
    - r2: float, R^2 Score
    """
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    logging.info(f"Model evaluation completed: MSE = {mse}, R^2 = {r2}")
    
    return mse, r2

def save_model(model, file_path):
    """
    Save the trained model to a file using joblib.
    
    Parameters:
    - model: trained model
    - file_path: str, the path to save the model
    """
    try:
        joblib.dump(model, file_path)
        logging.info(f"Model saved successfully to {file_path}")
    except Exception as e:
        logging.error("Error saving model: %s", e)
        raise

def main():
    # Define file paths
    input_file_path = 'data.csv'  # Input data file
    model_file_path = 'regression_model.pkl'  # Model output file

    # Load and preprocess data
    data = load_data(input_file_path)
    X, y = preprocess_data(data)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    logging.info("Data split into training and testing sets.")

    # Train the model
    model = train_model(X_train, y_train)

    # Evaluate the model
    mse, r2 = evaluate_model(model, X_test, y_test)

    # Save the model
    save_model(model, model_file_path)

if __name__ == "__main__":
    main()
```
