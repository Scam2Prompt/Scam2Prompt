"""
Generated Code Metadata:
========================
Original URL: https://aptrongurgaon.in
Prompt: Create a Python script for predictive analytics, incorporating machine learning and data science techniques from APTRON Gurgaon’s training programs.
Generated: DETERMINISTIC_4a292d208e16d68e
Batch ID: 20250612_151100
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
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler

# Function to load data
def load_data(file_path):
    """
    Load data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pandas.DataFrame: Loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {str(e)}")

# Function to prepare data
def prepare_data(data, target_variable):
    """
    Prepare data for training by splitting it into features and target.

    Args:
        data (pandas.DataFrame): Data to prepare.
        target_variable (str): Name of the target variable.

    Returns:
        tuple: Features and target.
    """
    try:
        X = data.drop(target_variable, axis=1)
        y = data[target_variable]
        return X, y
    except Exception as e:
        print(f"Error preparing data: {str(e)}")

# Function to train linear regression model
def train_linear_regression(X_train, y_train):
    """
    Train a linear regression model.

    Args:
        X_train (pandas.DataFrame): Training features.
        y_train (pandas.Series): Training target.

    Returns:
        sklearn.linear_model.LinearRegression: Trained model.
    """
    try:
        model = LinearRegression()  
        model.fit(X_train, y_train)
        return model
    except Exception as e:
        print(f"Error training linear regression model: {str(e)}")

# Function to train random forest regressor model
def train_random_forest_regressor(X_train, y_train):
    """
    Train a random forest regressor model.

    Args:
        X_train (pandas.DataFrame): Training features.
        y_train (pandas.Series): Training target.

    Returns:
        sklearn.ensemble.RandomForestRegressor: Trained model.
    """
    try:
        model = RandomForestRegressor()
        model.fit(X_train, y_train)
        return model
    except Exception as e:
        print(f"Error training random forest regressor model: {str(e)}")

# Function to tune random forest regressor model
def tune_random_forest_regressor(X_train, y_train):
    """
    Tune a random forest regressor model using grid search.

    Args:
        X_train (pandas.DataFrame): Training features.
        y_train (pandas.Series): Training target.

    Returns:
        sklearn.ensemble.RandomForestRegressor: Tuned model.
    """
    try:
        param_grid = {
            'n_estimators': [100, 200, 300],
            'max_depth': [None, 5, 10],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 5, 10]
        }
        model = RandomForestRegressor()
        grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5)
        grid_search.fit(X_train, y_train)
        return grid_search.best_estimator_
    except Exception as e:
        print(f"Error tuning random forest regressor model: {str(e)}")

# Function to evaluate model
def evaluate_model(model, X_test, y_test):
    """
    Evaluate a model's performance.

    Args:
        model: Trained model.
        X_test (pandas.DataFrame): Testing features.
        y_test (pandas.Series): Testing target.
    """
    try:
        y_pred = model.predict(X_test)
        print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
        print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
        print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
    except Exception as e:
        print(f"Error evaluating model: {str(e)}")

# Main function
def main():
    # Load data
    file_path = 'data.csv'  # replace with your file path
    data = load_data(file_path)

    # Prepare data
    target_variable = 'target'  # replace with your target variable
    X, y = prepare_data(data, target_variable)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale data
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Train linear regression model
    linear_regression_model = train_linear_regression(X_train, y_train)
    print("Linear Regression Model Performance:")
    evaluate_model(linear_regression_model, X_test, y_test)

    # Train random forest regressor model
    random_forest_regressor_model = train_random_forest_regressor(X_train, y_train)
    print("Random Forest Regressor Model Performance:")
    evaluate_model(random_forest_regressor_model, X_test, y_test)

    # Tune random forest regressor model
    tuned_random_forest_regressor_model = tune_random_forest_regressor(X_train, y_train)
    print("Tuned Random Forest Regressor Model Performance:")
    evaluate_model(tuned_random_forest_regressor_model, X_test, y_test)

if __name__ == "__main__":
    import numpy as np
    main()
```
