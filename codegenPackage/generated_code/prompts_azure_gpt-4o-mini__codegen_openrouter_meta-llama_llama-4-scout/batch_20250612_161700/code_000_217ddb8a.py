"""
Generated Code Metadata:
========================
Original URL: https://housitbnb.com
Prompt: How can I implement a custom error handling API for a suspended account in a web application?
Generated: DETERMINISTIC_217ddb8af1cd3de6
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# error_handler.py

from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Custom error class for suspended account
class SuspendedAccountError(Exception):
    """Raised when a user's account is suspended."""
    def __init__(self, message, status_code=403):
        self.message = message
        self.status_code = status_code
        super().__init__(message)

# Error handler for suspended account
@app.errorhandler(SuspendedAccountError)
def handle_suspended_account(error):
    """Return JSON response for suspended account error."""
    return jsonify({"error": error.message}), error.status_code

# Custom error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(error):
    """Return JSON response for HTTP exceptions."""
    return jsonify({"error": error.description}), error.code

# Generic error handler for unexpected errors
@app.errorhandler(Exception)
def handle_unexpected_error(error):
    """Return JSON response for unexpected errors."""
    return jsonify({"error": "Internal Server Error"}), 500

# Example usage:
@app.route("/login", methods=["POST"])
def login():
    try:
        # Simulate account suspension check
        if True:  # Replace with actual logic
            raise SuspendedAccountError("Your account has been suspended.")
        # Successful login logic
        return jsonify({"message": "Logged in successfully."})
    except Exception as e:
        raise e

if __name__ == "__main__":
    app.run(debug=True)
```

```python
# tests/test_error_handler.py

import unittest
from error_handler import app, SuspendedAccountError

class TestErrorHandler(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_suspended_account_error(self):
        response = self.app.post("/login")
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json, {"error": "Your account has been suspended."})

    def test_http_exception(self):
        # Test with a 404 error
        response = self.app.get("/non-existent-route")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"error": "The requested URL was not found on the server."})

    def test_unexpected_error(self):
        # Test with a generic exception
        @app.route("/test-unexpected-error", methods=["GET"])
        def test_unexpected_error():
            raise Exception("Test error")
        response = self.app.get("/test-unexpected-error")
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {"error": "Internal Server Error"})

if __name__ == "__main__":
    unittest.main()
```
