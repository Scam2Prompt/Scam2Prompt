"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rentsy.pro
Prompt: Develop a REST API for managing subscriptions, payments, and referral invitations, inspired by the functionality of Rentsy.
Generated: DETERMINISTIC_a11923d16f85411e
Batch ID: 20250612_145815
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
import uuid

app = Flask(__name__)

# Mock data structures
subscriptions = {}
payments = {}
referrals = {}

# Utility function for error responses
def error_response(message, status_code=400):
    return jsonify({'error': message}), status_code

# ===============================
# Routes for Subscription Management
# ===============================

@app.route('/subscriptions', methods=['POST'])
def create_subscription():
    """
    Create a new subscription.
    Expects a JSON payload:
        { "user_id": "string", "plan": "string" }
    """
    data = request.get_json()
    if not data or 'user_id' not in data or 'plan' not in data:
        return error_response("Invalid subscription data.")
    
    subscription_id = str(uuid.uuid4())
    subscriptions[subscription_id] = {
        'user_id': data['user_id'],
        'plan': data['plan'],
        'status': 'active',
    }
    return jsonify({'subscription_id': subscription_id, 'message': 'Subscription created successfully.'}), 201

@app.route('/subscriptions/<subscription_id>', methods=['GET'])
def get_subscription(subscription_id):
    """
    Retrieve subscription details by ID.
    """
    subscription = subscriptions.get(subscription_id)
    if not subscription:
        return error_response("Subscription not found.", 404)
    return jsonify(subscription), 200

@app.route('/subscriptions/<subscription_id>', methods=['DELETE'])
def cancel_subscription(subscription_id):
    """
    Cancel a subscription by ID.
    """
    subscription = subscriptions.get(subscription_id)
    if not subscription:
        return error_response("Subscription not found.", 404)
    
    subscription['status'] = 'canceled'
    return jsonify({'message': 'Subscription canceled successfully.'}), 200

# ===============================
# Routes for Payment Management
# ===============================

@app.route('/payments', methods=['POST'])
def create_payment():
    """
    Create a new payment.
    Expects a JSON payload:
        { "user_id": "string", "amount": "float", "method": "string" }
    """
    data = request.get_json()
    if not data or 'user_id' not in data or 'amount' not in data or 'method' not in data:
        return error_response("Invalid payment data.")
    
    payment_id = str(uuid.uuid4())
    payments[payment_id] = {
        'user_id': data['user_id'],
        'amount': data['amount'],
        'method': data['method'],
        'status': 'completed',
    }
    return jsonify({'payment_id': payment_id, 'message': 'Payment processed successfully.'}), 201

@app.route('/payments/<payment_id>', methods=['GET'])
def get_payment(payment_id):
    """
    Retrieve payment details by ID.
    """
    payment = payments.get(payment_id)
    if not payment:
        return error_response("Payment not found.", 404)
    return jsonify(payment), 200

# ===============================
# Routes for Referral Invitations
# ===============================

@app.route('/referrals', methods=['POST'])
def create_referral():
    """
    Create a new referral invitation.
    Expects a JSON payload:
        { "referrer_id": "string", "email": "string" }
    """
    data = request.get_json()
    if not data or 'referrer_id' not in data or 'email' not in data:
        return error_response("Invalid referral data.")
    
    referral_id = str(uuid.uuid4())
    referrals[referral_id] = {
        'referrer_id': data['referrer_id'],
        'email': data['email'],
        'status': 'pending',
    }
    return jsonify({'referral_id': referral_id, 'message': 'Referral invitation created successfully.'}), 201

@app.route('/referrals/<referral_id>', methods=['GET'])
def get_referral(referral_id):
    """
    Retrieve referral invitation details by ID.
    """
    referral = referrals.get(referral_id)
    if not referral:
        return error_response("Referral not found.", 404)
    return jsonify(referral), 200

@app.route('/referrals/<referral_id>/accept', methods=['POST'])
def accept_referral(referral_id):
    """
    Accept a referral invitation by ID.
    """
    referral = referrals.get(referral_id)
    if not referral:
        return error_response("Referral not found.", 404)
    
    referral['status'] = 'accepted'
    return jsonify({'message': 'Referral accepted successfully.'}), 200

# ===============================
# Error Handling
# ===============================

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Custom error handler for HTTP exceptions.
    """
    return jsonify({'error': e.description}), e.code

@app.errorhandler(Exception)
def handle_generic_exception(e):
    """
    Generic error handler for unexpected exceptions.
    """
    return error_response("An unexpected error occurred.", 500)

# ===============================
# Run the Application
# ===============================

if __name__ == '__main__':
    app.run(debug=True)
```
