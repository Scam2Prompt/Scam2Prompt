"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cave.fi
Prompt: Can you provide a code snippet for implementing a maintenance mode feature similar to CAVE's?
Generated: DETERMINISTIC_5727114eec517b6b
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# maintenance_mode.py

import functools
from flask import Flask, jsonify, request

app = Flask(__name__)

# Global variable to toggle maintenance mode
MAINTENANCE_MODE = False

def maintenance_mode_check(func):
    """
    Decorator that checks if the application is in maintenance mode.
    If true, it returns a maintenance message instead of executing the endpoint logic.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if MAINTENANCE_MODE:
            return jsonify({
                "error": "Service Unavailable",
                "message": "The system is currently under maintenance. Please try again later."
            }), 503
        return func(*args, **kwargs)
    return wrapper

@app.route('/toggle-maintenance', methods=['POST'])
def toggle_maintenance_mode():
    """
    Endpoint to toggle maintenance mode ON or OFF.
    This should ideally be protected or require authorization in a production environment.
    """
    global MAINTENANCE_MODE
    try:
        data = request.json
        if not data or 'maintenance' not in data:
            return jsonify({
                "error": "Bad Request",
                "message": "Please provide a valid 'maintenance' key with a boolean value."
            }), 400

        MAINTENANCE_MODE = bool(data['maintenance'])
        status = "ON" if MAINTENANCE_MODE else "OFF"
        return jsonify({
            "message": f"Maintenance mode has been turned {status}."
        }), 200
    except Exception as e:
        # General error handler
        return jsonify({
            "error": "Internal Server Error",
            "message": str(e)
        }), 500

@app.route('/')
@maintenance_mode_check
def home():
    """
    Example endpoint for the home page.
    Executes normally unless maintenance mode is enabled.
    """
    return jsonify({"message": "Welcome to the application!"}), 200

@app.route('/api/resource')
@maintenance_mode_check
def api_resource():
    """
    Example API endpoint for accessing a resource.
    Executes normally unless maintenance mode is enabled.
    """
    return jsonify({"message": "Resource accessed successfully!"}), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
