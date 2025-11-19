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
from flask import Flask, jsonify, request
from functools import wraps

app = Flask(__name__)

# Configuration for maintenance mode
MAINTENANCE_MODE = False

def maintenance_required(f):
    """Decorator to enforce maintenance mode on specific routes."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if MAINTENANCE_MODE:
            return jsonify({"message": "Service is currently under maintenance. Please try again later."}), 503
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@maintenance_required
def home():
    """Home route that is accessible only when not in maintenance mode."""
    return jsonify({"message": "Welcome to the service!"})

@app.route('/toggle_maintenance', methods=['POST'])
def toggle_maintenance():
    """Admin route to toggle maintenance mode."""
    global MAINTENANCE_MODE
    try:
        MAINTENANCE_MODE = not MAINTENANCE_MODE
        status = "enabled" if MAINTENANCE_MODE else "disabled"
        return jsonify({"message": f"Maintenance mode has been {status}."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=False)
```
