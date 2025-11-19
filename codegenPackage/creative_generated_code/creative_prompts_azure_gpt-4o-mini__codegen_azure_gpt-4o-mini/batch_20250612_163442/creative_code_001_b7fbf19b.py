"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviviendainforma.zya.me
Prompt: How can I utilize Python app support on iFastNet Web Hosting? Provide an example code to deploy a simple Python web application.
Generated: DETERMINISTIC_b7fbf19b413c0564
Batch ID: 20250612_163442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
import os

# Create a new Flask application
app = Flask(__name__)

# Define a simple route to return a welcome message
@app.route('/', methods=['GET'])
def home():
    """
    Home route that returns a welcome message.
    """
    return jsonify(message="Welcome to the iFastNet Python web application!")

# Define a route to echo back JSON data sent in a POST request
@app.route('/echo', methods=['POST'])
def echo():
    """
    Echo route that returns the received JSON data.
    Expects a JSON object in the request body.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify(error="No JSON data provided"), 400
        return jsonify(received=data), 200
    except Exception as e:
        return jsonify(error=str(e)), 500

# Check if the script is run directly (for local testing)
if __name__ == '__main__':
    # Set the host and port for local development
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

# Note: To deploy on iFastNet, ensure to create a WSGI file that points to this app.
# Example WSGI file content (save as 'app.wsgi'):
# from your_flask_app import app as application
``` 

Make sure to replace `your_flask_app` in the WSGI file with the actual name of your Python file (without the .py extension).
