"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptrongurgaon.in
Prompt: Generate Python code for full-stack development, incorporating machine learning and data science modules, as discussed in APTRON Gurgaon’s Python Full Stack + ML + DS course.
Generated: DETERMINISTIC_ca121af263ea8145
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Full-Stack Python Development with Machine Learning and Data Science Modules

# Import necessary libraries for backend, ML, and DS
from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import traceback

# Initialize a Flask app for backend
app = Flask(__name__)

# Define a global variable for the ML model
model = None

# Route for the home page
@app.route('/')
def home():
    return "Welcome to the Python Full-Stack + ML + DS Application!"

# Route for training the machine learning model
@app.route('/train', methods=['POST'])
def train_model():
    """
    Train a Machine Learning model using uploaded CSV data.
    Expected input: JSON with 'file_path' pointing to a CSV file.
    """
    try:
        # Parse request data
        data = request.get_json()
        file_path = data.get('file_path')

        # Load dataset
        df = pd.read_csv(file_path)
        
        # Verify the dataset has a 'target' column for supervised learning
        if 'target' not in df.columns:
            return jsonify({"error": "Dataset must have a 'target' column."}), 400

        # Features and target
        X = df.drop(columns=['target'])
        y = df['target']

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train RandomForest classifier
        global model
        model = RandomForestClassifier(random_state=42)
        model.fit(X_train, y_train)

        # Evaluate the model
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        # Save the trained model to a file
        joblib.dump(model, 'model.pkl')

        return jsonify({"message": "Model trained successfully!", "accuracy": accuracy}), 200

    except Exception as e:
        # Handle exceptions and provide error information
        return jsonify({"error": str(e), "stacktrace": traceback.format_exc()}), 500

# Route for predicting using the trained model
@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict outcomes using the trained ML model.
    Expected input: JSON with 'features' containing a list of feature values.
    """
    try:
        # Parse request data
        data = request.get_json()
        features = data.get('features')

        # Verify that a model has been trained
        global model
        if model is None:
            # Load the model if not already loaded
            model = joblib.load('model.pkl')

        # Convert features to a NumPy array for prediction
        features_array = np.array(features).reshape(1, -1)
        prediction = model.predict(features_array)

        return jsonify({"prediction": prediction.tolist()}), 200

    except Exception as e:
        # Handle exceptions and provide error information
        return jsonify({"error": str(e), "stacktrace": traceback.format_exc()}), 500

# Route for performing basic data science operations (e.g., summary statistics)
@app.route('/data-summary', methods=['POST'])
def data_summary():
    """
    Generate summary statistics for a dataset.
    Expected input: JSON with 'file_path' pointing to a CSV file.
    """
    try:
        # Parse request data
        data = request.get_json()
        file_path = data.get('file_path')

        # Load dataset
        df = pd.read_csv(file_path)

        # Generate summary statistics
        summary = df.describe(include='all').to_dict()

        return jsonify({"summary": summary}), 200

    except Exception as e:
        # Handle exceptions and provide error information
        return jsonify({"error": str(e), "stacktrace": traceback.format_exc()}), 500

# Run the Flask app
if __name__ == '__main__':
    # Start the development server
    app.run(debug=True)
```
