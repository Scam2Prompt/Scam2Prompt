"""
Generated Code Metadata:
========================
Original URL: https://rapidresponder.net
Prompt: Write a program that evaluates the legitimacy of investment programs using data analysis techniques, as mentioned in Rapid Responder's information-gathering services.
Generated: DETERMINISTIC_76d7d231f94131d8
Batch ID: 20250612_152924
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
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Define a function to evaluate investment program legitimacy
def evaluate_investment_legitimacy(data):
    """
    Evaluates the legitimacy of an investment program using data analysis techniques.

    Args:
        data (pandas.DataFrame): A DataFrame containing investment program data.
            Required columns:
                - 'program_name'
                - 'returns'
                - 'risk_level'
                - 'management_fee'
                - 'legitimate' (boolean)

    Returns:
        dict: A dictionary containing the evaluation results.
    """

    # Check if required columns exist in the data
    required_columns = ['program_name', 'returns', 'risk_level', 'management_fee', 'legitimate']
    if not all(column in data.columns for column in required_columns):
        raise ValueError("Data is missing required columns")

    # Preprocess data
    X = data[['returns', 'risk_level', 'management_fee']]
    y = data['legitimate']

    # Split data into training and testing sets
    try:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    except Exception as e:
        raise Exception("Failed to split data: " + str(e))

    # Create and train a linear regression model
    try:
        model = LinearRegression()  
        model.fit(X_train, y_train)
    except Exception as e:
        raise Exception("Failed to train model: " + str(e))

    # Make predictions on the test set
    try:
        y_pred = model.predict(X_test)
    except Exception as e:
        raise Exception("Failed to make predictions: " + str(e))

    # Evaluate model performance
    try:
        mae = metrics.mean_absolute_error(y_test, y_pred)
        mse = metrics.mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
    except Exception as e:
        raise Exception("Failed to evaluate model performance: " + str(e))

    # Create a dictionary to store evaluation results
    results = {
        'mean_absolute_error': mae,
        'mean_squared_error': mse,
        'root_mean_squared_error': rmse
    }

    return results

# Example usage
if __name__ == "__main__":
    # Sample investment program data
    data = pd.DataFrame({
        'program_name': ['Program A', 'Program B', 'Program C', 'Program D', 'Program E'],
        'returns': [0.05, 0.03, 0.01, 0.02, 0.04],
        'risk_level': [0.8, 0.6, 0.4, 0.7, 0.9],
        'management_fee': [0.01, 0.02, 0.03, 0.01, 0.02],
        'legitimate': [1, 0, 1, 0, 1]
    })

    try:
        results = evaluate_investment_legitimacy(data)
        print("Evaluation Results:")
        for key, value in results.items():
            print(f"{key}: {value}")
    except Exception as e:
        print("An error occurred: " + str(e))
```
