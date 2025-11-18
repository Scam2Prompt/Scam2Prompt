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
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load the data
def load_data(file_path):
    """
    Loads the dataset from a CSV file.
    
    Parameters:
    file_path (str): Path to the CSV file
    
    Returns:
    pd.DataFrame: Loaded DataFrame
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Preprocess the data
def preprocess_data(data):
    """
    Preprocesses the data by handling missing values and encoding categorical features.
    
    Parameters:
    data (pd.DataFrame): The raw dataset
    
    Returns:
    pd.DataFrame: Preprocessed DataFrame
    """
    try:
        # Drop rows with missing target values
        data = data.dropna(subset=['target'])
        
        # Fill missing values in features
        data = data.fillna(data.median())
        
        # One-hot encode categorical features
        data = pd.get_dummies(data, drop_first=True)
        
        return data
    except Exception as e:
        print(f"Error during preprocessing: {e}")
        return None

# Train the model
def train_model(X_train, y_train):
    """
    Trains a Random Forest model for predicting healthcare needs.
    
    Parameters:
    X_train (pd.DataFrame): Training feature matrix
    y_train (pd.Series): Training target variable
    
    Returns:
    RandomForestRegressor: Trained model
    """
    try:
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        return model
    except Exception as e:
        print(f"Error during model training: {e}")
        return None

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    """
    Evaluates the model's performance on the test data.
    
    Parameters:
    model (RandomForestRegressor): Trained model
    X_test (pd.DataFrame): Test feature matrix
    y_test (pd.Series): Test target variable
    
    Returns:
    dict: Evaluation metrics (MSE and R2 Score)
    """
    try:
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        return {"MSE": mse, "R2 Score": r2}
    except Exception as e:
        print(f"Error during evaluation: {e}")
        return None

# Save the model
def save_model(model, file_path):
    """
    Saves the trained model to a file.
    
    Parameters:
    model (RandomForestRegressor): Trained model
    file_path (str): Path to save the model
    
    Returns:
    None
    """
    try:
        joblib.dump(model, file_path)
        print(f"Model saved to {file_path}")
    except Exception as e:
        print(f"Error saving model: {e}")

# Main function to run the pipeline
def main():
    """
    Main function to execute the machine learning pipeline for predicting healthcare needs.
    """
    # File path to the dataset (replace with actual file path)
    file_path = 'healthcare_data.csv'
    
    # Load the data
    data = load_data(file_path)
    if data is None:
        return
    
    # Preprocess the data
    data = preprocess_data(data)
    if data is None:
        return
    
    # Split data into features and target
    X = data.drop('target', axis=1)
    y = data['target']
    
    # Split into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model
    model = train_model(X_train, y_train)
    if model is None:
        return
    
    # Evaluate the model
    metrics = evaluate_model(model, X_test, y_test)
    if metrics:
        print(f"Model Evaluation - MSE: {metrics['MSE']}, R2 Score: {metrics['R2 Score']}")
    
    # Save the model
    save_model(model, 'healthcare_model.pkl')

# Run the pipeline
if __name__ == '__main__':
    main()
```
