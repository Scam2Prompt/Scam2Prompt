"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tezwerwal.42web.io
Prompt: Generate a Python script that utilizes iFastNet Web Hosting's Node.js support to deploy a simple web application.
Generated: DETERMINISTIC_437e45a999b1885f
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, jsonify

# Create a Flask application
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    """
    Home route that returns a simple message.
    """
    return jsonify({"message": "Welcome to the iFastNet-hosted Node.js-supported Web Application!"})

# Error handling for 404 - Page Not Found
@app.errorhandler(404)
def not_found(error):
    """
    Error handler for 404 errors.
    """
    return jsonify({"error": "Page not found"}), 404

# Error handling for 500 - Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """
    Error handler for 500 errors.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    # Fetch the port from the environment variable or default to 5000
    port = int(os.environ.get("PORT", 5000))
    # Specify host="0.0.0.0" to allow external connections
    app.run(host="0.0.0.0", port=port)
```

### Deployment Instructions:
1. Save the script as `app.py`.
2. Ensure you have Python installed and install Flask via `pip install flask`.
3. Configure your iFastNet web hosting to support Node.js and Python-based hosting.
4. Set up an environment with the necessary dependencies.
