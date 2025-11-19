"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://housitbnb.com
Prompt: How can I implement a custom error handling API for a suspended account in a web application?
Generated: DETERMINISTIC_217ddb8af1cd3de6
Batch ID: 20250612_161700
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

# Custom exception for suspended accounts
class SuspendedAccountError(Exception):
    def __init__(self, message="The account is suspended. Please contact support."):
        self.message = message
        super().__init__(self.message)

# Error handler for SuspendedAccountError
@app.errorhandler(SuspendedAccountError)
def handle_suspended_account_error(error):
    response = {
        "status": "error",
        "error": "SuspendedAccountError",
        "message": error.message
    }
    return jsonify(response), 403  # HTTP 403 Forbidden status code

# Sample route to simulate account suspension
@app.route("/account", methods=["GET"])
def account_details():
    # Simulated condition for a suspended account
    user_account = {"username": "john_doe", "status": "suspended"}
    
    if user_account["status"] == "suspended":
        # Raise the custom error for suspended accounts
        raise SuspendedAccountError()
    
    return jsonify(user_account)

# Generic error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_generic_error(error):
    response = {
        "status": "error",
        "error": "InternalServerError",
        "message": str(error)
    }
    return jsonify(response), 500  # HTTP 500 Internal Server Error

# Health check endpoint
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```
