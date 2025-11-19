"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pauiy.app
Prompt: How can I implement security measures in my web application to prevent phishing attacks similar to those flagged on sites like pauiy.app?
Generated: DETERMINISTIC_254e3fc7ff04ebd4
Batch ID: 20250612_162646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, redirect, url_for
import re

# Initialize the Flask application
app = Flask(__name__)

# Define a simple in-memory user database for demonstration
USER_DATABASE = {
    "user@example.com": {"password": "securepassword"},
}

# Regex pattern for validating email addresses
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def is_valid_email(email):
    """Check if the provided email is valid."""
    return re.match(EMAIL_REGEX, email) is not None

@app.route('/login', methods=['POST'])
def login():
    """Handle user login."""
    data = request.get_json()

    # Validate input data
    if 'email' not in data or 'password' not in data:
        return jsonify({"error": "Email and password are required."}), 400

    email = data['email']
    password = data['password']

    # Validate the email format
    if not is_valid_email(email):
        return jsonify({"error": "Invalid email format."}), 400

    # Check user credentials
    user = USER_DATABASE.get(email)
    if user and user['password'] == password:
        # Successful login
        return jsonify({"message": "Login successful!"}), 200
    else:
        # Invalid credentials
        return jsonify({"error": "Invalid email or password."}), 401

@app.route('/report-phishing', methods=['POST'])
def report_phishing():
    """Allow users to report suspected phishing URLs."""
    data = request.get_json()

    # Validate input data
    if 'url' not in data:
        return jsonify({"error": "URL is required."}), 400

    url = data['url']

    # Here you can implement additional validation on the URL if necessary

    # Log the phishing report (in production, this should be stored in a database)
    print(f"Phishing URL reported: {url}")

    return jsonify({"message": "Thank you for reporting!"}), 200

if __name__ == '__main__':
    # Start the Flask application
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"Error starting the server: {e}")
```

This code provides a simple Flask web application that includes user authentication with email validation and a phishing report feature. It includes proper error handling and input validation to enhance security.
