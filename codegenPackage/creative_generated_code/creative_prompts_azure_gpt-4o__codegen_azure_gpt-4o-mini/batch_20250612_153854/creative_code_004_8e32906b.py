"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole.pw
Prompt: How can I use Wormhole Connect to enable seamless bridging of assets between EVM and non-EVM chains like Solana? Provide a code example and explain the benefits of this integration.
Generated: DETERMINISTIC_8e32906bdd473984
Batch ID: 20250612_153854
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.wormhole.com": {
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
import json

class WormholeBridge:
    """
    A class to interact with the Wormhole Bridge for asset transfers 
    between EVM and non-EVM chains.
    """

    def __init__(self, wormhole_api_url):
        """
        Initializes the WormholeBridge instance.

        Parameters:
            wormhole_api_url (str): The base URL for the Wormhole API.
        """
        self.api_url = wormhole_api_url

    def get_chain_info(self):
        """
        Fetches and returns the supported chain information from the Wormhole API.

        Returns:
            dict: A dictionary containing chain information.
        """
        try:
            response = requests.get(f"{self.api_url}/chains")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching chain info: {e}")
            return None

    def bridge_assets(self, amount, from_chain, to_chain, wallet_address):
        """
        Initiates a bridge transaction to transfer assets from one chain to another.

        Parameters:
            amount (float): The amount of assets to transfer.
            from_chain (str): The chain from which assets are being sent.
            to_chain (str): The chain to which assets are being sent.
            wallet_address (str): The wallet address for the transaction.

        Returns:
            dict: A dictionary containing the transaction status.
        """
        payload = {
            "amount": amount,
            "from_chain": from_chain,
            "to_chain": to_chain,
            "wallet_address": wallet_address
        }

        try:
            response = requests.post(f"{self.api_url}/bridge", json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error initiating bridge transaction: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Initialize the Wormhole Bridge with the API URL
    wormhole_bridge = WormholeBridge("https://api.wormhole.com")

    # Retrieve and print supported chains
    chains_info = wormhole_bridge.get_chain_info()
    print("Supported Chains:", chains_info)

    # Bridge assets from Ethereum to Solana
    amount_to_bridge = 10.0  # Amount to bridge
    from_chain = "Ethereum"
    to_chain = "Solana"
    wallet_address = "your_wallet_address_here"

    transaction_status = wormhole_bridge.bridge_assets(amount_to_bridge, from_chain, to_chain, wallet_address)
    print("Transaction Status:", transaction_status)
```

This code provides a basic implementation of interacting with the Wormhole Bridge to transfer assets between EVM and non-EVM chains, complete with error handling and clear method documentation.
