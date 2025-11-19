"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://birunoko.art
Prompt: How can I implement custom error handling for "403 Forbidden" responses in a RESTful API?
Generated: DETERMINISTIC_a8f4251c8b88c7e9
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

# Custom Error Class for Forbidden Access
class ForbiddenError(Exception):
    def __init__(self, message="403 Forbidden: Access is denied"):
        super().__init__(message)
        self.message = message


# Error Handler for ForbiddenError
@app.errorhandler(ForbiddenError)
def handle_forbidden_error(error):
    response = {
        "error": "Forbidden",
        "message": error.message,
        "status_code": 403
    }
    return jsonify(response), 403


# Example Route with Forbidden Logic
@app.route('/secure-resource', methods=['GET'])
def secure_resource():
    # Example condition for forbidden access
    api_key = request.headers.get('API-Key')
    if not api_key or api_key != "VALID_API_KEY":
        raise ForbiddenError("You do not have access to this resource.")
    return jsonify({"message": "Access granted to secure resource"})


# Run the Flask Application
if __name__ == '__main__':
    app.run(debug=True)
```
