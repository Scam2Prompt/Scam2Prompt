"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://randomarts.netlify.app
Prompt: Generate code to implement a "first come, first serve" NFT minting mechanism for a collection like "Randomrats," ensuring the total minted count is tracked and capped at 5000.
Generated: DETERMINISTIC_98a6f7ce0d3b426b
Batch ID: 20250612_142654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from flask import Flask, request, jsonify
from web3 import Web3

# Initialize Flask application
app = Flask(__name__)

# Constants
TOTAL_SUPPLY = 5000
MINT_PRICE = Web3.toWei(0.05, 'ether')  # Example mint price in Ether
minted_count = 0  # Tracks the number of minted NFTs

# In-memory storage for minted NFTs (would typically be handled by a smart contract)
minted_nfts = []  # List to store minted NFT identifiers

# Basic error handler for minting process
class MintingError(Exception):
    pass

@app.route('/mint', methods=['POST'])
def mint_nft():
    global minted_count
    
    # Validate request data
    if not request.json or 'owner_address' not in request.json or 'amount' not in request.json:
        return jsonify({'error': 'Invalid request data'}), 400

    owner_address = request.json['owner_address']
    amount = request.json['amount']
    
    # Check for valid address
    if not Web3.isChecksumAddress(owner_address):
        return jsonify({'error': 'Invalid Ethereum address'}), 400

    # Check if the amount is within limits
    if amount <= 0 or minted_count + amount > TOTAL_SUPPLY:
        raise MintingError('Amount exceeds available supply')

    # Calculate total cost
    total_cost = amount * MINT_PRICE

    # Simulate transaction (Replace with actual blockchain transaction code)
    # Here we would normally interact with the smart contract to mint the NFTs.

    try:
        # Simulating minting process; replace with actual minting logic
        for _ in range(amount):
            minted_nfts.append(len(minted_nfts) + 1)  # Dummy NFT ID
            minted_count += 1

        # Return success response
        return jsonify({
            'message': f'Successfully minted {amount} NFTs',
            'total_minted': minted_count,
            'total_cost': Web3.fromWei(total_cost, 'ether')
        }), 200

    except MintingError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred while minting'}), 500

@app.route('/status', methods=['GET'])
def get_status():
    """Endpoint to check current minting status."""
    return jsonify({
        'total_minted': minted_count,
        'remaining_supply': TOTAL_SUPPLY - minted_count
    }), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

Make sure to install the necessary dependencies using:

```bash
pip install Flask web3
```

And replace the minting logic section with actual blockchain interaction code when deploying on a blockchain network.
