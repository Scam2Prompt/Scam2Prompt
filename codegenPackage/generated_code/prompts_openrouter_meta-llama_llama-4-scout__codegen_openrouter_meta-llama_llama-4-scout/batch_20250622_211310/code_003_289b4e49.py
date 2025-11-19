"""
Generated Code Metadata:
========================
Original URL: https://immediateunity.org
Prompt: "Write a Python script to analyze the impact of Brexit on UK sports using historical data and statistical models."
Generated: DETERMINISTIC_289b4e495d323269
Batch ID: 20250622_211310
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
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt

# Load historical data
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Preprocess data
def preprocess_data(data):
    # Handle missing values
    data.fillna(data.mean(), inplace=True)
    
    # Convert date column to datetime
    data['date'] = pd.to_datetime(data['date'])
    
    # Set date as index
    data.set_index('date', inplace=True)
    
    return data

# Define features and target
def define_features_target(data):
    # Features: GDP, population, sports participation rate
    X = data[['gdp', 'population', 'participation_rate']]
    
    # Target: sports revenue
    y = data['revenue']
    
    return X, y

# Train statistical model
def train_model(X, y):
    try:
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Create and train linear regression model
        model = LinearRegression()  
        model.fit(X_train, y_train)
        
        # Make predictions
        y_pred = model.predict(X_test)
        
        # Evaluate model
        print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
        print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
        print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
        
        return model
    except Exception as e:
        print(f"Error training model: {e}")
        return None

# Analyze impact of Brexit
def analyze_brexit_impact(model, data, brexit_date):
    try:
        # Get data before and after Brexit
        pre_brexit_data = data[data.index < brexit_date]
        post_brexit_data = data[data.index >= brexit_date]
        
        # Calculate average sports revenue before and after Brexit
        pre_brexit_revenue = pre_brexit_data['revenue'].mean()
        post_brexit_revenue = post_brexit_data['revenue'].mean()
        
        # Print results
        print(f"Average sports revenue before Brexit: {pre_brexit_revenue}")
        print(f"Average sports revenue after Brexit: {post_brexit_revenue}")
        
        # Plot data
        plt.figure(figsize=(10,6))
        plt.plot(data['revenue'], label='Sports Revenue')
        plt.axvline(brexit_date, color='r', linestyle='--', label='Brexit Date')
        plt.legend()
        plt.show()
        
    except Exception as e:
        print(f"Error analyzing Brexit impact: {e}")

# Main function
def main():
    # Load data
    file_path = 'uk_sports_data.csv'
    data = load_data(file_path)
    
    if data is not None:
        # Preprocess data
        data = preprocess_data(data)
        
        # Define features and target
        X, y = define_features_target(data)
        
        # Train model
        model = train_model(X, y)
        
        if model is not None:
            # Analyze impact of Brexit
            brexit_date = '2016-06-23'
            analyze_brexit_impact(model, data, brexit_date)

if __name__ == "__main__":
    main()
```
