"""
Generated Code Metadata:
========================
Original URL: https://ypredict.de
Prompt: "Write a Python script using a machine learning library to deploy a simple predictive model, similar to what YPredict offers."
Generated: DETERMINISTIC_2e10ecb9d2fb8aa0
Batch ID: 20250622_204939
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
A Python script to deploy a simple predictive model using scikit-learn.
This script trains a linear regression model on sample data, saves the model,
and provides a simple API endpoint for predictions using Flask.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pickle
from flask import Flask, request, jsonify

# Step 1: Generate sample data
def generate_sample_data():
    """
    Generates sample data for training a linear regression model.
    Returns:
        X (numpy array): Feature matrix
        y (numpy array): Target vector
    """
    np.random.seed(42)
    X = np.random.rand(100, 1) * 10  # Random numbers between 0 and 10
    y = 2.5 * X + np.random.randn(100, 1) * 2  # Linear relationship with noise
    return X, y

# Step 2: Train the model
def train_model(X, y):
    """
    Trains a linear regression model on the provided data.
    Args:
        X (numpy array): Feature matrix
        y (numpy array): Target vector
    Returns:
        model (LinearRegression): Trained linear regression model
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Model trained successfully. Mean Squared Error: {mse:.2f}")
    
    return model

# Step 3: Save the model
def save_model(model, filename="model.pkl"):
    """
    Saves the trained model to a file using pickle.
    Args:
        model (LinearRegression): Trained model
        filename (str): File name to save the model
    """
    with open(filename, "wb") as file:
        pickle.dump(model, file)
    print(f"Model saved to {filename}")

# Step 4: Load the model
def load_model(filename="model.pkl"):
    """
    Loads a trained model from a file using pickle.
    Args:
        filename (str): File name to load the model from
    Returns:
        model (LinearRegression): Loaded model
    """
    with open(filename, "rb") as file:
        model = pickle.load(file)
    print(f"Model loaded from {filename}")
    return model

# Step 5: Create a Flask API for predictions
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    """
    API endpoint to make predictions using the trained model.
    Expects JSON input with a key "features" containing a list of feature values.
    Returns:
        JSON response with predictions or error message.
    """
    try:
        # Load the model
        model = load_model()
        
        # Parse input data
        data = request.get_json()
        features = data.get("features")
        if features is None:
            return jsonify({"error": "Missing 'features' in request data"}), 400
        
        # Convert features to numpy array and make predictions
        features = np.array(features).reshape(-1, 1)
        predictions = model.predict(features).tolist()
        
        return jsonify({"predictions": predictions})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main script execution
if __name__ == "__main__":
    # Generate data, train model, and save it
    X, y = generate_sample_data()
    model = train_model(X, y)
    save_model(model)
    
    # Run the Flask app
    print("Starting Flask API server...")
    app.run(debug=True)
```
