"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3inbox.com
Prompt: Describe the security features of Web3Inbox and how it uses Sign In With Ethereum (SIWE) for authentication.
Generated: DETERMINISTIC_c128bfdd84328d63
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from eth_account import Account
from web3 import Web3
import jwt
import os

app = Flask(__name__)

# Configuration for JWT
SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_secret_key_here')

# Security feature: Function to verify SIWE message
def verify_siwe_message(message, signature):
    """Verifies the SIWE message using the Ethereum address."""
    # Decode the message and extract the address
    try:
        message_json = json.loads(message)
        address = message_json.get('address')
        # Recover the address from the signature
        recovered_address = Account.recover_message(message_json, signature=signature)
        return address.lower() == recovered_address.lower()
    except Exception as e:
        print(f"Error verifying SIWE message: {e}")
        return False

# Route for user authentication using SIWE
@app.route('/api/authenticate', methods=['POST'])
def authenticate_user():
    """Authenticates user via SIWE and issues a JWT."""
    data = request.json
    if not data or 'message' not in data or 'signature' not in data:
        return jsonify({'error': 'Invalid request'}), 400

    message = data['message']
    signature = data['signature']

    # Verify the SIWE message
    if not verify_siwe_message(message, signature):
        return jsonify({'error': 'Signature verification failed'}), 401

    # Create JWT token for the authenticated user
    try:
        payload = {
            'address': json.loads(message).get('address'),
            'exp': Web3.toInt(Web3.solidityKeccak(['uint256'], [3600]))  # Token expires in 1 hour
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return jsonify({'token': token}), 200
    except Exception as e:
        print(f"Error creating JWT token: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
