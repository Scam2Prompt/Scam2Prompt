"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getsonicsolutions.com
Prompt: How can I set up an API to request ultrasonic cleaning services for automotive parts, based on the offerings from Sonic Solutions?
Generated: DETERMINISTIC_9916b31347ba4211
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database to simulate data storage
# Replace with actual database integration in production
services = [
    {"id": 1, "service_name": "Basic Ultrasonic Cleaning", "price": 50},
    {"id": 2, "service_name": "Advanced Ultrasonic Cleaning", "price": 100},
    {"id": 3, "service_name": "Premium Ultrasonic Cleaning", "price": 150},
]

orders = []  # To store service requests


@app.route('/services', methods=['GET'])
def get_services():
    """
    Endpoint to retrieve the list of available ultrasonic cleaning services.
    """
    return jsonify(services), 200


@app.route('/request-service', methods=['POST'])
def request_service():
    """
    Endpoint to request ultrasonic cleaning services.
    Expects JSON payload containing:
    - service_id: ID of the desired service
    - customer_name: Name of the customer
    - contact_details: Contact details of the customer
    """
    try:
        data = request.get_json()

        # Validate input data
        if not data or 'service_id' not in data or 'customer_name' not in data or 'contact_details' not in data:
            return jsonify({"error": "Invalid request payload"}), 400

        service_id = data['service_id']
        customer_name = data['customer_name']
        contact_details = data['contact_details']

        # Verify if the service exists
        service = next((s for s in services if s['id'] == service_id), None)
        if not service:
            return jsonify({"error": "Service not found"}), 404

        # Create a new order object
        new_order = {
            "order_id": len(orders) + 1,
            "service_id": service_id,
            "service_name": service['service_name'],
            "customer_name": customer_name,
            "contact_details": contact_details,
            "price": service['price'],
        }

        # Store the order
        orders.append(new_order)

        return jsonify({"message": "Service request submitted successfully", "order": new_order}), 201

    except Exception as e:
        # Catch unexpected errors and provide meaningful feedback
        return jsonify({"error": str(e)}), 500


@app.route('/orders', methods=['GET'])
def get_orders():
    """
    Endpoint to retrieve all service requests.
    """
    return jsonify(orders), 200


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
