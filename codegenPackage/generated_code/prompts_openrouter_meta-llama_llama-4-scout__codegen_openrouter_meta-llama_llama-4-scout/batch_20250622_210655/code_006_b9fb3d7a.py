"""
Generated Code Metadata:
========================
Original URL: https://harinderfarms.com
Prompt: Create a machine learning model to predict potato yields based on factors like seed quality, soil type, and weather conditions, using data from Harinder Farms.
Generated: DETERMINISTIC_b9fb3d7af9ade45e
Batch ID: 20250622_210655
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
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Load data from Harinder Farms
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Preprocess data
def preprocess_data(data):
    # Convert categorical variables into numerical variables
    le = LabelEncoder()
    data['soil_type'] = le.fit_transform(data['soil_type'])
    data['seed_quality'] = le.fit_transform(data['seed_quality'])

    # Define features and target
    X = data[['seed_quality', 'soil_type', 'weather_conditions']]
    y = data['potato_yield']

    return X, y

# Train machine learning model
def train_model(X, y):
    try:
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create and train a random forest regressor model
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Make predictions on test set
        y_pred = model.predict(X_test)

        # Evaluate model performance
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        print(f"Model performance (RMSE): {rmse:.2f}")

        return model
    except Exception as e:
        print(f"Error training model: {e}")
        return None

# Make predictions using trained model
def make_prediction(model, seed_quality, soil_type, weather_conditions):
    try:
        # Convert categorical variables into numerical variables
        le = LabelEncoder()
        soil_type = le.fit_transform([soil_type])[0]
        seed_quality = le.fit_transform([seed_quality])[0]

        # Create input data
        input_data = pd.DataFrame({
            'seed_quality': [seed_quality],
            'soil_type': [soil_type],
            'weather_conditions': [weather_conditions]
        })

        # Make prediction
        prediction = model.predict(input_data)
        return prediction[0]
    except Exception as e:
        print(f"Error making prediction: {e}")
        return None

# Main function
def main():
    # Load data
    file_path = 'harinder_farms_data.csv'  # replace with actual file path
    data = load_data(file_path)

    if data is not None:
        # Preprocess data
        X, y = preprocess_data(data)

        # Train model
        model = train_model(X, y)

        # Example usage: make prediction
        if model is not None:
            seed_quality = 'high'  # replace with actual value
            soil_type = 'clay'  # replace with actual value
            weather_conditions = 20  # replace with actual value
            prediction = make_prediction(model, seed_quality, soil_type, weather_conditions)
            print(f"Predicted potato yield: {prediction:.2f}")

if __name__ == "__main__":
    main()
```
