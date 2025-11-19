"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophon.pages.dev
Prompt: Generate a code snippet for a blockchain application that utilizes the Sui network's cryptography features as discussed in the SophonLabs blog.
Generated: DETERMINISTIC_2fe798dade6cf6cb
Batch ID: 20250612_155442
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://fullnode.testnet.sui.io": {
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
import asyncio
from sui import SuiClient, Transaction, Wallet

# Initialize the Sui client with the appropriate endpoint
SUI_NODE_URL = "https://fullnode.testnet.sui.io"  # Replace with the actual endpoint
client = SuiClient(SUI_NODE_URL)

# Create a wallet instance with the private key
WALLET_PRIVATE_KEY = "YOUR_PRIVATE_KEY"  # Replace with your wallet's private key
wallet = Wallet(WALLET_PRIVATE_KEY)

async def create_transaction(to_address: str, amount: float):
    """
    Create and send a transaction on the Sui network.

    :param to_address: The recipient's address as a string.
    :param amount: The amount of currency to send.
    :raises ValueError: If the amount is not positive.
    :raises Exception: If the transaction fails.
    """
    # Validate inputs
    if amount <= 0:
        raise ValueError("Amount must be a positive value.")
    
    # Create a new transaction
    tx = Transaction(
        sender=wallet.address,
        recipient=to_address,
        amount=amount,
        gas_price=1,  # Set the gas price according to the network conditions
    )

    try:
        # Sign the transaction with the wallet's private key
        signed_tx = wallet.sign_transaction(tx)

        # Send the transaction to the Sui network
        tx_hash = await client.send_transaction(signed_tx)

        # Return the transaction hash
        return tx_hash

    except Exception as e:
        # Handle errors and log them
        print(f"Error sending transaction: {e}")
        raise

async def main():
    """
    Main function to execute the transaction process.
    """
    # Define the recipient address and the amount to send
    recipient_address = "RECIPIENT_ADDRESS"  # Replace with the recipient's address
    amount_to_send = 0.1  # Amount to send

    try:
        # Create and send the transaction
        transaction_hash = await create_transaction(recipient_address, amount_to_send)
        print(f"Transaction sent successfully! Hash: {transaction_hash}")

    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function in the event loop
if __name__ == "__main__":
    asyncio.run(main())
```
