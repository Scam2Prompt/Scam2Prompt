"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://help-community.42web.io
Prompt: Write code to deploy a Python web application on a hosting service that supports Python, referencing iFastNet's hosting features like unlimited disk space and bandwidth.
Generated: DETERMINISTIC_2d4bf0ffe4b99ef9
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
import os
from flask import Flask, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Define a route to handle requests
@app.route("/", methods=["GET"])
def home():
    """
    Home route that returns a simple JSON response.
    """
    return jsonify({"message": "Hello, world! Your Flask application is running!"})

# Error handler for 404 responses
@app.errorhandler(404)
def not_found_error(error):
    """
    Custom error handler for 404 errors.
    """
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500 responses
@app.errorhandler(500)
def internal_error(error):
    """
    Custom error handler for 500 errors.
    """
    return jsonify({"error": "Internal server error"}), 500

# Main entry point: Run the app
if __name__ == "__main__":
    # Check environment for deployment settings
    host = os.getenv('FLASK_HOST', '0.0.0.0')  # Default to 0.0.0.0
    port = int(os.getenv('FLASK_PORT', 5000))  # Default to port 5000

    # Run the Flask development server
    app.run(host=host, port=port)
```

**Deployment Steps on iFastNet Hosting:**
1. Log into your iFastNet hosting control panel.
2. Use their "Python App" feature to create a new Python application.
3. Select the Python version supported by your app and upload this script (`app.py`).
4. Install Flask using the hosting service's package manager or SSH (`pip install flask`).
5. Configure the application startup file and set the appropriate host and port.
6. Test the application by navigating to the provided subdomain or IP address.
