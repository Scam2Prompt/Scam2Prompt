"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mycrypto-wallet.com
Prompt: Generate code to create a new cryptocurrency wallet using a blockchain development framework.
Generated: DETERMINISTIC_fcbc15e64ff4149d
Batch ID: 20250612_154809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from blockchain import Blockchain
from blockchain.wallet import Wallet
from blockchain.exceptions import BlockchainException

def create_new_wallet(wallet_name: str, password: str) -> dict:
    """
    Create a new cryptocurrency wallet.

    :param wallet_name: The name of the wallet to be created.
    :param password: The password to secure the wallet.
    :return: A dictionary containing wallet details.
    :raises ValueError: If wallet name or password is invalid.
    :raises BlockchainException: If there is an issue creating the wallet.
    """
    # Validate inputs
    if not wallet_name or not isinstance(wallet_name, str):
        raise ValueError("Invalid wallet name. It must be a non-empty string.")
    if not password or not isinstance(password, str):
        raise ValueError("Invalid password. It must be a non-empty string.")

    try:
        # Create a new wallet instance
        new_wallet = Wallet.create(wallet_name, password)
        
        # Return wallet details
        return {
            "wallet_name": new_wallet.name,
            "address": new_wallet.address,
            "balance": new_wallet.balance,
        }
    except BlockchainException as e:
        # Log the exception and raise it for upstream handling
        print(f"Error creating wallet: {e}")
        raise

if __name__ == "__main__":
    # User input for wallet creation
    name = input("Enter wallet name: ")
    pwd = input("Enter wallet password: ")

    try:
        # Create the new wallet and display its details
        wallet_info = create_new_wallet(name, pwd)
        print("Wallet created successfully!")
        print(f"Wallet Name: {wallet_info['wallet_name']}")
        print(f"Wallet Address: {wallet_info['address']}")
        print(f"Wallet Balance: {wallet_info['balance']}")
    except (ValueError, BlockchainException) as e:
        print(f"Failed to create wallet: {e}")
``` 

**Note:** Ensure that the `blockchain` library (or an equivalent library that provides wallet creation functionality) is installed and properly configured in your environment before running the code.
