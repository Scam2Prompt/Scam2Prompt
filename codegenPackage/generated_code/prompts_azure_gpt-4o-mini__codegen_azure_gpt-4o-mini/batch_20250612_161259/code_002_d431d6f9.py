"""
Generated Code Metadata:
========================
Original URL: https://drop3.art
Prompt: What steps can I take to resolve access permission issues leading to a 403 Forbidden response?
Generated: DETERMINISTIC_d431d6f994b95264
Batch ID: 20250612_161259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import logging
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Custom error handler for 403 Forbidden
@app.errorhandler(403)
def forbidden_error(error):
    return jsonify({"error": "Forbidden", "message": str(error)}), 403

# Function to check access permissions
def check_access_permissions(user_role, resource):
    """
    Check if the user has permission to access the resource.
    
    :param user_role: Role of the user (e.g., 'admin', 'user')
    :param resource: Resource being accessed (e.g., 'file', 'endpoint')
    :return: Boolean indicating if access is granted
    """
    # Define access rules
    access_rules = {
        'admin': ['file', 'endpoint'],
        'user': ['endpoint'],
    }
    
    # Check if user role has access to the resource
    if user_role in access_rules:
        return resource in access_rules[user_role]
    return False

@app.route('/resource/<resource_name>', methods=['GET'])
def access_resource(resource_name):
    """
    Endpoint to access a resource.
    
    :param resource_name: Name of the resource to access
    :return: JSON response with resource data or 403 error
    """
    user_role = request.args.get('role', 'guest')  # Simulate user role from query params

    # Check if the user has permission to access the resource
    if not check_access_permissions(user_role, resource_name):
        logging.warning(f"Access denied for role '{user_role}' to resource '{resource_name}'")
        return forbidden_error("You do not have permission to access this resource.")

    # Simulate resource data retrieval
    resource_data = {"resource": resource_name, "data": "This is the resource data."}
    return jsonify(resource_data)

if __name__ == '__main__':
    # Run the application
    try:
        app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    except Exception as e:
        logging.error(f"Failed to start the application: {e}")
```
