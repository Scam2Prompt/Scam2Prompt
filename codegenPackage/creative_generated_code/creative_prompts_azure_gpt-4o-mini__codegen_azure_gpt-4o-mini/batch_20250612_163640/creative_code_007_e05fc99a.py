"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://readyplayai.com
Prompt: How can I enforce access control and IAM policies within ReadyPlayAI to protect my AI infrastructure?
Generated: DETERMINISTIC_e05fc99a65252424
Batch ID: 20250612_163640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from flask import Flask, request, jsonify
from functools import wraps

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Sample IAM policy structure stored in memory for demonstration
# This would typically be replaced by a database or a more secure storage
iam_policies = {
    "admin": {"permissions": ["read", "write", "delete"]},
    "user": {"permissions": ["read"]},
}

# Dummy data to simulate users and their roles
user_roles = {
    "alice": "admin",
    "bob": "user",
}

# Function to check user permissions
def check_permissions(role, action):
    """Check if the role has the permission to perform the action."""
    if role in iam_policies:
        permissions = iam_policies[role]["permissions"]
        return action in permissions
    return False

# Decorator for access control
def access_control(action):
    """Decorator to enforce access control based on IAM policies."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Simulate getting the user's username from request headers
            username = request.headers.get("X-Username")
            if not username or username not in user_roles:
                logger.warning(f"Access denied for user: {username}")
                return jsonify({"error": "Access denied"}), 403
            
            role = user_roles[username]
            
            if not check_permissions(role, action):
                logger.warning(f"User {username} with role {role} tried to access {action} without permission")
                return jsonify({"error": "Permission denied"}), 403
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

@app.route('/data', methods=['GET'])
@access_control(action='read')
def read_data():
    """Endpoint to read data, accessible by authorized users only."""
    return jsonify({"data": "Here is your data!"}), 200

@app.route('/data', methods=['POST'])
@access_control(action='write')
def write_data():
    """Endpoint to write data, accessible by users with write permission."""
    content = request.json
    logger.info(f"Data written: {content}")
    return jsonify({"message": "Data written successfully!"}), 201

@app.route('/data', methods=['DELETE'])
@access_control(action='delete')
def delete_data():
    """Endpoint to delete data, accessible by users with delete permission."""
    logger.info("Data deleted successfully!")
    return jsonify({"message": "Data deleted successfully!"}), 204

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=False)
```
