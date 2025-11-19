"""
Generated Code Metadata:
========================
Original URL: https://wormhole.pw
Prompt: Explain how to use Wormhole's SDK to build a custom multichain application, referencing the 3-line code integration and support for 30+ blockchains.
Generated: DETERMINISTIC_f094fadca7193d3a
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import the Wormhole SDK
from wormhole_sdk import Wormhole

# Initialize the Wormhole client
# Replace 'your_api_key' with your actual API key obtained from Wormhole
try:
    wormhole_client = Wormhole(api_key="your_api_key")
except Exception as e:
    print(f"Error initializing Wormhole client: {e}")
    raise

# Function to transfer assets across chains
def transfer_assets(source_chain, target_chain, asset, amount, recipient_address):
    """
    Transfers assets from one blockchain to another using Wormhole's SDK.

    Args:
        source_chain (str): The source blockchain (e.g., 'ethereum').
        target_chain (str): The target blockchain (e.g., 'solana').
        asset (str): The asset to transfer (e.g., 'USDC').
        amount (float): The amount of the asset to transfer.
        recipient_address (str): The recipient's address on the target chain.

    Returns:
        dict: Transaction details if successful.
    """
    try:
        # Perform the cross-chain transfer
        transaction = wormhole_client.transfer(
            source_chain=source_chain,
            target_chain=target_chain,
            asset=asset,
            amount=amount,
            recipient=recipient_address
        )
        return transaction
    except Exception as e:
        print(f"Error during asset transfer: {e}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        # Define transfer parameters
        source_chain = "ethereum"
        target_chain = "solana"
        asset = "USDC"
        amount = 100.0
        recipient_address = "RecipientAddressOnTargetChain"

        # Execute the transfer
        transaction_details = transfer_assets(
            source_chain, target_chain, asset, amount, recipient_address
        )

        # Print transaction details
        print("Transaction successful!")
        print(transaction_details)
    except Exception as e:
        print(f"An error occurred: {e}")
```

### Notes:
- Replace `"your_api_key"` with your actual API key from Wormhole.
- Replace `"RecipientAddressOnTargetChain"` with the recipient's address on the target blockchain.
- Ensure the Wormhole SDK is installed in your environment (`pip install wormhole-sdk` or equivalent).
