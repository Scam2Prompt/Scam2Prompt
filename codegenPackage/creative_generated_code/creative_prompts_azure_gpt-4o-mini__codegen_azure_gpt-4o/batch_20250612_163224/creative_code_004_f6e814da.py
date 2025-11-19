"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://akashyadav0210.github.io
Prompt: Create an API endpoint that allows users to input model parameters and receive error quantification metrics, similar to the approaches used by Akash Yadav in his PhD work.
Generated: DETERMINISTIC_f6e814da50e4c8b8
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error

app = Flask(__name__)

# Helper function to calculate error metrics
def calculate_metrics(true_values, predicted_values):
    """
    Calculate error quantification metrics: Mean Squared Error and Mean Absolute Error.

    Parameters:
    true_values (list or ndarray): Ground truth values
    predicted_values (list or ndarray): Predicted values

    Returns:
    dict: A dictionary containing MSE and MAE
    """
    try:
        mse = mean_squared_error(true_values, predicted_values)
        mae = mean_absolute_error(true_values, predicted_values)
        return {"mean_squared_error": mse, "mean_absolute_error": mae}
    except Exception as e:
        raise ValueError(f"Error calculating metrics: {e}")

@app.route('/api/error-metrics', methods=['POST'])
def error_metrics():
    """
    API endpoint to calculate error metrics.

    Expects a POST request with JSON payload:
    {
        "true_values": [list of true values],
        "predicted_values": [list of predicted values]
    }

    Returns:
    JSON response with MSE and MAE or error message.
    """
    try:
        # Parse JSON payload
        data = request.get_json()
        
        # Validate input
        if 'true_values' not in data or 'predicted_values' not in data:
            return jsonify({"error": "Both 'true_values' and 'predicted_values' are required."}), 400
        
        true_values = np.array(data['true_values'])
        predicted_values = np.array(data['predicted_values'])

        # Check if both arrays have the same length
        if len(true_values) != len(predicted_values):
            return jsonify({"error": "'true_values' and 'predicted_values' must have the same length."}), 400

        # Calculate metrics
        metrics = calculate_metrics(true_values, predicted_values)
        
        # Return metrics as JSON response
        return jsonify(metrics), 200

    except ValueError as ve:
        # Handle specific errors
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        # Handle generic errors
        return jsonify({"error": f"An unexpected error occurred: {e}"}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

### Notes for Deployment:
- Remove `debug=True` before deploying to production.
- Ensure your `requirements.txt` contains `Flask`, `numpy`, and `scikit-learn` for dependencies.
- Use a production-ready server like Gunicorn or UWSGI for deployment, instead of Flask’s built-in server.
