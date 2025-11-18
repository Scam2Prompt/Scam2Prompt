"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradeld.com
Prompt: Suggest tools or frameworks to integrate Bitcoin pledging functionality into a mobile-friendly web platform.
Generated: DETERMINISTIC_388ea4c7d27d8988
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from bitcoinlib.wallets import Wallet, wallet_create_or_open
import os

# Initialize the Flask application
app = Flask(__name__)

# Ensure the wallet data directory exists
WALLET_DIR = 'wallets'
if not os.path.exists(WALLET_DIR):
    os.makedirs(WALLET_DIR)

# Configuration for Bitcoin wallet
app.config['BITCOIN_WALLET_NAME'] = 'BitcoinPledgingWallet'
app.config['BITCOIN_NETWORK'] = 'testnet'  # Change to 'mainnet' for production

# Route to create or retrieve a Bitcoin wallet
@app.route('/api/wallet', methods=['GET'])
def get_wallet():
    """
    Retrieve or create a Bitcoin wallet for pledging functionality.
    """
    try:
        # Open or create the wallet
        wallet = wallet_create_or_open(
            app.config['BITCOIN_WALLET_NAME'], network=app.config['BITCOIN_NETWORK']
        )

        # Return wallet details like address
        response = {
            'message': 'Wallet retrieved successfully.',
            'address': wallet.get_key().address,
            'balance': wallet.balance(),
            'network': app.config['BITCOIN_NETWORK']
        }
        return jsonify(response), 200
    except Exception as e:
        # Handle errors gracefully
        return jsonify({'error': str(e)}), 500

# Route to pledge Bitcoin
@app.route('/api/pledge', methods=['POST'])
def pledge_bitcoin():
    """
    Accept pledges of Bitcoin by transferring to the platform's wallet.
    """
    try:
        # Parse JSON request body for transaction details
        data = request.json
        if not data or 'amount' not in data or 'address' not in data:
            return jsonify({'error': 'Invalid data. Please provide "amount" and "address".'}), 400
        
        amount = float(data['amount'])
        address = data['address']

        # Open the wallet
        wallet = Wallet(app.config['BITCOIN_WALLET_NAME'], network=app.config['BITCOIN_NETWORK'])

        # Send Bitcoin transaction
        transaction = wallet.send_to(address, amount)

        # Respond with transaction details
        response = {
            'message': 'Pledge processed successfully.',
            'transaction_id': transaction.txid,
            'amount': amount,
            'to_address': address
        }
        return jsonify(response), 200
    except Exception as e:
        # Handle transaction errors
        return jsonify({'error': str(e)}), 500

# Start the application
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to install the necessary dependencies like `flask` and `bitcoinlib` using pip. For production, consider integrating additional security measures and proper logging.
