"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.premierpointing.com.au
Prompt: Create a RESTful API endpoint that allows users to submit requests for brick and stone restoration services, incorporating features like ventilation replacement and water repellant application mentioned on the Premier Pointing website.
Generated: DETERMINISTIC_068e41435907bd0f
Batch ID: 20250612_163423
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

# In-memory storage for service requests
service_requests = []

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        response = e.get_response()
        response.data = jsonify({"error": e.description}).get_data()
        response.content_type = "application/json"
        return response
    return jsonify({"error": "Internal server error"}), 500


# RESTful API endpoint to submit a service request
@app.route("/api/service-request", methods=["POST"])
def submit_service_request():
    """
    Endpoint to submit a restoration service request.

    Request JSON format:
    {
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "123-456-7890",
        "address": "123 Main Street",
        "services": {
            "brick_restoration": true,
            "stone_restoration": false,
            "ventilation_replacement": true,
            "water_repellant_application": true
        },
        "additional_notes": "Please call before arriving."
    }

    Response JSON format:
    {
        "message": "Service request submitted successfully",
        "request_id": 1
    }
    """
    # Validate and parse the request JSON
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON data"}), 400

        # Required fields
        required_fields = ["name", "email", "phone", "address", "services"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        # Validate services field
        services_required_fields = [
            "brick_restoration",
            "stone_restoration",
            "ventilation_replacement",
            "water_repellant_application",
        ]
        if not isinstance(data["services"], dict):
            return jsonify({"error": "'services' must be a JSON object"}), 400
        for field in services_required_fields:
            if field not in data["services"]:
                return jsonify({"error": f"Missing service field: {field}"}), 400

        # Create and store the service request
        new_request = {
            "id": len(service_requests) + 1,
            "name": data["name"],
            "email": data["email"],
            "phone": data["phone"],
            "address": data["address"],
            "services": data["services"],
            "additional_notes": data.get("additional_notes", ""),
        }
        service_requests.append(new_request)

        return jsonify(
            {
                "message": "Service request submitted successfully",
                "request_id": new_request["id"],
            }
        ), 201
    except Exception as e:
        return jsonify({"error": "An error occurred while processing your request"}), 500


# RESTful API endpoint to retrieve all service requests (optional)
@app.route("/api/service-requests", methods=["GET"])
def get_service_requests():
    """
    Endpoint to retrieve all submitted service requests.

    Response JSON format:
    {
        "service_requests": [
            {
                "id": 1,
                "name": "John Doe",
                "email": "john@example.com",
                "phone": "123-456-7890",
                "address": "123 Main Street",
                "services": {
                    "brick_restoration": true,
                    "stone_restoration": false,
                    "ventilation_replacement": true,
                    "water_repellant_application": true
                },
                "additional_notes": "Please call before arriving."
            }
        ]
    }
    """
    return jsonify({"service_requests": service_requests}), 200


if __name__ == "__main__":
    # Start the Flask development server
    app.run(debug=True)
```
