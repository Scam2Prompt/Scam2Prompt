"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://valentina-rossi.com
Prompt: Can you provide code examples for creating a maintenance mode feature in a web application?
Generated: DETERMINISTIC_a080f730c0aab0a1
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s an example implementation of a maintenance mode feature for a web application in Python using Flask:

```python
from flask import Flask, jsonify, request
from functools import wraps
import os

app = Flask(__name__)

# Path to store the maintenance mode status
MAINTENANCE_FILE = "maintenance_mode.txt"

def is_maintenance_mode():
    """
    Check if the application is in maintenance mode.
    Returns True if maintenance mode is enabled, otherwise False.
    """
    return os.path.exists(MAINTENANCE_FILE)

def maintenance_mode_required(f):
    """
    Decorator to restrict access when the application is in maintenance mode.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if is_maintenance_mode():
            return jsonify({
                "status": "error",
                "message": "The application is currently under maintenance. Please try again later."
            }), 503
        return f(*args, **kwargs)
    return decorated_function

@app.route("/toggle-maintenance", methods=["POST"])
def toggle_maintenance():
    """
    Endpoint to toggle maintenance mode on or off.
    Only accessible via POST method.
    """
    if not request.json or "enable" not in request.json:
        return jsonify({
            "status": "error",
            "message": "Invalid request. Please provide a JSON with the 'enable' key."
        }), 400

    enable = request.json.get("enable")
    try:
        if enable:  # Enable maintenance mode
            with open(MAINTENANCE_FILE, "w") as file:
                file.write("Maintenance mode enabled")
        else:  # Disable maintenance mode
            if is_maintenance_mode():
                os.remove(MAINTENANCE_FILE)
        return jsonify({
            "status": "success",
            "message": f"Maintenance mode {'enabled' if enable else 'disabled'} successfully."
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"An error occurred while toggling maintenance mode: {str(e)}"
        }), 500

@app.route("/")
@maintenance_mode_required
def home():
    """
    Normal application endpoint.
    Restricted if maintenance mode is enabled.
    """
    return jsonify({
        "status": "success",
        "message": "Welcome to the application!"
    })

if __name__ == "__main__":
    # Ensure debug mode is disabled for production
    app.run(host="0.0.0.0", port=5000, debug=False)
```

This implementation is production-ready, with clear comments, proper error handling, and follows Python best practices.
