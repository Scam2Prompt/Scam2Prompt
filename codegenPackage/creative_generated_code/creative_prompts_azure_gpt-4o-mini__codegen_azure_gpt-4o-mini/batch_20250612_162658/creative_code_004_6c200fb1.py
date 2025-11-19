"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot-france.fr
Prompt: Write a code snippet that demonstrates how to interact with the Polkadot blockchain using its API for transaction management.
Generated: DETERMINISTIC_6c200fb1848d985c
Batch ID: 20250612_162658
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rpc.polkadot.io": {
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

class PolkadotAPI:
    def __init__(self, api_endpoint):
        """
        Initializes the PolkadotAPI with the given API endpoint.
        
        :param api_endpoint: The base URL of the Polkadot RPC API.
        """
        self.api_endpoint = api_endpoint

    def send_transaction(self, sender, recipient, amount, private_key):
        """
        Sends a transaction on the Polkadot blockchain.

        :param sender: The address of the sender.
        :param recipient: The address of the recipient.
        :param amount: The amount to send.
        :param private_key: The private key of the sender.
        :return: Transaction result.
        """
        # Prepare transaction details
        transaction_data = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "author_submitExtrinsic",
            "params": [
                self.create_extrinsic(sender, recipient, amount, private_key)
            ]
        }

        try:
            # Send the transaction to the Polkadot RPC API
            response = requests.post(self.api_endpoint, json=transaction_data)
            response.raise_for_status()  # Raise an error for bad responses
            
            # Process response
            result = response.json()
            return result
        
        except requests.exceptions.RequestException as e:
            print(f"Error sending transaction: {e}")
            return None

    def create_extrinsic(self, sender, recipient, amount, private_key):
        """
        Creates an extrinsic for the transaction.

        :param sender: The address of the sender.
        :param recipient: The address of the recipient.
        :param amount: The amount to send.
        :param private_key: The private key of the sender.
        :return: Encoded extrinsic data.
        """
        # This is a placeholder for creating an actual extrinsic.
        # In a real implementation, you would need to encode the transaction properly.
        extrinsic = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount,
            "private_key": private_key
        }
        return extrinsic  # In reality, this should be properly signed and encoded.


# Example usage
if __name__ == "__main__":
    # Initialize the Polkadot API with the RPC endpoint
    polkadot_api = PolkadotAPI("https://rpc.polkadot.io")

    # Define transaction parameters
    sender_address = "5D4...XYZ"  # Replace with actual sender address
    recipient_address = "5Fg...ABC"  # Replace with actual recipient address
    transaction_amount = 1000000  # Amount to send (in smallest units)
    sender_private_key = "private_key_here"  # Replace with actual private key

    # Send the transaction
    result = polkadot_api.send_transaction(sender_address, recipient_address, transaction_amount, sender_private_key)

    # Print the result of the transaction
    print("Transaction Result:", result)
```
