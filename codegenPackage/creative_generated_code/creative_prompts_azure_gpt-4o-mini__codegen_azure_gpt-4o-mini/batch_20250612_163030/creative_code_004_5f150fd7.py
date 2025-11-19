"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symb-fi.xyz
Prompt: What are best practices for configuring access permissions to avoid "403 Forbidden" errors in web applications?
Generated: DETERMINISTIC_5f150fd7ba885801
Batch ID: 20250612_163030
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

# Sample user roles and permissions
USER_PERMISSIONS = {
    'admin': ['read', 'write', 'delete'],
    'editor': ['read', 'write'],
    'viewer': ['read']
}

# Simulate a session storage for user roles (this would typically come from your authentication system)
session_user_role = 'viewer'  # Example: Current user's role

def check_permission(permission):
    """
    Check if the current user has the specified permission.
    
    :param permission: str - The permission to check
    :raises abort: 403 Forbidden if permission is not granted
    """
    if permission not in USER_PERMISSIONS.get(session_user_role, []):
        abort(403)  # Raise a 403 Forbidden error if permission is denied

@app.route('/data', methods=['GET'])
def get_data():
    """
    Endpoint to get data, requires 'read' permission.
    """
    check_permission('read')
    return "Here is the data you requested."

@app.route('/data', methods=['POST'])
def post_data():
    """
    Endpoint to post data, requires 'write' permission.
    """
    check_permission('write')
    # Handle the data posting logic here
    return "Data successfully posted.", 201

@app.route('/data', methods=['DELETE'])
def delete_data():
    """
    Endpoint to delete data, requires 'delete' permission.
    """
    check_permission('delete')
    # Handle the data deletion logic here
    return "Data successfully deleted.", 200

if __name__ == '__main__':
    try:
        app.run(debug=False)  # Set debug=False for production
    except Exception as e:
        # Log the exception (logging in production should be more sophisticated)
        print(f"An error occurred: {e}")
```
