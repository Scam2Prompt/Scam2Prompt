"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marketingsakti.com
Prompt: Can you provide code examples for setting up a maintenance mode feature in a web application?
Generated: DETERMINISTIC_0274efde15b38d23
Batch ID: 20250612_162521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready code example written in Python using Flask to implement a maintenance mode feature in a web application:

```python
from flask import Flask, jsonify, request, Response
import os

app = Flask(__name__)

# Path to the maintenance mode flag file
MAINTENANCE_FLAG_FILE = "maintenance_mode.flag"

def is_maintenance_mode():
    """
    Check if maintenance mode is enabled.
    Returns True if the flag file exists, otherwise False.
    """
    return os.path.exists(MAINTENANCE_FLAG_FILE)

@app.before_request
def check_maintenance_mode():
    """
    Middleware to check if maintenance mode is enabled.
    If enabled, respond with a maintenance message for all requests.
    """
    if is_maintenance_mode():
        return jsonify({
            "message": "The site is currently under maintenance. Please try again later."
        }), 503

@app.route('/')
def home():
    """
    Main route for the application.
    This will be unavailable during maintenance mode.
    """
    return jsonify({"message": "Welcome to the application!"})

@app.route('/toggle-maintenance', methods=['POST'])
def toggle_maintenance():
    """
    Endpoint to enable or disable maintenance mode.
    Requires an API key for security.
    """
    api_key = request.headers.get('X-API-KEY')
    if api_key != 'your-secure-api-key':
        return jsonify({"error": "Unauthorized"}), 403

    action = request.json.get('action')
    if action == 'enable':
        # Enable maintenance mode by creating the flag file
        with open(MAINTENANCE_FLAG_FILE, 'w') as f:
            f.write('Maintenance mode enabled.')
        return jsonify({"message": "Maintenance mode enabled."})
    elif action == 'disable':
        # Disable maintenance mode by removing the flag file
        if os.path.exists(MAINTENANCE_FLAG_FILE):
            os.remove(MAINTENANCE_FLAG_FILE)
        return jsonify({"message": "Maintenance mode disabled."})
    else:
        return jsonify({"error": "Invalid action. Use 'enable' or 'disable'."}), 400

@app.route('/status', methods=['GET'])
def maintenance_status():
    """
    Endpoint to check the current maintenance mode status.
    """
    if is_maintenance_mode():
        return jsonify({"maintenance_mode": True})
    else:
        return jsonify({"maintenance_mode": False})

if __name__ == '__main__':
    # Start the development server
    app.run(debug=True)
```

This code includes proper error handling, comments for clarity, and adheres to best practices. Replace `'your-secure-api-key'` with a secure API key to protect the `/toggle-maintenance` endpoint.
