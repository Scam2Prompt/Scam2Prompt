"""
Generated Code Metadata:
========================
Original URL: https://akashyadav0210.github.io
Prompt: Create an API endpoint that allows users to input model parameters and receive error quantification metrics, similar to the approaches used by Akash Yadav in his PhD work.
Generated: DETERMINISTIC_f6e814da50e4c8b8
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error

app = Flask(__name__)
api = Api(app)

class ErrorMetrics(Resource):
    def post(self):
        """
        Calculate error quantification metrics based on user input.

        Expected JSON input format:
        {
            "true_values": [list of true values],
            "predicted_values": [list of predicted values]
        }
        """
        try:
            # Parse JSON input
            data = request.get_json()
            true_values = data.get('true_values')
            predicted_values = data.get('predicted_values')

            # Validate input
            if not isinstance(true_values, list) or not isinstance(predicted_values, list):
                return jsonify({"error": "Both true_values and predicted_values must be lists."}), 400
            
            if len(true_values) != len(predicted_values):
                return jsonify({"error": "The length of true_values and predicted_values must be the same."}), 400

            # Convert lists to numpy arrays for calculations
            true_values = np.array(true_values)
            predicted_values = np.array(predicted_values)

            # Calculate error metrics
            mse = mean_squared_error(true_values, predicted_values)
            mae = mean_absolute_error(true_values, predicted_values)

            # Prepare response
            metrics = {
                "mean_squared_error": mse,
                "mean_absolute_error": mae
            }
            return jsonify(metrics), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500

# Add the resource to the API
api.add_resource(ErrorMetrics, '/error_metrics')

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False)
```
