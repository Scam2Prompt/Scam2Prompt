"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://start-concrete.pages.dev
Prompt: Generate a script that allows users to join a waitlist for an appchain, similar to Concrete, with a focus on tokenproof integration.
Generated: DETERMINISTIC_41be88e839c55626
Batch ID: 20250612_161500
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
import uuid
from flask import Flask, request, jsonify
from web3 import Web3
from eth_account.messages import encode_defunct

app = Flask(__name__)

# Initialize Web3 instance and set provider
WEB3_PROVIDER = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
web3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER))

# Mock database to hold waitlist information
waitlist = {}

# Function to validate Ethereum signature
def validate_signature(address, signature, message):
    try:
        # Hash the message
        message_hash = encode_defunct(text=message)
        # Recover the signing address
        recovered_address = web3.eth.account.recover_message(message_hash, signature=signature)
        # Compare the recovered address with the provided address
        return web3.toChecksumAddress(address) == web3.toChecksumAddress(recovered_address)
    except Exception as e:
        print(f"Error validating signature: {e}")
        return False

@app.route('/join-waitlist', methods=['POST'])
def join_waitlist():
    """
    Endpoint to allow users to join the appchain waitlist.
    Expects JSON payload with:
    - address: Ethereum wallet address
    - signature: Signed message from the user's wallet
    """
    try:
        # Parse request JSON
        data = request.get_json()
        address = data.get('address')
        signature = data.get('signature')

        # Validate input
        if not address or not signature:
            return jsonify({"error": "Address and signature are required"}), 400

        # The message that must be signed by the user
        required_message = "Join the waitlist for AppChain - TokenProof Integration"

        # Validate the Ethereum signature
        if not validate_signature(address, signature, required_message):
            return jsonify({"error": "Invalid signature"}), 401

        # Check if the address is already on the waitlist
        if address in waitlist:
            return jsonify({"message": "Address is already on the waitlist"}), 200

        # Generate a unique ID for the waitlist entry
        waitlist_id = str(uuid.uuid4())

        # Add the user to the waitlist
        waitlist[address] = {
            "id": waitlist_id,
            "address": address
        }

        return jsonify({
            "message": "Successfully joined the waitlist",
            "waitlist_id": waitlist_id
        }), 201
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"error": "An error occurred while processing your request"}), 500

@app.route('/get-waitlist', methods=['GET'])
def get_waitlist():
    """
    Endpoint to retrieve the current waitlist.
    Returns the list of addresses and their associated IDs.
    """
    try:
        return jsonify({"waitlist": waitlist}), 200
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"error": "An error occurred while retrieving the waitlist"}), 500

if __name__ == '__main__':
    # Run the Flask app on localhost, port 5000
    app.run(host='0.0.0.0', port=5000)
```
