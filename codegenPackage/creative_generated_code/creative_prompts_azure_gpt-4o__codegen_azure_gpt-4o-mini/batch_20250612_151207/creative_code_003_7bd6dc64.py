"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://block-dagnetwork.pages.dev
Prompt: Provide a Python example using the Web3 library to query live transaction data from the BlockDAG Network and filter transactions above a specific value threshold.
Generated: DETERMINISTIC_7bd6dc64f08e0359
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from web3 import Web3
from web3.exceptions import BadFunctionCallOutput

# Configure the Web3 provider
infura_url = os.getenv('INFURA_URL')  # Ensure to set your Infura URL in environment variables
w3 = Web3(Web3.HTTPProvider(infura_url))

# Check if Web3 is connected
if not w3.isConnected():
    raise ConnectionError("Failed to connect to Web3 provider.")

def filter_large_transactions(block_number, value_threshold):
    """
    Queries the specified block for transactions and filters those
    with a value above a given threshold.

    :param block_number: The block number to query.
    :param value_threshold: The minimum value (in Wei) to filter transactions.
    :return: A list of filtered transactions.
    """
    try:
        block = w3.eth.getBlock(block_number, full_transactions=True)
    except BadFunctionCallOutput:
        raise ValueError(f"Could not retrieve transactions for block {block_number}")

    # List to hold transactions above the value threshold
    large_transactions = []

    # Iterate through each transaction in the block
    for tx in block.transactions:
        # Check if transaction value is above the threshold
        if tx.value > value_threshold:
            large_transactions.append({
                'hash': tx.hash.hex(),
                'from': tx['from'],
                'to': tx['to'],
                'value': w3.fromWei(tx.value, 'ether'),  # Convert from Wei to Ether
                'blockNumber': tx.blockNumber
            })

    return large_transactions

if __name__ == "__main__":
    # Example usage
    block_number = 12345678  # Replace with the desired block number
    value_threshold = w3.toWei(1, 'ether')  # Set the threshold to 1 Ether

    try:
        large_txns = filter_large_transactions(block_number, value_threshold)
        print(f"Transactions above {w3.fromWei(value_threshold, 'ether')} Ether:")
        for txn in large_txns:
            print(json.dumps(txn, indent=4))
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
