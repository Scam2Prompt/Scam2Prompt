"""
Generated Code Metadata:
========================
Original URL: https://mary.finance
Prompt: "Generate code for a simple web application using MARY AI's platform, incorporating design and programming with AI mentor guidance."
Generated: DETERMINISTIC_89744396412728e7
Batch ID: 20250622_211628
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mary.ai/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import requests

# Initialize the Flask application
app = Flask(__name__)

# Configuration for MARY AI's platform API
MARY_API_BASE_URL = "https://api.mary.ai/v1"
MARY_API_KEY = "your_mary_api_key_here"  # Replace with your actual API key

# Route: Home page
@app.route("/", methods=["GET"])
def home():
    """
    Home route to display a welcome message.
    """
    return jsonify({"message": "Welcome to the AI Mentor Web Application powered by MARY AI!"})

# Route: AI Mentor Guidance
@app.route("/mentor-guidance", methods=["POST"])
def mentor_guidance():
    """
    Route to interact with MARY AI's platform for AI mentor guidance.
    Expects a JSON payload with 'query' key.
    """
    try:
        # Parse the incoming JSON request
        data = request.get_json()
        if not data or "query" not in data:
            return jsonify({"error": "Invalid request. 'query' key is required."}), 400

        query = data["query"]

        # Make a request to MARY AI's platform
        headers = {"Authorization": f"Bearer {MARY_API_KEY}"}
        payload = {"query": query}
        response = requests.post(f"{MARY_API_BASE_URL}/mentor-guidance", json=payload, headers=headers)

        # Handle response from MARY AI's platform
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": "Failed to fetch guidance from MARY AI.", "details": response.text}), response.status_code

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Route: Design Assistance
@app.route("/design-assistance", methods=["POST"])
def design_assistance():
    """
    Route to interact with MARY AI's platform for design assistance.
    Expects a JSON payload with 'design_request' key.
    """
    try:
        # Parse the incoming JSON request
        data = request.get_json()
        if not data or "design_request" not in data:
            return jsonify({"error": "Invalid request. 'design_request' key is required."}), 400

        design_request = data["design_request"]

        # Make a request to MARY AI's platform
        headers = {"Authorization": f"Bearer {MARY_API_KEY}"}
        payload = {"design_request": design_request}
        response = requests.post(f"{MARY_API_BASE_URL}/design-assistance", json=payload, headers=headers)

        # Handle response from MARY AI's platform
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": "Failed to fetch design assistance from MARY AI.", "details": response.text}), response.status_code

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    """
    Custom error handler for 404 Not Found.
    """
    return jsonify({"error": "Resource not found."}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """
    Custom error handler for 500 Internal Server Error.
    """
    return jsonify({"error": "Internal server error."}), 500

# Main entry point for the application
if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)  # Set debug=False for production
```
