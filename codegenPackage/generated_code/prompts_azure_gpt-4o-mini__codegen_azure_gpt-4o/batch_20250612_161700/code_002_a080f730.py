"""
Generated Code Metadata:
========================
Original URL: https://valentina-rossi.com
Prompt: Can you provide code examples for creating a maintenance mode feature in a web application?
Generated: DETERMINISTIC_a080f730c0aab0a1
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here is a clean, production-ready implementation of a maintenance mode feature in a web application using Python and Flask:

```python
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Configuration for maintenance mode
MAINTENANCE_MODE_FILE = "maintenance_mode.flag"

def is_maintenance_mode():
    """
    Check if the application is in maintenance mode.
    Returns True if the maintenance mode flag file exists, False otherwise.
    """
    return os.path.exists(MAINTENANCE_MODE_FILE)

@app.before_request
def check_maintenance_mode():
    """
    Middleware to check if the application is in maintenance mode.
    If maintenance mode is enabled, return a 503 Service Unavailable response.
    """
    if is_maintenance_mode():
        return jsonify({
            "message": "The application is currently under maintenance. Please try again later."
        }), 503

@app.route('/toggle-maintenance', methods=['POST'])
def toggle_maintenance():
    """
    Endpoint to toggle maintenance mode on or off.
    Requires an admin token for security.
    """
    admin_token = request.headers.get('Admin-Token')
    if admin_token != "your-secure-admin-token":
        return jsonify({"error": "Unauthorized"}), 403

    action = request.json.get('action')
    if action == "enable":
        # Enable maintenance mode by creating the flag file
        with open(MAINTENANCE_MODE_FILE, 'w') as f:
            f.write("Maintenance mode enabled.")
        return jsonify({"message": "Maintenance mode enabled."}), 200
    elif action == "disable":
        # Disable maintenance mode by removing the flag file
        if is_maintenance_mode():
            os.remove(MAINTENANCE_MODE_FILE)
        return jsonify({"message": "Maintenance mode disabled."}), 200
    else:
        return jsonify({"error": "Invalid action. Use 'enable' or 'disable'."}), 400

@app.route('/')
def home():
    """
    Main application route.
    """
    return jsonify({"message": "Welcome to the application!"})

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

This code provides a simple mechanism to enable and disable maintenance mode in a Flask web application. It uses a flag file to track the maintenance state and includes an admin-protected endpoint to toggle the mode.
