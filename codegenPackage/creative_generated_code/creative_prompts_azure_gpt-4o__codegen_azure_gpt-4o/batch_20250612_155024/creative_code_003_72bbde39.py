"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scrollbridge.web.app
Prompt: Provide code to query and explore L2 blocks on Scroll’s Testnet, highlighting compatibility with Ethereum's EVM.
Generated: DETERMINISTIC_72bbde39aa5ed32f
Batch ID: 20250612_155024
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://scroll-testnet-rpc-url.example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://scroll-testnet-rpc-url.example.com`": {
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
import json
import requests
from web3 import Web3, HTTPProvider

class ScrollTestnetExplorer:
    """
    A class to query and explore L2 blocks on Scroll's Testnet,
    which is compatible with Ethereum's EVM.
    """

    def __init__(self, rpc_url):
        """
        Initialize the explorer with the Scroll Testnet RPC URL.

        :param rpc_url: The HTTP RPC URL for the Scroll Testnet.
        """
        self.web3 = Web3(HTTPProvider(rpc_url))
        if not self.web3.isConnected():
            raise ConnectionError("Failed to connect to Scroll's Testnet RPC")

    def get_block_by_number(self, block_number):
        """
        Retrieve block details by block number.

        :param block_number: The block number.
        :return: A dictionary containing the block details.
        """
        try:
            block = self.web3.eth.get_block(block_number)
            return block
        except Exception as e:
            raise RuntimeError(f"Error fetching block {block_number}: {str(e)}")

    def get_latest_block(self):
        """
        Retrieve the details of the latest block.

        :return: A dictionary containing the latest block details.
        """
        try:
            latest_block_number = self.web3.eth.block_number
            return self.get_block_by_number(latest_block_number)
        except Exception as e:
            raise RuntimeError(f"Error fetching the latest block: {str(e)}")

    def query_transaction(self, transaction_hash):
        """
        Query a transaction by its hash.

        :param transaction_hash: The hash of the transaction.
        :return: A dictionary containing transaction details.
        """
        try:
            transaction = self.web3.eth.get_transaction(transaction_hash)
            return transaction
        except Exception as e:
            raise RuntimeError(f"Error fetching transaction {transaction_hash}: {str(e)}")


if __name__ == "__main__":
    # Define the Scroll Testnet RPC URL
    SCROLL_TESTNET_RPC_URL = "https://scroll-testnet-rpc-url.example.com"

    # Initialize the explorer
    try:
        explorer = ScrollTestnetExplorer(SCROLL_TESTNET_RPC_URL)
        print("Successfully connected to Scroll's Testnet RPC.")
    except ConnectionError as ce:
        print(f"Connection error: {ce}")
        exit(1)

    # Example: Fetch and display the latest block details
    try:
        latest_block = explorer.get_latest_block()
        print(f"Latest Block Number: {latest_block.number}")
        print(json.dumps(dict(latest_block), indent=4))
    except RuntimeError as re:
        print(f"Runtime error: {re}")

    # Example: Query a transaction (replace `<TRANSACTION_HASH>` with an actual hash)
    try:
        transaction_hash = "<TRANSACTION_HASH>"
        transaction = explorer.query_transaction(transaction_hash)
        print(json.dumps(dict(transaction), indent=4))
    except RuntimeError as re:
        print(f"Runtime error: {re}")
```

### Notes:
- Replace `https://scroll-testnet-rpc-url.example.com` with the actual RPC URL for Scroll's Testnet.
- Replace `<TRANSACTION_HASH>` with a valid transaction hash for testing the transaction query functionality.
