"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engaztop.com
Prompt: Generate a code snippet for a web application that allows users to request home cleaning services, similar to the offerings of شركة انجاز, including features for scheduling and pricing.
Generated: DETERMINISTIC_9da4c2ca8ce07c09
Batch ID: 20250612_162051
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
from datetime import datetime
import re

# Initialize Flask application
app = Flask(__name__)

# Temporary in-memory storage for service requests
service_requests = []

# Helper function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

# Helper function to validate phone number format
def is_valid_phone(phone):
    phone_regex = r'^\+?[0-9]{10,13}$'
    return re.match(phone_regex, phone)

# Route for requesting home cleaning services
@app.route('/request-service', methods=['POST'])
def request_service():
    """
    Endpoint to allow users to request home cleaning services.
    Expects a JSON payload with name, email, phone, date, time, and service type.
    """
    try:
        # Parse JSON request data
        data = request.json
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        date_str = data.get("date")  # Expected format: YYYY-MM-DD
        time_str = data.get("time")  # Expected format: HH:MM
        service_type = data.get("service_type")  # Example: "deep cleaning", "basic cleaning"

        # Validate request fields
        if not name or not email or not phone or not date_str or not time_str or not service_type:
            return jsonify({"error": "Missing required fields"}), 400

        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format"}), 400

        if not is_valid_phone(phone):
            return jsonify({"error": "Invalid phone number format"}), 400

        try:
            # Validate and parse date and time
            service_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            service_time = datetime.strptime(time_str, "%H:%M").time()
        except ValueError:
            return jsonify({"error": "Invalid date or time format"}), 400

        # Calculate pricing based on service type (example logic)
        pricing = {
            "basic cleaning": 50,
            "deep cleaning": 100,
            "move-in/move-out cleaning": 150,
        }
        price = pricing.get(service_type.lower())
        if not price:
            return jsonify({"error": "Invalid service type"}), 400

        # Store the service request (in-memory for now)
        request_id = len(service_requests) + 1
        service_requests.append({
            "id": request_id,
            "name": name,
            "email": email,
            "phone": phone,
            "date": service_date,
            "time": service_time,
            "service_type": service_type,
            "price": price
        })

        # Return success response with request ID
        return jsonify({
            "message": "Service request created successfully",
            "request_id": request_id,
            "price": price
        }), 201

    except Exception as e:
        # Catch unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Route to list all service requests (for admin purposes)
@app.route('/service-requests', methods=['GET'])
def list_service_requests():
    """
    Endpoint to retrieve all service requests.
    Only for administrative purposes.
    """
    return jsonify({"service_requests": service_requests}), 200

# Main entry point for running the application
if __name__ == '__main__':
    # Run the Flask app on localhost
    app.run(debug=True)
```

### Notes:
- This code uses Flask, a lightweight Python web framework.
- Replace the temporary in-memory storage (`service_requests`) with a database in a real production application.
- Test and secure endpoints before deploying to production.
