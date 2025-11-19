"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lulu-malls.in
Prompt: What are the common reasons for a website account suspension and how can I prevent it in my web applications?
Generated: DETERMINISTIC_a9c2dea68d37bab8
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is Python code for a web application that demonstrates how to handle and prevent common account suspension issues:

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Mock database of user accounts
accounts = {
    "user1": {"status": "active", "login_attempts": 0, "email": "user1@example.com"},
    "user2": {"status": "suspended", "login_attempts": 0, "email": "user2@example.com"},
}

# Suspension reasons constants
REASONS = {
    "TOO_MANY_LOGIN_ATTEMPTS": "Too many failed login attempts.",
    "INVALID_EMAIL": "Invalid email format.",
    "VIOLATED_TERMS": "Violation of terms of service.",
}

def validate_email(email):
    """
    Validates email format using regex.
    
    :param email: Email address to validate
    :return: True if valid, False otherwise
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@app.route('/login', methods=['POST'])
def login():
    """
    Handles user login and checks for account suspension reasons.
    
    :return: JSON response indicating success or reason for suspension
    """
    data = request.json
    username = data.get("username")
    password = data.get("password")  # In production, hash and verify passwords securely

    if username not in accounts:
        return jsonify({"error": "Account not found."}), 404

    account = accounts[username]

    # Check if account is suspended
    if account["status"] == "suspended":
        return jsonify({"error": "Account suspended.", "reason": REASONS.get("VIOLATED_TERMS")}), 403

    # Mock login attempt processing
    if password != "correct_password":  # Replace with secure password checking
        account["login_attempts"] += 1
        if account["login_attempts"] > 3:
            account["status"] = "suspended"
            return jsonify({"error": "Account suspended due to too many failed login attempts.",
                            "reason": REASONS["TOO_MANY_LOGIN_ATTEMPTS"]}), 403
        return jsonify({"error": "Invalid credentials."}), 401

    account["login_attempts"] = 0  # Reset login attempts on successful login
    return jsonify({"message": "Login successful!"}), 200

@app.route('/update-email', methods=['POST'])
def update_email():
    """
    Handles email updates and checks for valid email format.
    
    :return: JSON response indicating success or reason for invalid format
    """
    data = request.json
    username = data.get("username")
    new_email = data.get("email")

    if username not in accounts:
        return jsonify({"error": "Account not found."}), 404

    if not validate_email(new_email):
        return jsonify({"error": "Invalid email format.", "reason": REASONS["INVALID_EMAIL"]}), 400

    accounts[username]["email"] = new_email
    return jsonify({"message": "Email updated successfully!"}), 200

@app.route('/terms-violation', methods=['POST'])
def report_violation():
    """
    Handles account suspension for terms violations.
    
    :return: JSON response confirming suspension
    """
    data = request.json
    username = data.get("username")

    if username not in accounts:
        return jsonify({"error": "Account not found."}), 404

    accounts[username]["status"] = "suspended"
    return jsonify({"message": f"Account {username} has been suspended due to violation of terms.",
                    "reason": REASONS["VIOLATED_TERMS"]}), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

This code represents a basic web application using Flask to demonstrate prevention of common account suspension reasons. It includes features like validating email format, limiting login attempts, and handling violations of terms of service.
