"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maqicedao.web.app
Prompt: Develop a program to track the minting progress of the Magic Box NFT collection, displaying the total minted percentage and enforcing the "3 per wallet" restriction.
Generated: DETERMINISTIC_05fc25e9a82f584a
Batch ID: 20250612_150601
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

# Initialize the Flask application
app = Flask(__name__)

# Constants for the NFT collection
TOTAL_NFTS = 1000  # Total number of NFTs in the collection
MAX_PER_WALLET = 3  # Maximum NFTs allowed per wallet

# Dictionary to track the minting progress
minted_count = {
    'total_minted': 0,
    'wallets': {}
}

@app.route('/mint', methods=['POST'])
def mint_nft():
    """Mint an NFT for a given wallet if it meets the criteria."""
    global minted_count

    # Get the wallet address from the request
    data = request.json
    wallet_address = data.get('wallet_address')
    
    # Validate the wallet address
    if not wallet_address:
        return jsonify({'error': 'Wallet address is required'}), 400

    # Check if the wallet has reached the minting limit
    current_count = minted_count['wallets'].get(wallet_address, 0)
    if current_count >= MAX_PER_WALLET:
        return jsonify({'error': f'Maximum {MAX_PER_WALLET} NFTs already minted for this wallet'}), 403

    # Mint the NFT
    minted_count['total_minted'] += 1
    minted_count['wallets'][wallet_address] = current_count + 1

    # Calculate the percentage of total minted NFTs
    minted_percentage = (minted_count['total_minted'] / TOTAL_NFTS) * 100

    return jsonify({
        'message': 'NFT minted successfully',
        'total_minted': minted_count['total_minted'],
        'minted_percentage': minted_percentage,
        'remaining': TOTAL_NFTS - minted_count['total_minted']
    }), 201

@app.route('/status', methods=['GET'])
def get_status():
    """Get the current minting status."""
    minted_percentage = (minted_count['total_minted'] / TOTAL_NFTS) * 100

    return jsonify({
        'total_minted': minted_count['total_minted'],
        'minted_percentage': minted_percentage,
        'remaining': TOTAL_NFTS - minted_count['total_minted'],
        'wallets': minted_count['wallets']
    }), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False)
```

This code snippet creates a simple Flask application to track the minting of an NFT collection, enforcing a limit of 3 NFTs per wallet and providing endpoints to mint NFTs and check the current minting status.
