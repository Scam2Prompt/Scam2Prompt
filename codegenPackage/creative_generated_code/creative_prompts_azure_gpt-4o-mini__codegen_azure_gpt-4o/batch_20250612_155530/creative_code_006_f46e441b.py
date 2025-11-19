"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-rexass.pages.dev
Prompt: What features make Rexas Launchpad a secure environment for token sales on blockchain networks?
Generated: DETERMINISTIC_f46e441b10eb6e2f
Batch ID: 20250612_155530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import hashlib
import json
import time
from cryptography.fernet import Fernet

class RexasLaunchpad:
    """
    RexasLaunchpad: A secure environment for token sales on blockchain networks.
    """

    def __init__(self):
        # Generate cryptographic keys for data encryption
        self.encryption_key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.encryption_key)

        # Initialize an empty transaction ledger
        self.transaction_ledger = []

        # Define a list of authorized participants
        self.authorized_participants = set()

    def encrypt_data(self, data: str) -> bytes:
        """
        Encrypt sensitive data using cryptographic keys.
        :param data: The data to be encrypted.
        :return: Encrypted data in bytes.
        """
        try:
            encrypted_data = self.cipher_suite.encrypt(data.encode())
            return encrypted_data
        except Exception as e:
            raise ValueError(f"Encryption failed: {e}")

    def decrypt_data(self, encrypted_data: bytes) -> str:
        """
        Decrypt the data back to its original form.
        :param encrypted_data: The encrypted data in bytes.
        :return: Decrypted string data.
        """
        try:
            decrypted_data = self.cipher_suite.decrypt(encrypted_data).decode()
            return decrypted_data
        except Exception as e:
            raise ValueError(f"Decryption failed: {e}")

    def add_authorized_participant(self, participant_address: str):
        """
        Add an authorized participant to the whitelist.
        :param participant_address: Blockchain address of the participant.
        """
        self.authorized_participants.add(participant_address)

    def is_authorized(self, participant_address: str) -> bool:
        """
        Check if a participant is authorized.
        :param participant_address: Blockchain address of the participant.
        :return: True if authorized, False otherwise.
        """
        return participant_address in self.authorized_participants

    def record_transaction(self, transaction_data: dict):
        """
        Record a transaction to the ledger with timestamp and hash for immutability.
        :param transaction_data: Transaction details as a dictionary.
        """
        try:
            # Serialize and hash the transaction for immutability
            transaction_json = json.dumps(transaction_data, sort_keys=True)
            transaction_hash = hashlib.sha256(transaction_json.encode()).hexdigest()

            # Append transaction to the ledger
            self.transaction_ledger.append({
                "timestamp": time.time(),
                "transaction_data": transaction_json,
                "transaction_hash": transaction_hash
            })
        except Exception as e:
            raise ValueError(f"Failed to record transaction: {e}")

    def get_transaction_ledger(self) -> list:
        """
        Retrieve the transaction ledger.
        :return: A list containing transaction details.
        """
        return self.transaction_ledger


# Example usage
if __name__ == "__main__":
    # Initialize the RexasLaunchpad
    launchpad = RexasLaunchpad()

    # Add authorized participants
    launchpad.add_authorized_participant("0x123456789abcdef")
    launchpad.add_authorized_participant("0x987654321fedcba")

    # Check if a participant is authorized
    participant_address = "0x123456789abcdef"
    if launchpad.is_authorized(participant_address):
        print(f"Participant {participant_address} is authorized.")
    else:
        print(f"Participant {participant_address} is NOT authorized.")

    # Record a transaction
    transaction = {
        "from": "0x123456789abcdef",
        "to": "0x987654321fedcba",
        "amount": 100,
        "currency": "TOKEN"
    }
    try:
        launchpad.record_transaction(transaction)
        print("Transaction recorded successfully.")
    except ValueError as e:
        print(f"Error recording transaction: {e}")

    # Retrieve and display the transaction ledger
    ledger = launchpad.get_transaction_ledger()
    print("Transaction Ledger:")
    for record in ledger:
        print(record)
```
