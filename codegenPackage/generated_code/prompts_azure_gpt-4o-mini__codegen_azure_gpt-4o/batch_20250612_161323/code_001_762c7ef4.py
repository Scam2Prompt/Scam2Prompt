"""
Generated Code Metadata:
========================
Original URL: https://sum-subs.cloud
Prompt: Generate a code snippet for a subscription management API that could be implemented on a cloud platform like sum-subs.cloud.
Generated: DETERMINISTIC_762c7ef4a1ba8df6
Batch ID: 20250612_161323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory database for demonstration purposes
subscriptions = {}

# Error handling utility
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Route to create a new subscription
@app.route('/subscriptions', methods=['POST'])
def create_subscription():
    try:
        # Parse request data
        data = request.json
        if not data or 'email' not in data or 'plan' not in data:
            return error_response("Missing required fields: 'email' and 'plan'")

        # Generate a unique subscription ID
        subscription_id = str(uuid.uuid4())
        subscriptions[subscription_id] = {
            "email": data['email'],
            "plan": data['plan'],
            "status": "active"
        }

        # Return the created subscription
        return jsonify({"subscription_id": subscription_id, "subscription": subscriptions[subscription_id]}), 201
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Route to retrieve a subscription by ID
@app.route('/subscriptions/<subscription_id>', methods=['GET'])
def get_subscription(subscription_id):
    try:
        subscription = subscriptions.get(subscription_id)
        if not subscription:
            return error_response("Subscription not found", 404)

        return jsonify({"subscription_id": subscription_id, "subscription": subscription}), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Route to update a subscription
@app.route('/subscriptions/<subscription_id>', methods=['PUT'])
def update_subscription(subscription_id):
    try:
        subscription = subscriptions.get(subscription_id)
        if not subscription:
            return error_response("Subscription not found", 404)

        # Parse request data
        data = request.json
        if not data:
            return error_response("Missing request body")

        # Update subscription fields
        subscription.update({key: value for key, value in data.items() if key in ['email', 'plan', 'status']})

        return jsonify({"subscription_id": subscription_id, "subscription": subscription}), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Route to delete a subscription
@app.route('/subscriptions/<subscription_id>', methods=['DELETE'])
def delete_subscription(subscription_id):
    try:
        subscription = subscriptions.pop(subscription_id, None)
        if not subscription:
            return error_response("Subscription not found", 404)

        return jsonify({"message": "Subscription deleted successfully"}), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Health check route
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
