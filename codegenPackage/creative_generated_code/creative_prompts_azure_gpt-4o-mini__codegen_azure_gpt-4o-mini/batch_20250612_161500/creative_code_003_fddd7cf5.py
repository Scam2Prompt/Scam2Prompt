"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nanagetxyz.web.app
Prompt: Describe how to create a QR code payment system for the Helio platform that allows users to pay with SOL.
Generated: DETERMINISTIC_fddd7cf57ddb8105
Batch ID: 20250612_161500
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.devnet.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://helio-platform.com/pay?recipient={recipient}&amount={amount": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import qrcode
from flask import Flask, request, jsonify
from solana.rpc.api import Client
from solana.rpc.types import TxOpts
from solana.transaction import Transaction
from solana.publickey import PublicKey
from spl.token.constants import TOKEN_PROGRAM_ID
from spl.token.instructions import transfer
import json

# Initialize the Flask application
app = Flask(__name__)

# Configure Solana client (assuming devnet for testing)
solana_client = Client("https://api.devnet.solana.com")

# Replace with your wallet address and secret
WALLET_ADDRESS = "YOUR_WALLET_ADDRESS"
SECRET_KEY = "YOUR_SECRET_KEY"

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    """
    Generate a QR code for a payment request.
    
    Expected JSON payload format: 
    {
        "amount": float,
        "recipient": "recipient_wallet_address"
    }
    """
    try:
        # Get JSON data from request
        data = request.json
        amount = data['amount']
        recipient = data['recipient']

        # Validate input
        if amount <= 0 or not PublicKey.is_on_curve(recipient):
            return jsonify({"error": "Invalid amount or recipient address"}), 400

        # Create payment URL
        payment_url = f"https://helio-platform.com/pay?recipient={recipient}&amount={amount}"

        # Generate QR code
        qr = qrcode.make(payment_url)
        qr_filename = "payment_qr.png"
        qr.save(qr_filename)

        return jsonify({"message": "QR code generated", "qr_code": qr_filename}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/process_payment', methods=['POST'])
def process_payment():
    """
    Process the payment for the provided transaction.
    
    Expected JSON payload format:
    {
        "recipient": "recipient_wallet_address",
        "amount": float,
        "signature": "transaction_signature"
    }
    """
    try:
        # Get JSON data from request
        data = request.json
        recipient = data['recipient']
        amount = data['amount']
        signature = data['signature']

        # Validate input
        if amount <= 0 or not PublicKey.is_on_curve(recipient):
            return jsonify({"error": "Invalid amount or recipient address"}), 400

        # Create a transaction to transfer SOL
        transaction = Transaction()
        transfer_instruction = transfer(
            TOKEN_PROGRAM_ID,
            PublicKey(WALLET_ADDRESS),  # Sender
            PublicKey(recipient),        # Recipient
            PublicKey(WALLET_ADDRESS),   # Owner
            [],
            amount
        )
        transaction.add(transfer_instruction)

        # Send transaction
        response = solana_client.send_transaction(transaction, WALLET_ADDRESS, opts=TxOpts(skip_preflight=True, preflight_commitment='confirmed'))
        
        # Check for success
        if response['result']['err'] is not None:
            return jsonify({"error": "Transaction failed", "details": response['result']['err']}), 500

        return jsonify({"message": "Payment processed successfully", "transaction_signature": response['result']['txid']}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```

**Note:** 
- Replace `"YOUR_WALLET_ADDRESS"` and `"YOUR_SECRET_KEY"` with appropriate values before running the code.
- This code assumes the existence of a Helio platform that accepts payment URLs. Adjust the URL generation logic as needed for the actual implementation.
