"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toncoinclaim.xyz
Prompt: Create a TON blockchain-based application that facilitates mentorship programs for the TON Accelerator, including mentor registration and reward tracking.
Generated: DETERMINISTIC_ccf2b80e73e3b1f9
Batch ID: 20250612_145916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for interacting with the TON blockchain and handling web application
from tonclient.client import TonClient, ClientConfig
from tonclient.types import Abi, DeploySet, CallSet, Signer
from flask import Flask, request, jsonify
import os

# Initialize TON client
client = TonClient(config=ClientConfig(network='mainnet'))

# Flask web application initialization
app = Flask(__name__)

# Load environment variables for security purposes
TON_WALLET_PRIVATE_KEY = os.getenv("TON_WALLET_PRIVATE_KEY")
TON_WALLET_PUBLIC_KEY = os.getenv("TON_WALLET_PUBLIC_KEY")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")  # Smart contract address deployed on the blockchain

# ABI file for smart contract interaction
CONTRACT_ABI_PATH = "MentorProgramContract.abi.json"

# Load contract ABI
with open(CONTRACT_ABI_PATH, 'r') as abi_file:
    contract_abi = Abi.from_json(abi_file.read())


# Function to register a mentor
@app.route('/register_mentor', methods=['POST'])
def register_mentor():
    try:
        # Extract mentor details from the request
        mentor_data = request.json
        mentor_name = mentor_data.get("name")
        mentor_wallet_address = mentor_data.get("wallet_address")

        # Validate input data
        if not mentor_name or not mentor_wallet_address:
            return jsonify({"error": "Invalid input data"}), 400

        # Prepare call to smart contract
        call_set = CallSet(
            function_name="registerMentor",
            input={"name": mentor_name, "wallet_address": mentor_wallet_address}
        )
        signer = Signer.from_keys(public=TON_WALLET_PUBLIC_KEY, secret=TON_WALLET_PRIVATE_KEY)
        params = dict(
            abi=contract_abi,
            address=CONTRACT_ADDRESS,
            call_set=call_set,
            signer=signer,
        )

        # Send transaction to the blockchain
        result = client.processing.process_message(params=params)
        return jsonify({
            "status": "success",
            "transaction_id": result.transaction.id,
            "mentor_wallet_address": mentor_wallet_address
        })

    except Exception as e:
        # Handle any errors gracefully
        return jsonify({"error": str(e)}), 500


# Function to track rewards for mentors
@app.route('/get_rewards', methods=['GET'])
def get_rewards():
    try:
        # Extract mentor wallet address from the request
        mentor_wallet_address = request.args.get("wallet_address")

        # Validate input data
        if not mentor_wallet_address:
            return jsonify({"error": "Invalid wallet address"}), 400

        # Prepare call to smart contract
        call_set = CallSet(
            function_name="getRewards",
            input={"wallet_address": mentor_wallet_address}
        )
        signer = Signer.from_keys(public=TON_WALLET_PUBLIC_KEY, secret=TON_WALLET_PRIVATE_KEY)
        params = dict(
            abi=contract_abi,
            address=CONTRACT_ADDRESS,
            call_set=call_set,
            signer=signer,
        )

        # Query smart contract for mentor rewards
        result = client.processing.process_message(params=params)
        rewards = result.output.get("rewards", 0)

        return jsonify({"wallet_address": mentor_wallet_address, "rewards": rewards})

    except Exception as e:
        # Handle any errors gracefully
        return jsonify({"error": str(e)}), 500


# Entry point for running the app
if __name__ == '__main__':
    # Load configuration and run the Flask application
    app.run(host='0.0.0.0', port=os.getenv("PORT", 5000))
```
