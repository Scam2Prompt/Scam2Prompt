"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://9aa542c7.c817588e7585f833a0bc52c8.workers.dev
Prompt: Write a code snippet that enhances website security by validating user connections before granting access.
Generated: DETERMINISTIC_f8bb6563864c490f
Batch ID: 20250612_160625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import hashlib
import hmac
from flask import Flask, request, jsonify

app = Flask(__name__)

# Secret key for HMAC validation (keep this secure and private)
SECRET_KEY = b'super_secret_key'

# Helper function to validate IP address
def is_valid_ip(ip_address):
    # Regular expression for validating IPv4 addresses
    ip_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(ip_pattern, ip_address):
        octets = ip_address.split('.')
        return all(0 <= int(octet) <= 255 for octet in octets)  # Check range for each octet
    return False

# Helper function to validate HMAC signature
def validate_hmac_signature(data, signature):
    hashed = hmac.new(SECRET_KEY, data.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(hashed, signature)

@app.route('/validate_connection', methods=['POST'])
def validate_connection():
    try:
        # Get JSON payload from the request
        payload = request.get_json()
        
        # Validate required fields
        if not payload or 'ip_address' not in payload or 'hmac_signature' not in payload:
            return jsonify({"error": "Invalid payload"}), 400

        ip_address = payload['ip_address']
        hmac_signature = payload['hmac_signature']

        # Validate IP address
        if not is_valid_ip(ip_address):
            return jsonify({"error": "Invalid IP address"}), 400

        # Validate HMAC signature
        if not validate_hmac_signature(ip_address, hmac_signature):
            return jsonify({"error": "Invalid HMAC signature"}), 403

        # All validations passed
        return jsonify({"message": "Connection validated successfully"}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=False, host='0.0.0.0', port=5000)
```
