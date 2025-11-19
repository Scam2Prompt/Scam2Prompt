"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idealproblemsolver.net
Prompt: Can you provide a code snippet for implementing a maintenance mode in a web application?
Generated: DETERMINISTIC_6db8dea886c71067
Batch ID: 20250612_161059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Flag to indicate if the application is in maintenance mode
MAINTENANCE_MODE = True

@app.before_request
def check_maintenance_mode():
    """
    Middleware to check if the application is in maintenance mode.
    If maintenance mode is active, respond with a 503 Service Unavailable error.
    """
    if MAINTENANCE_MODE:
        return jsonify({
            "error": "Service Unavailable",
            "message": "The application is currently in maintenance mode. Please try again later."
        }), 503

@app.route('/')
def home():
    """
    Main route to serve the homepage.
    This will only be accessible if maintenance mode is disabled.
    """
    return jsonify({
        "message": "Welcome to the web application!",
        "status": "Running normally"
    })

@app.route('/toggle-maintenance', methods=['POST'])
def toggle_maintenance():
    """
    Route to toggle maintenance mode.
    Accepts a JSON payload with a 'maintenance_mode' key.
    Example: { "maintenance_mode": true }
    """
    global MAINTENANCE_MODE
    try:
        data = request.get_json()
        if not data or 'maintenance_mode' not in data:
            return jsonify({
                "error": "Bad Request",
                "message": "Missing 'maintenance_mode' in request body."
            }), 400
        MAINTENANCE_MODE = data['maintenance_mode']
        return jsonify({
            "message": f"Maintenance mode is now {'enabled' if MAINTENANCE_MODE else 'disabled'}."
        })
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({
            "error": "Internal Server Error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```
