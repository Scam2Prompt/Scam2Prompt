"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-token-bridge-git-bridge-and-tx-hi-d503e2-offchain-labs.vercel.app
Prompt: Generate an example of a transaction that utilizes L2 gas savings when using the Arbitrum Bridge.
Generated: DETERMINISTIC_0214d71a5011b0d3
Batch ID: 20250612_135427
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
from web3 import Web3
import requests

# Replace with your Ethereum node provider
ETH_NODE_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
# Replace with the Arbitrum Bridge contract address
ARBITRUM_BRIDGE_ADDRESS = "0xYourArbitrumBridgeAddress"

# Setting up the web3 connection
web3 = Web3(Web3.HTTPProvider(ETH_NODE_URL))

# Check if connected to Ethereum node
if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum node.")

# Define the transaction details
def create_transaction(from_address, to_address, amount, private_key):
    """
    Create a transaction to transfer funds to Arbitrum using the bridge.

    :param from_address: Address from which to send funds.
    :param to_address: Address that will receive funds on Arbitrum.
    :param amount: Amount of ETH to transfer.
    :param private_key: Private key of the sender's account.
    :return: Transaction hash if successful, None otherwise.
    """
    try:
        # Convert amount to Wei
        amount_in_wei = web3.toWei(amount, 'ether')

        # Build the transaction
        transaction = {
            'to': ARBITRUM_BRIDGE_ADDRESS,
            'value': amount_in_wei,
            'gas': 2000000,  # Estimate appropriate gas limit
            'gasPrice': web3.toWei('100', 'gwei'),  # Set gas price
            'nonce': web3.eth.getTransactionCount(from_address),
            'chainId': 1  # Mainnet
        }

        # Sign the transaction
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key)

        # Send the transaction
        txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        print(f"Transaction sent! Hash: {txn_hash.hex()}")
        return txn_hash

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Replace with the correct addresses and private key
    FROM_ADDRESS = "0xYourEthereumAddress"
    TO_ADDRESS = "0xYourArbitrumAddress"
    AMOUNT = 0.1  # Amount in Ether
    PRIVATE_KEY = "0xYourPrivateKey"

    # Create and send the transaction
    transaction_hash = create_transaction(FROM_ADDRESS, TO_ADDRESS, AMOUNT, PRIVATE_KEY)

    if transaction_hash:
        print(f"Transaction successful with hash: {transaction_hash.hex()}")
    else:
        print("Transaction failed.")
```
