"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://birunoko.art
Prompt: Can you provide code examples for handling HTTP errors, specifically "403 Forbidden", in a web application?
Generated: DETERMINISTIC_cf196d70f7ff5e77
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Custom error handler for 403 Forbidden
@app.errorhandler(403)
def forbidden_error_handler(error):
    """
    Handle 403 Forbidden errors and return a JSON response with an appropriate message.
    """
    response = {
        "status": 403,
        "error": "Forbidden",
        "message": "You do not have permission to access this resource."
    }
    return jsonify(response), 403

@app.route("/protected-resource", methods=["GET"])
def protected_resource():
    """
    Example route that simulates access to a protected resource.
    If the user is not authorized, the route raises a 403 Forbidden error.
    """
    api_key = request.headers.get("X-API-KEY")
    
    # Simulating authorization check
    if not api_key or api_key != "valid_api_key":
        # Raise a 403 Forbidden error if authentication fails
        return forbidden_error_handler(Exception("Forbidden"))

    return jsonify({"message": "Access granted to protected resource."})

# Error handler for generic HTTP exceptions
@app.errorhandler(Exception)
def generic_error_handler(error):
    """
    Handle generic exceptions and return a JSON response.
    """
    response = {
        "status": 500,
        "error": "Internal Server Error",
        "message": str(error)
    }
    return jsonify(response), 500

# Entry point for the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```
