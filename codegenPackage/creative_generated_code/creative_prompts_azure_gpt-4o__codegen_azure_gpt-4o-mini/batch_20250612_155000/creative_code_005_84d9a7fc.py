"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ntes.me
Prompt: Suggest an Ethereum 2.0 API for querying real-time blockchain metrics and demonstrate how to integrate it into a web application.
Generated: DETERMINISTIC_84d9a7fccef1676c
Batch ID: 20250612_155000
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://beaconcha.in/api/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify
import requests

# Initialize Flask application
app = Flask(__name__)

# Ethereum 2.0 API endpoint for querying real-time blockchain metrics
ETH2_API_URL = "https://beaconcha.in/api/v1"

# Define a function to fetch Ethereum 2.0 metrics
def fetch_eth2_metrics():
    try:
        # Send a GET request to the Ethereum 2.0 API
        response = requests.get(f"{ETH2_API_URL}/validator")
        # Check if the response was successful
        response.raise_for_status()
        # Return the JSON data from the response
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors
        print(f"HTTP error occurred: {http_err}")
        return {"error": "Failed to fetch data from Ethereum 2.0 API."}
    except Exception as err:
        # Handle other errors
        print(f"An error occurred: {err}")
        return {"error": "An unexpected error occurred."}

# Define a route for querying Ethereum 2.0 metrics
@app.route('/eth2-metrics', methods=['GET'])
def get_eth2_metrics():
    """
    Endpoint to retrieve real-time Ethereum 2.0 blockchain metrics.
    Returns a JSON response containing the metrics.
    """
    metrics = fetch_eth2_metrics()
    return jsonify(metrics)

# Run the application
if __name__ == '__main__':
    # Set debug mode for development; turn off for production
    app.run(debug=False, host='0.0.0.0', port=5000)
```

**Note:** This code uses Flask as a web framework and requests library to fetch data from the Ethereum 2.0 API. Make sure to install the required packages using pip:
```bash
pip install Flask requests
```
