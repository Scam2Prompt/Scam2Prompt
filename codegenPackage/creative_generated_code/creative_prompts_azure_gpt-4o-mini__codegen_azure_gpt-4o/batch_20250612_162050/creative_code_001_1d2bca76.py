"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://birlikjenerator.com
Prompt: Generate a code snippet for a web application that allows users to request periodic maintenance for their diesel generators, referencing the services offered by Birlik Jeneratör.
Generated: DETERMINISTIC_1d2bca764ad21fd0
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: maintenance_scheduler.py

from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock database for demonstration purposes
maintenance_requests = []  # A list to store maintenance requests

# Available services from Birlik Jeneratör
AVAILABLE_SERVICES = [
    "Oil Change",
    "Filter Replacement",
    "Battery Check",
    "Cooling System Inspection",
    "General Inspection"
]

# Error messages
ERROR_MESSAGES = {
    "missing_fields": "Required fields are missing in the request.",
    "invalid_service": "Requested service is not available."
}


@app.route('/request-maintenance', methods=['POST'])
def request_maintenance():
    """
    Endpoint to allow users to request periodic maintenance for their diesel generators.
    Expected JSON input:
    {
        "customer_name": "John Doe",
        "contact_email": "john.doe@example.com",
        "generator_model": "Model X",
        "requested_service": "Oil Change",
        "preferred_date": "2023-11-15"
    }
    """
    try:
        # Parse incoming JSON request
        data = request.get_json()

        # Validate required fields
        required_fields = ["customer_name", "contact_email", "generator_model", "requested_service", "preferred_date"]
        if not all(field in data for field in required_fields):
            return jsonify({"error": ERROR_MESSAGES["missing_fields"]}), 400

        # Validate service availability
        if data["requested_service"] not in AVAILABLE_SERVICES:
            return jsonify({"error": ERROR_MESSAGES["invalid_service"]}), 400

        # Validate preferred date format
        try:
            preferred_date = datetime.strptime(data["preferred_date"], "%Y-%m-%d")
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

        # Ensure preferred date is not in the past
        if preferred_date < datetime.now():
            return jsonify({"error": "Preferred date cannot be in the past."}), 400

        # Save maintenance request
        maintenance_request = {
            "customer_name": data["customer_name"],
            "contact_email": data["contact_email"],
            "generator_model": data["generator_model"],
            "requested_service": data["requested_service"],
            "preferred_date": preferred_date.strftime("%Y-%m-%d"),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        maintenance_requests.append(maintenance_request)

        # Log the request
        logging.info(f"New maintenance request: {maintenance_request}")

        # Return successful response
        return jsonify({"message": "Maintenance request submitted successfully.", "request": maintenance_request}), 201

    except Exception as e:
        # Handle unexpected errors
        logging.error(f"Error processing maintenance request: {str(e)}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500


@app.route('/available-services', methods=['GET'])
def get_available_services():
    """
    Endpoint to retrieve a list of services offered by Birlik Jeneratör.
    """
    return jsonify({"services": AVAILABLE_SERVICES}), 200


@app.route('/maintenance-requests', methods=['GET'])
def get_maintenance_requests():
    """
    Endpoint to retrieve all maintenance requests (for debugging or admin purposes).
    """
    return jsonify({"requests": maintenance_requests}), 200


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
