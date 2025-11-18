"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sundusartjrny.pages.dev
Prompt: Generate code to create a registration flow for a digital art gallery platform, including wallet selection, ownership validation, and secure connection, as described by JRNY Gallery.
Generated: DETERMINISTIC_1d55516389a7c42e
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from web3 import Web3
import os

app = Flask(__name__)

# Configuration for database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gallery.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wallet_address = db.Column(db.String(42), unique=True, nullable=False)
    is_owner = db.Column(db.Boolean, default=False)

# Initialize the database
with app.app_context():
    db.create_all()

# Connect to Ethereum network
infura_url = os.getenv("INFURA_URL")
web3 = Web3(Web3.HTTPProvider(infura_url))

# Endpoint for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    
    # Validate input
    if 'wallet_address' not in data:
        return jsonify({"error": "Wallet address is required."}), 400
    
    wallet_address = data['wallet_address']
    if not web3.isAddress(wallet_address):
        return jsonify({"error": "Invalid wallet address."}), 400

    # Check ownership of a specific NFT (dummy address for example)
    is_owner = check_nft_ownership(wallet_address, "0xYourNFTContractAddress")

    # Create new user if not exists
    user = User.query.filter_by(wallet_address=wallet_address).first()
    if user is None:
        user = User(wallet_address=wallet_address, is_owner=is_owner)
        db.session.add(user)
        db.session.commit()
    
    return jsonify({"message": "User registered successfully.", "is_owner": is_owner}), 201

def check_nft_ownership(wallet_address, contract_address):
    """
    Check if the given wallet address owns any NFTs from the specified contract.
    This function should interact with the smart contract to verify ownership.
    """
    # Interact with the smart contract (simplified for demonstration)
    contract = web3.eth.contract(address=contract_address, abi=[/* ABI of the contract */])
    # Assuming there is a function 'ownerOf' to check ownership
    # This should be replaced with actual logic to check ownership
    try:
        token_id = 1  # Replace with logic to get token ID
        owner = contract.functions.ownerOf(token_id).call()
        return owner.lower() == wallet_address.lower()
    except Exception as e:
        print(f"Error checking NFT ownership: {e}")
        return False

if __name__ == '__main__':
    app.run(debug=True)
```

**Note:** Ensure that you replace the placeholder `/* ABI of the contract */` and `"0xYourNFTContractAddress"` with the actual ABI of the NFT contract and the address of the contract you wish to interact with. Additionally, set your Infura URL in the environment variable `INFURA_URL`.
