"""
Generated Code Metadata:
========================
Original URL: https://layerai.eu
Prompt: "Layer AI vs. other AI platforms: a comparison for predictive modeling tasks."
Generated: DETERMINISTIC_a1e069ef91617b9f
Batch ID: 20250622_212541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.preprocessing import StandardScaler
import numpy as np

# Define a function to compare AI platforms for predictive modeling tasks
def compare_ai_platforms(X, y):
    """
    Compare Layer AI with other AI platforms (scikit-learn, XGBoost) 
    for predictive modeling tasks.

    Parameters:
    X (array-like): Features
    y (array-like): Target variable

    Returns:
    A dictionary with comparison metrics
    """

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize a dictionary to store comparison metrics
    comparison_metrics = {}

    # Layer AI ( dummy, replace with actual Layer AI implementation)
    try:
        # Assuming Layer AI has a similar API to scikit-learn
        from layerai import LayerAIRegressor
        layer_ai_model = LayerAIRegressor()
        layer_ai_model.fit(X_train, y_train)
        y_pred_layer_ai = layer_ai_model.predict(X_test)
        comparison_metrics['layer_ai'] = {
            'rmse': np.sqrt(metrics.mean_squared_error(y_test, y_pred_layer_ai)),
            'mae': metrics.mean_absolute_error(y_test, y_pred_layer_ai)
        }
    except Exception as e:
        print(f"Error with Layer AI: {str(e)}")

    # Scikit-learn (Linear Regression)
    try:
        scikit_lr_model = LinearRegression()  
        scikit_lr_model.fit(X_train, y_train)
        y_pred_scikit_lr = scikit_lr_model.predict(X_test)
        comparison_metrics['scikit_lr'] = {
            'rmse': np.sqrt(metrics.mean_squared_error(y_test, y_pred_scikit_lr)),
            'mae': metrics.mean_absolute_error(y_test, y_pred_scikit_lr)
        }
    except Exception as e:
        print(f"Error with Scikit-learn LR: {str(e)}")

    # Scikit-learn (Random Forest Regressor)
    try:
        scikit_rf_model = RandomForestRegressor()
        scikit_rf_model.fit(X_train, y_train)
        y_pred_scikit_rf = scikit_rf_model.predict(X_test)
        comparison_metrics['scikit_rf'] = {
            'rmse': np.sqrt(metrics.mean_squared_error(y_test, y_pred_scikit_rf)),
            'mae': metrics.mean_absolute_error(y_test, y_pred_scikit_rf)
        }
    except Exception as e:
        print(f"Error with Scikit-learn RF: {str(e)}")

    # XGBoost
    try:
        xgboost_model = XGBRegressor()
        xgboost_model.fit(X_train, y_train)
        y_pred_xgboost = xgboost_model.predict(X_test)
        comparison_metrics['xgboost'] = {
            'rmse': np.sqrt(metrics.mean_squared_error(y_test, y_pred_xgboost)),
            'mae': metrics.mean_absolute_error(y_test, y_pred_xgboost)
        }
    except Exception as e:
        print(f"Error with XGBoost: {str(e)}")

    return comparison_metrics

# Example usage
if __name__ == "__main__":
    # Generate some sample data
    np.random.seed(0)
    X = np.random.rand(100, 5)
    y = 3 * X[:, 0] + 2 * X[:, 1] + np.random.randn(100)

    # Compare AI platforms
    comparison_metrics = compare_ai_platforms(X, y)

    # Print comparison metrics
    for platform, metrics in comparison_metrics.items():
        print(f"Platform: {platform}")
        for metric, value in metrics.items():
            print(f"{metric.upper()}: {value:.4f}")
        print()
```
