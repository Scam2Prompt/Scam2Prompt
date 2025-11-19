"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Suggest tools or libraries to implement a scientific validation system for DBT therapy outcomes, such as reducing self-harm and suicidal ideation, based on the claims made on the Mente Sana Psicología site.
Generated: DETERMINISTIC_6139cc38e29a0354
Batch ID: 20250612_153225
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
from sklearn.model_selection import cross_val_score
import numpy as np

# Define a function to load and preprocess data
def load_data(file_path):
    """
    Load and preprocess data for DBT therapy outcomes.

    Args:
    file_path (str): Path to the data file.

    Returns:
    pandas.DataFrame: Preprocessed data.
    """
    try:
        # Load data from file
        data = pd.read_csv(file_path)

        # Handle missing values
        data.fillna(data.mean(), inplace=True)

        return data

    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Define a function to evaluate DBT therapy outcomes
def evaluate_dbt_outcomes(data):
    """
    Evaluate DBT therapy outcomes using linear regression and random forest regressor.

    Args:
    data (pandas.DataFrame): Preprocessed data.

    Returns:
    dict: Dictionary containing evaluation metrics.
    """
    try:
        # Define features and target variable
        X = data.drop(['self_harm', 'suicidal_ideation'], axis=1)
        y_self_harm = data['self_harm']
        y_suicidal_ideation = data['suicidal_ideation']

        # Split data into training and testing sets
        X_train, X_test, y_train_self_harm, y_test_self_harm = train_test_split(X, y_self_harm, test_size=0.2, random_state=42)
        _, _, y_train_suicidal_ideation, y_test_suicidal_ideation = train_test_split(X, y_suicidal_ideation, test_size=0.2, random_state=42)

        # Linear Regression Model for self_harm
        model_self_harm = LinearRegression()  
        model_self_harm.fit(X_train, y_train_self_harm)
        y_pred_self_harm = model_self_harm.predict(X_test)

        # Linear Regression Model for suicidal_ideation
        model_suicidal_ideation = LinearRegression()  
        model_suicidal_ideation.fit(X_train, y_train_suicidal_ideation)
        y_pred_suicidal_ideation = model_suicidal_ideation.predict(X_test)

        # Random Forest Regressor Model for self_harm
        model_rf_self_harm = RandomForestRegressor()
        model_rf_self_harm.fit(X_train, y_train_self_harm)
        y_pred_rf_self_harm = model_rf_self_harm.predict(X_test)

        # Random Forest Regressor Model for suicidal_ideation
        model_rf_suicidal_ideation = RandomForestRegressor()
        model_rf_suicidal_ideation.fit(X_train, y_train_suicidal_ideation)
        y_pred_rf_suicidal_ideation = model_rf_suicidal_ideation.predict(X_test)

        # Evaluation metrics for self_harm
        mae_self_harm_lr = metrics.mean_absolute_error(y_test_self_harm, y_pred_self_harm)
        rmse_self_harm_lr = np.sqrt(metrics.mean_squared_error(y_test_self_harm, y_pred_self_harm))

        mae_self_harm_rf = metrics.mean_absolute_error(y_test_self_harm, y_pred_rf_self_harm)
        rmse_self_harm_rf = np.sqrt(metrics.mean_squared_error(y_test_self_harm, y_pred_rf_self_harm))

        # Evaluation metrics for suicidal_ideation
        mae_suicidal_ideation_lr = metrics.mean_absolute_error(y_test_suicidal_ideation, y_pred_suicidal_ideation)
        rmse_suicidal_ideation_lr = np.sqrt(metrics.mean_squared_error(y_test_suicidal_ideation, y_pred_suicidal_ideation))

        mae_suicidal_ideation_rf = metrics.mean_absolute_error(y_test_suicidal_ideation, y_pred_rf_suicidal_ideation)
        rmse_suicidal_ideation_rf = np.sqrt(metrics.mean_squared_error(y_test_suicidal_ideation, y_pred_rf_suicidal_ideation))

        # Cross-validation
        scores_self_harm_lr = cross_val_score(model_self_harm, X, y_self_harm, cv=5, scoring='neg_mean_absolute_error')
        scores_suicidal_ideation_lr = cross_val_score(model_suicidal_ideation, X, y_suicidal_ideation, cv=5, scoring='neg_mean_absolute_error')

        scores_self_harm_rf = cross_val_score(model_rf_self_harm, X, y_self_harm, cv=5, scoring='neg_mean_absolute_error')
        scores_suicidal_ideation_rf = cross_val_score(model_rf_suicidal_ideation, X, y_suicidal_ideation, cv=5, scoring='neg_mean_absolute_error')

        # Return evaluation metrics
        return {
            "self_harm_lr": {
                "mae": mae_self_harm_lr,
                "rmse": rmse_self_harm_lr,
                "cv_scores": scores_self_harm_lr
            },
            "self_harm_rf": {
                "mae": mae_self_harm_rf,
                "rmse": rmse_self_harm_rf,
                "cv_scores": scores_self_harm_rf
            },
            "suicidal_ideation_lr": {
                "mae": mae_suicidal_ideation_lr,
                "rmse": rmse_suicidal_ideation_lr,
                "cv_scores": scores_suicidal_ideation_lr
            },
            "suicidal_ideation_rf": {
                "mae": mae_suicidal_ideation_rf,
                "rmse": rmse_suicidal_ideation_rf,
                "cv_scores": scores_suicidal_ideation_rf
            }
        }

    except Exception as e:
        print(f"Error evaluating DBT therapy outcomes: {e}")
        return None

# Example usage
if __name__ == "__main__":
    file_path = "dbt_therapy_outcomes.csv"  # replace with actual file path
    data = load_data(file_path)
    if data is not None:
        evaluation_metrics = evaluate_dbt_outcomes(data)
        print(evaluation_metrics)
```
