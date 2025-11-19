"""
Generated Code Metadata:
========================
Original URL: https://shravrav1.co.il
Prompt: How can I use machine learning algorithms to predict and prevent common plumbing issues, such as pipe bursts or water heater failures, for a company like י.א. אינסטלציה?
Generated: DETERMINISTIC_3dff2cbee590166c
Batch ID: 20250622_210655
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
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib

# Load the dataset
def load_data(file_path):
    """
    Load the dataset from a CSV file.
    
    :param file_path: str - Path to the CSV file containing plumbing data.
    :return: DataFrame - Loaded data as a pandas DataFrame.
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
    Preprocess the data for machine learning.
    
    :param data: DataFrame - Raw data to preprocess.
    :return: DataFrame - Preprocessed data.
    """
    # Handle missing values
    data.fillna(method='ffill', inplace=True)
    
    # Convert categorical variables to numerical
    data = pd.get_dummies(data, drop_first=True)
    
    return data

# Train the machine learning model
def train_model(X, y):
    """
    Train a Random Forest Classifier model.
    
    :param X: DataFrame - Features for training.
    :param y: Series - Target variable for training.
    :return: model - Trained Random Forest model.
    """
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model using test data.
    
    :param model: model - Trained machine learning model.
    :param X_test: DataFrame - Test features.
    :param y_test: Series - True labels for test data.
    """
    predictions = model.predict(X_test)
    print("Confusion Matrix:\n", confusion_matrix(y_test, predictions))
    print("\nClassification Report:\n", classification_report(y_test, predictions))

# Save the model to disk
def save_model(model, filename):
    """
    Save the trained model to a file.
    
    :param model: model - Trained machine learning model.
    :param filename: str - Filename to save the model.
    """
    try:
        joblib.dump(model, filename)
        print(f"Model saved to {filename}")
    except Exception as e:
        print(f"Error saving model: {e}")

# Main function to execute the workflow
def main():
    # Load the dataset
    data = load_data('plumbing_data.csv')
    if data is None:
        return
    
    # Preprocess the data
    processed_data = preprocess_data(data)
    
    # Define features and target variable
    X = processed_data.drop('failure', axis=1)  # Assuming 'failure' is the target column
    y = processed_data['failure']
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model
    model = train_model(X_train, y_train)
    
    # Evaluate the model
    evaluate_model(model, X_test, y_test)
    
    # Save the model
    save_model(model, 'plumbing_failure_model.pkl')

if __name__ == "__main__":
    main()
```
