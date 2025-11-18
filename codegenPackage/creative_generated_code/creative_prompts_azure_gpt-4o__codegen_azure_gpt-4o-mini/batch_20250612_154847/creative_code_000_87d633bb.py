"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ostpp.ru
Prompt: Write Python code to interact with the Hop Protocol API for transferring tokens between Ethereum and Polygon networks. Include the use of relayers and cross-chain bridge functionality described on the website.
Generated: DETERMINISTIC_87d633bb6122bb7b
Batch ID: 20250612_154847
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hop.exchange/v1": {
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

class HopProtocolAPI:
    """A class to interact with the Hop Protocol API for token transfers between Ethereum and Polygon networks."""

    BASE_URL = "https://api.hop.exchange/v1"

    def __init__(self, relayer_address):
        self.relayer_address = relayer_address

    def get_bridge_info(self):
        """
        Fetches the bridge information from the Hop Protocol API.
        
        Returns:
            dict: A dictionary containing bridge information.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/bridge_info")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching bridge info: {e}")
            return None

    def transfer_tokens(self, from_chain, to_chain, amount, token, recipient):
        """
        Initiates a token transfer from one chain to another.

        Args:
            from_chain (str): The chain to transfer tokens from (e.g., "Ethereum").
            to_chain (str): The chain to transfer tokens to (e.g., "Polygon").
            amount (float): The amount of tokens to transfer.
            token (str): The token symbol to transfer.
            recipient (str): The recipient's address on the destination chain.

        Returns:
            dict: A dictionary containing the transaction details, or None if an error occurred.
        """
        transfer_data = {
            "fromChain": from_chain,
            "toChain": to_chain,
            "amount": amount,
            "token": token,
            "recipient": recipient,
            "relayer": self.relayer_address
        }

        try:
            response = requests.post(f"{self.BASE_URL}/transfer", json=transfer_data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error initiating transfer: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Replace with your relayer address and desired transfer parameters
    RELAYER_ADDRESS = "0xYourRelayerAddress"
    hop_api = HopProtocolAPI(relayer_address=RELAYER_ADDRESS)

    # Fetch bridge information
    bridge_info = hop_api.get_bridge_info()
    if bridge_info:
        print("Bridge Info:", json.dumps(bridge_info, indent=2))

    # Example transfer (replace with actual parameters)
    transfer_response = hop_api.transfer_tokens(
        from_chain="Ethereum",
        to_chain="Polygon",
        amount=1.0,
        token="ETH",
        recipient="0xRecipientAddress"
    )

    if transfer_response:
        print("Transfer Response:", json.dumps(transfer_response, indent=2))
```
