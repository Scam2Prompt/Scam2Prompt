"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reparaciondeturbo.cl
Prompt: Recommend a machine learning model to predict the likelihood of turbo failure based on vehicle usage data and common issues like oil loss or excessive smoke.
Generated: DETERMINISTIC_decdafbd3401dd41
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.exceptions import NotFittedError

# Define a function to recommend and train a machine learning model
def predict_turbo_failure(data: pd.DataFrame):
    """
    Predict the likelihood of turbo failure based on vehicle usage data.

    Parameters:
        data (pd.DataFrame): A DataFrame containing vehicle usage data and labels.
                             Assumes the last column is the target (turbo failure).

    Returns:
        dict: A dictionary containing model performance metrics.
    """
    try:
        # Validate input DataFrame
        if data.empty:
            raise ValueError("Input DataFrame is empty.")

        # Separate features and target
        X = data.iloc[:, :-1]  # Features (vehicle usage data)
        y = data.iloc[:, -1]   # Target (turbo failure: 0 or 1)

        # Split the data into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        # Create a pipeline with a scaler and a Random Forest classifier
        model_pipeline = Pipeline([
            ('scaler', StandardScaler()),  # Standardize features
            ('classifier', RandomForestClassifier(
                n_estimators=100, random_state=42, class_weight='balanced'))
        ])

        # Train the model
        model_pipeline.fit(X_train, y_train)

        # Make predictions
        y_pred = model_pipeline.predict(X_test)

        # Calculate performance metrics
        metrics = {
            "accuracy": accuracy_score(y_test, y_pred),
            "precision": precision_score(y_test, y_pred),
            "recall": recall_score(y_test, y_pred),
            "f1_score": f1_score(y_test, y_pred)
        }

        return metrics

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except NotFittedError as nfe:
        print(f"NotFittedError: The model is not fitted. {nfe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage (replace with actual data):
if __name__ == "__main__":
    # Example DataFrame structure: replace this with real vehicle usage data
    example_data = pd.DataFrame({
        'mileage': [12000, 25000, 36000, 45000, 54000],
        'oil_loss': [1, 0, 1, 1, 0],
        'excessive_smoke': [0, 1, 1, 0, 1],
        'turbo_failure': [0, 1, 1, 0, 1]  # Target column
    })

    # Predict and print model metrics
    results = predict_turbo_failure(example_data)
    if results:
        print("Model Performance Metrics:")
        for metric, value in results.items():
            print(f"{metric}: {value:.4f}")
```
