"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carehelpers.pt
Prompt: Generate a code snippet for a web application that allows users to request home care services similar to those offered by CARE HELPERS, including personal hygiene, meal preparation, and social activities.
Generated: DETERMINISTIC_575dff228568ef83
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from datetime import datetime

# Initialize the Flask app
app = Flask(__name__)

# In-memory database simulation (for demonstration purposes)
requests_db = []

# Service options
SERVICE_OPTIONS = ["Personal Hygiene", "Meal Preparation", "Social Activities"]

# Endpoint to view available services
@app.route('/services', methods=['GET'])
def get_services():
    """
    GET /services
    Returns the list of available home care services.
    """
    return jsonify({"services": SERVICE_OPTIONS}), 200

# Endpoint to request a service
@app.route('/request-service', methods=['POST'])
def request_service():
    """
    POST /request-service
    Allows a user to request a home care service.
    Expected JSON body:
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "123-456-7890",
        "service": "Personal Hygiene",
        "date": "2023-10-01"
    }
    """
    try:
        # Parse the request JSON
        data = request.get_json()

        # Validate input data
        if not all(key in data for key in ["name", "email", "phone", "service", "date"]):
            return jsonify({"error": "Missing required fields"}), 400
        
        if data["service"] not in SERVICE_OPTIONS:
            return jsonify({"error": f"Service '{data['service']}' is not available"}), 400

        # Validate date format
        try:
            service_date = datetime.strptime(data["date"], "%Y-%m-%d")
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

        # Save the requested service to the database
        service_request = {
            "id": len(requests_db) + 1,
            "name": data["name"],
            "email": data["email"],
            "phone": data["phone"],
            "service": data["service"],
            "date": service_date.strftime("%Y-%m-%d"),
            "status": "Pending"
        }
        requests_db.append(service_request)

        # Return success response
        return jsonify({"message": "Service requested successfully", "request": service_request}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Endpoint to view all service requests (for admin use)
@app.route('/admin/service-requests', methods=['GET'])
def view_service_requests():
    """
    GET /admin/service-requests
    Returns all requested services. (Admin use only)
    """
    return jsonify({"requests": requests_db}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
