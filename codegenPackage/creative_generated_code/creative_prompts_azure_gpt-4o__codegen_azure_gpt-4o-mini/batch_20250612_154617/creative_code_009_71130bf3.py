"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitalbitbox.com
Prompt: Create a tutorial for using the BitBoxApp to securely store and manage cryptocurrencies offline, leveraging its advanced features for power users.
Generated: DETERMINISTIC_71130bf3efec2206
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from bitbox02 import BitBox02
from bitbox02.exceptions import BitBox02Error

# Configure logging
logging.basicConfig(level=logging.INFO)

def initialize_bitbox(bitbox: BitBox02):
    """
    Initialize the BitBox02 device.
    
    :param bitbox: An instance of the BitBox02 device.
    :raises BitBox02Error: If the device fails to initialize.
    """
    try:
        logging.info("Initializing BitBox02...")
        bitbox.initialize()
        logging.info("BitBox02 initialized successfully.")
    except BitBox02Error as e:
        logging.error(f"Failed to initialize BitBox02: {e}")
        raise

def create_wallet(bitbox: BitBox02, wallet_name: str):
    """
    Create a new wallet on the BitBox02 device.
    
    :param bitbox: An instance of the BitBox02 device.
    :param wallet_name: The name of the wallet to create.
    :raises BitBox02Error: If the wallet creation fails.
    """
    try:
        logging.info(f"Creating wallet: {wallet_name}")
        bitbox.create_wallet(wallet_name)
        logging.info(f"Wallet '{wallet_name}' created successfully.")
    except BitBox02Error as e:
        logging.error(f"Failed to create wallet: {e}")
        raise

def backup_wallet(bitbox: BitBox02, wallet_name: str):
    """
    Backup the specified wallet on the BitBox02 device.
    
    :param bitbox: An instance of the BitBox02 device.
    :param wallet_name: The name of the wallet to back up.
    :raises BitBox02Error: If the backup fails.
    """
    try:
        logging.info(f"Backing up wallet: {wallet_name}")
        backup_data = bitbox.backup_wallet(wallet_name)
        logging.info(f"Wallet '{wallet_name}' backed up successfully.")
        return backup_data
    except BitBox02Error as e:
        logging.error(f"Failed to back up wallet: {e}")
        raise

def manage_funds(bitbox: BitBox02, wallet_name: str, action: str, amount: float):
    """
    Manage funds in the specified wallet on the BitBox02 device.
    
    :param bitbox: An instance of the BitBox02 device.
    :param wallet_name: The name of the wallet to manage funds in.
    :param action: The action to perform ('deposit' or 'withdraw').
    :param amount: The amount of cryptocurrency to manage.
    :raises ValueError: If the action is invalid.
    :raises BitBox02Error: If the fund management fails.
    """
    try:
        if action not in ['deposit', 'withdraw']:
            raise ValueError("Action must be either 'deposit' or 'withdraw'.")

        logging.info(f"{action.capitalize()}ing {amount} in wallet: {wallet_name}")
        
        if action == 'deposit':
            bitbox.deposit(wallet_name, amount)
        else:  # action == 'withdraw'
            bitbox.withdraw(wallet_name, amount)

        logging.info(f"{action.capitalize()} of {amount} in wallet '{wallet_name}' completed successfully.")
    except ValueError as ve:
        logging.error(f"Invalid action: {ve}")
        raise
    except BitBox02Error as e:
        logging.error(f"Failed to {action} funds: {e}")
        raise

def main():
    """
    Main function to drive the BitBoxApp tutorial.
    """
    # Create an instance of the BitBox02 device
    bitbox = BitBox02()

    # Initialize the BitBox02 device
    initialize_bitbox(bitbox)

    # Create a new wallet
    wallet_name = "CryptoWallet"
    create_wallet(bitbox, wallet_name)

    # Backup the wallet
    backup_data = backup_wallet(bitbox, wallet_name)

    # Manage funds in the wallet
    manage_funds(bitbox, wallet_name, 'deposit', 1.0)
    manage_funds(bitbox, wallet_name, 'withdraw', 0.5)

if __name__ == "__main__":
    main()
```
