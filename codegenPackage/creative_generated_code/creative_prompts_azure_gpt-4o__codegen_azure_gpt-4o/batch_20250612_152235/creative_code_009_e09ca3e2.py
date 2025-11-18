"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cart3.pages.dev
Prompt: Write code to implement a secure communication system for clients to collaborate with legal and accounting professionals online, inspired by Carthew Chau & Co's client portal.
Generated: DETERMINISTIC_e09ca3e2c284c9e7
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import ssl
from flask import Flask, request, jsonify
from cryptography.fernet import Fernet
from werkzeug.exceptions import HTTPException

# Flask application setup
app = Flask(__name__)

# Generate or load encryption key for secure communication
KEY_FILE = "encryption_key.key"

if not os.path.exists(KEY_FILE):
    # Generate a new key if it doesn't exist
    encryption_key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(encryption_key)
else:
    # Load the existing key
    with open(KEY_FILE, "rb") as key_file:
        encryption_key = key_file.read()

# Initialize the Fernet instance for encryption/decryption
cipher = Fernet(encryption_key)

# Secure communication routes
@app.route("/send_message", methods=["POST"])
def send_message():
    """
    Endpoint for clients to send encrypted messages to professionals.
    """
    try:
        # Parse incoming JSON request data
        data = request.get_json()
        message = data.get("message")
        
        if not message:
            return jsonify({"error": "Message is required"}), 400

        # Encrypt the message
        encrypted_message = cipher.encrypt(message.encode())
        
        return jsonify({"encrypted_message": encrypted_message.decode()}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route("/receive_message", methods=["POST"])
def receive_message():
    """
    Endpoint for professionals to decrypt and read messages sent by clients.
    """
    try:
        # Parse incoming JSON request data
        data = request.get_json()
        encrypted_message = data.get("encrypted_message")
        
        if not encrypted_message:
            return jsonify({"error": "Encrypted message is required"}), 400
        
        # Decrypt the message
        decrypted_message = cipher.decrypt(encrypted_message.encode()).decode()
        
        return jsonify({"decrypted_message": decrypted_message}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Error handling
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Global error handler for HTTP exceptions.
    """
    response = e.get_response()
    response.data = json.dumps({
        "error": e.name,
        "message": e.description
    })
    response.content_type = "application/json"
    return response

@app.errorhandler(Exception)
def handle_general_exception(e):
    """
    Global error handler for unexpected exceptions.
    """
    return jsonify({"error": "Unexpected error", "message": str(e)}), 500

# SSL/TLS certificate setup for secure communication
SSL_CERT_FILE = "cert.pem"
SSL_KEY_FILE = "key.pem"

if __name__ == "__main__":
    # Check if SSL certificates exist before starting the application
    if not os.path.exists(SSL_CERT_FILE) or not os.path.exists(SSL_KEY_FILE):
        raise FileNotFoundError("SSL certificate or key file not found.")
    
    # Run the Flask application with SSL enabled
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(SSL_CERT_FILE, SSL_KEY_FILE)
    app.run(host="0.0.0.0", port=443, ssl_context=context)
```
