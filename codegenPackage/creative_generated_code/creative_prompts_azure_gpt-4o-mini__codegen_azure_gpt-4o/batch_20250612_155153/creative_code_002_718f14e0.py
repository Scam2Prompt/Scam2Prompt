"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cave.fi
Prompt: How can I create a user login system that incorporates a maintenance mode like the one on CAVE?
Generated: DETERMINISTIC_718f14e063121679
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a complete, clean, and well-documented implementation of a user login system with a maintenance mode feature in Python. This implementation uses Flask as the web framework:

```python
from flask import Flask, request, jsonify, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Secret key for session management

# Mock database (replace with actual database in production)
users_db = {
    "admin": generate_password_hash("password123")  # Example user
}

# Maintenance mode flag
maintenance_mode = False  # Set to True to enable maintenance mode

@app.before_request
def check_maintenance_mode():
    """
    Middleware to check if the application is in maintenance mode.
    Redirects all requests (except admin login) to a maintenance page.
    """
    if maintenance_mode and request.endpoint != 'admin_login':
        return jsonify({"error": "The system is currently under maintenance. Please try again later."}), 503


@app.route('/')
def home():
    """
    Default home route for users. Displays a welcome message if logged in.
    """
    if 'user' in session:
        return jsonify({"message": f"Welcome {session['user']}!"})
    return jsonify({"message": "Please log in to access the system."})


@app.route('/login', methods=['POST'])
def login():
    """
    User login route. Validates user credentials and starts a session.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required."}), 400

    # Check if user exists in database
    user_password_hash = users_db.get(username)
    if user_password_hash and check_password_hash(user_password_hash, password):
        session['user'] = username  # Start user session
        return jsonify({"message": "Login successful!"})
    return jsonify({"error": "Invalid username or password."}), 401


@app.route('/logout', methods=['POST'])
def logout():
    """
    User logout route. Ends the user session.
    """
    session.pop('user', None)  # Clear session
    return jsonify({"message": "Logged out successfully!"})


@app.route('/admin/login', methods=['POST'])
def admin_login():
    """
    Admin login route. Allows the admin to log in and toggle maintenance mode.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username == "admin" and check_password_hash(users_db["admin"], password):
        session['admin'] = username  # Start admin session
        return jsonify({"message": "Admin login successful!"})
    return jsonify({"error": "Invalid admin credentials."}), 401


@app.route('/admin/toggle-maintenance', methods=['POST'])
def toggle_maintenance():
    """
    Admin route to toggle maintenance mode on/off.
    """
    if 'admin' not in session:
        return jsonify({"error": "Unauthorized access. Admin login required."}), 403

    global maintenance_mode
    maintenance_mode = not maintenance_mode  # Toggle maintenance mode
    status = "ON" if maintenance_mode else "OFF"
    return jsonify({"message": f"Maintenance mode is now {status}."})


# Error handler for 404 (Not Found)
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "The requested resource was not found."}), 404


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Key Features:
1. **User Authentication**: Users can log in and log out securely.
2. **Maintenance Mode**: A global flag managed by the admin prevents access to the system during maintenance.
3. **Admin Access**: Admins have a separate login route to toggle maintenance mode. Only authenticated admins can perform this action.
4. **Error Handling**: Includes checks for invalid data and unauthorized access, and handles 404 errors gracefully.

To test this, install Flask (`pip install flask`) and run the script.
