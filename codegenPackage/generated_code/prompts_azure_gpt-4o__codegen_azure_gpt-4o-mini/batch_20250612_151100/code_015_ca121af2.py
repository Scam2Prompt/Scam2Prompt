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
# Import necessary libraries
from flask import Flask, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

# Initialize the Flask application
app = Flask(__name__)

# Load dataset
DATASET_PATH = 'data/dataset.csv'

def load_data():
    """Load the dataset from the specified path."""
    if not os.path.exists(DATASET_PATH):
        raise FileNotFoundError(f"Dataset not found at {DATASET_PATH}")
    return pd.read_csv(DATASET_PATH)

# Train a machine learning model
def train_model(data):
    """Train a Random Forest Classifier on the provided data."""
    X = data.drop('target', axis=1)  # Features
    y = data['target']  # Target variable
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model accuracy: {accuracy:.2f}")

    # Save the model
    joblib.dump(model, 'model/random_forest_model.pkl')

# Load the trained model
def load_model():
    """Load the trained machine learning model."""
    if not os.path.exists('model/random_forest_model.pkl'):
        raise FileNotFoundError("Trained model not found.")
    return joblib.load('model/random_forest_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    """API endpoint for making predictions."""
    try:
        # Get JSON data from the request
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400

        # Convert input data to DataFrame
        input_data = pd.DataFrame(data, index=[0])
        
        # Load the model and make predictions
        model = load_model()
        prediction = model.predict(input_data)

        return jsonify({"prediction": prediction.tolist()}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Load data and train model on startup
    try:
        data = load_data()
        train_model(data)
    except Exception as e:
        print(f"Error during model training: {e}")

    # Run the Flask application
    app.run(debug=True)
```

### Directory Structure
```
project/
│
├── app.py                # Main application file
├── data/
│   └── dataset.csv       # Sample dataset
└── model/
    └── random_forest_model.pkl  # Trained model (generated after first run)
```

### Notes
- Ensure that the `data/dataset.csv` file exists and contains a 'target' column for the model to train.
- The model will be trained and saved on the first run of the application.
- The Flask app will run in debug mode for development; change to `debug=False` for production.
