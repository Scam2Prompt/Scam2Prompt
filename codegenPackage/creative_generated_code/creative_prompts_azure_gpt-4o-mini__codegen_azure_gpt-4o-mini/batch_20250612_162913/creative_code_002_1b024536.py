"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atomic-wallet.fr
Prompt: Generate a code snippet that demonstrates how to backup and restore a wallet using the backup phrase feature of Atomic Wallet.
Generated: DETERMINISTIC_1b02453623bf07ff
Batch ID: 20250612_162913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import hashlib

class WalletBackup:
    """Class to handle the backup and restoration of a wallet using a backup phrase."""

    def __init__(self, wallet_file):
        """
        Initializes the WalletBackup instance.
        
        :param wallet_file: str, path to the wallet file that contains the backup phrase.
        """
        self.wallet_file = wallet_file

    def _hash_phrase(self, phrase):
        """
        Hashes the backup phrase for secure storage.
        
        :param phrase: str, the backup phrase to hash.
        :return: str, the hashed backup phrase.
        """
        return hashlib.sha256(phrase.encode()).hexdigest()

    def backup_wallet(self, phrase):
        """
        Saves the backup phrase to a file securely.
        
        :param phrase: str, the backup phrase to save.
        :raises IOError: if the backup process fails.
        """
        try:
            hashed_phrase = self._hash_phrase(phrase)
            with open(self.wallet_file, 'w') as f:
                json.dump({'backup_phrase': hashed_phrase}, f)
            print("Wallet backup successful.")
        except IOError as e:
            print(f"Error during wallet backup: {e}")
            raise

    def restore_wallet(self):
        """
        Restores the wallet using the backup phrase from the file.
        
        :return: str, the hashed backup phrase if restoration is successful.
        :raises IOError: if the restoration process fails.
        :raises ValueError: if the backup file is not found or is invalid.
        """
        if not os.path.exists(self.wallet_file):
            raise ValueError("Backup file does not exist.")

        try:
            with open(self.wallet_file, 'r') as f:
                data = json.load(f)
            if 'backup_phrase' not in data:
                raise ValueError("Invalid backup file format.")
            print("Wallet restoration successful.")
            return data['backup_phrase']
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error during wallet restoration: {e}")
            raise

# Example usage:
if __name__ == "__main__":
    wallet_backup = WalletBackup("wallet_backup.json")

    # Backing up the wallet
    backup_phrase = "your recovery phrase goes here"
    wallet_backup.backup_wallet(backup_phrase)

    # Restoring the wallet
    try:
        restored_phrase = wallet_backup.restore_wallet()
        print(f"Restored backup phrase hash: {restored_phrase}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
