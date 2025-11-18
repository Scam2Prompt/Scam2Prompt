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
# Import necessary libraries
from flask import Flask, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

# Initialize Flask application
app = Flask(__name__)

# Set the path for model storage
MODEL_PATH = 'model/rf_model.pkl'

# Load or train the model
def load_or_train_model():
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)
    else:
        # Load dataset (ensure you have a CSV file named 'data.csv' in the current directory)
        try:
            data = pd.read_csv('data.csv')
            X = data.drop('target', axis=1)  # Features
            y = data['target']                # Target variable
            
            # Split data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Train the Random Forest model
            model = RandomForestClassifier()
            model.fit(X_train, y_train)

            # Save the model
            joblib.dump(model, MODEL_PATH)

            # Evaluate model performance
            y_pred = model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            print(f'Model trained with accuracy: {accuracy:.2f}')
        except Exception as e:
            print(f"Error while loading or training the model: {e}")
            model = None

    return model

# Initialize model
model = load_or_train_model()

# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve JSON data from the request
        data = request.json
        
        # Validate input data
        if not data or 'features' not in data:
            return jsonify({'error': 'Invalid input data'}), 400
        
        # Convert features to DataFrame
        features = pd.DataFrame(data['features'])
        
        # Make predictions
        predictions = model.predict(features)
        
        # Return predictions as JSON
        return jsonify({'predictions': predictions.tolist()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Entry point for the application
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Note:
- Ensure you have the necessary packages installed (`flask`, `pandas`, `scikit-learn`, `joblib`).
- The code expects a CSV file named `data.csv` with a target column named `target` and relevant features. Adjust the code accordingly to fit your dataset structure.
- Adjust the model, features, and response structure to match your specific application requirements.
