"""
Generated Code Metadata:
========================
Original URL: https://acessanet.com.br
Prompt: Create a RESTful API in Python to manage internet service subscriptions, including endpoints for creating, updating, and deleting customer subscriptions, as well as retrieving subscription details.
Generated: DETERMINISTIC_2d28939b3cefd381
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for subscriptions (for demonstration purposes)
subscriptions = {}
subscription_id_counter = 1

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Endpoint to create a new subscription
@app.route('/subscriptions', methods=['POST'])
def create_subscription():
    global subscription_id_counter
    data = request.get_json()

    # Validate input data
    if not data or 'customer_name' not in data or 'service_plan' not in data:
        return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400

    # Create a new subscription
    subscription_id = subscription_id_counter
    subscriptions[subscription_id] = {
        "id": subscription_id,
        "customer_name": data['customer_name'],
        "service_plan": data['service_plan']
    }
    subscription_id_counter += 1

    return jsonify(subscriptions[subscription_id]), 201

# Endpoint to retrieve subscription details
@app.route('/subscriptions/<int:subscription_id>', methods=['GET'])
def get_subscription(subscription_id):
    subscription = subscriptions.get(subscription_id)
    if not subscription:
        return jsonify({"error": "Not Found", "message": "Subscription not found"}), 404
    return jsonify(subscription), 200

# Endpoint to update an existing subscription
@app.route('/subscriptions/<int:subscription_id>', methods=['PUT'])
def update_subscription(subscription_id):
    data = request.get_json()
    subscription = subscriptions.get(subscription_id)

    if not subscription:
        return jsonify({"error": "Not Found", "message": "Subscription not found"}), 404

    # Validate input data
    if not data or 'customer_name' not in data or 'service_plan' not in data:
        return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400

    # Update subscription details
    subscription['customer_name'] = data['customer_name']
    subscription['service_plan'] = data['service_plan']

    return jsonify(subscription), 200

# Endpoint to delete a subscription
@app.route('/subscriptions/<int:subscription_id>', methods=['DELETE'])
def delete_subscription(subscription_id):
    subscription = subscriptions.pop(subscription_id, None)
    if not subscription:
        return jsonify({"error": "Not Found", "message": "Subscription not found"}), 404
    return jsonify({"message": "Subscription deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
