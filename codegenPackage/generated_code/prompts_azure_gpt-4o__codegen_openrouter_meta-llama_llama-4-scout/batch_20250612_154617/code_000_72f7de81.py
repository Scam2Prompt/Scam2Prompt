"""
Generated Code Metadata:
========================
Original URL: https://digitalbitbox.com
Prompt: Write Python code to interact with the BitBox02 hardware wallet using its open-source API for securely managing Bitcoin transactions. Include features like multisig account registration and microSD card backup.
Generated: DETERMINISTIC_72f7de817aa07582
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import json
from bitbox02 import BitBox02

class BitBox02Client:
    def __init__(self, device_path):
        """
        Initialize the BitBox02 client.

        Args:
            device_path (str): The path to the BitBox02 device.
        """
        self.device_path = device_path
        self.bitbox02 = BitBox02(device_path)

    def connect(self):
        """
        Connect to the BitBox02 device.

        Returns:
            bool: True if connected, False otherwise.
        """
        try:
            self.bitbox02.connect()
            return True
        except Exception as e:
            print(f"Error connecting to device: {e}")
            return False

    def disconnect(self):
        """
        Disconnect from the BitBox02 device.
        """
        self.bitbox02.disconnect()

    def get_device_info(self):
        """
        Get information about the BitBox02 device.

        Returns:
            dict: Device information.
        """
        return self.bitbox02.get_device_info()

    def register_multisig_account(self, account_name, xpubs, threshold):
        """
        Register a multisig account.

        Args:
            account_name (str): The name of the account.
            xpubs (list): A list of xpubs.
            threshold (int): The threshold for the multisig account.

        Returns:
            bool: True if registered, False otherwise.
        """
        try:
            self.bitbox02.register_multisig_account(account_name, xpubs, threshold)
            return True
        except Exception as e:
            print(f"Error registering multisig account: {e}")
            return False

    def backup_microsd(self, backup_password):
        """
        Backup the wallet to microSD card.

        Args:
            backup_password (str): The password for the backup.

        Returns:
            bool: True if backed up, False otherwise.
        """
        try:
            self.bitbox02.backup_microsd(backup_password)
            return True
        except Exception as e:
            print(f"Error backing up to microSD: {e}")
            return False

    def sign_transaction(self, tx_hex, account_name):
        """
        Sign a transaction.

        Args:
            tx_hex (str): The transaction hex.
            account_name (str): The name of the account.

        Returns:
            str: The signed transaction hex.
        """
        try:
            return self.bitbox02.sign_transaction(tx_hex, account_name)
        except Exception as e:
            print(f"Error signing transaction: {e}")
            return None

def main():
    device_path = "/path/to/bitbox02"  # Replace with the actual device path
    client = BitBox02Client(device_path)

    if client.connect():
        print("Connected to device")
        device_info = client.get_device_info()
        print(json.dumps(device_info, indent=4))

        # Register multisig account
        account_name = "my_multisig_account"
        xpubs = ["xpub...", "xpub..."]  # Replace with actual xpubs
        threshold = 2
        if client.register_multisig_account(account_name, xpubs, threshold):
            print("Multisig account registered")

        # Backup to microSD
        backup_password = "my_backup_password"  # Replace with actual backup password
        if client.backup_microsd(backup_password):
            print("Backed up to microSD")

        # Sign transaction
        tx_hex = "tx_hex..."  # Replace with actual transaction hex
        signed_tx_hex = client.sign_transaction(tx_hex, account_name)
        if signed_tx_hex:
            print("Signed transaction hex:", signed_tx_hex)

        client.disconnect()
    else:
        print("Failed to connect to device")

if __name__ == "__main__":
    main()
```
