"""
Generated Code Metadata:
========================
Original URL: https://ton.me
Prompt: Create a tutorial on using the TON DNS service to register a domain name on the TON network, including code examples.
Generated: DETERMINISTIC_77335e65c975a23d
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Tutorial: Registering a Domain Name on the TON Network using TON DNS Service

This script demonstrates how to interact with the TON DNS service to register a domain name.
It uses the TonWeb library to interact with the TON blockchain.

Requirements:
- Install the TonWeb library: `pip install tonweb`
- Have a TON wallet with sufficient funds to pay for the domain registration.
"""

import asyncio
from tonweb import TonWeb
from tonweb.types import Address

# Constants
TON_DNS_CONTRACT_ADDRESS = "EQC...TON_DNS_CONTRACT_ADDRESS_HERE"  # Replace with the actual TON DNS contract address
WALLET_PRIVATE_KEY = "YOUR_PRIVATE_KEY_HERE"  # Replace with your wallet's private key
DOMAIN_NAME = "example.ton"  # Replace with the domain name you want to register
REGISTRATION_FEE = 0.1  # Replace with the actual registration fee (in TON)

async def register_domain():
    try:
        # Initialize TonWeb instance
        tonweb = TonWeb()

        # Create wallet instance using private key
        wallet = tonweb.wallet.create(WALLET_PRIVATE_KEY)

        # Get wallet address
        wallet_address = await wallet.get_address()
        print(f"Wallet Address: {wallet_address}")

        # Check wallet balance
        balance = await tonweb.get_balance(wallet_address)
        print(f"Wallet Balance: {balance} TON")

        if balance < REGISTRATION_FEE:
            raise ValueError("Insufficient balance to register the domain.")

        # Prepare DNS registration payload
        dns_contract_address = Address(TON_DNS_CONTRACT_ADDRESS)
        payload = tonweb.utils.encode_domain_registration_payload(DOMAIN_NAME)

        # Send transaction to register the domain
        print(f"Registering domain '{DOMAIN_NAME}'...")
        transaction = await wallet.send_transaction(
            to_address=dns_contract_address,
            amount=REGISTRATION_FEE,
            payload=payload
        )

        print(f"Transaction sent successfully: {transaction}")
        print(f"Domain '{DOMAIN_NAME}' registered successfully!")

    except Exception as e:
        print(f"Error: {e}")

# Run the script
if __name__ == "__main__":
    asyncio.run(register_domain())
```
