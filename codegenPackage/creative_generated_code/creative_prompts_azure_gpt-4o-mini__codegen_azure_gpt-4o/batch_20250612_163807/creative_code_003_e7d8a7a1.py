"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mantaxbonk.network
Prompt: Can you provide code snippets for handling website downtime gracefully in a web application?
Generated: DETERMINISTIC_e7d8a7a1e1afff01
Batch ID: 20250612_163807
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask application example for handling website downtime gracefully

from flask import Flask, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Flag for downtime status (can be modified based on maintenance schedule or external triggers)
IS_DOWNTIME = False

@app.before_request
def check_downtime():
    """
    Middleware to check if the website is under maintenance.
    If downtime is active, return a graceful message with a 503 status code.
    """
    if IS_DOWNTIME:
        logging.info("Website is under maintenance.")
        return jsonify({
            "status": "error",
            "message": "The website is currently down for maintenance. Please try again later."
        }), 503

@app.route('/')
def home():
    """
    Normal route for homepage. Will only be accessible if IS_DOWNTIME is False.
    """
    return jsonify({
        "status": "success",
        "message": "Welcome to the homepage!"
    })

@app.route('/toggle-downtime', methods=['POST'])
def toggle_downtime():
    """
    Route to toggle downtime status for testing purposes.
    Ideally, this should be protected with authentication in a real-world scenario.
    """
    global IS_DOWNTIME
    IS_DOWNTIME = not IS_DOWNTIME
    status = "enabled" if IS_DOWNTIME else "disabled"
    logging.info(f"Downtime status has been {status}.")
    return jsonify({
        "status": "success",
        "message": f"Downtime has been {status}."
    })

# Error handler for general server errors
@app.errorhandler(500)
def internal_server_error(error):
    """
    Graceful error message for internal server failures.
    """
    logging.error(f"Internal server error: {error}")
    return jsonify({
        "status": "error",
        "message": "An internal error occurred. Please contact support if the issue persists."
    }), 500

# Error handler for 404 errors
@app.errorhandler(404)
def not_found_error(error):
    """
    Graceful error message for resource not found errors.
    """
    logging.warning("Resource not found.")
    return jsonify({
        "status": "error",
        "message": "The requested resource was not found."
    }), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
