"""
Generated Code Metadata:
========================
Original URL: https://digitaldhara.com
Prompt: Create a data analysis script that leverages advanced analytics techniques to extract insights from large datasets, as outlined by Digital Dhara.
Generated: DETERMINISTIC_46b1573a999e7b03
Batch ID: 20250612_155905
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
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

def load_data(file_path):
    """
    Load data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.

    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
        pd.errors.ParserError: If the file is malformed.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("The file does not exist")
        return None
    except pd.errors.EmptyDataError:
        print("The file is empty")
        return None
    except pd.errors.ParserError:
        print("Error parsing the file")
        return None

def clean_data(data):
    """
    Clean the data by handling missing values and encoding categorical variables.

    Args:
        data (pd.DataFrame): Data to be cleaned.

    Returns:
        pd.DataFrame: Cleaned data.
    """
    # Handle missing values
    data.fillna(data.mean(), inplace=True)
    
    # Encode categorical variables
    categorical_cols = data.select_dtypes(include=['object']).columns
    data[categorical_cols] = data[categorical_cols].apply(lambda x: pd.factorize(x)[0])
    
    return data

def split_data(data, target_variable):
    """
    Split the data into training and testing sets.

    Args:
        data (pd.DataFrame): Data to be split.
        target_variable (str): Target variable.

    Returns:
        tuple: Training features, testing features, training target, testing target.
    """
    # Split the data into features and target
    X = data.drop(target_variable, axis=1)
    y = data[target_variable]
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test

def linear_regression(X_train, X_test, y_train, y_test):
    """
    Perform linear regression.

    Args:
        X_train (pd.DataFrame): Training features.
        X_test (pd.DataFrame): Testing features.
        y_train (pd.Series): Training target.
        y_test (pd.Series): Testing target.

    Returns:
        dict: Coefficients and evaluation metrics.
    """
    # Create a linear regression model
    model = LinearRegression()  
    
    # Train the model
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    mae = metrics.mean_absolute_error(y_test, y_pred)
    mse = metrics.mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    
    return {
        'coefficients': model.coef_,
        'mae': mae,
        'mse': mse,
        'rmse': rmse
    }

def random_forest_regression(X_train, X_test, y_train, y_test):
    """
    Perform random forest regression.

    Args:
        X_train (pd.DataFrame): Training features.
        X_test (pd.DataFrame): Testing features.
        y_train (pd.Series): Training target.
        y_test (pd.Series): Testing target.

    Returns:
        dict: Evaluation metrics.
    """
    # Define hyperparameter tuning space
    param_grid = {
        'n_estimators': [100, 200, 300],
        'max_depth': [None, 5, 10]
    }
    
    # Create a random forest regressor
    model = RandomForestRegressor(random_state=42)
    
    # Perform hyperparameter tuning
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5)
    grid_search.fit(X_train, y_train)
    
    # Make predictions
    y_pred = grid_search.predict(X_test)
    
    # Evaluate the model
    mae = metrics.mean_absolute_error(y_test, y_pred)
    mse = metrics.mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    
    return {
        'mae': mae,
        'mse': mse,
        'rmse': rmse
    }

def main():
    # Load data
    file_path = 'data.csv'  # replace with your file path
    data = load_data(file_path)
    
    if data is not None:
        # Clean data
        data = clean_data(data)
        
        # Split data
        target_variable = 'target'  # replace with your target variable
        X_train, X_test, y_train, y_test = split_data(data, target_variable)
        
        # Perform linear regression
        linear_regression_results = linear_regression(X_train, X_test, y_train, y_test)
        print("Linear Regression Results:")
        print(f"Coefficients: {linear_regression_results['coefficients']}")
        print(f"MAE: {linear_regression_results['mae']}")
        print(f"MSE: {linear_regression_results['mse']}")
        print(f"RMSE: {linear_regression_results['rmse']}")
        
        # Perform random forest regression
        random_forest_regression_results = random_forest_regression(X_train, X_test, y_train, y_test)
        print("\nRandom Forest Regression Results:")
        print(f"MAE: {random_forest_regression_results['mae']}")
        print(f"MSE: {random_forest_regression_results['mse']}")
        print(f"RMSE: {random_forest_regression_results['rmse']}")

if __name__ == "__main__":
    main()
```
