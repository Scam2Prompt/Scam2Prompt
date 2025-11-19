"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://9aa542c7.c817588e7585f833a0bc52c8.workers.dev
Prompt: How can I implement a secure connection check in my web application using an API?
Generated: DETERMINISTIC_7ab107289aeff9c0
Batch ID: 20250612_160625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# secure_connection_check.py

from flask import Flask, request, jsonify

app = Flask(__name__)

def is_secure_connection(headers):
    """
    Function to check if the incoming request is secure.
    It checks for HTTPS in the URL and for the presence of
    the 'X-Forwarded-Proto' header indicating the protocol used.

    Args:
        headers (dict): The request headers.

    Returns:
        bool: True if the connection is secure (HTTPS), False otherwise.
    """
    # Check if the 'X-Forwarded-Proto' header indicates HTTPS
    forwarded_proto = headers.get('X-Forwarded-Proto', '').lower()
    if forwarded_proto == 'https':
        return True
    
    # Check if the request scheme is HTTPS
    if request.scheme == 'https':
        return True

    # If neither condition is satisfied, the connection is not secure
    return False

@app.route('/check_secure_connection', methods=['GET'])
def check_connection():
    """
    API endpoint to check if the incoming request is secure.

    Returns:
        Response: JSON response with the connection status.
    """
    try:
        # Perform secure connection check
        secure = is_secure_connection(request.headers)
        response = {
            'secure_connection': secure,
            'message': 'Connection is secure' if secure else 'Connection is not secure'
        }
        return jsonify(response), 200
    except Exception as e:
        # Handle any unexpected errors
        error_response = {
            'error': 'An error occurred while checking the connection security',
            'details': str(e)
        }
        return jsonify(error_response), 500

if __name__ == '__main__':
    """
    Main entry point for the application.

    To run the app, execute: python secure_connection_check.py
    The app will start a Flask development server on localhost:5000.
    """
    # Run the Flask application
    app.run(debug=True)
```
