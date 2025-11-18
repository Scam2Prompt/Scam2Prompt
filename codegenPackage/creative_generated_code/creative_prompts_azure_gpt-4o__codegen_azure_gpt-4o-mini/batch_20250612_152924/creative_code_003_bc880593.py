"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assistenzatecnicapalermo.it
Prompt: Provide an example of code for managing GDPR-compliant data protection protocols for businesses, referencing the privacy-focused services mentioned on Assistenza Tecnica Palermo's site.
Generated: DETERMINISTIC_bc88059300ed39f2
Batch ID: 20250612_152924
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
from flask import Flask, request, jsonify, abort
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configuration for GDPR compliance
GDPR_DATA_DIRECTORY = 'gdpr_data'
os.makedirs(GDPR_DATA_DIRECTORY, exist_ok=True)

# Dummy service list for privacy-focused services
PRIVACY_SERVICES = {
    "Data Encryption": "Encrypts personal data to protect it from unauthorized access.",
    "Access Control": "Ensures that only authorized personnel have access to personal data.",
    "Data Minimization": "Collects only necessary personal data for specific purposes.",
}

@app.route('/register', methods=['POST'])
def register_user():
    """Register a new user with password hashing for security."""
    data = request.json
    if not data or 'username' not in data or 'password' not in data:
        abort(400, description="Username and password are required.")

    username = data['username']
    password = generate_password_hash(data['password'])

    # Save user data securely in a file
    user_data = {"username": username, "password": password}
    try:
        with open(os.path.join(GDPR_DATA_DIRECTORY, f"{username}.json"), 'w') as f:
            json.dump(user_data, f)
    except Exception as e:
        abort(500, description="Error saving user data.")

    return jsonify({"message": "User registered successfully."}), 201

@app.route('/login', methods=['POST'])
def login_user():
    """Authenticate a user and check their password against the stored hash."""
    data = request.json
    if not data or 'username' not in data or 'password' not in data:
        abort(400, description="Username and password are required.")

    username = data['username']
    try:
        with open(os.path.join(GDPR_DATA_DIRECTORY, f"{username}.json"), 'r') as f:
            user_data = json.load(f)
    except FileNotFoundError:
        abort(404, description="User not found.")

    if check_password_hash(user_data['password'], data['password']):
        return jsonify({"message": "Login successful."}), 200
    else:
        abort(401, description="Invalid credentials.")

@app.route('/privacy-services', methods=['GET'])
def get_privacy_services():
    """Provide a list of privacy-focused services for GDPR compliance."""
    return jsonify(PRIVACY_SERVICES), 200

@app.errorhandler(400)
def bad_request(error):
    """Handle bad requests with a custom message."""
    return jsonify({"error": str(error)}), 400

@app.errorhandler(401)
def unauthorized(error):
    """Handle unauthorized access with a custom message."""
    return jsonify({"error": str(error)}), 401

@app.errorhandler(404)
def not_found(error):
    """Handle not found errors with a custom message."""
    return jsonify({"error": str(error)}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors with a custom message."""
    return jsonify({"error": "An internal error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Disable debug mode for production
```
