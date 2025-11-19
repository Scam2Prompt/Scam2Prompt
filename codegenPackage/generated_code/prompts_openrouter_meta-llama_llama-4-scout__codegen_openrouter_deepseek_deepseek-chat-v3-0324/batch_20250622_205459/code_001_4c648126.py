"""
Generated Code Metadata:
========================
Original URL: https://refactorlogs.pages.dev
Prompt: Generate a code snippet for a server-side validation system that verifies wallet ownership for dApps and servers, considering limitations of use and intellectual property rights.
Generated: DETERMINISTIC_4c64812648e8a6bf
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Wallet Ownership Validator for dApps and Servers

This module provides server-side validation of wallet ownership
with proper rate limiting and IP-based restrictions to prevent abuse.
"""

import hashlib
import hmac
import time
from functools import wraps
from typing import Optional, Tuple

import requests
from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# Rate limiting configuration
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# Configuration (should be moved to environment variables in production)
API_KEYS = {
    "dapp1": "secure_api_key_1",
    "dapp2": "secure_api_key_2"
}

SIGNATURE_EXPIRY = 300  # 5 minutes in seconds

class ValidationError(Exception):
    """Custom exception for validation failures"""
    pass

def validate_api_key(api_key: str) -> bool:
    """
    Validate the provided API key against registered applications.
    """
    return api_key in API_KEYS.values()

def generate_nonce() -> str:
    """
    Generate a unique nonce for signature verification.
    """
    return str(int(time.time() * 1000))

def verify_signature(wallet_address: str, signature: str, nonce: str, message: str) -> bool:
    """
    Verify the cryptographic signature against the wallet address.
    This is a placeholder - implement proper cryptographic verification
    based on your blockchain's requirements.
    """
    # In production, implement proper signature verification for your blockchain
    # This example uses a simple HMAC for demonstration
    expected_signature = hmac.new(
        key=wallet_address.encode(),
        msg=f"{nonce}:{message}".encode(),
        digestmod=hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(expected_signature, signature)

def validate_request(f):
    """
    Decorator to validate incoming requests.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            # Check API key
            api_key = request.headers.get('X-API-KEY')
            if not api_key or not validate_api_key(api_key):
                raise ValidationError("Invalid API key")
            
            # Get request data
            data = request.get_json()
            if not data:
                raise ValidationError("Missing request data")
            
            required_fields = ['wallet_address', 'signature', 'nonce', 'message']
            for field in required_fields:
                if field not in data:
                    raise ValidationError(f"Missing required field: {field}")
            
            # Verify signature
            if not verify_signature(
                data['wallet_address'],
                data['signature'],
                data['nonce'],
                data['message']
            ):
                raise ValidationError("Invalid signature")
            
            # Check nonce expiry
            current_time = int(time.time() * 1000)
            if current_time - int(data['nonce']) > SIGNATURE_EXPIRY * 1000:
                raise ValidationError("Signature expired")
            
            return f(*args, **kwargs)
        
        except ValidationError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            app.logger.error(f"Validation error: {str(e)}")
            return jsonify({"error": "Internal server error"}), 500
    
    return decorated_function

@app.route('/validate', methods=['POST'])
@limiter.limit("10 per minute")
@validate_request
def validate_wallet():
    """
    Endpoint to validate wallet ownership.
    """
    data = request.get_json()
    return jsonify({
        "status": "success",
        "wallet_address": data['wallet_address'],
        "valid": True,
        "timestamp": int(time.time())
    })

if __name__ == '__main__':
    app.run(debug=False)
```
