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
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
import matplotlib.pyplot as plt

# Load historical demand data
def load_data(file_path):
    """
    Load historical demand data from a CSV file.
    
    Parameters:
    file_path (str): Path to the CSV file containing the data.
    
    Returns:
    pd.DataFrame: DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Preprocess the data
def preprocess_data(data):
    """
    Preprocess the data for modeling.
    
    Parameters:
    data (pd.DataFrame): DataFrame containing the raw data.
    
    Returns:
    pd.DataFrame: Preprocessed DataFrame ready for modeling.
    """
    # Handle missing values
    data.fillna(method='ffill', inplace=True)
    
    # Convert date column to datetime
    data['date'] = pd.to_datetime(data['date'])
    
    # Extract features from date
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.month
    data['day'] = data['date'].dt.day
    data['day_of_week'] = data['date'].dt.dayofweek
    
    # Drop unnecessary columns
    data.drop(columns=['date'], inplace=True)
    
    return data

# Train the predictive model
def train_model(X_train, y_train):
    """
    Train a Random Forest Regressor model.
    
    Parameters:
    X_train (pd.DataFrame): Features for training.
    y_train (pd.Series): Target variable for training.
    
    Returns:
    RandomForestRegressor: Trained model.
    """
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model using Mean Squared Error.
    
    Parameters:
    model (RandomForestRegressor): Trained model.
    X_test (pd.DataFrame): Features for testing.
    y_test (pd.Series): True target variable for testing.
    
    Returns:
    float: Mean Squared Error of the model.
    """
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    return mse

# Save the model to disk
def save_model(model, file_name):
    """
    Save the trained model to a file.
    
    Parameters:
    model (RandomForestRegressor): Trained model.
    file_name (str): Name of the file to save the model.
    """
    joblib.dump(model, file_name)

# Main function to execute the workflow
def main():
    # Load the data
    data = load_data('historical_demand_data.csv')
    if data is None:
        return
    
    # Preprocess the data
    processed_data = preprocess_data(data)
    
    # Define features and target variable
    X = processed_data.drop(columns=['demand'])
    y = processed_data['demand']
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model
    model = train_model(X_train, y_train)
    
    # Evaluate the model
    mse = evaluate_model(model, X_test, y_test)
    print(f"Mean Squared Error: {mse}")
    
    # Save the model
    save_model(model, 'demand_forecast_model.pkl')

    # Optional: Plot feature importances
    feature_importances = model.feature_importances_
    features = X.columns
    plt.barh(features, feature_importances)
    plt.xlabel('Feature Importance')
    plt.title('Feature Importances for Demand Forecasting')
    plt.show()

if __name__ == "__main__":
    main()
```
