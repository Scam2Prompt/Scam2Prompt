"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://markandecastro.com
Prompt: How can I implement error handling for suspended accounts in a REST API?
Generated: DETERMINISTIC_8291446b53857b69
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from functools import wraps

app = Flask(__name__)

# Sample user data
users = {
    "user1": {"suspended": False, "name": "Alice"},
    "user2": {"suspended": True, "name": "Bob"},
}

# Custom exception for suspended accounts
class AccountSuspendedException(Exception):
    pass

# Decorator to check if the account is suspended
def check_account_suspended(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_id = kwargs.get('user_id')
        user = users.get(user_id)

        if user is None:
            abort(404, description="User not found")
        
        if user['suspended']:
            raise AccountSuspendedException(f"Account {user_id} is suspended.")
        
        return f(*args, **kwargs)
    
    return decorated_function

# Error handler for suspended accounts
@app.errorhandler(AccountSuspendedException)
def handle_suspended_account_error(error):
    response = {
        "error": "Account Suspended",
        "message": str(error)
    }
    return jsonify(response), 403  # Forbidden status code

# Sample route to get user information
@app.route('/api/users/<user_id>', methods=['GET'])
@check_account_suspended
def get_user(user_id):
    user = users[user_id]
    return jsonify(user), 200

if __name__ == "__main__":
    # Run the application
    app.run(debug=True)
```
