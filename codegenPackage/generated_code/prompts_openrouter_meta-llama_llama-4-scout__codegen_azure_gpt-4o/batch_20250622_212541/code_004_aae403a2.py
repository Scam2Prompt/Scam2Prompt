"""
Generated Code Metadata:
========================
Original URL: https://stronglp.com
Prompt: Suggest a suitable machine learning model for predicting athlete performance improvements based on factors like training sessions, age, and fitness level.
Generated: DETERMINISTIC_aae403a2a03ee013
Batch ID: 20250622_212541
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
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Define a function to train and evaluate a machine learning model
def predict_athlete_performance(data):
    """
    Predict athlete performance improvements based on training sessions, age, and fitness level.

    Parameters:
        data (pd.DataFrame): Input data containing features and target variable.

    Returns:
        dict: A dictionary containing model performance metrics (R2 score and RMSE).
    """
    try:
        # Ensure the input data has the required columns
        required_columns = ['training_sessions', 'age', 'fitness_level', 'performance_improvement']
        if not all(col in data.columns for col in required_columns):
            raise ValueError(f"Input data must contain the following columns: {required_columns}")

        # Split the data into features (X) and target (y)
        X = data[['training_sessions', 'age', 'fitness_level']]
        y = data['performance_improvement']

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create a pipeline with preprocessing and model
        pipeline = Pipeline([
            ('scaler', StandardScaler()),  # Standardize features
            ('model', RandomForestRegressor(random_state=42))  # Random Forest Regressor
        ])

        # Train the model
        pipeline.fit(X_train, y_train)

        # Make predictions on the test set
        y_pred = pipeline.predict(X_test)

        # Calculate performance metrics
        r2 = r2_score(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))

        # Return the performance metrics
        return {
            'R2 Score': r2,
            'RMSE': rmse
        }

    except Exception as e:
        # Handle exceptions and provide meaningful error messages
        print(f"An error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Create a sample dataset
    sample_data = pd.DataFrame({
        'training_sessions': [10, 15, 20, 25, 30],
        'age': [20, 25, 30, 35, 40],
        'fitness_level': [3, 4, 5, 6, 7],
        'performance_improvement': [1.2, 1.5, 1.8, 2.0, 2.3]
    })

    # Predict athlete performance improvements
    metrics = predict_athlete_performance(sample_data)

    # Print the results
    if metrics:
        print("Model Performance Metrics:")
        print(f"R2 Score: {metrics['R2 Score']:.2f}")
        print(f"RMSE: {metrics['RMSE']:.2f}")
```
