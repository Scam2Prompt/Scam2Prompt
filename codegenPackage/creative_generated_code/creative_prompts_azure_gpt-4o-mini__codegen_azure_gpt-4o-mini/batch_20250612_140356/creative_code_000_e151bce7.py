"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multidappschain.web.app
Prompt: How can I implement a synthetic protocol for secure communication between wallets and Dapps using the features described on the MultidappsChain website?
Generated: DETERMINISTIC_e151bce751cc8dfe
Batch ID: 20250612_140356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import hashlib
import hmac
import os
from datetime import datetime, timedelta
from flask import Flask, request, jsonify

app = Flask(__name__)

# Secret key for HMAC signing (should be stored securely in production)
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')

def generate_signature(data):
    """
    Generate a HMAC signature for the given data.
    
    Parameters:
    data (dict): The data to sign.
    
    Returns:
    str: The generated HMAC signature.
    """
    serialized_data = json.dumps(data, sort_keys=True).encode()
    return hmac.new(SECRET_KEY.encode(), serialized_data, hashlib.sha256).hexdigest()

def verify_signature(data, signature):
    """
    Verify the HMAC signature for the given data.
    
    Parameters:
    data (dict): The data to verify.
    signature (str): The HMAC signature to check against.
    
    Returns:
    bool: True if the signature is valid, False otherwise.
    """
    expected_signature = generate_signature(data)
    return hmac.compare_digest(expected_signature, signature)

def is_token_valid(token):
    """
    Check if the token is valid by verifying its expiration.
    
    Parameters:
    token (dict): The token containing the expiration time.
    
    Returns:
    bool: True if the token is valid, False otherwise.
    """
    return datetime.utcnow() < datetime.fromisoformat(token['exp'])

@app.route('/api/secure-communication', methods=['POST'])
def secure_communication():
    """
    Endpoint for secure communication between wallets and DApps.
    
    Returns:
    json: Response with status and message.
    """
    try:
        # Extract data from the request
        content = request.json
        
        if not content or 'data' not in content or 'signature' not in content:
            return jsonify({'error': 'Invalid request format'}), 400
        
        # Extract data and signature
        data = content['data']
        signature = content['signature']

        # Verify the signature
        if not verify_signature(data, signature):
            return jsonify({'error': 'Invalid signature'}), 403
        
        # Check token validity if a token is included in the data
        if 'token' in data and not is_token_valid(data['token']):
            return jsonify({'error': 'Token has expired'}), 403
        
        # Process the valid request (implement your logic here)
        return jsonify({'status': 'success', 'message': 'Secure communication established'}), 200

    except Exception as e:
        # General error handling
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000, debug=False)
```
