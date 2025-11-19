"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cousdt.com
Prompt: Generate a code snippet for a web application that allows users to buy gift cards using USDT, based on the examples provided by COusdt.
Generated: DETERMINISTIC_bf9191733698e8dc
Batch ID: 20250612_135557
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
from flask_sqlalchemy import SQLAlchemy
from web3 import Web3
import os

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)

# GiftCard model for database
class GiftCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    recipient_email = db.Column(db.String(120), nullable=False)

# Web3 setup for interacting with the USDT smart contract
w3 = Web3(Web3.HTTPProvider(os.getenv('WEB3_PROVIDER_URL')))
usdt_contract_address = os.getenv('USDT_CONTRACT_ADDRESS')
usdt_abi = [...]  # USDT contract ABI JSON goes here

# Initialize USDT contract
usdt_contract = w3.eth.contract(address=usdt_contract_address, abi=usdt_abi)

@app.route('/buy_gift_card', methods=['POST'])
def buy_gift_card():
    """
    Endpoint to purchase a gift card using USDT.

    Expected JSON payload:
    {
        "value": <float>,                # Value of the gift card
        "recipient_email": "<string>",   # Email of the gift card recipient
        "sender_address": "<string>"      # Address of the buyer
    }
    """
    try:
        data = request.get_json()
        value = data['value']
        recipient_email = data['recipient_email']
        sender_address = data['sender_address']

        # Validate input
        if not isinstance(value, (int, float)) or value <= 0:
            return jsonify({'error': 'Invalid gift card value'}), 400
        if not recipient_email:
            return jsonify({'error': 'Recipient email is required'}), 400
        if not Web3.isChecksumAddress(sender_address):
            return jsonify({'error': 'Invalid sender address'}), 400

        # Calculate the amount of USDT to transfer (assuming 1 USDT = 1 USD)
        usdt_amount = w3.toWei(value, 'ether')

        # Create transaction
        transaction = usdt_contract.functions.transfer(recipient_email, usdt_amount).buildTransaction({
            'chainId': 1,  # Mainnet
            'gas': 2000000,
            'gasPrice': w3.toWei('50', 'gwei'),
            'nonce': w3.eth.getTransactionCount(sender_address),
        })

        # Sign and send the transaction (using a private key)
        private_key = os.getenv('PRIVATE_KEY')
        signed_txn = w3.eth.account.signTransaction(transaction, private_key)
        txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

        # Store gift card details in database
        new_gift_card = GiftCard(value=value, recipient_email=recipient_email)
        db.session.add(new_gift_card)
        db.session.commit()

        return jsonify({'message': 'Gift card purchased successfully', 'transaction_hash': txn_hash.hex()}), 201

    except Exception as e:
        # Log the exception for further investigation
        print(f"Error occurred: {str(e)}")
        return jsonify({'error': 'An error occurred while processing your request'}), 500

if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
