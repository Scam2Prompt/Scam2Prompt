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
from flask_restful import Api, Resource
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np

app = Flask(__name__)
api = Api(app)

class ErrorMetrics(Resource):
    def post(self):
        """
        Calculate error metrics based on user-provided model parameters and predictions.

        Expects a JSON body with the following structure:
        {
            "y_true": [list of true values],
            "y_pred": [list of predicted values]
        }
        Returns a JSON object containing the calculated metrics.
        """

        try:
            # Parse the JSON request body
            data = request.get_json()

            # Validate the input data
            if 'y_true' not in data or 'y_pred' not in data:
                return {"error": "Both 'y_true' and 'y_pred' must be provided."}, 400
            
            y_true = data['y_true']
            y_pred = data['y_pred']

            # Validate that both lists are of the same length
            if len(y_true) != len(y_pred):
                return {"error": "The length of 'y_true' and 'y_pred' must be the same."}, 400
            
            # Calculate error metrics
            mse = mean_squared_error(y_true, y_pred)
            mae = mean_absolute_error(y_true, y_pred)

            # Prepare the response
            metrics = {
                "mean_squared_error": mse,
                "mean_absolute_error": mae,
            }
            return jsonify(metrics)

        except ValueError as ve:
            return {"error": str(ve)}, 400
        except Exception as e:
            return {"error": "An unexpected error occurred: " + str(e)}, 500

# Define the API resource routing
api.add_resource(ErrorMetrics, '/api/error_metrics')

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=False, host='0.0.0.0', port=5000)
```
