"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Create a REST API endpoint to manage HVAC installation requests, incorporating details from Quality Sheet Metal, Inc. about their services and warranties.
Generated: DETERMINISTIC_7d8a37740c204971
Batch ID: 20250612_135105
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

# Mock data structure for storing HVAC installation requests
hvac_requests = []

# Warranty and services details from Quality Sheet Metal, Inc.
COMPANY_DETAILS = {
    "company_name": "Quality Sheet Metal, Inc.",
    "services": ["Residential HVAC Installation", "Commercial HVAC Installation", "Maintenance and Repairs"],
    "warranty": "10-year limited warranty on parts and 1-year warranty on labor."
}

@app.errorhandler(Exception)
def handle_exception(e):
    """
    Global error handler for the API.
    Returns a JSON response with error details.
    """
    if isinstance(e, HTTPException):
        return jsonify(error=str(e)), e.code
    return jsonify(error="An unexpected error occurred"), 500

@app.route('/api/hvac/requests', methods=['POST'])
def create_hvac_request():
    """
    Endpoint to create a new HVAC installation request.
    Validates the incoming data and adds it to the mock data store.
    """
    try:
        # Validate incoming data
        data = request.json
        if not data:
            return jsonify({"error": "Request payload is missing"}), 400

        # Required fields
        required_fields = ["customer_name", "address", "contact_number", "service_type"]
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400

        # Ensure valid service type
        if data['service_type'] not in COMPANY_DETAILS['services']:
            return jsonify({"error": f"Invalid service type. Available services: {', '.join(COMPANY_DETAILS['services'])}"}), 400

        # Create new request
        new_request = {
            "id": len(hvac_requests) + 1,
            "customer_name": data["customer_name"],
            "address": data["address"],
            "contact_number": data["contact_number"],
            "service_type": data["service_type"],
            "status": "Pending"  # Default status
        }
        hvac_requests.append(new_request)
        return jsonify({"message": "HVAC installation request created successfully", "request": new_request}), 201
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

@app.route('/api/hvac/requests', methods=['GET'])
def get_hvac_requests():
    """
    Endpoint to retrieve all HVAC installation requests.
    """
    return jsonify({"requests": hvac_requests}), 200

@app.route('/api/hvac/company-details', methods=['GET'])
def get_company_details():
    """
    Endpoint to retrieve company details including services and warranties.
    """
    return jsonify(COMPANY_DETAILS), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
