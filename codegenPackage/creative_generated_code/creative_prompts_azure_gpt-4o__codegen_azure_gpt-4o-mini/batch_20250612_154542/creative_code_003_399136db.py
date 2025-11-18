"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zapper-dve8s7yrg-epherum.vercel.app
Prompt: Generate code for a demo login system with predefined roles (Admin, Project Manager, Developer, Submitter) to simulate the functionality of the Zapper task tracker platform.
Generated: DETERMINISTIC_399136dba45cafb1
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret string

# In-memory user database simulation
users_db = {
    'admin': {'password': generate_password_hash('admin_pass'), 'role': 'Admin'},
    'pm': {'password': generate_password_hash('pm_pass'), 'role': 'Project Manager'},
    'dev': {'password': generate_password_hash('dev_pass'), 'role': 'Developer'},
    'submitter': {'password': generate_password_hash('submitter_pass'), 'role': 'Submitter'}
}

@app.route('/login', methods=['POST'])
def login():
    """Endpoint to log in a user."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not username or not password:
        return jsonify({"error": "Username and password are required."}), 400

    user = users_db.get(username)
    
    # Check if user exists and password is correct
    if user and check_password_hash(user['password'], password):
        session['username'] = username  # Store username in session
        return jsonify({"message": "Login successful.", "role": user['role']}), 200
    else:
        return jsonify({"error": "Invalid username or password."}), 401

@app.route('/logout', methods=['POST'])
def logout():
    """Endpoint to log out a user."""
    session.pop('username', None)  # Remove user from session
    return jsonify({"message": "Logout successful."}), 200

@app.route('/current_user', methods=['GET'])
def current_user():
    """Endpoint to get the current logged-in user's details."""
    username = session.get('username')
    if not username:
        return jsonify({"error": "User not logged in."}), 401

    user = users_db.get(username)
    return jsonify({"username": username, "role": user['role']}), 200

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```

### Notes:
- This code demonstrates a basic login system using Flask.
- It uses an in-memory dictionary to simulate user data.
- Passwords are hashed for security.
- Sessions are used to maintain logged-in state.
- The code includes error handling for missing credentials and invalid logins.
