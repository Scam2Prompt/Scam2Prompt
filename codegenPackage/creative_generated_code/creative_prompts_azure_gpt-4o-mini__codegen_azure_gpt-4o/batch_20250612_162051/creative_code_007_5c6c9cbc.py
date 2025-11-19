"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cemnazmakine.com
Prompt: Explain how to use machine learning to optimize the operation of a potato processing facility, focusing on the frying and cooling stages.
Generated: DETERMINISTIC_5c6c9cbc8723f19d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This program demonstrates the use of machine learning to optimize the frying and cooling stages 
of a potato processing facility. The code uses a regression model to predict the optimal frying 
temperature and cooling duration based on input parameters (e.g., potato weight, moisture content, 
desired crispiness). 

Libraries used:
- NumPy (for numerical operations)
- Pandas (for data manipulation)
- scikit-learn (for machine learning model creation and training)
"""

# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def train_model(data_path):
    """
    Trains a machine learning model to optimize operation parameters in the potato processing facility.

    :param data_path: Path to the input dataset (CSV file) containing historical frying and cooling data.
    :return: Trained model and feature columns.
    """
    try:
        # Load the data
        data = pd.read_csv(data_path)
        
        # Ensure the dataset contains the necessary columns
        required_columns = ['potato_weight', 'moisture_content', 'desired_crispiness', 
                            'frying_temperature', 'cooling_duration']
        if not all(col in data.columns for col in required_columns):
            raise ValueError(f"The dataset must contain the following columns: {required_columns}")

        # Separate features (input variables) and target (output variables)
        X = data[['potato_weight', 'moisture_content', 'desired_crispiness']]
        y = data[['frying_temperature', 'cooling_duration']]

        # Split the dataset into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train a Random Forest Regressor (can be replaced with other algorithms)
        model = RandomForestRegressor(random_state=42)
        model.fit(X_train, y_train)

        # Evaluate the model's performance
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print(f"Model training completed. Mean Squared Error on test set: {mse:.2f}")

        # Return the trained model and the feature set
        return model, X.columns.tolist()

    except FileNotFoundError:
        print("Error: The specified dataset file was not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def predict_optimal_parameters(model, feature_columns, potato_weight, moisture_content, desired_crispiness):
    """
    Uses the trained model to predict optimal frying temperature and cooling duration.

    :param model: Trained machine learning model.
    :param feature_columns: List of feature column names used during model training.
    :param potato_weight: Weight of the potato batch (in kilograms).
    :param moisture_content: Moisture content of the potato batch (percentage).
    :param desired_crispiness: Desired level of crispiness (scale of 1 to 10).
    :return: Predicted frying temperature and cooling duration.
    """
    try:
        # Create input data for prediction
        input_data = pd.DataFrame([[potato_weight, moisture_content, desired_crispiness]], 
                                  columns=feature_columns)

        # Use the model to predict frying temperature and cooling duration
        prediction = model.predict(input_data)
        frying_temperature, cooling_duration = prediction[0]
        
        print(f"Optimal Frying Temperature: {frying_temperature:.2f} °C")
        print(f"Optimal Cooling Duration: {cooling_duration:.2f} minutes")

        return frying_temperature, cooling_duration

    except Exception as e:
        print(f"An error occurred during prediction: {e}")

# Example usage
if __name__ == "__main__":
    # Train the model using historical data (provide the actual path to your dataset)
    trained_model, feature_cols = train_model("potato_processing_data.csv")

    if trained_model:
        # Predict optimal parameters for a new batch of potatoes
        predict_optimal_parameters(trained_model, feature_cols, 
                                   potato_weight=50, 
                                   moisture_content=20, 
                                   desired_crispiness=7)
```
