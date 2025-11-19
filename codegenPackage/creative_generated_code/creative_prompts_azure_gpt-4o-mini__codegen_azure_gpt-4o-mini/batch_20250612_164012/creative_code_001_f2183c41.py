"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connecting-collabs.vip
Prompt: What are best practices for handling session timeouts in APIs, and how can I ensure users can request a new session seamlessly?
Generated: DETERMINISTIC_f2183c417890191d
Batch ID: 20250612_164012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session, make_response
from datetime import timedelta
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key
app.permanent_session_lifetime = timedelta(minutes=30)  # Set session timeout duration

# Custom decorator to check session validity
def require_session(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # If session is expired or does not exist, send a session expired response
            return jsonify({'message': 'Session expired. Please log in again.'}), 401
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['POST'])
def login():
    """Simulate user login and create a session."""
    user_id = request.json.get('user_id')
    if user_id:
        session['user_id'] = user_id  # Store user ID in session
        session.permanent = True  # Make the session permanent
        return jsonify({'message': 'Login successful', 'user_id': user_id}), 200
    return jsonify({'message': 'Invalid user ID'}), 400

@app.route('/renew-session', methods=['POST'])
@require_session
def renew_session():
    """Renew the session for an active user."""
    session.modified = True  # Mark the session as modified to reset the timeout
    return jsonify({'message': 'Session renewed successfully'}), 200

@app.route('/protected', methods=['GET'])
@require_session
def protected_route():
    """Example of a protected route that requires a valid session."""
    return jsonify({'message': 'This is a protected route!', 'user_id': session['user_id']}), 200

@app.route('/logout', methods=['POST'])
@require_session
def logout():
    """Logout the user and clear the session."""
    session.clear()  # Clear the session data
    return jsonify({'message': 'Logout successful'}), 200

if __name__ == '__main__':
    # Run the app on localhost with debug mode off for production
    app.run(host='0.0.0.0', port=5000, debug=False)
```
