"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.linea.ai
Prompt: Provide an example of using Disarray to build on collective knowledge from previous experiments and avoid redundant computations in ML workflows.
Generated: DETERMINISTIC_7f34f548f81fd3f9
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from disarray import Disarray
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Initialize Disarray database for storing experiment results
# This allows us to track and reuse prior computations to avoid redundancy
db = Disarray("ml_workflows.db")  # Create or connect to the database file

# Define a function to check prior results and compute new ones if necessary
def train_and_evaluate(model_name, features, targets):
    """
    Train a machine learning model and evaluate its performance.

    Args:
        model_name (str): A unique identifier for the model (e.g., 'linear_regression').
        features (ndarray): Feature matrix for training/testing.
        targets (ndarray): Target values for training/testing.

    Returns:
        dict: Results including model coefficients and mean squared error.
    """
    # Check if the model's result is already stored in Disarray
    prior_result = db.get(model_name=model_name, features_hash=np.hash(features), targets_hash=np.hash(targets))
    if prior_result:
        print("Using cached result to avoid redundant computation.")
        return prior_result

    # Train the model if no prior result is available
    print("No prior result found, training the model...")
    model = LinearRegression()
    model.fit(features, targets)
    predictions = model.predict(features)
    mse = mean_squared_error(targets, predictions)

    # Store the result in Disarray for future reuse
    result = {
        "model_name": model_name,
        "coefficients": model.coef_.tolist(),
        "mean_squared_error": mse
    }
    db.add(result, model_name=model_name, features_hash=np.hash(features), targets_hash=np.hash(targets))

    return result

# Example usage
if __name__ == "__main__":
    # Simulated dataset
    X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    y = np.array([1, 2, 3, 4])

    # Train and evaluate a linear regression model
    result = train_and_evaluate("linear_regression_v1", X, y)
    print("Result:", result)

    # Attempt to reuse the computation with the same dataset
    cached_result = train_and_evaluate("linear_regression_v1", X, y)
    print("Cached Result:", cached_result)
```
