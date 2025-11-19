"""
Generated Code Metadata:
========================
Original URL: https://1b108266.629eba10136958fd8144e651.workers.dev
Prompt: Write a code snippet to implement a secure connection check for a web application, ensuring performance and security.
Generated: DETERMINISTIC_601c91218ed0fdc4
Batch ID: 20250622_212633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import ssl
from flask import Flask, request, jsonify

app = Flask(__name__)

# Middleware to enforce secure connection
@app.before_request
def enforce_https():
    """
    Middleware to ensure all requests are made over HTTPS.
    If the request is not secure, it returns a 403 Forbidden response.
    """
    if not request.is_secure:
        return jsonify({"error": "Secure connection required"}), 403

# Route to test secure connection
@app.route('/')
def home():
    """
    A simple route to test secure connection enforcement.
    Returns a success message if accessed over HTTPS.
    """
    return jsonify({"message": "Secure connection established successfully!"})

# SSL context setup for production
def create_ssl_context(cert_file, key_file):
    """
    Creates an SSL context for secure HTTPS connections.
    Args:
        cert_file (str): Path to the SSL certificate file.
        key_file (str): Path to the SSL private key file.
    Returns:
        ssl.SSLContext: Configured SSL context for the server.
    """
    try:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile=cert_file, keyfile=key_file)
        return context
    except Exception as e:
        raise RuntimeError(f"Failed to create SSL context: {e}")

if __name__ == '__main__':
    # Paths to SSL certificate and key files (update with actual paths)
    CERT_FILE = 'path/to/certificate.pem'
    KEY_FILE = 'path/to/privatekey.pem'

    try:
        ssl_context = create_ssl_context(CERT_FILE, KEY_FILE)
        # Run the Flask app with SSL enabled
        app.run(host='0.0.0.0', port=443, ssl_context=ssl_context)
    except RuntimeError as e:
        print(f"Error starting the server: {e}")
```
