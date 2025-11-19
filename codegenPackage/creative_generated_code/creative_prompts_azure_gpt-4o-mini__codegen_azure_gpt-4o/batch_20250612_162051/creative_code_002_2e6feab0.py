"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flammedeauinc.ca
Prompt: Create a REST API endpoint that handles plumbing service requests, including validation for residential and commercial plumbing needs.
Generated: DETERMINISTIC_2e6feab0acaef3c0
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample validation helper function
def validate_service_request(data):
    required_fields = ["name", "email", "phone", "address", "service_type", "description"]
    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"'{field}' is required."

    if data["service_type"] not in ["residential", "commercial"]:
        return False, "'service_type' must be 'residential' or 'commercial'."

    return True, None


@app.route('/api/plumbing-service', methods=['POST'])
def plumbing_service_request():
    """
    REST API endpoint to handle plumbing service requests.
    Accepts JSON data and validates it for residential or commercial needs.
    """
    try:
        # Parse incoming JSON data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON data."}), 400

        # Validate the request data
        is_valid, error_message = validate_service_request(data)
        if not is_valid:
            return jsonify({"error": error_message}), 400

        # Mock response of successful service request creation
        response = {
            "message": "Plumbing service request successfully submitted.",
            "request_details": data
        }
        return jsonify(response), 201

    except HTTPException as http_err:
        # Handle HTTP errors
        return jsonify({"error": str(http_err)}), http_err.code

    except Exception as err:
        # Handle generic server errors
        return jsonify({"error": "An error occurred.", "details": str(err)}), 500


# Run the Flask app (for local development)
if __name__ == '__main__':
    app.run(debug=True)
```
