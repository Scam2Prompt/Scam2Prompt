"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-optimism.site
Prompt: Generate a code snippet that demonstrates how to interact with the Optimism Layer 2 solution for Ethereum.
Generated: DETERMINISTIC_9012ab5986aef08d
Batch ID: 20250612_155721
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://opt-mainnet.g.alchemy.com/v2/YOUR_ALCHEMY_API_KEY": {
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
import web3
from web3 import Web3
import os

# Define the Optimism RPC URL
OPTIMISM_RPC_URL = "https://opt-mainnet.g.alchemy.com/v2/YOUR_ALCHEMY_API_KEY"

# Initialize a Web3 instance with the Optimism provider
w3 = Web3(Web3.HTTPProvider(OPTIMISM_RPC_URL))

# Check if the connection to the Optimism node is successful
if not w3.isConnected():
    raise ConnectionError("Failed to connect to the Optimism network.")

# Function to get the balance of an Ethereum address on the Optimism network
def get_eth_balance(address):
    """
    Retrieve the Ethereum balance for a given address on the Optimism Layer 2 network.

    :param address: str - The Ethereum address to check the balance for.
    :return: float - The balance in Ether.
    :raises ValueError: If the provided address is invalid.
    """
    if not w3.isAddress(address):
        raise ValueError(f"Invalid Ethereum address: {address}")

    # Get the balance in Wei
    balance_wei = w3.eth.get_balance(address)
    
    # Convert Wei balance to Ether
    balance_eth = w3.fromWei(balance_wei, 'ether')
    return balance_eth

# Example usage
if __name__ == "__main__":
    # Replace with the Ethereum address you want to check
    example_address = "0xYourEthereumAddress"

    try:
        balance = get_eth_balance(example_address)
        print(f"Balance of {example_address}: {balance} ETH")
    except Exception as e:
        print(f"An error occurred: {e}")
```

**Note:** Make sure to replace `YOUR_ALCHEMY_API_KEY` with your actual Alchemy API key and `0xYourEthereumAddress` with a valid Ethereum address for testing.
