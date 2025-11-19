"""
Generated Code Metadata:
========================
Original URL: https://id.stromkonto.net
Prompt: Create a Python script to export and import device keys securely, as described in Stromkonto's documentation, with functionality for password encryption.
Generated: DETERMINISTIC_67a1495901dc4897
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import base64
import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from typing import Dict, Optional, Tuple

class DeviceKeyManager:
    """
    A class to securely export and import device keys with password encryption.
    """
    
    def __init__(self, salt: bytes = None):
        """
        Initialize the DeviceKeyManager with an optional salt.
        If no salt is provided, a random one will be generated.
        """
        self.salt = salt if salt else os.urandom(16)
    
    def _derive_key(self, password: str) -> bytes:
        """
        Derive a cryptographic key from the password using PBKDF2.
        """
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
        )
        return base64.urlsafe_b64encode(kdf.derive(password.encode()))
    
    def encrypt_keys(self, keys: Dict, password: str) -> str:
        """
        Encrypt device keys with the provided password.
        
        Args:
            keys: Dictionary containing device keys to encrypt
            password: Password used for encryption
            
        Returns:
            Base64 encoded string containing salt and encrypted data
        """
        key = self._derive_key(password)
        f = Fernet(key)
        encrypted_data = f.encrypt(json.dumps(keys).encode())
        
        # Combine salt and encrypted data for storage
        combined = self.salt + encrypted_data
        return base64.urlsafe_b64encode(combined).decode()
    
    def decrypt_keys(self, encrypted_data: str, password: str) -> Dict:
        """
        Decrypt device keys with the provided password.
        
        Args:
            encrypted_data: Base64 encoded string containing salt and encrypted data
            password: Password used for decryption
            
        Returns:
            Decrypted device keys as a dictionary
            
        Raises:
            ValueError: If decryption fails (invalid password or corrupted data)
        """
        try:
            combined = base64.urlsafe_b64decode(encrypted_data.encode())
            salt = combined[:16]
            encrypted_keys = combined[16:]
            
            # Reinitialize with the stored salt
            self.salt = salt
            key = self._derive_key(password)
            
            f = Fernet(key)
            decrypted_data = f.decrypt(encrypted_keys)
            return json.loads(decrypted_data.decode())
        except Exception as e:
            raise ValueError("Decryption failed. Invalid password or corrupted data.") from e
    
    @staticmethod
    def generate_key_pair() -> Tuple[str, str]:
        """
        Generate a new pair of device keys (public and private).
        
        Returns:
            Tuple of (public_key, private_key) as base64 encoded strings
        """
        private_key = base64.urlsafe_b64encode(os.urandom(32)).decode()
        public_key = hashlib.sha256(private_key.encode()).hexdigest()
        return public_key, private_key

# Example usage
if __name__ == "__main__":
    try:
        # Initialize key manager
        key_manager = DeviceKeyManager()
        
        # Generate sample keys
        public_key, private_key = key_manager.generate_key_pair()
        keys = {
            "public_key": public_key,
            "private_key": private_key,
            "device_id": "example_device_123"
        }
        
        # Export (encrypt) keys
        password = "secure_password_123"
        encrypted = key_manager.encrypt_keys(keys, password)
        print(f"Encrypted keys: {encrypted}")
        
        # Import (decrypt) keys
        decrypted = key_manager.decrypt_keys(encrypted, password)
        print(f"Decrypted keys: {decrypted}")
        
        # Test with wrong password
        try:
            key_manager.decrypt_keys(encrypted, "wrong_password")
        except ValueError as e:
            print(f"Expected error with wrong password: {e}")
            
    except Exception as e:
        print(f"Error: {e}")
```
