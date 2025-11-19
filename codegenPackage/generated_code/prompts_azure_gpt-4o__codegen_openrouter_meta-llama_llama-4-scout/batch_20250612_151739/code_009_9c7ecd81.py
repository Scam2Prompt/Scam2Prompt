"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: Suggest libraries or frameworks for creating a training module in "Coordination SPS," similar to the training programs mentioned in collaboration with AFCO AURA.
Generated: DETERMINISTIC_9c7ecd81bfbc95e7
Batch ID: 20250612_151739
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
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """
    Load data from a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The loaded data.

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
        print("The file is malformed")
        return None

def preprocess_data(data):
    """
    Preprocess the data by handling missing values and encoding categorical variables.

    Args:
        data (pd.DataFrame): The data to preprocess.

    Returns:
        pd.DataFrame: The preprocessed data.
    """
    # Handle missing values
    data.fillna(data.mean(), inplace=True)
    
    # Encode categorical variables
    categorical_cols = data.select_dtypes(include=['object']).columns
    data[categorical_cols] = data[categorical_cols].apply(lambda x: pd.factorize(x)[0])
    
    return data

def split_data(data, target):
    """
    Split the data into training and testing sets.

    Args:
        data (pd.DataFrame): The data to split.
        target (str): The target variable.

    Returns:
        tuple: The training features, testing features, training target, and testing target.
    """
    X = data.drop(target, axis=1)
    y = data[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    """
    Train a linear regression model and a random forest regressor.

    Args:
        X_train (pd.DataFrame): The training features.
        y_train (pd.DataFrame): The training target.

    Returns:
        tuple: The trained linear regression model and random forest regressor.
    """
    # Train a linear regression model
    lr_model = LinearRegression()  
    lr_model.fit(X_train, y_train)

    # Train a random forest regressor
    rf_model = RandomForestRegressor()
    rf_model.fit(X_train, y_train)

    return lr_model, rf_model

def tune_hyperparameters(X_train, y_train):
    """
    Tune the hyperparameters of a random forest regressor using grid search.

    Args:
        X_train (pd.DataFrame): The training features.
        y_train (pd.DataFrame): The training target.

    Returns:
        RandomForestRegressor: The tuned random forest regressor.
    """
    # Define hyperparameter tuning space
    param_grid = {
        'n_estimators': [100, 200, 300],
        'max_depth': [None, 5, 10],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 5, 10]
    }

    # Perform grid search
    grid_search = GridSearchCV(RandomForestRegressor(), param_grid, cv=5, scoring='neg_mean_squared_error')
    grid_search.fit(X_train, y_train)

    return grid_search.best_estimator_

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the performance of a model.

    Args:
        model: The model to evaluate.
        X_test (pd.DataFrame): The testing features.
        y_test (pd.DataFrame): The testing target.

    Returns:
        dict: The evaluation metrics.
    """
    y_pred = model.predict(X_test)
    mae = metrics.mean_absolute_error(y_test, y_pred)
    mse = metrics.mean_squared_error(y_test, y_pred)
    rmse = mse ** 0.5
    return {'MAE': mae, 'MSE': mse, 'RMSE': rmse}

def main():
    # Load data
    file_path = 'coordination_sps_data.csv'  # replace with your file path
    data = load_data(file_path)

    if data is not None:
        # Preprocess data
        data = preprocess_data(data)

        # Split data
        target = 'target_variable'  # replace with your target variable
        X_train, X_test, y_train, y_test = split_data(data, target)

        # Scale data
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        # Train models
        lr_model, rf_model = train_model(X_train, y_train)

        # Tune hyperparameters
        tuned_rf_model = tune_hyperparameters(X_train, y_train)

        # Evaluate models
        lr_metrics = evaluate_model(lr_model, X_test, y_test)
        rf_metrics = evaluate_model(rf_model, X_test, y_test)
        tuned_rf_metrics = evaluate_model(tuned_rf_model, X_test, y_test)

        # Print evaluation metrics
        print('Linear Regression Metrics:')
        for metric, value in lr_metrics.items():
            print(f'{metric}: {value}')

        print('\nRandom Forest Regressor Metrics:')
        for metric, value in rf_metrics.items():
            print(f'{metric}: {value}')

        print('\nTuned Random Forest Regressor Metrics:')
        for metric, value in tuned_rf_metrics.items():
            print(f'{metric}: {value}')

if __name__ == '__main__':
    main()
```
