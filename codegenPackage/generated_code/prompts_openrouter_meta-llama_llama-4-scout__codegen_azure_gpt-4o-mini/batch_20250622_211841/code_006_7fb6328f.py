"""
Generated Code Metadata:
========================
Original URL: https://financestargate.com
Prompt: Write a Python script using machine learning libraries for multi-class classification tasks, as discussed in the article "One-Versus-All (OvR): The Multi-Class Classification Workhorse" on Finance StarGate.
Generated: DETERMINISTIC_7fb6328fe32b8d4d
Batch ID: 20250622_211841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.datasets import load_iris
import joblib

# Load dataset (using Iris dataset as an example)
def load_data():
    """Load the Iris dataset for multi-class classification."""
    iris = load_iris()
    X = iris.data
    y = iris.target
    return X, y

# Preprocess the data
def preprocess_data(X, y):
    """Split and scale the dataset."""
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    return X_train, X_test, y_train, y_test, scaler

# Train the model using One-Versus-All strategy
def train_model(X_train, y_train):
    """Train a multi-class classifier using One-Versus-All strategy."""
    model = LogisticRegression(multi_class='ovr', solver='liblinear', random_state=42)
    model.fit(X_train, y_train)
    return model

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    """Evaluate the trained model and print the classification report and confusion matrix."""
    y_pred = model.predict(X_test)
    
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

# Save the model and scaler
def save_model(model, scaler, model_filename='model.joblib', scaler_filename='scaler.joblib'):
    """Save the trained model and scaler to disk."""
    joblib.dump(model, model_filename)
    joblib.dump(scaler, scaler_filename)
    print(f"Model and scaler saved to {model_filename} and {scaler_filename}.")

# Main function to execute the workflow
def main():
    """Main function to execute the multi-class classification workflow."""
    try:
        # Load and preprocess data
        X, y = load_data()
        X_train, X_test, y_train, y_test, scaler = preprocess_data(X, y)
        
        # Train the model
        model = train_model(X_train, y_train)
        
        # Evaluate the model
        evaluate_model(model, X_test, y_test)
        
        # Save the model and scaler
        save_model(model, scaler)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
