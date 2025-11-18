"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://edukacija.net
Prompt: Write a Python script for data classification based on the techniques discussed in the "Classification with Python Live Course" from edukacija.net.
Generated: DETERMINISTIC_8aa61377f209d63c
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
import logging

# Set up logging for debugging purposes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path):
    """
    Load the dataset from a CSV file.

    :param file_path: Path to the CSV file
    :return: DataFrame containing the dataset
    """
    try:
        data = pd.read_csv(file_path)
        logging.info("Data loaded successfully from %s", file_path)
        return data
    except Exception as e:
        logging.error("Error loading data: %s", e)
        raise

def preprocess_data(data):
    """
    Preprocess the data by separating features and labels,
    and scaling the features.

    :param data: DataFrame containing the dataset
    :return: Scaled features and labels
    """
    try:
        # Assuming the last column is the label
        X = data.iloc[:, :-1].values
        y = data.iloc[:, -1].values
        
        # Scale the features
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        logging.info("Data preprocessed successfully.")
        return X_scaled, y
    except Exception as e:
        logging.error("Error during data preprocessing: %s", e)
        raise

def split_data(X, y, test_size=0.2, random_state=42):
    """
    Split the dataset into training and testing sets.

    :param X: Features
    :param y: Labels
    :param test_size: Proportion of the dataset to include in the test split
    :param random_state: Seed used by the random number generator
    :return: Training and testing sets
    """
    try:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        logging.info("Data split into training and testing sets successfully.")
        return X_train, X_test, y_train, y_test
    except Exception as e:
        logging.error("Error splitting data: %s", e)
        raise

def train_model(X_train, y_train):
    """
    Train a Random Forest classifier on the training data.

    :param X_train: Training features
    :param y_train: Training labels
    :return: Trained Random Forest model
    """
    try:
        model = RandomForestClassifier(random_state=42)
        model.fit(X_train, y_train)
        logging.info("Model trained successfully.")
        return model
    except Exception as e:
        logging.error("Error training model: %s", e)
        raise

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model on the test data.

    :param model: Trained model
    :param X_test: Testing features
    :param y_test: Testing labels
    """
    try:
        y_pred = model.predict(X_test)
        print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
        print("\nClassification Report:\n", classification_report(y_test, y_pred))
        logging.info("Model evaluation completed.")
    except Exception as e:
        logging.error("Error evaluating model: %s", e)
        raise

def main(file_path):
    """
    Main function to execute the data classification workflow.

    :param file_path: Path to the input data file
    """
    data = load_data(file_path)
    X, y = preprocess_data(data)
    X_train, X_test, y_train, y_test = split_data(X, y)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    # Replace 'data.csv' with the actual path to your dataset
    main('data.csv')
```
