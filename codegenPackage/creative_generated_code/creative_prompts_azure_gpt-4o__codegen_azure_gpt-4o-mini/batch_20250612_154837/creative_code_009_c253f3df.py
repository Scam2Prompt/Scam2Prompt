"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://master-brain.com
Prompt: Generate a Python script to evaluate the impact of strategic consulting on small business growth, inspired by Master-Brain's services.
Generated: DETERMINISTIC_c253f3df8efd0885
Batch ID: 20250612_154837
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
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Set plot style
sns.set(style='whitegrid')

def load_data(filepath):
    """
    Loads the dataset from the specified filepath.

    :param filepath: Path to the CSV file containing the data
    :return: DataFrame containing the loaded data
    """
    try:
        data = pd.read_csv(filepath)
        return data
    except FileNotFoundError:
        print(f"Error: The file {filepath} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: There was a problem parsing the file.")
        return None

def preprocess_data(data):
    """
    Preprocesses the data by handling missing values and encoding categorical variables.

    :param data: DataFrame containing the raw data
    :return: DataFrame processed for analysis
    """
    # Drop rows with missing target values
    data = data.dropna(subset=['business_growth'])

    # Fill missing values in other columns with column mean
    data.fillna(data.mean(), inplace=True)

    # One-hot encoding for categorical variables
    data = pd.get_dummies(data, drop_first=True)

    return data

def train_model(X_train, y_train):
    """
    Trains a linear regression model on the training data.

    :param X_train: Training features
    :param y_train: Training target variable
    :return: Trained Linear Regression model
    """
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluates the trained model using mean squared error and R^2 score.

    :param model: Trained Linear Regression model
    :param X_test: Test features
    :param y_test: Test target variable
    """
    predictions = model.predict(X_test)
    
    # Calculate metrics
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R² Score: {r2:.2f}")

    # Plotting actual vs predicted values
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, predictions, alpha=0.7)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.xlabel('Actual Growth')
    plt.ylabel('Predicted Growth')
    plt.title('Actual vs Predicted Business Growth')
    plt.show()

def main(filepath):
    """
    Main function to execute the script.

    :param filepath: Path to the CSV file containing the data
    """
    # Load and preprocess data
    data = load_data(filepath)
    if data is None:
        return

    processed_data = preprocess_data(data)
    
    # Define features and target variable
    X = processed_data.drop('business_growth', axis=1)
    y = processed_data['business_growth']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = train_model(X_train, y_train)

    # Evaluate the model
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    # Specify the path to the data file
    data_file_path = 'business_growth_data.csv'  # Update this path as necessary
    main(data_file_path)
```
