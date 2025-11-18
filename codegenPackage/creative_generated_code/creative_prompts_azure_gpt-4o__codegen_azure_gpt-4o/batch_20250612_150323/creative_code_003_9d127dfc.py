"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openseam.co
Prompt: Create a Python script that analyzes sewing machine downtime data and predicts inefficiencies in production lines, inspired by OpenSeam's approach to capturing lost time.
Generated: DETERMINISTIC_9d127dfcada09fcc
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
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path):
    """
    Load sewing machine downtime data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file containing the data.
    
    Returns:
        pd.DataFrame: DataFrame containing the downtime data.
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
    Preprocess the downtime data for analysis and model training.
    
    Args:
        data (pd.DataFrame): Raw downtime data.
    
    Returns:
        pd.DataFrame: Preprocessed data.
    """
    try:
        # Drop rows with missing values
        data = data.dropna()
        
        # Convert categorical columns to numerical using one-hot encoding
        categorical_cols = data.select_dtypes(include=['object']).columns
        data = pd.get_dummies(data, columns=categorical_cols, drop_first=True)
        
        logging.info("Data preprocessing completed successfully.")
        return data
    except Exception as e:
        logging.error(f"Error preprocessing data: {e}")
        raise

def train_model(data, target_column):
    """
    Train a Random Forest classifier to predict inefficiencies in production lines.
    
    Args:
        data (pd.DataFrame): Preprocessed data.
        target_column (str): Name of the target column in the data.
    
    Returns:
        RandomForestClassifier: Trained Random Forest model.
        pd.DataFrame: Test data for evaluation.
        pd.Series: Test labels for evaluation.
    """
    try:
        # Split data into features and target
        X = data.drop(columns=[target_column])
        y = data[target_column]
        
        # Split into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Initialize and train Random Forest model
        model = RandomForestClassifier(random_state=42)
        model.fit(X_train, y_train)
        
        logging.info("Model training completed successfully.")
        return model, X_test, y_test
    except Exception as e:
        logging.error(f"Error training model: {e}")
        raise

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model on the test data.
    
    Args:
        model (RandomForestClassifier): Trained Random Forest model.
        X_test (pd.DataFrame): Test features.
        y_test (pd.Series): Test labels.
    """
    try:
        predictions = model.predict(X_test)
        report = classification_report(y_test, predictions)
        logging.info("Model evaluation completed successfully.")
        print("Classification Report:\n", report)
    except Exception as e:
        logging.error(f"Error evaluating model: {e}")
        raise

def main():
    """
    Main function to load, preprocess, train, and evaluate the model.
    """
    try:
        # File path to the downtime data
        file_path = "downtime_data.csv"
        
        # Load the data
        data = load_data(file_path)
        
        # Preprocess the data
        data = preprocess_data(data)
        
        # Define the target column
        target_column = 'inefficiency_flag'  # Replace with actual column name for inefficiencies
        
        # Train the model
        model, X_test, y_test = train_model(data, target_column)
        
        # Evaluate the model
        evaluate_model(model, X_test, y_test)
    except Exception as e:
        logging.error(f"Error in main function: {e}")
        raise

if __name__ == "__main__":
    main()
```
