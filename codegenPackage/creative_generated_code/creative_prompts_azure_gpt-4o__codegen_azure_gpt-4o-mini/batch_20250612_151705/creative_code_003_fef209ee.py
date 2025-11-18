"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridge.xyz
Prompt: Provide an example of how to use blockchain bridging APIs to transfer assets between chains, referencing platforms like deBridge.
Generated: DETERMINISTIC_fef209eeb6c1c516
Batch ID: 20250612_151705
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.debridge.finance/v1": {
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

class BlockchainBridge:
    """
    A class to handle asset transfers between blockchain networks using deBridge API.
    """

    def __init__(self, api_url):
        """
        Initializes the BlockchainBridge with the specified API URL.

        :param api_url: The base URL of the deBridge API.
        """
        self.api_url = api_url

    def get_supported_chains(self):
        """
        Retrieves the list of supported chains from the deBridge API.

        :return: List of supported chains.
        :raises Exception: If API request fails or returns an error.
        """
        try:
            response = requests.get(f"{self.api_url}/chains")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching supported chains: {e}")

    def transfer_asset(self, from_chain, to_chain, asset_id, amount, recipient_address):
        """
        Initiates the transfer of an asset from one chain to another.

        :param from_chain: The chain from which to transfer the asset.
        :param to_chain: The chain to which to transfer the asset.
        :param asset_id: The identifier of the asset to be transferred.
        :param amount: The amount of the asset to transfer.
        :param recipient_address: The address to receive the transferred asset.
        :return: Transaction details upon successful transfer.
        :raises Exception: If API request fails or returns an error.
        """
        payload = {
            "fromChain": from_chain,
            "toChain": to_chain,
            "assetId": asset_id,
            "amount": amount,
            "recipient": recipient_address
        }
        
        try:
            response = requests.post(f"{self.api_url}/transfer", json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error transferring asset: {e}")

# Example usage
if __name__ == "__main__":
    API_URL = "https://api.debridge.finance/v1"  # Replace with actual deBridge API URL
    bridge = BlockchainBridge(API_URL)

    try:
        # Retrieve and print supported chains
        supported_chains = bridge.get_supported_chains()
        print("Supported Chains:", supported_chains)

        # Transfer assets between chains
        from_chain = "Ethereum"
        to_chain = "Binance Smart Chain"
        asset_id = "0x123456789abcdef"  # Replace with actual asset ID
        amount = 10.0
        recipient_address = "0xabcdefabcdefabcdef"  # Replace with actual recipient address

        transfer_result = bridge.transfer_asset(from_chain, to_chain, asset_id, amount, recipient_address)
        print("Transfer Result:", transfer_result)

    except Exception as e:
        print(f"An error occurred: {e}")
```
