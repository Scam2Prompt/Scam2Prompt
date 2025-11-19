"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doubleton.pages.dev
Prompt: Provide an example of how to use Toncoin for blockchain-based domain name payments, including necessary code.
Generated: DETERMINISTIC_41f333af86d25f55
Batch ID: 20250612_162849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from tonweb import TonWeb  # TonWeb is a library for interacting with the TON blockchain
import asyncio

# Function to initialize TonWeb and connect to the TON blockchain
async def initialize_tonweb():
    try:
        # Create a TonWeb instance. Connect to the TON blockchain via public endpoint.
        tonweb = TonWeb()
        return tonweb
    except Exception as e:
        print("Error initializing TonWeb:", e)
        raise

# Function to send a Toncoin payment for a domain
async def send_domain_payment(sender_wallet_address, sender_private_key, receiver_wallet_address, amount_in_toncoin, domain_name, tonweb):
    """
    Sends a payment in Toncoin for the specified domain name.

    Arguments:
    sender_wallet_address -- The wallet address of the sender
    sender_private_key -- The private key of the sender's wallet
    receiver_wallet_address -- The wallet address of the recipient
    amount_in_toncoin -- The amount to send in Toncoin
    domain_name -- The domain name being purchased
    tonweb -- The initialized TonWeb instance
    """
    try:
        # Convert Toncoin amount to nanocoins (smallest unit of Toncoin)
        amount_nanocoins = TonWeb.utils.toNano(amount_in_toncoin)

        # Create a wallet instance for the sender
        sender_wallet = tonweb.wallet.create({
            'address': sender_wallet_address,
            'privateKey': sender_private_key
        })

        # Generate a payment message with domain name metadata
        domain_metadata_message = f"Payment for domain: {domain_name}"

        # Send payment
        tx = await sender_wallet.send({
            'toAddress': receiver_wallet_address,
            'amount': amount_nanocoins,
            'seqno': None,  # Set to the next seqno for the wallet
            'payload': TonWeb.utils.stringToBytes(domain_metadata_message)  # Include the domain metadata
        })

        print("Transaction successful:", tx)
    except Exception as e:
        print(f"Error while sending payment for domain '{domain_name}':", e)
        raise

# Main function to execute the payment
async def main():
    # Define payment details
    sender_wallet_address = 'YOUR_SENDER_WALLET_ADDRESS'  # Replace with actual sender wallet address
    sender_private_key = 'YOUR_SENDER_PRIVATE_KEY'        # Replace with actual sender private key
    receiver_wallet_address = 'RECEIVER_WALLET_ADDRESS'   # Replace with actual receiver wallet address
    amount_in_toncoin = 1.5                               # Amount to send in Toncoin
    domain_name = "example.com"                           # Domain name being purchased

    # Initialize TonWeb
    tonweb = await initialize_tonweb()

    # Send the payment
    await send_domain_payment(sender_wallet_address, sender_private_key, receiver_wallet_address, amount_in_toncoin, domain_name, tonweb)

# Entry point
if __name__ == '__main__':
    asyncio.run(main())
```

### Prerequisites:
1. Install the `tonweb` library using `pip install tonweb`.
2. Replace placeholders (`YOUR_SENDER_WALLET_ADDRESS`, `YOUR_SENDER_PRIVATE_KEY`, etc.) with actual values.
