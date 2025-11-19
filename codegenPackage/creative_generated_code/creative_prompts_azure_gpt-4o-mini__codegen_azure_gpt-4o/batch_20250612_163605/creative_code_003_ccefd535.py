"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.khadamy.com
Prompt: Develop a REST API endpoint for managing mobile car polishing requests in Mecca, including validation for service areas.
Generated: DETERMINISTIC_ccefd535f7d0e39e
Batch ID: 20250612_163605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Define valid service areas for mobile car polishing requests
VALID_SERVICE_AREAS = {"Mecca"}

# Mock database for storing requests
car_polish_requests = []

# Error Handler for HTTP Exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = jsonify({"error": e.name, "message": e.description})
    response.status_code = e.code
    return response

# Error handler for generic exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    response = jsonify({"error": "Internal Server Error", "message": str(e)})
    response.status_code = 500
    return response

# Endpoint to create a new car polishing request
@app.route('/api/car-polish-requests', methods=['POST'])
def create_car_polish_request():
    """
    Handles the creation of a new car polishing request.
    Expects a JSON payload with `name`, `phone`, and `location`.
    """
    try:
        # Get JSON data from the request
        data = request.get_json()
        if not data:
            return jsonify({"error": "Bad Request", "message": "Request body is missing or invalid"}), 400

        # Validate required fields
        name = data.get("name")
        phone = data.get("phone")
        location = data.get("location")

        if not name or not phone or not location:
            return jsonify({"error": "Bad Request", "message": "Name, phone, and location are required"}), 400

        # Validate location against valid service areas
        if location not in VALID_SERVICE_AREAS:
            return jsonify({"error": "Unprocessable Entity", "message": "Service not available in the provided location"}), 422

        # Create the request data
        request_id = len(car_polish_requests) + 1
        new_request = {
            "id": request_id,
            "name": name,
            "phone": phone,
            "location": location
        }

        # Save to mock database
        car_polish_requests.append(new_request)

        # Respond with the created request details
        return jsonify({"message": "Car polishing request created successfully", "data": new_request}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Endpoint to retrieve all car polishing requests
@app.route('/api/car-polish-requests', methods=['GET'])
def get_car_polish_requests():
    """
    Returns a list of all car polishing requests stored in the mock database.
    """
    return jsonify({"message": "Car polishing requests retrieved successfully", "data": car_polish_requests}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
