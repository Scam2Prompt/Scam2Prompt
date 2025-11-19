"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://locinews.com
Prompt: Illustrate how to implement a secure payment gateway for Bet88, focusing on deposit and withdrawal functionalities.
Generated: DETERMINISTIC_a44f6c14ed803f8d
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import logging
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import stripe

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load environment variables
stripe.api_key = os.getenv('STRIPE_API_KEY')

# In-memory storage for user data (Replace with a database in production)
users = {}

# Function to register a new user
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # Store user credentials securely
    users[username] = generate_password_hash(password)
    return jsonify({"message": "User registered successfully"}), 201

# Function to authenticate user
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user_password_hash = users.get(username)
    if not user_password_hash or not check_password_hash(user_password_hash, password):
        return jsonify({"error": "Invalid credentials"}), 401

    return jsonify({"message": "Login successful"}), 200

# Function to deposit funds
@app.route('/deposit', methods=['POST'])
def deposit():
    data = request.json
    username = data.get('username')
    amount = data.get('amount')
    token = data.get('token')

    # Basic validation
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    if amount <= 0:
        return jsonify({"error": "Invalid amount"}), 400

    try:
        # Process the payment using Stripe
        charge = stripe.Charge.create(
            amount=int(amount * 100),  # Amount in cents
            currency="usd",
            source=token,
            description=f"Deposit for {username}"
        )
        return jsonify({"message": "Deposit successful", "charge": charge}), 200
    except stripe.error.StripeError as e:
        logging.error(f"Stripe error during deposit: {e}")
        return jsonify({"error": "Payment processing error"}), 500

# Function to withdraw funds
@app.route('/withdraw', methods=['POST'])
def withdraw():
    data = request.json
    username = data.get('username')
    amount = data.get('amount')

    # Basic validation
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    if amount <= 0:
        return jsonify({"error": "Invalid amount"}), 400

    # Note: In a real application, you'd check user balance here
    try:
        # Simulate withdrawal process
        logging.info(f"Withdrawal request for {username}: ${amount}")
        return jsonify({"message": "Withdrawal successful"}), 200
    except Exception as e:
        logging.error(f"Error processing withdrawal: {e}")
        return jsonify({"error": "Withdrawal processing error"}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements:
- Make sure to set the environment variable `STRIPE_API_KEY` with your actual Stripe API key.
- Adjust the in-memory storage of users to a persistent database for production use.
- Implement additional security measures as necessary, such as rate limiting and input validation.
