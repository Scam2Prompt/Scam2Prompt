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
# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import joblib

# Define a function to preprocess data
def preprocess_data(data):
    """
    Preprocess the input data for machine learning.

    Parameters:
        data (pd.DataFrame): The raw data to preprocess.

    Returns:
        X (pd.DataFrame): Features after preprocessing.
        y (pd.Series): Target variable.
    """
    # Assume the ROI column is the target variable
    y = data['ROI']
    X = data.drop(columns=['ROI'])
    
    # One-hot encode categorical features
    X = pd.get_dummies(X, drop_first=True)
    
    # Scale features
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    
    return X, y, scaler

# Define a function to train the model
def train_model(X_train, y_train):
    """
    Train the machine learning model.

    Parameters:
        X_train (np.ndarray): Training features.
        y_train (pd.Series): Training target variable.

    Returns:
        model (RandomForestRegressor): Trained model.
    """
    model = RandomForestRegressor(random_state=42, n_estimators=100)
    model.fit(X_train, y_train)
    return model

# Define a function for evaluating the model
def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model's performance.

    Parameters:
        model (RandomForestRegressor): Trained model.
        X_test (np.ndarray): Testing features.
        y_test (pd.Series): Testing target variable.

    Returns:
        metrics (dict): Dictionary containing evaluation metrics.
    """
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    return {"Mean Squared Error": mse, "R2 Score": r2}

# Main function to execute the script
def main():
    """
    Main function to run the machine learning pipeline for predicting ROI.
    
    Steps:
        1. Load dataset.
        2. Preprocess data.
        3. Split data into training and testing sets.
        4. Train the model.
        5. Evaluate the model.
        6. Save the trained model for future use.
    """
    try:
        # Load dataset (replace 'data.csv' with the actual file path)
        data = pd.read_csv('data.csv')
        
        # Preprocess data
        X, y, scaler = preprocess_data(data)
        
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train the model
        model = train_model(X_train, y_train)
        
        # Evaluate the model
        metrics = evaluate_model(model, X_test, y_test)
        print("Model Evaluation Metrics:")
        print(metrics)
        
        # Save the trained model and scaler for future use
        joblib.dump(model, 'roi_prediction_model.pkl')
        joblib.dump(scaler, 'scaler.pkl')
        print("Model and scaler saved successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        
# Entry point of the script
if __name__ == '__main__':
    main()
```
