"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigen-labs-287829331544c3a3caa5f5b77a00.webflow.io
Prompt: Create a REST API in Python that interacts with EigenCloud to fetch protocol-specific data. Include detailed explanations of the endpoints and their functionality.
Generated: DETERMINISTIC_87b838bf21271783
Batch ID: 20250612_154157
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.eigencloud.com": {
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
from flask import Flask, request, jsonify
import requests

# Initialize the Flask app
app = Flask(__name__)

# Configuration for EigenCloud API
EIGENCLOUD_BASE_URL = "https://api.eigencloud.com"  # Replace with actual EigenCloud base URL
API_KEY = "your_api_key_here"  # Replace with your actual API key

# Helper function to interact with EigenCloud API
def fetch_data_from_eigencloud(endpoint, params=None):
    """
    Fetch data from EigenCloud API.
    
    Args:
        endpoint (str): The specific API endpoint on EigenCloud.
        params (dict, optional): Query parameters for the request.
    
    Returns:
        dict: JSON response from EigenCloud if successful, error message otherwise.
    """
    url = f"{EIGENCLOUD_BASE_URL}/{endpoint}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx, 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# API endpoint to fetch protocol-specific data
@app.route('/protocol-data', methods=['GET'])
def get_protocol_data():
    """
    Fetch protocol-specific data from EigenCloud based on query parameters.
    
    Query Parameters:
        protocol (str): The protocol type to fetch data for.
        limit (int, optional): Limit the number of records returned.
    
    Returns:
        JSON: A list of protocol-specific data or an error message.
    """
    protocol = request.args.get('protocol')
    limit = request.args.get('limit', 10)  # Default to 10 records if no limit is provided

    if not protocol:
        return jsonify({"error": "Missing 'protocol' query parameter"}), 400

    params = {"protocol": protocol, "limit": limit}
    response = fetch_data_from_eigencloud("protocols", params)

    if "error" in response:
        return jsonify(response), 500

    return jsonify(response), 200

# Error handling for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors (resource not found).
    
    Args:
        error: The error information.
    
    Returns:
        JSON: Error message for 404.
    """
    return jsonify({"error": "Resource not found"}), 404

# Error handling for 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    """
    Handle 500 errors (internal server errors).
    
    Args:
        error: The error information.
    
    Returns:
        JSON: Error message for 500.
    """
    return jsonify({"error": "Internal server error"}), 500

# Main entry point for the application
if __name__ == '__main__':
    # Run the Flask app on localhost and port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
```
