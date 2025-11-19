"""
Generated Code Metadata:
========================
Original URL: https://al-afdel.com
Prompt: Generate a code snippet for a web application that allows users to request home cleaning services, referencing the unique offerings of the company mentioned in the content.
Generated: DETERMINISTIC_6d0d82dcd8076210
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Mock database for storing service requests
service_requests = []

# Unique offerings of the company
UNIQUE_OFFERINGS = [
    "Eco-friendly cleaning products",
    "Pet-friendly cleaning services",
    "Customizable cleaning schedules",
    "Specialized deep cleaning for allergies"
]

@app.route('/offerings', methods=['GET'])
def get_unique_offerings():
    """
    Endpoint to retrieve the unique offerings of the company.
    """
    return jsonify({
        "success": True,
        "offerings": UNIQUE_OFFERINGS
    }), 200

@app.route('/request-service', methods=['POST'])
def request_service():
    """
    Endpoint to request a home cleaning service.
    Expects JSON payload with user details and service preferences.
    """
    try:
        # Parse the incoming JSON request
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "message": "Invalid JSON payload"}), 400

        # Validate required fields
        required_fields = ["name", "email", "address", "preferred_date", "services"]
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({
                "success": False,
                "message": f"Missing required fields: {', '.join(missing_fields)}"
            }), 400

        # Validate date format
        try:
            preferred_date = datetime.strptime(data["preferred_date"], "%Y-%m-%d")
        except ValueError:
            return jsonify({
                "success": False,
                "message": "Invalid date format. Use YYYY-MM-DD."
            }), 400

        # Create a new service request
        service_request = {
            "id": len(service_requests) + 1,
            "name": data["name"],
            "email": data["email"],
            "address": data["address"],
            "preferred_date": preferred_date.strftime("%Y-%m-%d"),
            "services": data["services"],
            "special_requests": data.get("special_requests", ""),
            "status": "Pending"
        }
        service_requests.append(service_request)

        return jsonify({
            "success": True,
            "message": "Service request submitted successfully.",
            "request_id": service_request["id"]
        }), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({
            "success": False,
            "message": "An error occurred while processing your request.",
            "error": str(e)
        }), 500

@app.route('/service-requests', methods=['GET'])
def get_service_requests():
    """
    Endpoint to retrieve all service requests.
    """
    return jsonify({
        "success": True,
        "requests": service_requests
    }), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
