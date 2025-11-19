"""
Generated Code Metadata:
========================
Original URL: https://www.icyd.org
Prompt: Develop a machine learning model to predict the effectiveness of youth development programs in Iowa, using features from the ICYD.org website.
Generated: DETERMINISTIC_3c1bca7500558c47
Batch ID: 20250622_212410
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
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load the dataset
def load_data(file_path):
    """
    Load the dataset from a CSV file.
    :param file_path: Path to the CSV file.
    :return: Pandas DataFrame containing the dataset.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: File is empty.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Preprocess the data
def preprocess_data(data):
    """
    Preprocess the data by handling missing values and encoding categorical features.
    :param data: Raw DataFrame.
    :return: Preprocessed DataFrame.
    """
    # Drop rows with missing target values
    data = data.dropna(subset=['effectiveness_score'])

    # Fill missing values in features with the median
    for column in data.columns:
        if data[column].dtype in ['int64', 'float64']:
            data[column].fillna(data[column].median(), inplace=True)
        elif data[column].dtype == 'object':
            data[column].fillna(data[column].mode()[0], inplace=True)

    # Encode categorical features using one-hot encoding
    data = pd.get_dummies(data, drop_first=True)

    return data

# Split the data into training and testing sets
def split_data(data, target_column):
    """
    Split the data into training and testing sets.
    :param data: Preprocessed DataFrame.
    :param target_column: Name of the target column.
    :return: X_train, X_test, y_train, y_test
    """
    X = data.drop(columns=[target_column])
    y = data[target_column]
    return train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
def train_model(X_train, y_train):
    """
    Train a Random Forest model.
    :param X_train: Training features.
    :param y_train: Training target.
    :return: Trained model.
    """
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)
    return model

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model using R^2 and Mean Squared Error.
    :param model: Trained model.
    :param X_test: Testing features.
    :param y_test: Testing target.
    :return: None
    """
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    print(f"Mean Squared Error: {mse}")
    print(f"R^2 Score: {r2}")

# Save the model
def save_model(model, file_path):
    """
    Save the trained model to a file.
    :param model: Trained model.
    :param file_path: Path to save the model.
    :return: None
    """
    try:
        joblib.dump(model, file_path)
        print(f"Model saved to {file_path}")
    except Exception as e:
        print(f"Error saving model: {e}")

# Main function
def main():
    """
    Main function to execute the machine learning pipeline.
    :return: None
    """
    # File path to the dataset
    file_path = 'iowa_youth_programs.csv'  # Replace with the actual file path

    # Load the data
    data = load_data(file_path)
    if data is None:
        return

    # Preprocess the data
    data = preprocess_data(data)

    # Split the data
    target_column = 'effectiveness_score'  # Replace with the actual target column name
    X_train, X_test, y_train, y_test = split_data(data, target_column)

    # Train the model
    model = train_model(X_train, y_train)

    # Evaluate the model
    evaluate_model(model, X_test, y_test)

    # Save the model
    save_model(model, 'youth_program_model.pkl')

# Entry point
if __name__ == "__main__":
    main()
```
