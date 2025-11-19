"""
Generated Code Metadata:
========================
Original URL: https://plm.cr
Prompt: "Develop a predictive model using machine learning to forecast demand for logistics services in Costa Rica, based on historical data and trends, as PLM might use to optimize their operations."
Generated: DETERMINISTIC_7629ae29f109be55
Batch ID: 20250622_210243
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
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load historical data
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")

# Preprocess data
def preprocess_data(data):
    # Convert date column to datetime
    data['date'] = pd.to_datetime(data['date'])
    
    # Extract relevant features
    data['day_of_week'] = data['date'].dt.dayofweek
    data['month'] = data['date'].dt.month
    data['year'] = data['date'].dt.year
    
    # Drop unnecessary columns
    data.drop(['date'], axis=1, inplace=True)
    
    return data

# Split data into training and testing sets
def split_data(data):
    X = data.drop(['demand'], axis=1)
    y = data['demand']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test

# Train linear regression model
def train_linear_regression(X_train, y_train):
    try:
        model = LinearRegression()  
        model.fit(X_train, y_train)
        return model
    except Exception as e:
        print(f"Error training linear regression model: {e}")

# Train random forest model with hyperparameter tuning
def train_random_forest(X_train, y_train):
    try:
        param_grid = {
            'n_estimators': [100, 200, 300],
            'max_depth': [None, 5, 10]
        }
        
        model = RandomForestRegressor(random_state=42)
        grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5)
        grid_search.fit(X_train, y_train)
        
        return grid_search.best_estimator_
    except Exception as e:
        print(f"Error training random forest model: {e}")

# Make predictions and evaluate model performance
def evaluate_model(model, X_test, y_test):
    try:
        y_pred = model.predict(X_test)
        
        # Evaluate model performance
        mae = metrics.mean_absolute_error(y_test, y_pred)
        mse = metrics.mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        
        print(f"Mean Absolute Error: {mae}")
        print(f"Mean Squared Error: {mse}")
        print(f"Root Mean Squared Error: {rmse}")
        
        # Plot predicted vs actual values
        plt.scatter(y_test, y_pred)
        plt.xlabel('Actual Demand')
        plt.ylabel('Predicted Demand')
        plt.show()
    except Exception as e:
        print(f"Error evaluating model: {e}")

# Main function
def main():
    # Load historical data
    file_path = 'logistics_demand_data.csv'  # replace with actual file path
    data = load_data(file_path)
    
    # Preprocess data
    data = preprocess_data(data)
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = split_data(data)
    
    # Scale data
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    # Train and evaluate linear regression model
    linear_regression_model = train_linear_regression(X_train, y_train)
    print("Linear Regression Model Performance:")
    evaluate_model(linear_regression_model, X_test, y_test)
    
    # Train and evaluate random forest model
    random_forest_model = train_random_forest(X_train, y_train)
    print("Random Forest Model Performance:")
    evaluate_model(random_forest_model, X_test, y_test)

if __name__ == "__main__":
    main()
```
