"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wingerrandr.ca
Prompt: Develop a RESTful API endpoint for submitting requests for drywall repair and painting services, ensuring it captures necessary details from the user.
Generated: DETERMINISTIC_b5b947e6b67e1f2f
Batch ID: 20250612_135310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# In-memory storage for service requests (for demonstration purposes)
service_requests = []

# Utility function to validate request data
def validate_request_data(data):
    required_fields = ["name", "email", "phone", "address", "service_type", "details"]
    for field in required_fields:
        if field not in data or not data[field].strip():
            raise BadRequest(f"Missing or empty required field: {field}")

# Endpoint to submit a drywall repair or painting service request
@app.route('/submit-service-request', methods=['POST'])
def submit_service_request():
    """
    Handles service request submissions for drywall repair or painting.
    Expects a JSON payload with the following fields:
        - name: Name of the requester
        - email: Email of the requester
        - phone: Phone number of the requester
        - address: Address where the service is required
        - service_type: Type of service requested ('drywall_repair' or 'painting')
        - details: Additional details about the request
    """
    try:
        # Parse and validate request data
        request_data = request.get_json()
        if not request_data:
            raise BadRequest("Request must contain a JSON payload.")

        validate_request_data(request_data)

        # Ensure service_type is valid
        if request_data["service_type"] not in ["drywall_repair", "painting"]:
            raise BadRequest("Invalid service_type. Must be 'drywall_repair' or 'painting'.")

        # Add the request to the in-memory storage
        service_request = {
            "id": len(service_requests) + 1,
            "name": request_data["name"],
            "email": request_data["email"],
            "phone": request_data["phone"],
            "address": request_data["address"],
            "service_type": request_data["service_type"],
            "details": request_data["details"]
        }
        service_requests.append(service_request)

        # Return success response with the created request ID
        return jsonify({"message": "Service request submitted successfully.", "request_id": service_request["id"]}), 201

    except BadRequest as e:
        # Handle validation errors
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Handle unexpected server errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
