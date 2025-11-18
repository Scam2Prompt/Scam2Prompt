"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalfxoption.com
Prompt: Write a Python script to analyze Non-Farm Payroll (NFP) data and predict its impact on forex trading, as highlighted in the NFP section of Global FX Option.
Generated: DETERMINISTIC_8f1eb0c474995547
Batch ID: 20250612_153814
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
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Define global constants
DATE_COLUMN = 'Date'
NFP_COLUMN = 'NFP Change'
FOREX_IMPACT_COLUMN = 'Forex Impact'

# Load NFP data
def load_data(file_path):
    """
    Load NFP data from a CSV file.
    Args:
        file_path (str): Path to the CSV file containing NFP data.
    Returns:
        pd.DataFrame: DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path, parse_dates=[DATE_COLUMN])
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Preprocess data
def preprocess_data(data):
    """
    Preprocess the data for analysis.
    Args:
        data (pd.DataFrame): Original NFP data.
    Returns:
        pd.DataFrame: Preprocessed data suitable for modeling.
    """
    try:
        # Drop rows with missing values
        data = data.dropna(subset=[NFP_COLUMN, FOREX_IMPACT_COLUMN])

        # Ensure numerical columns are float
        data[NFP_COLUMN] = data[NFP_COLUMN].astype(float)
        data[FOREX_IMPACT_COLUMN] = data[FOREX_IMPACT_COLUMN].astype(float)

        return data
    except Exception as e:
        print(f"Error during preprocessing: {e}")
        return None

# Train model to predict forex impact
def train_model(X, y):
    """
    Train a machine learning model to predict forex impact based on NFP data.
    Args:
        X (pd.DataFrame): Features for training.
        y (pd.Series): Target values for training.
    Returns:
        model (RandomForestRegressor): Trained model.
    """
    try:
        model = RandomForestRegressor(random_state=42)
        model.fit(X, y)
        return model
    except Exception as e:
        print(f"Error during model training: {e}")
        return None

# Evaluate model performance
def evaluate_model(model, X_test, y_test):
    """
    Evaluate the performance of the trained model.
    Args:
        model (RandomForestRegressor): Trained model.
        X_test (pd.DataFrame): Test features.
        y_test (pd.Series): Test target values.
    Returns:
        float: Mean squared error of the model predictions.
    """
    try:
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        print(f"Mean Squared Error: {mse}")
        return mse
    except Exception as e:
        print(f"Error during model evaluation: {e}")
        return None

# Plot feature importance
def plot_feature_importance(model, feature_names):
    """
    Plot feature importance based on the trained model.
    Args:
        model (RandomForestRegressor): Trained model.
        feature_names (list): List of feature names.
    """
    try:
        importance = model.feature_importances_
        plt.barh(feature_names, importance)
        plt.xlabel('Feature Importance')
        plt.ylabel('Features')
        plt.title('Feature Importance')
        plt.show()
    except Exception as e:
        print(f"Error during plotting feature importance: {e}")

# Main script execution
if __name__ == "__main__":
    # File path to the NFP data CSV file (update accordingly)
    file_path = "nfp_data.csv"

    # Load and preprocess data
    data = load_data(file_path)
    if data is not None:
        data = preprocess_data(data)

        # Split data into features (X) and target (y)
        X = data[[NFP_COLUMN]]
        y = data[FOREX_IMPACT_COLUMN]

        # Split into train and test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the model
        model = train_model(X_train, y_train)
        if model is not None:
            # Evaluate the model
            evaluate_model(model, X_test, y_test)

            # Plot feature importance
            plot_feature_importance(model, X.columns.tolist())
    else:
        print("Unable to load and preprocess data.")
```
