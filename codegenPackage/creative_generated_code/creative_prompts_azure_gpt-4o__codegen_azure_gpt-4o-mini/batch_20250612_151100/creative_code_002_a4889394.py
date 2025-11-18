"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptrongurgaon.in
Prompt: Recommend libraries and write code for implementing machine learning algorithms, as taught in APTRON Gurgaon’s Machine Learning training.
Generated: DETERMINISTIC_a4889394a4d19216
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.exceptions import NotFittedError

# Function to load and preprocess data
def load_and_preprocess_data(file_path):
    """
    Load data from a CSV file and preprocess it.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    tuple: Features and labels as numpy arrays.
    """
    try:
        # Load dataset
        data = pd.read_csv(file_path)
        # Assuming the last column is the label
        X = data.iloc[:, :-1].values  # Features
        y = data.iloc[:, -1].values    # Labels
        return X, y
    except FileNotFoundError:
        print("Error: File not found.")
        raise
    except pd.errors.EmptyDataError:
        print("Error: No data found in the file.")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

# Function to split data into training and testing sets
def split_data(X, y, test_size=0.2, random_state=42):
    """
    Split the dataset into training and testing sets.

    Parameters:
    X (numpy.ndarray): Features.
    y (numpy.ndarray): Labels.
    test_size (float): Proportion of the dataset to include in the test split.
    random_state (int): Random seed for reproducibility.

    Returns:
    tuple: Training and test sets for features and labels.
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

# Function to scale features
def scale_features(X_train, X_test):
    """
    Scale features using StandardScaler.

    Parameters:
    X_train (numpy.ndarray): Training features.
    X_test (numpy.ndarray): Testing features.

    Returns:
    tuple: Scaled training and test features.
    """
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled

# Function to train and evaluate a logistic regression model
def train_logistic_regression(X_train, y_train, X_test, y_test):
    """
    Train a Logistic Regression model and evaluate its performance.

    Parameters:
    X_train (numpy.ndarray): Scaled training features.
    y_train (numpy.ndarray): Training labels.
    X_test (numpy.ndarray): Scaled testing features.
    y_test (numpy.ndarray): Testing labels.

    Returns:
    float: Accuracy of the model on the test set.
    """
    model = LogisticRegression()
    model.fit(X_train, y_train)  # Train the model
    y_pred = model.predict(X_test)  # Make predictions
    accuracy = accuracy_score(y_test, y_pred)  # Calculate accuracy
    print("Logistic Regression Model accuracy:", accuracy)
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    return accuracy

# Function to train and evaluate a random forest model
def train_random_forest(X_train, y_train, X_test, y_test):
    """
    Train a Random Forest model and evaluate its performance.

    Parameters:
    X_train (numpy.ndarray): Scaled training features.
    y_train (numpy.ndarray): Training labels.
    X_test (numpy.ndarray): Scaled testing features.
    y_test (numpy.ndarray): Testing labels.

    Returns:
    float: Accuracy of the model on the test set.
    """
    model = RandomForestClassifier()
    model.fit(X_train, y_train)  # Train the model
    y_pred = model.predict(X_test)  # Make predictions
    accuracy = accuracy_score(y_test, y_pred)  # Calculate accuracy
    print("Random Forest Model accuracy:", accuracy)
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    return accuracy

def main(file_path):
    """
    Main function to execute the machine learning workflow.

    Parameters:
    file_path (str): The path to the CSV file containing the dataset.
    """
    # Load and preprocess data
    X, y = load_and_preprocess_data(file_path)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Scale features
    X_train_scaled, X_test_scaled = scale_features(X_train, X_test)

    # Train and evaluate models
    train_logistic_regression(X_train_scaled, y_train, X_test_scaled, y_test)
    train_random_forest(X_train_scaled, y_train, X_test_scaled, y_test)

# Entry point for the script
if __name__ == "__main__":
    # Example file path; replace with your dataset location
    file_path = 'path/to/your/dataset.csv'
    main(file_path)
```
