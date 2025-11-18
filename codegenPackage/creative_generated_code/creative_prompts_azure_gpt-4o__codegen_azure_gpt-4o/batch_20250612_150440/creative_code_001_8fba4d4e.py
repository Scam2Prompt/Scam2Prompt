"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-token-bridge-git-new-tx-history-s-a94206-offchain-labs.vercel.app
Prompt: Generate a script to check the status of a token transfer using the Arbitrum Token Bridge, referencing the latest upgrade details mentioned in the documentation.
Generated: DETERMINISTIC_8fba4d4ecebd8d76
Batch ID: 20250612_150440
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://arb1.arbitrum.io/rpc": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.arbiscan.io/api": {
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
import requests
from web3 import Web3

# Constants
ARBITRUM_BRIDGE_API = "https://api.arbiscan.io/api"
ARBITRUM_RPC_URL = "https://arb1.arbitrum.io/rpc"  # RPC URL for interacting with Arbitrum's blockchain
ETHERSCAN_API_KEY = "your_etherscan_api_key"  # Replace with your Etherscan API key
BRIDGE_CONTRACT_ADDRESS = "0xYourBridgeContractAddress"  # Replace with Arbitrum Token Bridge contract address
TRANSFER_EVENT_TOPIC = "0xYourTransferEventTopic"  # Replace with the correct Transfer event topic

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(ARBITRUM_RPC_URL))

# Helper function to fetch logs for a token transfer transaction
def fetch_transfer_status(tx_hash):
    """
    Fetch the status of a token transfer using the Arbitrum Token Bridge.

    Args:
        tx_hash (str): Transaction hash of the token transfer.

    Returns:
        dict: A dictionary containing the status and details of the transfer.
    """
    try:
        # Validate transaction hash format
        if not w3.isAddress(tx_hash):
            raise ValueError("Invalid transaction hash format.")

        # Call the Arbiscan API for the transaction receipt status
        params = {
            "module": "transaction",
            "action": "gettxreceiptstatus",
            "txhash": tx_hash,
            "apikey": ETHERSCAN_API_KEY,
        }
        response = requests.get(ARBITRUM_BRIDGE_API, params=params)
        response.raise_for_status()

        data = response.json()
        if not data["status"] == "1":
            raise Exception(f"Error fetching transaction details: {data}")

        # Parse and return the results
```
