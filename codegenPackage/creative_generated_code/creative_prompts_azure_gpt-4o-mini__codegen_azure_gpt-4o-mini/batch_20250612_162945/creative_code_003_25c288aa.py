"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://birunoko.art
Prompt: What are best practices for securing a web application to prevent unauthorized access leading to a "403 Forbidden" response?
Generated: DETERMINISTIC_25c288aa0d9560d1
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, abort

app = Flask(__name__)

# Simulated user data for demonstration purposes
USER_CREDENTIALS = {
    "admin": "password123",
    "user": "mypassword"
}

# Set of allowed roles for accessing specific resources
ROLE_PERMISSIONS = {
    "admin": ["view", "edit", "delete"],
    "user": ["view"]
}

def validate_credentials(username, password):
    """Validate user credentials against stored user data."""
    return USER_CREDENTIALS.get(username) == password

def check_permissions(role, action):
    """Check if a user role has permission to perform a specific action."""
    if role not in ROLE_PERMISSIONS:
        return False
    return action in ROLE_PERMISSIONS[role]

@app.route('/secure-data', methods=['GET'])
def secure_data():
    """Endpoint that requires authentication and authorization."""
    username = request.authorization.username
    password = request.authorization.password

    # Validate user credentials
    if not validate_credentials(username, password):
        abort(403)  # Forbidden if credentials are invalid

    # Simulate fetching user role
    user_role = username  # In production, fetch the role from a database

    # Check if the user has permission to access this resource
    if not check_permissions(user_role, 'view'):
        abort(403)  # Forbidden if user does not have permission

    return "This is secure data."

@app.errorhandler(403)
def forbidden(error):
    """Custom error handler for 403 Forbidden responses."""
    return {
        "error": "You do not have permission to access this resource."
    }, 403

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
```
