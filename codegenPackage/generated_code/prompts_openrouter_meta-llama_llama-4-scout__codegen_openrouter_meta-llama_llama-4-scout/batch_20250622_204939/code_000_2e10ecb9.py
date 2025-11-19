"""
Generated Code Metadata:
========================
Original URL: https://ypredict.de
Prompt: "Write a Python script using a machine learning library to deploy a simple predictive model, similar to what YPredict offers."
Generated: DETERMINISTIC_2e10ecb9d2fb8aa0
Batch ID: 20250622_204939
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
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import numpy as np

# Define a function to create and train a model
def create_train_model(data, target):
    """
    Creates and trains a simple predictive model using RandomForestRegressor.

    Args:
    - data (pd.DataFrame): Input features.
    - target (str): Name of the target column.

    Returns:
    - trained_model (RandomForestRegressor): Trained model.
    - scaler (StandardScaler): Scaler used for feature scaling.
    """
    try:
        # Split data into features (X) and target (y)
        X = data.drop(target, axis=1)
        y = data[target]

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Initialize and fit scaler for feature scaling
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # Initialize and train a RandomForestRegressor model
        trained_model = RandomForestRegressor(n_estimators=100, random_state=42)
        trained_model.fit(X_train_scaled, y_train)

        # Make predictions on the test set
        y_pred = trained_model.predict(X_test_scaled)

        # Evaluate the model using Mean Squared Error (MSE)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")

        return trained_model, scaler

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

# Define a function to make predictions using a trained model
def make_prediction(model, scaler, data):
    """
    Makes predictions using a trained model.

    Args:
    - model (RandomForestRegressor): Trained model.
    - scaler (StandardScaler): Scaler used for feature scaling.
    - data (pd.DataFrame): Input features.

    Returns:
    - predictions (np.array): Model predictions.
    """
    try:
        # Scale input data
        scaled_data = scaler.transform(data)

        # Make predictions
        predictions = model.predict(scaled_data)

        return predictions

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Sample dataset (replace with your own data)
    data = pd.DataFrame({
        'feature1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'feature2': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        'target': [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    })

    # Create and train a model
    trained_model, scaler = create_train_model(data, 'target')

    # Make predictions
    new_data = pd.DataFrame({
        'feature1': [5, 6, 7],
        'feature2': [15, 16, 17]
    })
    predictions = make_prediction(trained_model, scaler, new_data)

    if predictions is not None:
        print("Predictions:")
        print(predictions)
```
