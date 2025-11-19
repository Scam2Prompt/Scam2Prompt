"""
Generated Code Metadata:
========================
Original URL: https://aptrongurgaon.in
Prompt: "Write a Python program for data analysis using popular libraries, as discussed in the data science training course at APTRON Gurgaon."
Generated: DETERMINISTIC_a37fe836a1db23c8
Batch ID: 20250622_204551
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
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Function to load data
def load_data(file_path):
    """
    Loads data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pandas.DataFrame: Loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Function to analyze data
def analyze_data(data):
    """
    Analyzes the loaded data.

    Args:
        data (pandas.DataFrame): Loaded data.

    Returns:
        None
    """
    # Get data info
    print("Data Info:")
    print(data.info())
    print("\nData Description:")
    print(data.describe())

    # Plot data
    plt.figure(figsize=(10,6))
    plt.plot(data)
    plt.title('Data Analysis')
    plt.xlabel('Index')
    plt.ylabel('Values')
    plt.show()

# Function to prepare data for modeling
def prepare_data(data):
    """
    Prepares data for modeling.

    Args:
        data (pandas.DataFrame): Loaded data.

    Returns:
        tuple: Features (X) and target (y)
    """
    try:
        # Assume the last column is the target variable
        X = data.iloc[:, :-1]
        y = data.iloc[:, -1]
        return X, y
    except Exception as e:
        print(f"Error preparing data: {e}")
        return None, None

# Function to train a linear regression model
def train_model(X, y):
    """
    Trains a linear regression model.

    Args:
        X (pandas.DataFrame): Features.
        y (pandas.Series): Target variable.

    Returns:
        sklearn.linear_model.LinearRegression: Trained model.
    """
    try:
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

        # Create and train a linear regression model
        model = LinearRegression()  
        model.fit(X_train, y_train)

        # Make predictions
        y_pred = model.predict(X_test)

        # Evaluate the model
        print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
        print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
        print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

        return model
    except Exception as e:
        print(f"Error training model: {e}")
        return None

# Main function
def main():
    file_path = 'data.csv'  # replace with your data file
    data = load_data(file_path)
    if data is not None:
        analyze_data(data)
        X, y = prepare_data(data)
        if X is not None and y is not None:
            model = train_model(X, y)

if __name__ == "__main__":
    main()
```
