"""
Generated Code Metadata:
========================
Original URL: https://birlikjenerator.com
Prompt: Generate a code snippet for a web application that allows users to request periodic maintenance for their diesel generators, referencing the services offered by Birlik Jeneratör.
Generated: DETERMINISTIC_1d2bca764ad21fd0
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import datetime

# Initialize the Flask application
app = Flask(__name__)

# Mock database for storing maintenance requests
maintenance_requests = []

# Define available services offered by Birlik Jeneratör
services = [
    "Oil Change",
    "Filter Replacement",
    "Battery Check",
    "Coolant Level Check",
    "General Inspection"
]

# Route to get available services
@app.route('/services', methods=['GET'])
def get_services():
    """
    Endpoint to retrieve the list of services offered by Birlik Jeneratör.
    """
    return jsonify({"services": services}), 200

# Route to submit a maintenance request
@app.route('/request-maintenance', methods=['POST'])
def request_maintenance():
    """
    Endpoint to submit a maintenance request for a diesel generator.
    """
    try:
        # Parse the incoming JSON request
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request format. JSON data expected."}), 400

        # Validate required fields
        required_fields = ["name", "email", "phone", "service", "preferred_date"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        # Validate service selection
        if data["service"] not in services:
            return jsonify({"error": f"Invalid service selected. Available services: {services}"}), 400

        # Validate preferred date format
        try:
            preferred_date = datetime.datetime.strptime(data["preferred_date"], "%Y-%m-%d")
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

        # Create a maintenance request object
        maintenance_request = {
            "id": len(maintenance_requests) + 1,
            "name": data["name"],
            "email": data["email"],
            "phone": data["phone"],
            "service": data["service"],
            "preferred_date": preferred_date.strftime("%Y-%m-%d"),
            "status": "Pending"
        }

        # Store the request in the mock database
        maintenance_requests.append(maintenance_request)

        # Return success response
        return jsonify({"message": "Maintenance request submitted successfully.", "request": maintenance_request}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Route to view all maintenance requests
@app.route('/maintenance-requests', methods=['GET'])
def view_maintenance_requests():
    """
    Endpoint to view all submitted maintenance requests.
    """
    return jsonify({"maintenance_requests": maintenance_requests}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
