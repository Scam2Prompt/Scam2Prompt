"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphamor.com
Prompt: Generate a code snippet for a web application that allows users to request installation services for aluminium window frames and burglar bars, referencing the offerings on Alphamor.
Generated: DETERMINISTIC_801c89f430825f19
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask application for requesting installation services for aluminium window frames and burglar bars

from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data for available services
services = [
    {
        "id": 1,
        "name": "Aluminium Window Frames Installation",
        "description": "Professional installation of durable aluminium window frames.",
        "price": 150.00  # per frame
    },
    {
        "id": 2,
        "name": "Burglar Bars Installation",
        "description": "Secure installation of burglar bars for enhanced home security.",
        "price": 100.00  # per bar
    }
]

# Route to get available services
@app.route('/services', methods=['GET'])
def get_services():
    """
    Endpoint to retrieve all available services.
    Returns:
        JSON response containing the list of services.
    """
    return jsonify({
        "success": True,
        "data": services
    }), 200


# Route to handle service requests
@app.route('/request-service', methods=['POST'])
def request_service():
    """
    Endpoint to request installation services.
    Expects a JSON payload with:
        - service_id: ID of the service being requested.
        - quantity: Number of units requested.
        - user_details: Dictionary containing user details (name, contact, etc.)
    """
    try:
        # Extract data from the request
        data = request.json
        service_id = data.get('service_id')
        quantity = data.get('quantity')
        user_details = data.get('user_details')

        # Validate input
        if not service_id or not quantity or not user_details:
            return jsonify({
                "success": False,
                "message": "Missing required fields: 'service_id', 'quantity', or 'user_details'."
            }), 400

        # Find the requested service
        requested_service = next((service for service in services if service['id'] == service_id), None)
        if not requested_service:
            return jsonify({
                "success": False,
                "message": "Invalid service ID."
            }), 404

        # Calculate total cost
        total_cost = requested_service['price'] * quantity

        # Mock response for successful service request
        return jsonify({
            "success": True,
            "message": "Service requested successfully.",
            "request_details": {
                "service_name": requested_service['name'],
                "quantity": quantity,
                "total_cost": f"${total_cost:.2f}",
                "user_details": user_details
            }
        }), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({
            "success": False,
            "message": f"An error occurred: {str(e)}"
        }), 500


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
