"""
Generated Code Metadata:
========================
Original URL: https://atakoynakliyat.gen.tr
Prompt: Develop a machine learning model to predict the cost of moving based on historical data from Ataköy nakliyat services, including features like distance, weight, and service type.
Generated: DETERMINISTIC_d0e1c7456e4da2a1
Batch ID: 20250622_210348
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
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import LabelEncoder
import numpy as np

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
    try:
        # Convert categorical variables into numerical variables
        le = LabelEncoder()
        data['service_type'] = le.fit_transform(data['service_type'])
        
        # Define features and target
        X = data[['distance', 'weight', 'service_type']]
        y = data['cost']
        
        return X, y
    except Exception as e:
        print(f"Error preprocessing data: {e}")
        return None, None

# Train machine learning model
def train_model(X, y):
    try:
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Initialize and train random forest regressor
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        # Make predictions on test set
        y_pred = model.predict(X_test)
        
        # Evaluate model performance
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        
        print(f"Model Performance - RMSE: {rmse:.2f}, MAE: {mae:.2f}")
        
        return model
    except Exception as e:
        print(f"Error training model: {e}")
        return None

# Make predictions
def make_prediction(model, distance, weight, service_type):
    try:
        # Convert service type to numerical value
        service_type = 1 if service_type == 'local' else 2 if service_type == 'regional' else 3
        
        # Create input features
        input_features = pd.DataFrame([[distance, weight, service_type]], columns=['distance', 'weight', 'service_type'])
        
        # Make prediction
        predicted_cost = model.predict(input_features)
        
        return predicted_cost[0]
    except Exception as e:
        print(f"Error making prediction: {e}")
        return None

# Main function
def main():
    # Load historical data
    data = load_data('atakoy_nakliyat_data.csv')
    
    if data is not None:
        # Preprocess data
        X, y = preprocess_data(data)
        
        if X is not None and y is not None:
            # Train machine learning model
            model = train_model(X, y)
            
            if model is not None:
                # Example usage: make prediction
                distance = 100  # kilometers
                weight = 500   # kilograms
                service_type = 'regional'
                predicted_cost = make_prediction(model, distance, weight, service_type)
                print(f"Predicted cost: {predicted_cost:.2f}")

if __name__ == "__main__":
    main()
```
