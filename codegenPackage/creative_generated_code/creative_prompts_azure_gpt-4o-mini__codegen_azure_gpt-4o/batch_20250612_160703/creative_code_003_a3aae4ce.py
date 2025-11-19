"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cm-coinmaster.home.blog
Prompt: Provide a code example for managing Coin Master subscriptions using a web API.
Generated: DETERMINISTIC_a3aae4ce8f42ab7b
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory data store for subscriptions (this would typically be a database in production)
subscriptions = {}

# Error handling utility function
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

@app.route('/subscriptions', methods=['POST'])
def create_subscription():
    """
    Endpoint to create a new Coin Master subscription.
    Expects a JSON body with 'user_id' and 'plan' fields.
    """
    data = request.get_json()

    # Validate incoming data
    if not data or 'user_id' not in data or 'plan' not in data:
        return error_response("Invalid request data. 'user_id' and 'plan' are required.")

    user_id = data['user_id']
    plan = data['plan']

    # Generate a unique subscription ID
    subscription_id = str(uuid.uuid4())

    # Create the subscription
    subscriptions[subscription_id] = {
        "subscription_id": subscription_id,
        "user_id": user_id,
        "plan": plan,
        "status": "active"  # Default status is 'active'
    }

    return jsonify(subscriptions[subscription_id]), 201

@app.route('/subscriptions/<subscription_id>', methods=['GET'])
def get_subscription(subscription_id):
    """
    Endpoint to retrieve details of a specific subscription by ID.
    """
    subscription = subscriptions.get(subscription_id)

    if subscription is None:
        return error_response(f"Subscription with ID {subscription_id} not found.", 404)

    return jsonify(subscription), 200

@app.route('/subscriptions/<subscription_id>', methods=['PATCH'])
def update_subscription(subscription_id):
    """
    Endpoint to update a subscription's details.
    Expects a JSON body with optional 'plan' or 'status'.
    """
    subscription = subscriptions.get(subscription_id)

    if subscription is None:
        return error_response(f"Subscription with ID {subscription_id} not found.", 404)

    data = request.get_json()
    if not data:
        return error_response("Invalid request data.")

    # Update subscription fields if provided
    if 'plan' in data:
        subscription['plan'] = data['plan']
    if 'status' in data:
        subscription['status'] = data['status']

    return jsonify(subscription), 200

@app.route('/subscriptions/<subscription_id>', methods=['DELETE'])
def delete_subscription(subscription_id):
    """
    Endpoint to delete a subscription by ID.
    """
    subscription = subscriptions.pop(subscription_id, None)

    if subscription is None:
        return error_response(f"Subscription with ID {subscription_id} not found.", 404)

    return jsonify({"message": f"Subscription {subscription_id} deleted successfully."}), 200

if __name__ == "__main__":
    # Run the Flask development server
    # In production, use a WSGI server like Gunicorn or uWSGI.
    app.run(debug=True)
```
