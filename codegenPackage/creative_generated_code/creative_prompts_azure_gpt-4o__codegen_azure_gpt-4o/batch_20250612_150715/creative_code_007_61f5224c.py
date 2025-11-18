"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxyfoxs.live
Prompt: Design a REST API for the Galaxy Fox NFT marketplace that allows users to list, buy, and sell NFTs, while ensuring transactions contribute to the ecosystem's treasury.
Generated: DETERMINISTIC_61f5224c864af6e2
Batch ID: 20250612_150715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: galaxy_fox_nft_marketplace.py

from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# Data storage for simplicity (In production, use a robust database)
nfts = {}
transactions = []
treasury_balance = 0.0

# Constants
TREASURY_CONTRIBUTION_PERCENTAGE = 2.5  # 2.5% of each transaction goes to treasury

# Utility functions
def calculate_treasury_contribution(price):
    """
    Calculate the treasury contribution based on the NFT price.
    """
    return price * (TREASURY_CONTRIBUTION_PERCENTAGE / 100)

def create_response(success, message, data=None):
    """
    Utility function to create a consistent JSON response.
    """
    response = {'success': success, 'message': message}
    if data:
        response['data'] = data
    return response

# Endpoints

@app.route('/nfts/list', methods=['POST'])
def list_nft():
    """
    Endpoint to list an NFT for sale.
    Request body:
    {
        "name": "Galaxy Fox #1",
        "description": "A rare Galaxy Fox NFT",
        "price": 100.0,
        "owner": "user123"
    }
    """
    try:
        data = request.json
        nft_id = str(uuid4())
        nfts[nft_id] = {
            'id': nft_id,
            'name': data['name'],
            'description': data['description'],
            'price': data['price'],
            'owner': data['owner'],
            'status': 'listed'
        }
        return jsonify(create_response(True, "NFT listed successfully.", nfts[nft_id]))
    except KeyError as e:
        return jsonify(create_response(False, f"Missing required field: {e}")), 400
    except Exception as e:
        return jsonify(create_response(False, f"An error occurred: {str(e)}")), 500

@app.route('/nfts/buy/<nft_id>', methods=['POST'])
def buy_nft(nft_id):
    """
    Endpoint to buy an NFT.
    Request body:
    {
        "buyer": "user456"
    }
    """
    try:
        if nft_id not in nfts or nfts[nft_id]['status'] != 'listed':
            return jsonify(create_response(False, "NFT not found or not available for purchase.")), 404
        
        data = request.json
        nft = nfts[nft_id]
        treasury_contribution = calculate_treasury_contribution(nft['price'])

        # Update treasury balance
        global treasury_balance
        treasury_balance += treasury_contribution

        # Record transaction
        transaction = {
            'transaction_id': str(uuid4()),
            'nft_id': nft_id,
            'buyer': data['buyer'],
            'seller': nft['owner'],
            'price': nft['price'],
            'treasury_contribution': treasury_contribution
        }
        transactions.append(transaction)

        # Update NFT ownership
        nft['owner'] = data['buyer']
        nft['status'] = 'sold'

        return jsonify(create_response(True, "NFT purchased successfully.", transaction))
    except KeyError as e:
        return jsonify(create_response(False, f"Missing required field: {e}")), 400
    except Exception as e:
        return jsonify(create_response(False, f"An error occurred: {str(e)}")), 500

@app.route('/treasury', methods=['GET'])
def get_treasury_balance():
    """
    Endpoint to get the current balance of the ecosystem treasury.
    """
    try:
        return jsonify(create_response(True, "Treasury balance retrieved successfully.", {'treasury_balance': treasury_balance}))
    except Exception as e:
        return jsonify(create_response(False, f"An error occurred: {str(e)}")), 500

@app.route('/transactions', methods=['GET'])
def get_transactions():
    """
    Endpoint to get the list of all transactions.
    """
    try:
        return jsonify(create_response(True, "Transactions retrieved successfully.", transactions))
    except Exception as e:
        return jsonify(create_response(False, f"An error occurred: {str(e)}")), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
