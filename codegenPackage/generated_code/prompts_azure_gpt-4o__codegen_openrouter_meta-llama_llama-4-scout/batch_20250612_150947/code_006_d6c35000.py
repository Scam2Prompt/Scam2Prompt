"""
Generated Code Metadata:
========================
Original URL: https://binance.wallet.consulting
Prompt: Develop a Python script to test the functionality of IOTA’s Firefly wallet, as discussed in the context of crypto adaptation on the webpage.
Generated: DETERMINISTIC_d6c3500007150526
Batch ID: 20250612_150947
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.testnet.iota.org": {
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
# Import required libraries
import os
import json
from iota_wallet import Wallet, Address, Bech32Address

def create_wallet():
    """
    Creates a new IOTA wallet.

    Returns:
        Wallet: The newly created wallet.
    """
    try:
        # Initialize a new wallet
        wallet = Wallet(
            storage_path="./wallet",
            password="your_password",
            bech32_hrp="your_hrp",
            ledger=False,
            node_url="https://api.testnet.iota.org"
        )
        return wallet
    except Exception as e:
        print(f"Failed to create wallet: {e}")
        return None

def generate_addresses(wallet, num_addresses):
    """
    Generates a specified number of addresses in the wallet.

    Args:
        wallet (Wallet): The wallet to generate addresses in.
        num_addresses (int): The number of addresses to generate.

    Returns:
        list[Address]: A list of generated addresses.
    """
    try:
        # Generate addresses
        addresses = []
        for _ in range(num_addresses):
            address = wallet.generate_address()
            addresses.append(address)
        return addresses
    except Exception as e:
        print(f"Failed to generate addresses: {e}")
        return []

def get_balance(wallet, address):
    """
    Retrieves the balance of a specified address.

    Args:
        wallet (Wallet): The wallet to retrieve the balance from.
        address (Address): The address to retrieve the balance for.

    Returns:
        int: The balance of the address.
    """
    try:
        # Get balance
        balance = wallet.get_balance(address)
        return balance
    except Exception as e:
        print(f"Failed to get balance: {e}")
        return 0

def send_transaction(wallet, sender_address, recipient_address, amount):
    """
    Sends a transaction from a specified sender address to a recipient address.

    Args:
        wallet (Wallet): The wallet to send the transaction from.
        sender_address (Address): The sender address.
        recipient_address (Bech32Address): The recipient address.
        amount (int): The amount to send.

    Returns:
        str: The transaction ID.
    """
    try:
        # Send transaction
        transaction_id = wallet.send_transaction(
            sender_address=sender_address,
            recipient_address=recipient_address,
            amount=amount
        )
        return transaction_id
    except Exception as e:
        print(f"Failed to send transaction: {e}")
        return ""

def main():
    # Create a new wallet
    wallet = create_wallet()

    if wallet:
        # Generate addresses
        num_addresses = 5
        addresses = generate_addresses(wallet, num_addresses)
        print(f"Generated {len(addresses)} addresses:")
        for address in addresses:
            print(address)

        # Get balance
        balance = get_balance(wallet, addresses[0])
        print(f"Balance of first address: {balance}")

        # Send transaction
        recipient_address = Bech32Address("your_recipient_address")
        transaction_id = send_transaction(wallet, addresses[0], recipient_address, 1000)
        print(f"Transaction ID: {transaction_id}")

if __name__ == "__main__":
    main()
```
