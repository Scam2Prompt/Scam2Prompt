"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zero-815.pages.dev
Prompt: Write a script that interacts with LayerZero's testnet to send a message between two chains. Include setup instructions for endpoints and relayer configuration.
Generated: DETERMINISTIC_9eedae091decd9d1
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# layerzero_message_sender.py

"""
A Python script to interact with LayerZero's testnet and send a message between two chains.

Prerequisites:
1. Install Web3.py: `pip install web3`
2. Install dotenv for managing environment variables: `pip install python-dotenv`
3. Add your LayerZero testnet configuration details in a `.env` file as below:
   - SOURCE_CHAIN_RPC_URL=<RPC URL of the source chain>
   - TARGET_CHAIN_RPC_URL=<RPC URL of the target chain>
   - PRIVATE_KEY=<Your wallet's private key>
   - LAYERZERO_ENDPOINT=<LayerZero endpoint address>
   - RELAYER_ADDRESS=<LayerZero relayer address>
   - TARGET_CHAIN_ID=<ID of the target chain>
"""

import os
import json
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants and configuration
SOURCE_CHAIN_RPC_URL = os.getenv("SOURCE_CHAIN_RPC_URL")
TARGET_CHAIN_RPC_URL = os.getenv("TARGET_CHAIN_RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
LAYERZERO_ENDPOINT = os.getenv("LAYERZERO_ENDPOINT")
RELAYER_ADDRESS = os.getenv("RELAYER_ADDRESS")
TARGET_CHAIN_ID = int(os.getenv("TARGET_CHAIN_ID"))

# Validate environment variables
if not all([SOURCE_CHAIN_RPC_URL, TARGET_CHAIN_RPC_URL, PRIVATE_KEY, LAYERZERO_ENDPOINT, RELAYER_ADDRESS, TARGET_CHAIN_ID]):
    raise EnvironmentError("One or more required environment variables are missing!")

# Initialize Web3 instances for source and target chains
source_chain_web3 = Web3(Web3.HTTPProvider(SOURCE_CHAIN_RPC_URL))
target_chain_web3 = Web3(Web3.HTTPProvider(TARGET_CHAIN_RPC_URL))

if not source_chain_web3.isConnected() or not target_chain_web3.isConnected():
    raise ConnectionError("Failed to connect to one or both blockchain RPC endpoints.")

# Load wallet information
account = source_chain_web3.eth.account.privateKeyToAccount(PRIVATE_KEY)
wallet_address = account.address

# Define LayerZero contract ABI (abridged for demonstration purposes; replace with full ABI)
layerzero_abi = [
    {
        "constant": False,
        "inputs": [
            {"name": "_dstChainId", "type": "uint16"},
            {"name": "_payload", "type": "bytes"},
        ],
        "name": "send",
        "outputs": [],
        "type": "function",
    },
    # Add other relevant methods and events from the LayerZero contract ABI
]

# Connect to the LayerZero endpoint contract
layerzero_contract = source_chain_web3.eth.contract(address=Web3.toChecksumAddress(LAYERZERO_ENDPOINT), abi=layerzero_abi)

# Function to send a message
def send_message(target_chain_id, payload, gas_limit=300000):
    """
    Sends a message from the source chain to the target chain using LayerZero.

    Args:
    - target_chain_id (int): The ID of the target chain.
    - payload (str): The message payload to send.
    - gas_limit (int): The maximum amount of gas for the transaction (default: 300,000).

    Returns:
    - tx_hash (str): The transaction hash of the sent message.
    """
    try:
        # Prepare transaction
        nonce = source_chain_web3.eth.getTransactionCount(wallet_address)
        transaction = layerzero_contract.functions.send(
            target_chain_id,
            payload.encode("utf-8")  # Convert string to bytes for payload
        ).buildTransaction({
            "chainId": source_chain_web3.eth.chain_id,
            "gas": gas_limit,
            "gasPrice": source_chain_web3.eth.gas_price,
            "nonce": nonce,
        })

        # Sign and send transaction
        signed_tx = source_chain_web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)
        tx_hash = source_chain_web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        print(f"Transaction sent. Hash: {tx_hash.hex()}")
        return tx_hash.hex()
    except Exception as e:
        print(f"Error sending message: {e}")
        return None

# Example usage
if __name__ == "__main__":
    try:
        # Sample payload
        message_payload = "Hello LayerZero!"
        tx_hash = send_message(TARGET_CHAIN_ID, message_payload)
        if tx_hash:
            print(f"Message successfully sent with transaction hash: {tx_hash}")
        else:
            print("Failed to send message.")
    except KeyboardInterrupt:
        print("Script interrupted by user.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
```

### Notes:
1. Replace the placeholder LayerZero contract ABI with the actual ABI provided by LayerZero.
2. Ensure the `.env` file is properly configured before running the script.
