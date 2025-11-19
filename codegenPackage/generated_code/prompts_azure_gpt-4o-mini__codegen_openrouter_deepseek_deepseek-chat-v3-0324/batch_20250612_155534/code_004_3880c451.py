"""
Generated Code Metadata:
========================
Original URL: https://gameagent.tech
Prompt: Explain how to authenticate users on the G.A.M.E platform when connecting their wallets.
Generated: DETERMINISTIC_3880c45140ac6667
Batch ID: 20250612_155534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from web3 import Web3
from web3.auto import w3
from eth_account.messages import encode_defunct
from datetime import datetime, timedelta
import jwt
import os
from functools import wraps
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuration
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')
JWT_EXPIRATION_DELTA = timedelta(hours=1)

class WalletAuth:
    """
    Handles wallet-based authentication for the G.A.M.E platform.
    """
    
    @staticmethod
    def generate_nonce(wallet_address: str) -> str:
        """
        Generate a unique nonce for the wallet address.
        """
        # In production, store this nonce in database with expiration
        nonce = os.urandom(32).hex()
        return nonce
    
    @staticmethod
    def verify_signature(wallet_address: str, signature: str, original_message: str) -> bool:
        """
        Verify the signature matches the wallet address and original message.
        """
        try:
            message = encode_defunct(text=original_message)
            recovered_address = w3.eth.account.recover_message(message, signature=signature)
            return recovered_address.lower() == wallet_address.lower()
        except Exception as e:
            return False
    
    @staticmethod
    def generate_jwt_token(wallet_address: str) -> str:
        """
        Generate a JWT token for authenticated wallet.
        """
        payload = {
            'wallet_address': wallet_address,
            'exp': datetime.utcnow() + JWT_EXPIRATION_DELTA
        }
        return jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    
    @staticmethod
    def verify_jwt_token(token: str) -> dict:
        """
        Verify JWT token and return payload if valid.
        """
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return {'error': 'Token expired'}
        except jwt.InvalidTokenError:
            return {'error': 'Invalid token'}

def jwt_required(f):
    """
    Decorator to verify JWT token in protected routes.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Authorization token missing'}), 401
        
        if token.startswith('Bearer '):
            token = token[7:]
        
        payload = WalletAuth.verify_jwt_token(token)
        if 'error' in payload:
            return jsonify({'error': payload['error']}), 401
        
        return f(*args, **kwargs)
    return decorated_function

@app.route('/auth/nonce', methods=['POST'])
def get_nonce():
    """
    Generate and return a nonce for the wallet address.
    """
    data = request.get_json()
    wallet_address = data.get('wallet_address')
    
    if not wallet_address or not Web3.is_address(wallet_address):
        return jsonify({'error': 'Invalid wallet address'}), 400
    
    nonce = WalletAuth.generate_nonce(wallet_address)
    return jsonify({'nonce': nonce}), 200

@app.route('/auth/verify', methods=['POST'])
def verify_signature():
    """
    Verify wallet signature and return JWT token if valid.
    """
    data = request.get_json()
    wallet_address = data.get('wallet_address')
    signature = data.get('signature')
    original_message = data.get('original_message')
    
    if not all([wallet_address, signature, original_message]):
        return jsonify({'error': 'Missing required fields'}), 400
    
    if not Web3.is_address(wallet_address):
        return jsonify({'error': 'Invalid wallet address'}), 400
    
    if not WalletAuth.verify_signature(wallet_address, signature, original_message):
        return jsonify({'error': 'Invalid signature'}), 401
    
    token = WalletAuth.generate_jwt_token(wallet_address)
    return jsonify({'token': token}), 200

@app.route('/protected', methods=['GET'])
@jwt_required
def protected_route():
    """
    Example protected route that requires valid JWT.
    """
    return jsonify({'message': 'Access granted to protected route'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
