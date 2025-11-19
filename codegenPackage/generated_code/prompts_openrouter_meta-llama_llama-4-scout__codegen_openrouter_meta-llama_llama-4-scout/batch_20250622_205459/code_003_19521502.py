"""
Generated Code Metadata:
========================
Original URL: https://srhfoundation.ca
Prompt: "How can I use data from preventative health checks to create predictive models for chronic conditions using machine learning libraries like scikit-learn?"
Generated: DETERMINISTIC_195215029b212cdf
Batch ID: 20250622_205459
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
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
import numpy as np

def load_data(file_path):
    """
    Load data from a CSV file.

    Args:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: The loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def preprocess_data(data):
    """
    Preprocess the data by handling missing values and scaling.

    Args:
    data (pd.DataFrame): The data to preprocess.

    Returns:
    pd.DataFrame: The preprocessed data.
    """
    # Handle missing values
    data.fillna(data.mean(), inplace=True)

    # Scale the data
    scaler = StandardScaler()
    data[['age', 'bmi', 'blood_pressure']] = scaler.fit_transform(data[['age', 'bmi', 'blood_pressure']])

    return data

def split_data(data, target):
    """
    Split the data into training and testing sets.

    Args:
    data (pd.DataFrame): The data to split.
    target (str): The target variable.

    Returns:
    tuple: The training data, testing data, training target, testing target.
    """
    try:
        X = data.drop(target, axis=1)
        y = data[target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test
    except Exception as e:
        print(f"Error splitting data: {e}")
        return None

def train_model(X_train, y_train):
    """
    Train a random forest classifier model.

    Args:
    X_train (pd.DataFrame): The training data.
    y_train (pd.Series): The training target.

    Returns:
    RandomForestClassifier: The trained model.
    """
    try:
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        return model
    except Exception as e:
        print(f"Error training model: {e}")
        return None

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model using accuracy score, classification report, and confusion matrix.

    Args:
    model (RandomForestClassifier): The trained model.
    X_test (pd.DataFrame): The testing data.
    y_test (pd.Series): The testing target.
    """
    try:
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        matrix = confusion_matrix(y_test, y_pred)

        print(f"Accuracy: {accuracy:.3f}")
        print("Classification Report:\n", report)
        print("Confusion Matrix:\n", matrix)
    except Exception as e:
        print(f"Error evaluating model: {e}")

def main():
    # Load data
    file_path = "health_checks.csv"
    data = load_data(file_path)

    if data is not None:
        # Preprocess data
        data = preprocess_data(data)

        # Split data
        target = "has_chronic_condition"
        X_train, X_test, y_train, y_test = split_data(data, target)

        if X_train is not None:
            # Train model
            model = train_model(X_train, y_train)

            if model is not None:
                # Evaluate model
                evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()
```
