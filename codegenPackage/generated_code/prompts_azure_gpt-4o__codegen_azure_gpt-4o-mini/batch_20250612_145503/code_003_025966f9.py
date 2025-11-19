"""
Generated Code Metadata:
========================
Original URL: https://ejecutortecnico.github.io
Prompt: Provide an example of a Python-based AI project for beginners, aligning with the "Inteligencia artificial basico" content from https://ejecutortecnico.github.io.
Generated: DETERMINISTIC_025966f96428d7bf
Batch ID: 20250612_145503
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
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load the dataset
def load_data(file_path):
    """
    Load the dataset from a CSV file.

    :param file_path: str, path to the CSV file
    :return: DataFrame, loaded data
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Preprocess the data
def preprocess_data(data):
    """
    Preprocess the data by handling missing values and splitting features and target.

    :param data: DataFrame, the loaded data
    :return: tuple, features and target variable
    """
    # Drop rows with missing values
    data = data.dropna()
    
    # Assuming the last column is the target variable
    X = data.iloc[:, :-1].values  # Features
    y = data.iloc[:, -1].values    # Target variable
    return X, y

# Train the model
def train_model(X_train, y_train):
    """
    Train a Linear Regression model.

    :param X_train: array-like, training features
    :param y_train: array-like, training target
    :return: model, trained Linear Regression model
    """
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model using Mean Squared Error.

    :param model: trained model
    :param X_test: array-like, test features
    :param y_test: array-like, test target
    :return: float, Mean Squared Error
    """
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    return mse

# Visualize the results
def plot_results(y_test, predictions):
    """
    Plot the actual vs predicted values.

    :param y_test: array-like, actual target values
    :param predictions: array-like, predicted target values
    """
    plt.scatter(y_test, predictions)
    plt.xlabel("Actual Values")
    plt.ylabel("Predicted Values")
    plt.title("Actual vs Predicted Values")
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
    plt.show()

def main():
    # Load the dataset
    data = load_data('data.csv')  # Replace with your dataset path
    if data is None:
        return

    # Preprocess the data
    X, y = preprocess_data(data)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = train_model(X_train, y_train)

    # Evaluate the model
    mse = evaluate_model(model, X_test, y_test)
    print(f"Mean Squared Error: {mse}")

    # Make predictions
    predictions = model.predict(X_test)

    # Visualize the results
    plot_results(y_test, predictions)

if __name__ == "__main__":
    main()
```
