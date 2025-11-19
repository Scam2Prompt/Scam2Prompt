"""
Generated Code Metadata:
========================
Original URL: https://zapper-dve8s7yrg-epherum.vercel.app
Prompt: Generate code for a demo login system with predefined roles (Admin, Project Manager, Developer, Submitter) to simulate the functionality of the Zapper task tracker platform.
Generated: DETERMINISTIC_399136dba45cafb1
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key in production

# Predefined users with roles
users = {
    "admin": generate_password_hash("admin_pass"),
    "pm": generate_password_hash("pm_pass"),
    "dev": generate_password_hash("dev_pass"),
    "submitter": generate_password_hash("submitter_pass")
}

# Predefined roles
roles = {
    "admin": "Admin",
    "pm": "Project Manager",
    "dev": "Developer",
    "submitter": "Submitter"
}

@app.route('/login', methods=['POST'])
def login():
    """
    Login endpoint to authenticate users.
    Expects JSON payload with 'username' and 'password'.
    """
    data = request.get_json()
    
    # Validate input
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Username and password are required."}), 400

    username = data['username']
    password = data['password']

    # Check if user exists and password is correct
    if username in users and check_password_hash(users[username], password):
        session['username'] = username
        session['role'] = roles[username]
        return jsonify({"message": "Login successful.", "role": session['role']}), 200
    else:
        return jsonify({"error": "Invalid username or password."}), 401

@app.route('/logout', methods=['POST'])
def logout():
    """
    Logout endpoint to clear the session.
    """
    session.clear()
    return jsonify({"message": "Logout successful."}), 200

@app.route('/role', methods=['GET'])
def get_role():
    """
    Endpoint to get the role of the logged-in user.
    Requires user to be logged in.
    """
    if 'username' in session:
        return jsonify({"username": session['username'], "role": session['role']}), 200
    else:
        return jsonify({"error": "User not logged in."}), 403

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)  # Set debug=False in production
```
