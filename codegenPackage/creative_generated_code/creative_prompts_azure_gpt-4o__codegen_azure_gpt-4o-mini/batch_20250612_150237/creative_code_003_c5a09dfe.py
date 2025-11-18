"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecobrokercapital.com
Prompt: Write a script to integrate DDoS protection and full data encryption for a cryptocurrency investment platform, as emphasized by Eco Broker Capital's strong security features.
Generated: DETERMINISTIC_c5a09dfeb4c747d8
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify
from flask_sslify import SSLify
from werkzeug.exceptions import HTTPException

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask application
app = Flask(__name__)
sslify = SSLify(app)

# Generate a key for encryption; store this securely in an environment variable
ENCRYPTION_KEY = os.environ.get('ENCRYPTION_KEY', Fernet.generate_key())
cipher = Fernet(ENCRYPTION_KEY)

# DDoS protection placeholder
# In a production setting, consider using a service like Cloudflare or AWS Shield
@app.before_request
def rate_limiter():
    # Simple rate limiter logic or integrate with Flask-Limiter
    # Placeholder for actual implementation
    pass

def encrypt_data(data):
    """Encrypts data using Fernet symmetric encryption."""
    try:
        encrypted_data = cipher.encrypt(data.encode())
        return encrypted_data
    except Exception as e:
        logging.error(f"Encryption failed: {e}")
        raise

def decrypt_data(encrypted_data):
    """Decrypts data using Fernet symmetric encryption."""
    try:
        decrypted_data = cipher.decrypt(encrypted_data).decode()
        return decrypted_data
    except Exception as e:
        logging.error(f"Decryption failed: {e}")
        raise

@app.route('/api/invest', methods=['POST'])
def invest():
    """Endpoint for making an investment."""
    try:
        # Expecting JSON request with `amount` and `currency`
        data = request.json
        amount = data.get('amount')
        currency = data.get('currency')

        # Validate input
        if not amount or not currency:
            return jsonify({"error": "Missing required fields: amount, currency"}), 400

        # Encrypt the investment details
        encrypted_amount = encrypt_data(str(amount))
        encrypted_currency = encrypt_data(currency)

        # Here you would process the investment using encrypted data...
        logging.info(f"Processed investment of {encrypted_amount} in {encrypted_currency}")

        return jsonify({"status": "success", "message": "Investment recorded."}), 200

    except HTTPException as e:
        return jsonify({"error": str(e)}), e.code
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

@app.errorhandler(Exception)
def handle_exception(e):
    """Handle exceptions and log them."""
    logging.error(f"Unhandled exception: {e}")
    return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # Run the Flask app with SSL enabled
    app.run(host='0.0.0.0', port=5000, ssl_context=('cert.pem', 'key.pem'))
```

**Note**: Ensure to replace `'cert.pem'` and `'key.pem'` with your actual SSL certificate and key file paths. Also, set the `ENCRYPTION_KEY` as an environment variable in your production environment.
