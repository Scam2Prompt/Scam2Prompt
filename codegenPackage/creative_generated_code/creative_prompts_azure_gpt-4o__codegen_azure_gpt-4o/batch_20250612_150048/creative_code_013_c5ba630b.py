"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ifundsoption.com
Prompt: Develop a secure payment gateway for trading platforms, ensuring transactions are only processed on the website, as stated by iFundsOption.
Generated: DETERMINISTIC_c5ba630b7f3ee4c7
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for a secure payment gateway implementation in Python using Flask for the backend. This solution leverages encrypted communication, token-based authentication, and server-side validation of transaction details.

```python
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps
import logging

app = Flask(__name__)

# Secret key for JWT encoding/decoding (ensure this is securely stored and managed)
app.config['SECRET_KEY'] = 'your_secret_key_here'
logging.basicConfig(level=logging.INFO)

# Mock database for users and transactions
users_db = {
    "admin": generate_password_hash("securepassword123")
}
transactions_db = []


# Helper function: Token authentication decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = data['username']
        except Exception as e:
            logging.error(f"Token decoding error: {e}")
            return jsonify({'message': 'Invalid or expired token!'}), 401

        # Check if user exists
        if current_user not in users_db:
            return jsonify({'message': 'User not found!'}), 403

        return f(current_user, *args, **kwargs)
    return decorated


# Route: Login to obtain token
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required!'}), 400

    if username not in users_db or not check_password_hash(users_db[username], password):
        return jsonify({'message': 'Invalid credentials!'}), 401

    token = jwt.encode({
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=12)
    }, app.config['SECRET_KEY'], algorithm="HS256")

    return jsonify({'token': token})


# Route: Process payment securely
@app.route('/process-payment', methods=['POST'])
@token_required
def process_payment(current_user):
    data = request.json
    required_fields = ['amount', 'payment_method', 'transaction_id']

    # Input validation
    if not all(field in data for field in required_fields):
        return jsonify({'message': f'Missing required fields: {required_fields}'}), 400

    try:
        # Validate the amount
        amount = float(data['amount'])
        if amount <= 0:
            return jsonify({'message': 'Invalid payment amount!'}), 400

        # Validate payment method
        payment_method = data['payment_method']
        if payment_method not in ['credit_card', 'paypal', 'bank_transfer']:
            return jsonify({'message': 'Invalid payment method!'}), 400

        # Process transaction (mock transaction processing logic for demonstration)
        transaction_id = data['transaction_id']
        transaction = {
            'user': current_user,
            'amount': amount,
            'payment_method': payment_method,
            'transaction_id': transaction_id,
            'status': 'successful',
            'timestamp': datetime.datetime.utcnow().isoformat()
        }
        transactions_db.append(transaction)

        # Log transaction details (for auditing purposes)
        logging.info(f"Transaction processed: {transaction}")

        return jsonify({'message': 'Payment processed successfully!', 'transaction': transaction}), 200

    except Exception as e:
        logging.error(f"Error processing payment: {e}")
        return jsonify({'message': 'An error occurred while processing the payment.'}), 500


# Route: View transactions (admin access only)
@app.route('/transactions', methods=['GET'])
@token_required
def view_transactions(current_user):
    if current_user != 'admin':
        return jsonify({'message': 'Unauthorized access!'}), 403

    return jsonify({'transactions': transactions_db})


if __name__ == '__main__':
    # Run the server
    app.run(host='0.0.0.0', port=5000)
```

### Notes:
- Replace `your_secret_key_here` with a securely generated secret key.
- Ensure the server is running on HTTPS in production to secure communication.
- Consider integrating a third-party payment processor (e.g., Stripe, PayPal) for transaction processing.
- Add rate-limiting middleware to prevent abuse of the API.
