"""
Generated Code Metadata:
========================
Original URL: https://kiberahamlets.org
Prompt: How can machine learning models be used to predict the effectiveness of programs like Kibera Hamlets' Girl Empowerment Programme in reducing early marriage and teenage pregnancy rates?
Generated: DETERMINISTIC_5bc68b42151b57cb
Batch ID: 20250622_210914
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

# Define a function to load and preprocess data
def load_data(file_path):
    """
    Loads data from a CSV file and performs basic preprocessing.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Preprocessed data.
    """
    try:
        # Load data
        data = pd.read_csv(file_path)

        # Handle missing values
        data.fillna(data.mean(), inplace=True)

        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Define a function to train a linear regression model
def train_linear_regression_model(data):
    """
    Trains a linear regression model to predict effectiveness.

    Args:
        data (pd.DataFrame): Preprocessed data.

    Returns:
        LinearRegression: Trained model.
    """
    try:
        # Define features and target
        X = data.drop(['effectiveness'], axis=1)
        y = data['effectiveness']

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train model
        model = LinearRegression()  
        model.fit(X_train, y_train)

        # Make predictions
        y_pred = model.predict(X_test)

        # Evaluate model
        print('Linear Regression Model Evaluation:')
        print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
        print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
        print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

        return model
    except Exception as e:
        print(f"Error training linear regression model: {e}")
        return None

# Define a function to train a random forest regressor model
def train_random_forest_model(data):
    """
    Trains a random forest regressor model to predict effectiveness.

    Args:
        data (pd.DataFrame): Preprocessed data.

    Returns:
        RandomForestRegressor: Trained model.
    """
    try:
        # Define features and target
        X = data.drop(['effectiveness'], axis=1)
        y = data['effectiveness']

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Define hyperparameter tuning space
        param_grid = {
            'n_estimators': [100, 200, 300],
            'max_depth': [None, 5, 10]
        }

        # Perform hyperparameter tuning
        model = GridSearchCV(RandomForestRegressor(), param_grid, cv=5)
        model.fit(X_train, y_train)

        # Make predictions
        y_pred = model.predict(X_test)

        # Evaluate model
        print('Random Forest Model Evaluation:')
        print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
        print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
        print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

        return model
    except Exception as e:
        print(f"Error training random forest model: {e}")
        return None

# Load data
data = load_data('kibera_data.csv')

# Train linear regression model
linear_model = train_linear_regression_model(data)

# Train random forest model
random_forest_model = train_random_forest_model(data)
```
