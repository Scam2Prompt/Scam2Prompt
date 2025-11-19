"""
Generated Code Metadata:
========================
Original URL: https://ip-net.org
Prompt: Can you provide code examples for handling 403 Forbidden errors in a web application?
Generated: DETERMINISTIC_3de960b4893544f6
Batch ID: 20250612_161017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from flask import Flask, jsonify, request
from werkzeug.exceptions import Forbidden

app = Flask(__name__)

# Example 1: Handling 403 in a Flask route
@app.route('/protected', methods=['GET'])
def protected_resource():
    auth_token = request.headers.get('Authorization')
    
    if not auth_token or auth_token != 'valid_token':
        raise Forbidden(description="Access denied. Invalid or missing token.")
    
    return jsonify({"message": "Access granted to protected resource"})

# Example 2: Custom 403 error handler in Flask
@app.errorhandler(403)
def handle_forbidden(error):
    response = jsonify({
        "error": "Forbidden",
        "message": error.description,
        "status_code": 403
    })
    response.status_code = 403
    return response

# Example 3: Making a request with 403 handling
def make_api_request(url, headers=None):
    try:
        response = requests.get(url, headers=headers or {})
        response.raise_for_status()  # Raises HTTPError for 4XX/5XX status codes
        return response.json()
    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 403:
            print(f"Access forbidden: {err.response.text}")
            # Implement retry logic or alternative flow here
            return None
        raise  # Re-raise other HTTP errors
    except requests.exceptions.RequestException as err:
        print(f"Request failed: {err}")
        return None

# Example 4: Decorator for role-based access control
def requires_role(role):
    def decorator(f):
        def wrapped(*args, **kwargs):
            user_role = request.headers.get('X-User-Role')
            if user_role != role:
                raise Forbidden(description=f"Requires {role} role")
            return f(*args, **kwargs)
        return wrapped
    return decorator

@app.route('/admin')
@requires_role('admin')
def admin_panel():
    return jsonify({"message": "Welcome to admin panel"})

if __name__ == '__main__':
    app.run(debug=True)
```
