"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alu-air.com
Prompt: Suggest an API for monitoring environmental sustainability metrics that aligns with the goals of alu-air©.
Generated: DETERMINISTIC_d8f9476233e2f7b9
Batch ID: 20250612_155002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

# Initialize the Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# In-memory database to store environmental metrics
# Example structure: {"carbon_emissions": 0.0, "energy_consumption": 0.0, "water_usage": 0.0}
metrics_data = {
    "carbon_emissions": 0.0,
    "energy_consumption": 0.0,
    "water_usage": 0.0
}

# Define API routes

@app.route('/api/v1/metrics', methods=['GET'])
def get_metrics():
    """
    Endpoint to fetch all environmental sustainability metrics.
    Returns:
        JSON object containing the current metrics.
    """
    logging.info("Fetching all environmental metrics.")
    return jsonify(metrics_data), 200


@app.route('/api/v1/metrics/<metric_name>', methods=['GET'])
def get_metric(metric_name):
    """
    Endpoint to fetch a specific metric by name.
    Args:
        metric_name (str): The name of the metric to retrieve.
    Returns:
        JSON object containing the metric value, or an error if the metric does not exist.
    """
    logging.info(f"Fetching metric: {metric_name}")
    if metric_name in metrics_data:
        return jsonify({metric_name: metrics_data[metric_name]}), 200
    else:
        logging.warning(f"Metric '{metric_name}' not found.")
        return jsonify({"error": "Metric not found"}), 404


@app.route('/api/v1/metrics', methods=['POST'])
def update_metrics():
    """
    Endpoint to update environmental sustainability metrics.
    Expects JSON payload containing metric names and their updated values.
    Returns:
        JSON object indicating success or error message.
    """
    try:
        data = request.get_json()
        if not data:
            raise ValueError("Invalid or missing JSON payload.")
        
        for key, value in data.items():
            if key in metrics_data:
                if not isinstance(value, (int, float)):
                    raise ValueError(f"Invalid value for metric '{key}'. Must be a number.")
                metrics_data[key] = value
                logging.info(f"Updated metric '{key}' to {value}.")
            else:
                logging.warning(f"Attempt to update non-existent metric '{key}'.")
                return jsonify({"error": f"Metric '{key}' does not exist."}), 400

        return jsonify({"message": "Metrics updated successfully."}), 200

    except ValueError as e:
        logging.error(str(e))
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500


# Start the Flask app
if __name__ == '__main__':
    # Ensure the app runs on port 5000 for local testing
    app.run(debug=True, host='0.0.0.0', port=5000)
```
