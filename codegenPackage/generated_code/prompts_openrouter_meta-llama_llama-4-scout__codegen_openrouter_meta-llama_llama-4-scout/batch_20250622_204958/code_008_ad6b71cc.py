"""
Generated Code Metadata:
========================
Original URL: https://natureexcursionsafaris.com
Prompt: Implement a machine learning model to predict the best time for a safari in Tanzania based on historical weather and wildlife migration data.
Generated: DETERMINISTIC_ad6b71cc25fa70b9
Batch ID: 20250622_204958
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
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

# Load historical weather data
def load_weather_data(file_path):
    """Load historical weather data from a CSV file."""
    try:
        weather_data = pd.read_csv(file_path)
        return weather_data
    except Exception as e:
        print(f"Error loading weather data: {e}")
        return None

# Load historical wildlife migration data
def load_migration_data(file_path):
    """Load historical wildlife migration data from a CSV file."""
    try:
        migration_data = pd.read_csv(file_path)
        return migration_data
    except Exception as e:
        print(f"Error loading migration data: {e}")
        return None

# Merge weather and migration data
def merge_data(weather_data, migration_data):
    """Merge weather and migration data based on date."""
    try:
        merged_data = pd.merge(weather_data, migration_data, on='date')
        return merged_data
    except Exception as e:
        print(f"Error merging data: {e}")
        return None

# Preprocess data
def preprocess_data(merged_data):
    """Preprocess data by handling missing values and scaling features."""
    try:
        # Handle missing values
        merged_data.fillna(merged_data.mean(), inplace=True)
        
        # Scale features
        scaler = StandardScaler()
        merged_data[['temperature', 'humidity', 'wind_speed']] = scaler.fit_transform(merged_data[['temperature', 'humidity', 'wind_speed']])
        return merged_data
    except Exception as e:
        print(f"Error preprocessing data: {e}")
        return None

# Split data into training and testing sets
def split_data(preprocessed_data):
    """Split preprocessed data into training and testing sets."""
    try:
        X = preprocessed_data.drop(['migration_date'], axis=1)
        y = preprocessed_data['migration_date']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test
    except Exception as e:
        print(f"Error splitting data: {e}")
        return None

# Train a random forest regressor model
def train_model(X_train, y_train):
    """Train a random forest regressor model."""
    try:
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        return model
    except Exception as e:
        print(f"Error training model: {e}")
        return None

# Make predictions and evaluate the model
def evaluate_model(model, X_test, y_test):
    """Make predictions and evaluate the model using mean squared error."""
    try:
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print(f"Mean Squared Error: {mse}")
    except Exception as e:
        print(f"Error evaluating model: {e}")

# Main function
def main():
    # Load data
    weather_data = load_weather_data('weather_data.csv')
    migration_data = load_migration_data('migration_data.csv')
    
    # Merge data
    merged_data = merge_data(weather_data, migration_data)
    
    # Preprocess data
    preprocessed_data = preprocess_data(merged_data)
    
    # Split data
    X_train, X_test, y_train, y_test = split_data(preprocessed_data)
    
    # Train model
    model = train_model(X_train, y_train)
    
    # Evaluate model
    evaluate_model(model, X_test, y_test)

    # Use the trained model to make a prediction
    def predict_best_time(model, weather_data):
        """Use the trained model to predict the best time for a safari."""
        try:
            weather_data[['temperature', 'humidity', 'wind_speed']] = StandardScaler().fit_transform(weather_data[['temperature', 'humidity', 'wind_speed']])
            prediction = model.predict(weather_data)
            return prediction
        except Exception as e:
            print(f"Error making prediction: {e}")
            return None

    # Example usage
    example_weather_data = pd.DataFrame({
        'temperature': [25],
        'humidity': [60],
        'wind_speed': [10]
    })
    best_time = predict_best_time(model, example_weather_data)
    print(f"Predicted best time for a safari: {best_time}")

if __name__ == "__main__":
    main()
```
