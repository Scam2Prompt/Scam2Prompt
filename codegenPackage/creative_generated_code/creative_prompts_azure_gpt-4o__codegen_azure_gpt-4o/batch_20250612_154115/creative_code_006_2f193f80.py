"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridge-finance.org
Prompt: Explain how to use deBridge's infrastructure to connect a private enterprise blockchain with public networks, reducing settlement times and ensuring security.
Generated: DETERMINISTIC_2f193f806a4899b6
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script demonstrates how to use deBridge's infrastructure to connect a private enterprise blockchain
with public networks for reducing settlement times and ensuring secure transactions.

Prerequisites:
- Install the deBridge SDK using `pip install debridge-sdk`
- Ensure you have API credentials for the deBridge platform
"""

from debridge_sdk import DeBridgeClient, TransactionPayload, BlockchainNetwork
import logging

# Set up logging for monitoring application behavior
logging.basicConfig(level=logging.INFO)

# Configuration: Replace with your actual credentials and network details
DEBRIDGE_API_KEY = "your_api_key_here"
PRIVATE_BLOCKCHAIN_NETWORK = "enterprise_private_network"
PUBLIC_BLOCKCHAIN_NETWORK = "ethereum_mainnet"

# Initialize the deBridge client
try:
    debridge_client = DeBridgeClient(api_key=DEBRIDGE_API_KEY)
    logging.info("Successfully initialized deBridge client.")
except Exception as e:
    logging.error("Failed to initialize deBridge client: %s", str(e))
    raise

# Function to create and send a cross-chain transaction
def send_cross_chain_transaction(payload_data, sender_address, receiver_address):
    """
    Sends a transaction across the private enterprise blockchain and the public network.

    :param payload_data: Transaction details, such as amount and metadata.
    :param sender_address: Address initiating the transaction on the private blockchain.
    :param receiver_address: Address receiving the transaction on the public network.
    :return: Transaction status or error message.
    """
    try:
        # Define payload for the transaction
        payload = TransactionPayload(
            data=payload_data,
            sender_address=sender_address,
            receiver_address=receiver_address,
            source_network=BlockchainNetwork(PRIVATE_BLOCKCHAIN_NETWORK),
            destination_network=BlockchainNetwork(PUBLIC_BLOCKCHAIN_NETWORK)
        )
        
        logging.info("Payload prepared successfully.")

        # Send the transaction using deBridge
        transaction_response = debridge_client.send_transaction(payload)
        logging.info("Transaction successfully sent. Response: %s", transaction_response)

        return transaction_response
    except Exception as e:
        logging.error("Failed to send cross-chain transaction: %s", str(e))
        return {"error": str(e)}

# Example usage of the function
if __name__ == "__main__":
    # Replace with actual sender and receiver addresses and payload details
    sender = "private_chain_address_123"
    receiver = "public_chain_address_456"
    payload_details = {
        "amount": 100,
        "currency": "USD",
        "metadata": "Settlement for invoice #98765"
    }
    
    result = send_cross_chain_transaction(payload_details, sender, receiver)
    
    # Output the result
    if "error" in result:
        logging.error("Transaction failed: %s", result["error"])
    else:
        logging.info("Transaction succeeded: %s", result)
```
