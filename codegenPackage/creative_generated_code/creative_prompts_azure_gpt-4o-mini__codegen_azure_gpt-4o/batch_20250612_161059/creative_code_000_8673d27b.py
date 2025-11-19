"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idealproblemsolver.net
Prompt: What are some common strategies for handling site maintenance in web applications?
Generated: DETERMINISTIC_8673d27b8f4c240d
Batch ID: 20250612_161059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based Python implementation for handling site maintenance in a web application.

from flask import Flask, jsonify, request, abort
import os

app = Flask(__name__)

# Configuration for maintenance mode
MAINTENANCE_MODE_FILE = "maintenance_mode.txt"


def is_maintenance_mode():
    """
    Check if the site is in maintenance mode.
    This function reads a predefined file to determine the status.
    Returns:
        bool: True if the site is in maintenance mode, False otherwise.
    """
    return os.path.exists(MAINTENANCE_MODE_FILE)


@app.before_request
def check_maintenance_mode():
    """
    Middleware to handle maintenance mode.
    If the site is in maintenance mode, all requests except to '/maintenance' are blocked.
    """
    if is_maintenance_mode() and request.path != "/maintenance":
        abort(503)  # Service Unavailable


@app.route("/")
def home():
    """
    Default route for the homepage.
    Returns:
        JSON: A welcome message if the site is not in maintenance mode.
    """
    return jsonify({"message": "Welcome to our site!"})


@app.route("/maintenance", methods=["GET", "POST"])
def maintenance():
    """
    Route to handle and toggle maintenance mode.
    Admins can enable or disable maintenance mode by POSTing a JSON payload.
    This route also serves as the informational page during maintenance mode.
    """
    if request.method == "GET":
        if is_maintenance_mode():
            return jsonify({"status": "Maintenance mode is ON"})
        else:
            return jsonify({"status": "Maintenance mode is OFF"})

    elif request.method == "POST":
        try:
            # Parse JSON payload
            data = request.json
            if not data or "enable" not in data:
                return jsonify({"error": "Invalid request. Include 'enable': true/false in JSON payload"}), 400

            # Enable or disable maintenance mode
            if data["enable"]:
                open(MAINTENANCE_MODE_FILE, "w").close()  # Create the file to enable maintenance mode
                return jsonify({"message": "Maintenance mode enabled"})
            else:
                if is_maintenance_mode():
                    os.remove(MAINTENANCE_MODE_FILE)  # Remove the file to disable maintenance mode
                return jsonify({"message": "Maintenance mode disabled"})
        except Exception as e:
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.errorhandler(503)
def maintenance_page(error):
    """
    Custom error handler for 503 Service Unavailable.
    Displays a friendly message during maintenance mode.
    """
    return jsonify({"error": "Service is temporarily unavailable due to maintenance. Please try again later."}), 503


@app.errorhandler(404)
def not_found_page(error):
    """
    Custom error handler for 404 Not Found.
    Displays a friendly message for invalid routes.
    """
    return jsonify({"error": "The requested resource was not found."}), 404


if __name__ == "__main__":
    # Run the Flask application
    app.run(host="0.0.0.0", port=5000)
```
