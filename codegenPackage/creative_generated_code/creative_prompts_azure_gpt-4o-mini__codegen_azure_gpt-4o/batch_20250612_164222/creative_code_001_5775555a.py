"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gifts.sparklingz.nl
Prompt: How can I implement a login feature for a webshop similar to Sparklingz that handles customer service inquiries?
Generated: DETERMINISTIC_5775555a91392dea
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a strong secret key for production

# Mock database for example purposes (use a proper database in production)
mock_users_db = {
    "customer1@example.com": generate_password_hash("SecurePassword123"),
    "customer2@example.com": generate_password_hash("AnotherSecurePassword456"),
}

@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint to handle user login.
    Expected JSON payload: { "email": "user@example.com", "password": "password123" }
    """
    try:
        # Parse input data
        data = request.json
        email = data.get("email")
        password = data.get("password")

        # Validate input
        if not email or not password:
            return jsonify({"error": "Email and password are required."}), 400
        
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return jsonify({"error": "Invalid email format."}), 400

        # Check if user exists
        stored_password_hash = mock_users_db.get(email)
        if not stored_password_hash or not check_password_hash(stored_password_hash, password):
            return jsonify({"error": "Invalid email or password."}), 401

        # Create session for user
        session['user_email'] = email

        return jsonify({"message": "Login successful."}), 200

    except Exception as e:
        # Catch unexpected errors
        print(f"Error during login: {e}")
        return jsonify({"error": "An internal error occurred. Please try again later."}), 500


@app.route('/logout', methods=['POST'])
def logout():
    """
    Endpoint to handle user logout.
    """
    try:
        # Clear session
        session.pop('user_email', None)
        return jsonify({"message": "Logout successful."}), 200
    except Exception as e:
        # Catch unexpected errors
        print(f"Error during logout: {e}")
        return jsonify({"error": "An internal error occurred. Please try again later."}), 500


@app.route('/customer-inquiry', methods=['POST'])
def customer_inquiry():
    """
    Endpoint to handle customer inquiries.
    Expected JSON payload: { "message": "I need help with my order." }
    """
    try:
        # Check if user is logged in
        user_email = session.get('user_email')
        if not user_email:
            return jsonify({"error": "Unauthorized. Please log in first."}), 401

        # Parse inquiry message
        data = request.json
        inquiry_message = data.get("message")

        if not inquiry_message:
            return jsonify({"error": "Inquiry message is required."}), 400

        # Process inquiry (in production, forward to customer service system)
        print(f"Customer inquiry from {user_email}: {inquiry_message}")

        return jsonify({"message": "Inquiry received. Customer service will respond shortly."}), 200

    except Exception as e:
        # Catch unexpected errors
        print(f"Error during customer inquiry: {e}")
        return jsonify({"error": "An internal error occurred. Please try again later."}), 500


if __name__ == '__main__':
    # Start the Flask development server (use a production server like Gunicorn in production)
    app.run(debug=True)
```
