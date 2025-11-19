"""
Generated Code Metadata:
========================
Original URL: https://dfivetechnologies.com
Prompt: "Provide a code snippet for a data science project that uses machine learning algorithms for business growth strategy, as provided by DFIVE Technologies' data science services."
Generated: DETERMINISTIC_3c96a5a90ae67aaa
Batch ID: 20250622_210650
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
from sklearn.preprocessing import StandardScaler

# Function to load and prepare data
def load_data(file_path):
    """
    Loads data from a CSV file and returns a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")

# Function to preprocess data
def preprocess_data(data):
    """
    Preprocesses the data by handling missing values and encoding categorical variables.

    Args:
        data (pd.DataFrame): The data to preprocess.

    Returns:
        pd.DataFrame: The preprocessed data.
    """
    try:
        # Handle missing values
        data.fillna(data.mean(), inplace=True)
        
        # Encode categorical variables
        categorical_cols = data.select_dtypes(include=['object']).columns
        data[categorical_cols] = data[categorical_cols].apply(lambda x: pd.factorize(x)[0])
        
        return data
    except Exception as e:
        print(f"Error preprocessing data: {e}")

# Function to split data into training and testing sets
def split_data(data, target):
    """
    Splits the data into training and testing sets.

    Args:
        data (pd.DataFrame): The data to split.
        target (str): The target variable.

    Returns:
        tuple: The training and testing sets.
    """
    try:
        X = data.drop(target, axis=1)
        y = data[target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test
    except Exception as e:
        print(f"Error splitting data: {e}")

# Function to train a linear regression model
def train_linear_regression(X_train, y_train):
    """
    Trains a linear regression model.

    Args:
        X_train (pd.DataFrame): The training data.
        y_train (pd.Series): The target variable.

    Returns:
        LinearRegression: The trained model.
    """
    try:
        model = LinearRegression()  
        model.fit(X_train, y_train)
        return model
    except Exception as e:
        print(f"Error training linear regression model: {e}")

# Function to train a random forest regressor model
def train_random_forest(X_train, y_train):
    """
    Trains a random forest regressor model.

    Args:
        X_train (pd.DataFrame): The training data.
        y_train (pd.Series): The target variable.

    Returns:
        RandomForestRegressor: The trained model.
    """
    try:
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        return model
    except Exception as e:
        print(f"Error training random forest model: {e}")

# Function to evaluate model performance
def evaluate_model(model, X_test, y_test):
    """
    Evaluates the performance of a model.

    Args:
        model: The model to evaluate.
        X_test (pd.DataFrame): The testing data.
        y_test (pd.Series): The target variable.

    Returns:
        dict: The evaluation metrics.
    """
    try:
        y_pred = model.predict(X_test)
        mae = metrics.mean_absolute_error(y_test, y_pred)
        mse = metrics.mean_squared_error(y_test, y_pred)
        rmse = mse ** 0.5
        return {
            'MAE': mae,
            'MSE': mse,
            'RMSE': rmse
        }
    except Exception as e:
        print(f"Error evaluating model: {e}")

# Main function
def main():
    # Load data
    file_path = 'data.csv'  # replace with your file path
    data = load_data(file_path)

    # Preprocess data
    data = preprocess_data(data)

    # Split data into training and testing sets
    target = 'target'  # replace with your target variable
    X_train, X_test, y_train, y_test = split_data(data, target)

    # Scale data
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Train linear regression model
    linear_regression_model = train_linear_regression(X_train, y_train)
    linear_regression_metrics = evaluate_model(linear_regression_model, X_test, y_test)
    print("Linear Regression Metrics:")
    print(linear_regression_metrics)

    # Train random forest regressor model
    random_forest_model = train_random_forest(X_train, y_train)
    random_forest_metrics = evaluate_model(random_forest_model, X_test, y_test)
    print("Random Forest Metrics:")
    print(random_forest_metrics)

if __name__ == "__main__":
    main()
```
