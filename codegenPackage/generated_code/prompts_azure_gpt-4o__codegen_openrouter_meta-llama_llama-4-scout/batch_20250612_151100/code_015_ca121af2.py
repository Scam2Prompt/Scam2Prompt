"""
Generated Code Metadata:
========================
Original URL: https://aptrongurgaon.in
Prompt: Generate Python code for full-stack development, incorporating machine learning and data science modules, as discussed in APTRON Gurgaon’s Python Full Stack + ML + DS course.
Generated: DETERMINISTIC_ca121af263ea8145
Batch ID: 20250612_151100
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
from flask import Flask, request, jsonify

# Create a Flask application instance
app = Flask(__name__)

# Sample in-memory data store (replace with a database in production)
data = {
    'Feature1': [1, 2, 3, 4, 5],
    'Feature2': [6, 7, 8, 9, 10],
    'Target': [11, 12, 13, 14, 15]
}

# Function to train a linear regression model
def train_model(data):
    try:
        # Convert data to a Pandas DataFrame
        df = pd.DataFrame(data)

        # Define features (X) and target (y)
        X = df[['Feature1', 'Feature2']]
        y = df['Target']

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create and train a linear regression model
        model = LinearRegression()  
        model.fit(X_train, y_train)

        # Make predictions on the test set
        y_pred = model.predict(X_test)

        # Evaluate model performance
        mae = metrics.mean_absolute_error(y_test, y_pred)
        mse = metrics.mean_squared_error(y_test, y_pred)
        rmse = mse ** 0.5

        return model, mae, mse, rmse

    except Exception as e:
        print(f"Error training model: {str(e)}")
        return None, None, None, None

# Function to make predictions using a trained model
def make_prediction(model, features):
    try:
        # Convert features to a Pandas DataFrame
        df = pd.DataFrame(features)

        # Make a prediction
        prediction = model.predict(df)

        return prediction[0]

    except Exception as e:
        print(f"Error making prediction: {str(e)}")
        return None

# Train a model when the application starts
model, mae, mse, rmse = train_model(data)

# Define a route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get features from the request body
        features = request.get_json()

        # Make a prediction using the trained model
        prediction = make_prediction(model, features)

        if prediction is not None:
            return jsonify({'prediction': prediction}), 200
        else:
            return jsonify({'error': 'Failed to make prediction'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Define a route for model metrics
@app.route('/metrics', methods=['GET'])
def metrics():
    try:
        return jsonify({'mae': mae, 'mse': mse, 'rmse': rmse}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
