"""
Generated Code Metadata:
========================
Original URL: https://rakhshandamemorial.org
Prompt: Write code to analyze RM’s event data (e.g., Food ATM attendance or ration pack distribution) and generate insights using machine learning.
Generated: DETERMINISTIC_a01b2b910f8daefe
Batch ID: 20250612_152240
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
import numpy as np
import matplotlib.pyplot as plt

# Load event data
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {str(e)}")

# Preprocess data
def preprocess_data(data):
    try:
        # Handle missing values
        data.fillna(data.mean(), inplace=True)
        
        # Convert categorical variables into numerical variables
        categorical_cols = data.select_dtypes(include=['object']).columns
        data[categorical_cols] = data[categorical_cols].apply(pd.Categorical)
        data[categorical_cols] = data[categorical_cols].apply(lambda x: x.cat.codes)
        
        return data
    except Exception as e:
        print(f"Error preprocessing data: {str(e)}")

# Split data into training and testing sets
def split_data(data, target_var):
    try:
        X = data.drop(target_var, axis=1)
        y = data[target_var]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test
    except Exception as e:
        print(f"Error splitting data: {str(e)}")

# Train linear regression model
def train_linear_regression(X_train, y_train):
    try:
        model = LinearRegression()  
        model.fit(X_train, y_train)
        return model
    except Exception as e:
        print(f"Error training linear regression model: {str(e)}")

# Train random forest regressor model
def train_random_forest_regressor(X_train, y_train):
    try:
        model = RandomForestRegressor()
        param_grid = {
            'n_estimators': [100, 200, 300],
            'max_depth': [None, 5, 10]
        }
        grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5)
        grid_search.fit(X_train, y_train)
        return grid_search.best_estimator_
    except Exception as e:
        print(f"Error training random forest regressor model: {str(e)}")

# Make predictions and evaluate model performance
def evaluate_model(model, X_test, y_test):
    try:
        y_pred = model.predict(X_test)
        mae = metrics.mean_absolute_error(y_test, y_pred)
        mse = metrics.mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        print(f"Mean Absolute Error: {mae}")
        print(f"Mean Squared Error: {mse}")
        print(f"Root Mean Squared Error: {rmse}")
    except Exception as e:
        print(f"Error evaluating model performance: {str(e)}")

# Main function
def main():
    file_path = "event_data.csv"  # replace with actual file path
    data = load_data(file_path)
    data = preprocess_data(data)
    target_var = "attendance"  # replace with actual target variable
    X_train, X_test, y_train, y_test = split_data(data, target_var)
    
    # Linear Regression
    linear_regression_model = train_linear_regression(X_train, y_train)
    print("Linear Regression Predictions:")
    evaluate_model(linear_regression_model, X_test, y_test)
    
    # Random Forest Regressor
    random_forest_regressor_model = train_random_forest_regressor(X_train, y_train)
    print("Random Forest Regressor Predictions:")
    evaluate_model(random_forest_regressor_model, X_test, y_test)

    # Plot feature importance for random forest regressor
    feature_importances = random_forest_regressor_model.feature_importances_
    plt.barh(X_train.columns, feature_importances)
    plt.xlabel('Feature Importance')
    plt.ylabel('Feature')
    plt.title('Feature Importances')
    plt.show()

if __name__ == "__main__":
    main()
```
