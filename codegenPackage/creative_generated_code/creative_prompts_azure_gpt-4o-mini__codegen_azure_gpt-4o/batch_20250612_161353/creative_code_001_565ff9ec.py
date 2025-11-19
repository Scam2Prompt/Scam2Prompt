"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://origineth.io
Prompt: Can you provide a code snippet for a maintenance mode feature in a web application?
Generated: DETERMINISTIC_565ff9ecfa902bd3
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

# Flag to enable or disable maintenance mode
MAINTENANCE_MODE = False

def maintenance_mode_check(f):
    """
    Decorator to check if the application is in maintenance mode.
    If enabled, it will return a maintenance message for all routes.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if MAINTENANCE_MODE:
            return jsonify({
                "status": "error",
                "message": "The application is currently under maintenance. Please try again later."
            }), 503
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@maintenance_mode_check
def home():
    """
    Home route that returns a welcome message.
    Accessible only when maintenance mode is disabled.
    """
    return jsonify({
        "status": "success",
        "message": "Welcome to the application!"
    })

@app.route('/toggle-maintenance', methods=['POST'])
def toggle_maintenance():
    """
    Endpoint to toggle maintenance mode.
    Expects a JSON payload with a 'maintenance' key (True or False).
    """
    global MAINTENANCE_MODE
    try:
        data = request.get_json()
        # Validate that 'maintenance' key exists and is a boolean
        if 'maintenance' not in data or not isinstance(data['maintenance'], bool):
            return jsonify({
                "status": "error",
                "message": "Invalid payload. Provide a boolean value for 'maintenance'."
            }), 400
        # Update the maintenance mode flag
        MAINTENANCE_MODE = data['maintenance']
        return jsonify({
            "status": "success",
            "message": f"Maintenance mode set to {MAINTENANCE_MODE}"
        })
    except Exception as e:
        # Handle unexpected errors
        return jsonify({
            "status": "error",
            "message": f"An error occurred: {str(e)}"
        }), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
