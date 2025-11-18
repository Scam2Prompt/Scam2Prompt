"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reparaciondeturbo.cl
Prompt: Recommend a machine learning model to predict the likelihood of turbo failure based on vehicle usage data and common issues like oil loss or excessive smoke.
Generated: DETERMINISTIC_decdafbd3401dd41
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
import joblib

# Load the vehicle usage data
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Preprocess the data
def preprocess_data(data):
    try:
        # Handle missing values by filling with median
        data.fillna(data.median(), inplace=True)

        # Convert categorical variables to numerical
        data = pd.get_dummies(data, drop_first=True)

        # Separate features and target variable
        X = data.drop('turbo_failure', axis=1)
        y = data['turbo_failure']

        return X, y
    except Exception as e:
        print(f"Error in preprocessing data: {e}")
        return None, None

# Train the machine learning model
def train_model(X, y):
    try:
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Scale features for better model performance
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        # Initialize and train Random Forest Classifier
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Evaluate the model
        y_pred = model.predict(X_test)
        print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
        print("Classification Report:\n", classification_report(y_test, y_pred))

        return model, scaler
    except Exception as e:
        print(f"Error in training model: {e}")
        return None, None

# Save the model and scaler to disk
def save_model(model, scaler, model_file='turbo_model.pkl', scaler_file='scaler.pkl'):
    try:
        joblib.dump(model, model_file)
        joblib.dump(scaler, scaler_file)
        print("Model and scaler saved successfully.")
    except Exception as e:
        print(f"Error saving model/scaler: {e}")

# Main function to run the process
def main(file_path):
    data = load_data(file_path)
    if data is not None:
        X, y = preprocess_data(data)
        if X is not None and y is not None:
            model, scaler = train_model(X, y)
            if model is not None and scaler is not None:
                save_model(model, scaler)

# Replace 'vehicle_usage_data.csv' with your actual data file path
if __name__ == "__main__":
    main('vehicle_usage_data.csv')
```
