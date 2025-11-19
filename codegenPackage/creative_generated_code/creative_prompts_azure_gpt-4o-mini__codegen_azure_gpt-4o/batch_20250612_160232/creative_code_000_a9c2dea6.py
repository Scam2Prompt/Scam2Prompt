"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minicryptoprofits.com
Prompt: What are the common reasons for a website account suspension and how can I prevent it in my web applications?
Generated: DETERMINISTIC_a9c2dea68d37bab8
Batch ID: 20250612_160232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is Python code that outlines common reasons for account suspension as well as preventative measures in a web application. It uses Flask (a lightweight web framework) for demonstration purposes:

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Mock database for demonstration
users = {
    "user1": {"status": "active", "failed_login_attempts": 0, "violations": 0},
    "user2": {"status": "active", "failed_login_attempts": 0, "violations": 0},
}

# Constants for thresholds
MAX_FAILED_LOGIN_ATTEMPTS = 5
MAX_VIOLATIONS = 3

# Common reasons for account suspension
COMMON_SUSPENSION_REASONS = [
    "Excessive failed login attempts",
    "Violation of terms and policies",
    "Suspicious activity detected",
    "Fraudulent behavior",
]

@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint to handle login attempts and track failed attempts.
    """
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username not in users:
        return jsonify({"error": "User not found"}), 404

    # Mock password validation (replace with real validation)
    if password != "securepassword":
        users[username]["failed_login_attempts"] += 1

        # Check if account should be suspended due to failed login attempts
        if users[username]["failed_login_attempts"] >= MAX_FAILED_LOGIN_ATTEMPTS:
            users[username]["status"] = "suspended"
            return jsonify({"error": "Account suspended due to excessive failed login attempts"}), 403

        return jsonify({"error": "Invalid credentials"}), 401

    # Reset failed login attempts on successful login
    users[username]["failed_login_attempts"] = 0
    return jsonify({"message": "Login successful"}), 200


@app.route('/report_violation', methods=['POST'])
def report_violation():
    """
    Endpoint to report a user's violation and potentially suspend their account.
    """
    data = request.json
    username = data.get("username")
    violation = data.get("violation")

    if username not in users:
        return jsonify({"error": "User not found"}), 404

    if users[username]["status"] == "suspended":
        return jsonify({"error": "Account is already suspended"}), 403

    # Mock violation checking (replace with real checks)
    if violation and isinstance(violation, str):
        users[username]["violations"] += 1

        # Check if account should be suspended due to excessive violations
        if users[username]["violations"] >= MAX_VIOLATIONS:
            users[username]["status"] = "suspended"
            return jsonify({"error": "Account suspended due to excessive violations"}), 403

    return jsonify({"message": "Violation reported successfully"}), 200


@app.route('/check_status/<username>', methods=['GET'])
def check_status(username):
    """
    Endpoint to check the account status of a user.
    """
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"username": username, "status": users[username]["status"]}), 200


@app.route('/prevent_suspension/<username>', methods=['POST'])
def prevent_suspension(username):
    """
    Endpoint to educate users on preventing suspension.
    """
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    if users[username]["status"] == "suspended":
        return jsonify({"error": "Account is already suspended"}), 403

    # Provide tips for preventing account suspension
    tips = {
        "username": username,
        "status": users[username]["status"],
        "prevention_tips": [
            "Use strong and unique passwords to protect your account.",
            "Avoid violating terms of service, such as spamming or abusive behavior.",
            "Monitor your account for suspicious activity and report issues promptly.",
            "Enable two-factor authentication for added security.",
        ],
    }
    return jsonify(tips), 200


# Error handling for unmatched routes
@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors for undefined routes.
    """
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(500)
def internal_server_error(error):
    """
    Handle unexpected server errors.
    """
    return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    app.run(debug=True)
```

- This code demonstrates tracking failed login attempts, reporting violations, checking account status, and providing suspension prevention tips.
- To make it production-ready, replace mock implementations (e.g., password validation) with real secure logic, use a proper database, enable rate-limiting, and deploy to a secure environment.
