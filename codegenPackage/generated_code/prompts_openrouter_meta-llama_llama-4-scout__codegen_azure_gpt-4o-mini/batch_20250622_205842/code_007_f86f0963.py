"""
Generated Code Metadata:
========================
Original URL: https://openmse.com
Prompt: Write a code snippet to calculate performance metrics for an MSE using openMSE, and how do I examine the results?
Generated: DETERMINISTIC_f86f09634a916de8
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import openMSE as mse
import pandas as pd

def calculate_mse_performance_metrics(data: pd.DataFrame, target_column: str) -> dict:
    """
    Calculate performance metrics for a Mean Squared Error (MSE) model using openMSE.

    Parameters:
    data (pd.DataFrame): The input data containing features and target variable.
    target_column (str): The name of the target column in the DataFrame.

    Returns:
    dict: A dictionary containing performance metrics.
    """
    try:
        # Ensure the target column exists in the DataFrame
        if target_column not in data.columns:
            raise ValueError(f"Target column '{target_column}' not found in the DataFrame.")

        # Split the data into features and target
        X = data.drop(columns=[target_column])
        y = data[target_column]

        # Initialize the MSE model
        model = mse.MSE()

        # Fit the model
        model.fit(X, y)

        # Make predictions
        predictions = model.predict(X)

        # Calculate performance metrics
        mse_value = mse.mean_squared_error(y, predictions)
        r_squared = mse.r2_score(y, predictions)

        # Return the performance metrics
        return {
            'Mean Squared Error': mse_value,
            'R-squared': r_squared
        }

    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

# Example usage
if __name__ == "__main__":
    # Load your dataset (ensure to replace 'your_data.csv' with your actual data file)
    try:
        data = pd.read_csv('your_data.csv')
        metrics = calculate_mse_performance_metrics(data, target_column='target')
        print("Performance Metrics:", metrics)
    except FileNotFoundError:
        print("The specified data file was not found.")
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
```
