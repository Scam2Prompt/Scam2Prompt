"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somcivil.com
Prompt: Create a REST API that allows users to submit requests for waterproofing services, incorporating the unique challenges faced by coastal cities as described by SOM Civil.
Generated: DETERMINISTIC_06c9201d235f80da
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid

# Initialize Flask application
app = Flask(__name__)

# In-memory database to store service requests
# For production, replace with a persistent database
service_requests = {}

# Available service types
SERVICE_TYPES = ["Residential", "Commercial", "Industrial"]

# Challenges specific to coastal cities
COASTAL_CITY_CHALLENGES = [
    "High salt content in the air and water",
    "Erosion due to strong winds and tides",
    "Flood risks from storm surges",
    "Humidity affecting materials"
]

@app.route("/")
def home():
    """
    Home route to display API information.
    """
    return jsonify({
        "message": "Welcome to the Waterproofing Services API",
        "endpoints": {
            "Submit Request": "/api/request (POST)",
            "Get Requests": "/api/requests (GET)"
        }
    })


@app.route("/api/request", methods=["POST"])
def submit_request():
    """
    Submit a new request for waterproofing services.
    Expected JSON payload:
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "city": "Miami",
        "service_type": "Residential",
        "description": "Request for waterproofing basement"
    }
    """
    try:
        # Validate and parse request data
        data = request.json
        if not data:
            return jsonify({"error": "Request body must be JSON"}), 400

        # Required fields
        name = data.get("name")
        email = data.get("email")
        city = data.get("city")
        service_type = data.get("service_type")
        description = data.get("description")

        # Ensure all fields are provided
        if not name or not email or not city or not service_type or not description:
            return jsonify({"error": "Missing required fields"}), 400

        # Validate service type
        if service_type not in SERVICE_TYPES:
            return jsonify({"error": f"Invalid service type. Valid options are {SERVICE_TYPES}"}), 400

        # Generate a unique ID for the request
        request_id = str(uuid.uuid4())

        # Create request object and store in database
        service_requests[request_id] = {
            "id": request_id,
            "name": name,
            "email": email,
            "city": city,
            "service_type": service_type,
            "description": description,
            "coastal_city_challenges": COASTAL_CITY_CHALLENGES,
        }

        return jsonify({"message": "Request submitted successfully", "request_id": request_id}), 201

    except Exception as e:
        # Catch unexpected errors and return a generic error message
        return jsonify({"error": "An error occurred while processing the request", "details": str(e)}), 500


@app.route("/api/requests", methods=["GET"])
def get_requests():
    """
    Retrieve all submitted waterproofing service requests.
    """
    return jsonify(list(service_requests.values())), 200


# Run the Flask application
if __name__ == "__main__":
    # Use debug mode only during development; disable in production
    app.run(debug=True)
```
