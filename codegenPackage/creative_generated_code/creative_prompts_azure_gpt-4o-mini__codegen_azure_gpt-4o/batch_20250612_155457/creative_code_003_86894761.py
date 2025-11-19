"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sensibleoptimism.com
Prompt: Develop an API endpoint for managing user subscriptions, taking cues from the subscription model mentioned on the Sensible Optimism page.
Generated: DETERMINISTIC_86894761cf36398f
Batch ID: 20250612_155457
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

# Mock database for user subscriptions
subscriptions = {}

# Error class for user-defined exceptions
class SubscriptionError(Exception):
    def __init__(self, message):
        self.message = message

# API Endpoint: Manage user subscriptions
@app.route('/subscriptions', methods=['POST', 'GET', 'PUT', 'DELETE'])
def manage_subscriptions():
    try:
        if request.method == 'POST':
            # Create a new subscription
            data = request.get_json()
            user_id = data.get('user_id')
            plan = data.get('plan')

            if not user_id or not plan:
                raise SubscriptionError("Missing required fields: 'user_id' and 'plan'")

            if user_id in subscriptions:
                raise SubscriptionError(f"User with ID {user_id} already has a subscription")

            subscriptions[user_id] = {'plan': plan}
            return jsonify({"message": "Subscription created successfully", "data": subscriptions[user_id]}), 201

        elif request.method == 'GET':
            # Retrieve subscription for a user
            user_id = request.args.get('user_id')

            if not user_id:
                raise SubscriptionError("Missing required query parameter: 'user_id'")

            subscription = subscriptions.get(user_id)
            if not subscription:
                raise SubscriptionError(f"No subscription found for user ID {user_id}")

            return jsonify({"message": "Subscription retrieved successfully", "data": subscription}), 200

        elif request.method == 'PUT':
            # Update subscription for a user
            data = request.get_json()
            user_id = data.get('user_id')
            new_plan = data.get('plan')

            if not user_id or not new_plan:
                raise SubscriptionError("Missing required fields: 'user_id' and 'plan'")

            subscription = subscriptions.get(user_id)
            if not subscription:
                raise SubscriptionError(f"No subscription found for user ID {user_id}")

            subscriptions[user_id]['plan'] = new_plan
            return jsonify({"message": "Subscription updated successfully", "data": subscriptions[user_id]}), 200

        elif request.method == 'DELETE':
            # Delete subscription for a user
            user_id = request.args.get('user_id')

            if not user_id:
                raise SubscriptionError("Missing required query parameter: 'user_id'")

            subscription = subscriptions.pop(user_id, None)
            if not subscription:
                raise SubscriptionError(f"No subscription found for user ID {user_id}")

            return jsonify({"message": "Subscription deleted successfully"}), 200

    except SubscriptionError as e:
        return jsonify({"error": e.message}), 400
    except HTTPException as e:
        return jsonify({"error": e.description}), e.code
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
