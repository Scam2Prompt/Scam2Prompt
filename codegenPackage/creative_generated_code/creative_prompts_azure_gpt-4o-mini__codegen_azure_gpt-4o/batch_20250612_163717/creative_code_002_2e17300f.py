"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://5f8d9eb3.d10f05e59e81e2f9cfa61b7e.workers.dev
Prompt: Write a code snippet that demonstrates how to perform a connection security check before allowing user access to a web application.
Generated: DETERMINISTIC_2e17300fdf51cf9f
Batch ID: 20250612_163717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ssl
from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to perform connection security check
def is_connection_secure(req):
    """
    Checks if the incoming request is secure.

    Args:
        req: The Flask request object.

    Returns:
        bool: True if the connection is secure, False otherwise.
    """
    # Check if the request is over HTTPS
    if req.is_secure:
        return True
    
    # Additional check for custom headers indicating SSL/TLS (e.g., if behind a reverse proxy)
    if req.headers.get('X-Forwarded-Proto', '').lower() == 'https':
        return True

    return False

@app.route('/secure-endpoint', methods=['GET'])
def secure_endpoint():
    """
    Endpoint that performs a security check before allowing access.
    """
    try:
        # Perform security check
        if not is_connection_secure(request):
            return jsonify({'error': 'Access denied: insecure connection'}), 403
        
        # If secure connection, proceed with request handling
        return jsonify({'message': 'Access granted: secure connection'}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': f'An internal error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    # Run the Flask app, usually behind a web server like Gunicorn for production
    # Ensure SSL/TLS termination is handled at the server level
    app.run(ssl_context='adhoc')  # For testing purposes, generates a self-signed certificate
```

This snippet demonstrates a connection security check in a Flask web application and includes proper error handling, comments, and best practices.
