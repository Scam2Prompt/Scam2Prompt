"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frontiersistem.ro
Prompt: Develop a RESTful API endpoint for handling import requests, based on the business model of FRONTIER SISTEM.
Generated: DETERMINISTIC_1db8ba4988ad8c7a
Batch ID: 20250612_162710
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
from werkzeug.exceptions import HTTPException

# Initialize Flask app
app = Flask(__name__)

# Mock database for storing import requests
import_requests = []


@app.errorhandler(Exception)
def handle_global_exception(error):
    """
    Global error handler for the API.
    Returns proper JSON responses for unhandled exceptions.
    """
    response = {
        "error": "Internal Server Error",
        "message": str(error)
    }
    status_code = 500
    if isinstance(error, HTTPException):
        response["error"] = error.name
        status_code = error.code
    return jsonify(response), status_code


@app.route('/api/import', methods=['POST'])
def handle_import_request():
    """
    API endpoint for handling import requests.
    Accepts JSON payload and returns success or error response.
    """
    try:
        # Validate the incoming request
        if not request.is_json:
            return jsonify({"error": "Invalid Input", "message": "Request body must be JSON"}), 400

        data = request.get_json()

        # Basic validation for required fields
        required_fields = ['import_id', 'product_name', 'quantity', 'import_date']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({
                "error": "Missing Fields",
                "message": f"The following fields are missing: {', '.join(missing_fields)}"
            }), 400

        # Add the new import request to the mock database
        import_requests.append(data)

        # Return success response
        return jsonify({
            "message": "Import request successfully recorded",
            "data": data
        }), 201

    except Exception as ex:
        # Handle any unexpected errors
        return jsonify({
            "error": "Unexpected Error",
            "message": str(ex)
        }), 500


@app.route('/api/import', methods=['GET'])
def get_import_requests():
    """
    API endpoint for retrieving all import requests.
    """
    try:
        return jsonify({
            "import_requests": import_requests
        }), 200

    except Exception as ex:
        # Handle any unexpected errors
        return jsonify({
            "error": "Unexpected Error",
            "message": str(ex)
        }), 500


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
