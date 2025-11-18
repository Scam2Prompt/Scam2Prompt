"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-kelexo-en.pages.dev
Prompt: Generate code for validating wallet connections and linking them to Kelexo accounts securely.
Generated: DETERMINISTIC_ba9433ce6b5bcf71
Batch ID: 20250612_153648
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
from werkzeug.exceptions import BadRequest, NotFound
import hashlib
import hmac
import os

app = Flask(__name__)

# Secret key for HMAC validation (should be stored securely, e.g., an environment variable)
SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')

# Simulated database for linking wallets to Kelexo accounts
wallet_db = {}

def validate_wallet_signature(wallet_address, signature):
    """
    Validate the wallet signature using HMAC.
    
    Args:
        wallet_address (str): The wallet address to validate.
        signature (str): The provided signature to verify.
    
    Returns:
        bool: True if the signature is valid, False otherwise.
    """
    message = wallet_address.encode()
    expected_signature = hmac.new(SECRET_KEY.encode(), message, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected_signature, signature)

@app.route('/link_wallet', methods=['POST'])
def link_wallet():
    """
    Link a wallet to a Kelexo account securely.
    
    Request Body:
        {
            "wallet_address": "string",
            "signature": "string",
            "account_id": "string"
        }
    
    Returns:
        JSON response indicating success or failure.
    """
    try:
        # Parse JSON request body
        data = request.get_json()
        if not data:
            raise BadRequest('Request body must be JSON.')

        # Extract data
        wallet_address = data.get('wallet_address')
        signature = data.get('signature')
        account_id = data.get('account_id')

        # Validate required fields
        if not wallet_address or not signature or not account_id:
            raise BadRequest('Missing required fields: wallet_address, signature, account_id.')

        # Validate the wallet signature
        if not validate_wallet_signature(wallet_address, signature):
            raise BadRequest('Invalid signature for the wallet address.')

        # Link the wallet to the account
        wallet_db[wallet_address] = account_id
        
        return jsonify({"message": "Wallet linked successfully."}), 200

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

@app.route('/get_linked_wallet/<account_id>', methods=['GET'])
def get_linked_wallet(account_id):
    """
    Retrieve the wallet linked to a specified Kelexo account.
    
    Args:
        account_id (str): The account ID to look up.
    
    Returns:
        JSON response with the linked wallet or an error message.
    """
    try:
        # Search for the wallet linked to the account_id
        linked_wallet = next((wallet for wallet, acc_id in wallet_db.items() if acc_id == account_id), None)
        
        if linked_wallet is None:
            raise NotFound('No wallet linked to the specified account ID.')
        
        return jsonify({"wallet_address": linked_wallet}), 200

    except NotFound as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
