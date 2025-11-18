"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.maxevent.pro
Prompt: Suggest libraries or tools to build an IPTV application that provides a 24-hour free trial and subscription management, similar to MaxEvent's service structure.
Generated: DETERMINISTIC_02ac818fb7e80903
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# IPTV Subscription Management System

from flask import Flask, jsonify, request, abort
from datetime import datetime, timedelta
from werkzeug.exceptions import NotFound

app = Flask(__name__)

# In-memory data stores (for demo purposes, use a database in production)
subscriptions = {}
trials = {}

# Subscription Plan
class SubscriptionPlan:
    def __init__(self, plan_id, name, price):
        self.plan_id = plan_id
        self.name = name
        self.price = price

# Sample subscription plans
plans = [
    SubscriptionPlan(1, 'Basic Plan', 9.99),
    SubscriptionPlan(2, 'Premium Plan', 19.99)
]

@app.route('/plans', methods=['GET'])
def get_plans():
    """Get available subscription plans"""
    return jsonify([{'id': plan.plan_id, 'name': plan.name, 'price': plan.price} for plan in plans])

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """Create subscription for user with trial period"""
    user_id = request.json.get('user_id')
    plan_id = request.json.get('plan_id')
    
    # Validate input
    if not user_id or not plan_id:
        abort(400, description="User ID and Plan ID are required")

    # Check if the user already has an active subscription
    if user_id in subscriptions:
        abort(400, description="User already has an active subscription")

    # Create a trial period
    trial_end = datetime.now() + timedelta(hours=24)
    trials[user_id] = trial_end
    subscriptions[user_id] = {'plan_id': plan_id, 'active': False}

    return jsonify({"message": "Trial started", "trial_end": trial_end.strftime('%Y-%m-%d %H:%M:%S')}), 201

@app.route('/activate/<user_id>', methods=['POST'])
def activate_subscription(user_id):
    """Activate subscription after trial"""
    # Check if user has a trial
    if user_id not in trials:
        abort(NotFound, description="User does not have an active trial")

    # Check if the trial period has expired
    if datetime.now() > trials[user_id]:
        abort(400, description="Trial period has expired")
    
    # Retrieve plan and activate it
    user_plan_id = subscriptions[user_id]['plan_id']
    subscriptions[user_id]['active'] = True

    # Remove trial data as activation is successful
    del trials[user_id]

    return jsonify({"message": "Subscription activated", "plan_id": user_plan_id}), 200

@app.route('/subscriptions', methods=['GET'])
def list_subscriptions():
    """List all subscriptions"""
    return jsonify(subscriptions)

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(400)
def bad_request(error):
    """Handle 400 errors"""
    return jsonify({"error": str(error)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
This code provides a basic structure for an IPTV application that includes subscription management and a 24-hour free trial feature. It utilizes Flask for web API functionality, handles input validation and errors, and provides endpoints for managing subscription plans, trials, and activations.
