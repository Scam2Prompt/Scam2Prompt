"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-f.pages.dev
Prompt: Provide an example of how to handle transaction errors when using the MultiChain Protocol for DApps.
Generated: DETERMINISTIC_ba793c0ba9fc7eaa
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from multichain.client import Client

# Configuration for MultiChain node connection
MULTICHAIN_NODE_HOST = 'localhost'  # Replace with your node's host
MULTICHAIN_NODE_PORT = 7000         # Replace with your node's port
MULTICHAIN_NODE_USER = 'rpcuser'    # Replace with your RPC username
MULTICHAIN_NODE_PASSWORD = 'rpcpassword'  # Replace with your RPC password

# Initialize the MultiChain client
client = Client(
    host=MULTICHAIN_NODE_HOST,
    port=MULTICHAIN_NODE_PORT,
    username=MULTICHAIN_NODE_USER,
    password=MULTICHAIN_NODE_PASSWORD
)

def create_and_send_transaction(to_address, asset_name, amount):
    """
    Creates and sends a transaction on MultiChain while handling potential errors.

    Args:
        to_address (str): The destination address for the transaction.
        asset_name (str): The asset name to transfer.
        amount (float): The amount of the asset to transfer.

    Returns:
        dict: The result of the transaction or error details.
    """
    try:
        # Step 1: Check if the destination address is valid
        if not client.validateaddress(to_address)['isvalid']:
            raise ValueError(f"Invalid destination address: {to_address}")

        # Step 2: Create the transaction
        tx_hex = client.createrawsendfrom(
            from_address='',  # Leave blank for default address
            amounts={to_address: {asset_name: amount}}
        )

        # Step 3: Sign the transaction
        signed_tx = client.signrawtransaction(tx_hex)
        if not signed_tx['complete']:
            raise RuntimeError("Transaction signing failed.")

        # Step 4: Broadcast the transaction
        tx_id = client.sendrawtransaction(signed_tx['hex'])

        # Return the transaction ID on success
        return {"status": "success", "transaction_id": tx_id}

    except ValueError as ve:
        # Handle validation errors
        return {"status": "error", "message": str(ve)}

    except RuntimeError as re:
        # Handle runtime errors during signing or broadcasting
        return {"status": "error", "message": str(re)}

    except Exception as e:
        # Catch-all for unexpected errors
        return {"status": "error", "message": f"An unexpected error occurred: {e}"}


# Example usage
if __name__ == "__main__":
    # Replace with valid values for your environment
    recipient_address = "1A2b3C4D5E6F7G8H9I0J"
    asset = "exampleAsset"
    transfer_amount = 10.0

    # Attempt to create and send a transaction
    result = create_and_send_transaction(recipient_address, asset, transfer_amount)
    print(json.dumps(result, indent=4))
```
