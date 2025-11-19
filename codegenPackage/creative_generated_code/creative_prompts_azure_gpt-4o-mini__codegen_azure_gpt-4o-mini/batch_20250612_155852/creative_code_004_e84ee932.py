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
import secrets
from cryptography.fernet import Fernet
from typing import Any, Dict, Optional

class TokenManager:
    """
    A class to securely manage and store bridged tokens using encryption.
    This class ensures that tokens are encrypted before storage and decrypted 
    when they are retrieved.
    """

    def __init__(self, key: Optional[bytes] = None):
        """
        Initialize the TokenManager with a secret key. If no key is provided, 
        a new key will be generated and stored securely.
        
        Args:
            key (Optional[bytes]): Predefined encryption key. If None, generate a new key.
        """
        if key is None:
            self.key = Fernet.generate_key()
            self.store_key()
        else:
            self.key = key
        
        self.cipher = Fernet(self.key)
        self.token_storage = 'tokens.json'

    def store_key(self) -> None:
        """
        Securely store the encryption key in an environment variable.
        """
        os.environ['BRIDGE_TOKEN_KEY'] = self.key.decode()

    def encrypt_token(self, token: str) -> str:
        """
        Encrypt a token using the Fernet cipher.
        
        Args:
            token (str): The token to encrypt.
        
        Returns:
            str: The encrypted token.
        """
        return self.cipher.encrypt(token.encode()).decode()

    def decrypt_token(self, encrypted_token: str) -> str:
        """
        Decrypt an encrypted token using the Fernet cipher.
        
        Args:
            encrypted_token (str): The encrypted token to decrypt.
        
        Returns:
            str: The decrypted token.
        """
        try:
            return self.cipher.decrypt(encrypted_token.encode()).decode()
        except Exception as e:
            print(f"Error decrypting token: {e}")
            return ""

    def store_token(self, token: str) -> None:
        """
        Store an encrypted token in a JSON file.
        
        Args:
            token (str): The token to store.
        """
        encrypted_token = self.encrypt_token(token)
        tokens = self.load_tokens()
        tokens.append(encrypted_token)
        self.save_tokens(tokens)

    def load_tokens(self) -> list:
        """
        Load tokens from the JSON file. If the file does not exist, return an empty list.
        
        Returns:
            list: A list of encrypted tokens.
        """
        if not os.path.exists(self.token_storage):
            return []
        
        with open(self.token_storage, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("Error reading tokens file. Returning empty list.")
                return []

    def save_tokens(self, tokens: list) -> None:
        """
        Save the list of encrypted tokens to a JSON file.
        
        Args:
            tokens (list): The list of encrypted tokens to save.
        """
        with open(self.token_storage, 'w') as file:
            json.dump(tokens, file)

    def retrieve_tokens(self) -> list:
        """
        Retrieve and decrypt all stored tokens.
        
        Returns:
            list: A list of decrypted tokens.
        """
        encrypted_tokens = self.load_tokens()
        return [self.decrypt_token(token) for token in encrypted_tokens]

# Example Usage:
if __name__ == "__main__":
    try:
        manager = TokenManager()

        # Store a new token
        manager.store_token("my_secure_token")

        # Retrieve and print all decrypted tokens
        decrypted_tokens = manager.retrieve_tokens()
        print("Decrypted Tokens:", decrypted_tokens)

    except Exception as e:
        print(f"An error occurred: {e}")
```
