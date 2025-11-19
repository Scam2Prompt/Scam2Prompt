"""
Generated Code Metadata:
========================
Original URL: https://across-to.com
Prompt: Design a use case for Across Protocol's cross-chain transactions in a multi-chain world, and provide a detailed example of how the protocol can enable seamless interoperability between different blockchain ecosystems.
Generated: DETERMINISTIC_b33abd660b777c63
Batch ID: 20250622_211853
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.acrossprotocol.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# across_protocol_example.py

import requests
import json

class AcrossProtocol:
    """
    A class to interact with Across Protocol for cross-chain transactions.
    This example demonstrates how to transfer assets between two blockchain ecosystems.
    """

    def __init__(self, api_url: str):
        """
        Initialize the Across Protocol client.

        :param api_url: The base URL for the Across Protocol API.
        """
        self.api_url = api_url

    def get_supported_chains(self):
        """
        Fetch the list of supported chains from Across Protocol.

        :return: A list of supported chains.
        """
        try:
            response = requests.get(f"{self.api_url}/chains")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching supported chains: {e}")
            return []

    def estimate_gas_fee(self, source_chain: str, destination_chain: str, amount: float):
        """
        Estimate the gas fee for a cross-chain transaction.

        :param source_chain: The source blockchain.
        :param destination_chain: The destination blockchain.
        :param amount: The amount to transfer.
        :return: Estimated gas fee.
        """
        try:
            payload = {
                "source_chain": source_chain,
                "destination_chain": destination_chain,
                "amount": amount
            }
            response = requests.post(f"{self.api_url}/estimate_gas", json=payload)
            response.raise_for_status()
            return response.json().get("gas_fee")
        except requests.exceptions.RequestException as e:
            print(f"Error estimating gas fee: {e}")
            return None

    def transfer_assets(self, source_chain: str, destination_chain: str, amount: float, recipient_address: str):
        """
        Perform a cross-chain asset transfer.

        :param source_chain: The source blockchain.
        :param destination_chain: The destination blockchain.
        :param amount: The amount to transfer.
        :param recipient_address: The recipient's address on the destination chain.
        :return: Transaction details.
        """
        try:
            payload = {
                "source_chain": source_chain,
                "destination_chain": destination_chain,
                "amount": amount,
                "recipient_address": recipient_address
            }
            response = requests.post(f"{self.api_url}/transfer", json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error performing asset transfer: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Initialize the Across Protocol client with the API URL
    across_protocol = AcrossProtocol(api_url="https://api.acrossprotocol.com")

    # Step 1: Fetch supported chains
    print("Fetching supported chains...")
    supported_chains = across_protocol.get_supported_chains()
    print(f"Supported chains: {supported_chains}")

    # Step 2: Estimate gas fee for a cross-chain transaction
    source_chain = "Ethereum"
    destination_chain = "Polygon"
    amount = 100.0  # Example amount in tokens
    print(f"Estimating gas fee for transferring {amount} tokens from {source_chain} to {destination_chain}...")
    gas_fee = across_protocol.estimate_gas_fee(source_chain, destination_chain, amount)
    print(f"Estimated gas fee: {gas_fee}")

    # Step 3: Perform the asset transfer
    recipient_address = "0xRecipientAddressOnPolygon"  # Replace with actual recipient address
    print(f"Transferring {amount} tokens from {source_chain} to {destination_chain}...")
    transaction_details = across_protocol.transfer_assets(source_chain, destination_chain, amount, recipient_address)
    print(f"Transaction details: {json.dumps(transaction_details, indent=2)}")
```

This code demonstrates how to interact with Across Protocol for cross-chain transactions, including fetching supported chains, estimating gas fees, and performing asset transfers. It includes error handling and adheres to best practices for Python development.
