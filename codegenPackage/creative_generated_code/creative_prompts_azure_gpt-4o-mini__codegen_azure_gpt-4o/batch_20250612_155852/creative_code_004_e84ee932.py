"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bridgetensor.org
Prompt: Illustrate how to securely store and manage bridged tokens using the guidelines from BridgeTensor, focusing on minimizing risks associated with the bridge and underlying keys.
Generated: DETERMINISTIC_e84ee9320a191c04
Batch ID: 20250612_155852
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
from cryptography.fernet import Fernet
from typing import Dict, Optional

# Generate and securely store a symmetric encryption key
# In production, store this key in a secure location, such as an HSM or a secrets manager.
def generate_encryption_key() -> bytes:
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)
    return key

# Load encryption key from a secure location
def load_encryption_key() -> bytes:
    if not os.path.exists("encryption_key.key"):
        raise FileNotFoundError("Encryption key file is missing.")
    with open("encryption_key.key", "rb") as key_file:
        return key_file.read()

# Encrypt sensitive token data
def encrypt_data(data: str, key: bytes) -> str:
    fernet = Fernet(key)
    return fernet.encrypt(data.encode()).decode()

# Decrypt sensitive token data
def decrypt_data(encrypted_data: str, key: bytes) -> str:
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data.encode()).decode()

# Secure storage and management of bridged tokens
class TokenBridgeManager:
    def __init__(self, storage_file: str):
        self.storage_file = storage_file
        self.encryption_key = load_encryption_key()
        self.token_storage: Dict[str, str] = self._load_tokens()

    # Load tokens from secure storage
    def _load_tokens(self) -> Dict[str, str]:
        if not os.path.exists(self.storage_file):
            return {}
        with open(self.storage_file, "r") as file:
            encrypted_data = file.read()
        try:
            decrypted_data = decrypt_data(encrypted_data, self.encryption_key)
            return json.loads(decrypted_data)
        except Exception as e:
            raise ValueError("Failed to load and decrypt token storage.") from e

    # Save tokens securely to the storage file
    def _save_tokens(self):
        encrypted_data = encrypt_data(json.dumps(self.token_storage), self.encryption_key)
        with open(self.storage_file, "w") as file:
            file.write(encrypted_data)

    # Add a new bridged token securely
    def add_token(self, token_id: str, token_data: str):
        if token_id in self.token_storage:
            raise ValueError(f"Token ID '{token_id}' already exists.")
        self.token_storage[token_id] = self._secure_hash(token_data)
        self._save_tokens()

    # Retrieve a bridged token
    def get_token(self, token_id: str) -> Optional[str]:
        return self.token_storage.get(token_id)

    # Remove a bridged token securely
    def remove_token(self, token_id: str):
        if token_id not in self.token_storage:
            raise ValueError(f"Token ID '{token_id}' does not exist.")
        del self.token_storage[token_id]
        self._save_tokens()

    # Securely hash token data for integrity
    @staticmethod
    def _secure_hash(data: str) -> str:
        return hashlib.sha256(data.encode()).hexdigest()

# Usage example
if __name__ == "__main__":
    try:
        # Initialize manager with storage file path
        manager = TokenBridgeManager("token_storage.json")

        # Add a new token
        manager.add_token("token_123", "example_token_data")

        # Retrieve a token
        token = manager.get_token("token_123")
        print(f"Retrieved token hash: {token}")

        # Remove a token
        manager.remove_token("token_123")
        print("Token removed successfully.")
    except Exception as error:
        print(f"An error occurred: {error}")
```
