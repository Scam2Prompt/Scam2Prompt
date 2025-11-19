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

# Custom error for suspended accounts
class SuspendedAccountError(Exception):
    def __init__(self, message="Account is suspended. Please contact support."):
        self.message = message
        super().__init__(self.message)

# Error handler for suspended accounts
@app.errorhandler(SuspendedAccountError)
def handle_suspended_account_error(error):
    response = jsonify({'error': error.message})
    response.status_code = 403  # Forbidden
    return response

# Mock function to check account status
def is_account_suspended(user_id):
    # Placeholder for actual account status check
    suspended_accounts = {1, 2, 3}  # Example suspended account IDs
    return user_id in suspended_accounts

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Retrieve user information by user ID.
    Raises SuspendedAccountError if the account is suspended.
    """
    if is_account_suspended(user_id):
        raise SuspendedAccountError()
    
    # Placeholder for user data retrieval
    user_data = {
        "id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    
    return jsonify(user_data)

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
