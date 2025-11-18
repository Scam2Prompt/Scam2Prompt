"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://klarna.ctpe.info
Prompt: Write a Python script using Flask to handle login requests and password recovery, inspired by the functionality on https://klarna.ctpe.info.
Generated: DETERMINISTIC_17df868f84459940
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session, render_template_string
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Use a secure and random key in production

# Mock database (replace with a real database in production)
users_db = {
    "user@example.com": {
        "password": generate_password_hash("password123"),  # Example hashed password
        "security_question": "What is your pet's name?",
        "security_answer": generate_password_hash("Fluffy"),  # Example hashed answer
    }
}

# Regular expression for validating email addresses
EMAIL_REGEX = re.compile(r'^[^@]+@[^@]+\.[^@]+$')


@app.route('/login', methods=['POST'])
def login():
    """
    Handles login requests.
    Expects JSON payload in the format:
    {
        "email": "user@example.com",
        "password": "password123"
    }
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input format. JSON expected"}), 400

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    if not EMAIL_REGEX.match(email):
        return jsonify({"error": "Invalid email format"}), 400

    # Simulate database lookup
    user = users_db.get(email)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid email or password"}), 401

    # Create session
    session['user'] = email
    return jsonify({"message": "Login successful"}), 200


@app.route('/recover_password', methods=['POST'])
def recover_password():
    """
    Handles password recovery.
    Expects JSON payload in the format:
    {
        "email": "user@example.com",
        "security_answer": "Fluffy"
    }
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input format. JSON expected"}), 400

    email = data.get('email')
    security_answer = data.get('security_answer')

    if not email or not security_answer:
        return jsonify({"error": "Email and security answer are required"}), 400

    if not EMAIL_REGEX.match(email):
        return jsonify({"error": "Invalid email format"}), 400

    # Simulate database lookup
    user = users_db.get(email)
    if not user:
        return jsonify({"error": "Email not found"}), 404

    # Verify security answer
    if not check_password_hash(user["security_answer"], security_answer):
        return jsonify({"error": "Security answer is incorrect"}), 401

    # Password recovery successful
    return jsonify({"message": "Password recovery successful. Please contact support to reset your password."}), 200


@app.route('/')
def index():
    """
    Simple homepage for testing purposes.
    """
    return render_template_string("""
    <h1>Welcome to the Flask Login and Password Recovery App</h1>
    <p>Use the /login and /recover_password endpoints for functionality.</p>
    """)


if __name__ == '__main__':
    app.run(debug=True)  # Disable debug mode in production
```
