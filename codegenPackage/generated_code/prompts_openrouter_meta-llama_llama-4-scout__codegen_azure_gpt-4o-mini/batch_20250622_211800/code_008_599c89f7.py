"""
Generated Code Metadata:
========================
Original URL: https://yfyuyyufy.pages.dev
Prompt: Design a system to securely manage node(s) and track rewards on the World Mobile network using a non-custodial vault, and explain the benefits of using such a system.
Generated: DETERMINISTIC_599c89f7d52c93eb
Batch ID: 20250622_211800
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
import hashlib
import hmac
import base64
from cryptography.fernet import Fernet
from typing import Dict, Any, Optional

class NonCustodialVault:
    """
    A class to manage nodes and track rewards on the World Mobile network using a non-custodial vault.
    This class provides methods to securely store, retrieve, and manage sensitive information.
    """

    def __init__(self, vault_file: str, encryption_key: Optional[bytes] = None):
        """
        Initializes the NonCustodialVault with a specified file for storage and an optional encryption key.
        
        :param vault_file: Path to the file where the vault data will be stored.
        :param encryption_key: Optional key for encrypting the vault data. If not provided, a new key will be generated.
        """
        self.vault_file = vault_file
        self.encryption_key = encryption_key or Fernet.generate_key()
        self.cipher = Fernet(self.encryption_key)
        self.data = self.load_vault()

    def load_vault(self) -> Dict[str, Any]:
        """
        Loads the vault data from the specified file. If the file does not exist, returns an empty dictionary.
        
        :return: A dictionary containing the vault data.
        """
        if os.path.exists(self.vault_file):
            with open(self.vault_file, 'rb') as file:
                encrypted_data = file.read()
                decrypted_data = self.cipher.decrypt(encrypted_data)
                return json.loads(decrypted_data)
        return {}

    def save_vault(self) -> None:
        """
        Saves the current vault data to the specified file in an encrypted format.
        """
        with open(self.vault_file, 'wb') as file:
            encrypted_data = self.cipher.encrypt(json.dumps(self.data).encode())
            file.write(encrypted_data)

    def add_node(self, node_id: str, rewards: float) -> None:
        """
        Adds a new node to the vault with its associated rewards.
        
        :param node_id: Unique identifier for the node.
        :param rewards: Initial rewards associated with the node.
        """
        if node_id in self.data:
            raise ValueError(f"Node ID '{node_id}' already exists.")
        self.data[node_id] = {'rewards': rewards}
        self.save_vault()

    def update_rewards(self, node_id: str, amount: float) -> None:
        """
        Updates the rewards for a specified node.
        
        :param node_id: Unique identifier for the node.
        :param amount: Amount to add to the current rewards.
        """
        if node_id not in self.data:
            raise KeyError(f"Node ID '{node_id}' not found.")
        self.data[node_id]['rewards'] += amount
        self.save_vault()

    def get_rewards(self, node_id: str) -> float:
        """
        Retrieves the current rewards for a specified node.
        
        :param node_id: Unique identifier for the node.
        :return: Current rewards associated with the node.
        """
        if node_id not in self.data:
            raise KeyError(f"Node ID '{node_id}' not found.")
        return self.data[node_id]['rewards']

    def generate_signature(self, data: str, secret: str) -> str:
        """
        Generates a HMAC signature for the given data using the provided secret.
        
        :param data: The data to sign.
        :param secret: The secret key used for signing.
        :return: The generated HMAC signature as a base64 encoded string.
        """
        signature = hmac.new(secret.encode(), data.encode(), hashlib.sha256).digest()
        return base64.b64encode(signature).decode()

# Example usage
if __name__ == "__main__":
    vault = NonCustodialVault('vault.json')

    # Adding a new node
    try:
        vault.add_node('node_1', 100.0)
        print("Node added successfully.")
    except ValueError as e:
        print(f"Error: {e}")

    # Updating rewards
    try:
        vault.update_rewards('node_1', 50.0)
        print("Rewards updated successfully.")
    except KeyError as e:
        print(f"Error: {e}")

    # Retrieving rewards
    try:
        rewards = vault.get_rewards('node_1')
        print(f"Current rewards for node_1: {rewards}")
    except KeyError as e:
        print(f"Error: {e}")
```
