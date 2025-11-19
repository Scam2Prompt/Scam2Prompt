"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tenon-restore.pages.dev
Prompt: How can I create a multi-asset cryptocurrency wallet that supports Bitcoin and Ethereum while ensuring secure access and management?
Generated: DETERMINISTIC_83619b7509d3e7fc
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code for a simple multi-asset cryptocurrency wallet supporting Bitcoin and Ethereum. It uses libraries like `cryptography` for encryption and `ecdsa` for key generation. Ensure you install required libraries (`pip install cryptography ecdsa`) before running this code.

```python
import os
import json
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidKey
from ecdsa import SigningKey, SECP256k1

class MultiAssetCryptoWallet:
    def __init__(self, wallet_file="wallet.json", encryption_password=None):
        """
        Initialize the wallet. Create or load an encrypted wallet file.
        :param wallet_file: Path to wallet JSON file
        :param encryption_password: Password for encrypting/decrypting the wallet
        """
        self.wallet_file = wallet_file
        self.encryption_password = encryption_password
        self.wallet_data = {"Bitcoin": None, "Ethereum": None}
        self.key = None

        # If wallet file exists, decrypt and load data
        if os.path.exists(self.wallet_file):
            self._load_wallet()
        else:
            self._generate_keys()
            self._save_wallet()

    def _derive_key(self, password):
        """Derive an AES key using PBKDF2."""
        salt = b"unique_salt"
        kdf = PBKDF2HMAC(
            algorithm=SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        return kdf.derive(password.encode())

    def _encrypt_data(self, data):
        """Encrypt data using AES."""
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_data = iv + encryptor.update(data.encode()) + encryptor.finalize()
        return encrypted_data

    def _decrypt_data(self, encrypted_data):
        """Decrypt AES encrypted data."""
        iv = encrypted_data[:16]
        cipher = Cipher(algorithms.AES(self.key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(encrypted_data[16:]) + decryptor.finalize()
        return decrypted_data.decode()

    def _generate_keys(self):
        """Generate private keys for supported cryptocurrencies."""
        # Generate Bitcoin private key
        bitcoin_private_key = SigningKey.generate(curve=SECP256k1)
        self.wallet_data["Bitcoin"] = bitcoin_private_key.to_pem().decode()

        # Generate Ethereum private key (reuse same curve for simplicity)
        ethereum_private_key = SigningKey.generate(curve=SECP256k1)
        self.wallet_data["Ethereum"] = ethereum_private_key.to_pem().decode()

    def _save_wallet(self):
        """Encrypt and save wallet data to file."""
        if not self.encryption_password:
            raise ValueError("Encryption password is required to save the wallet securely.")
        
        self.key = self._derive_key(self.encryption_password)
        encrypted_data = self._encrypt_data(json.dumps(self.wallet_data))
        with open(self.wallet_file, "wb") as file:
            file.write(encrypted_data)

    def _load_wallet(self):
        """Load and decrypt wallet data from file."""
        if not self.encryption_password:
            raise ValueError("Encryption password is required to load the wallet securely.")

        self.key = self._derive_key(self.encryption_password)
        with open(self.wallet_file, "rb") as file:
            encrypted_data = file.read()
        
        try:
            decrypted_data = self._decrypt_data(encrypted_data)
            self.wallet_data = json.loads(decrypted_data)
        except InvalidKey:
            raise ValueError("Failed to decrypt wallet data. Incorrect password.")

    def get_private_key(self, asset):
        """
        Retrieve private key for a specific cryptocurrency.
        :param asset: Cryptocurrency name (e.g., 'Bitcoin', 'Ethereum')
        :return: Private key string or None if asset is unsupported
        """
        return self.wallet_data.get(asset, None)

    def add_custom_asset(self, asset_name):
        """
        Add a custom cryptocurrency asset to the wallet.
        :param asset_name: Name of the cryptocurrency asset
        """
        private_key = SigningKey.generate(curve=SECP256k1).to_pem().decode()
        self.wallet_data[asset_name] = private_key
        self._save_wallet()


# Example usage of the MultiAssetCryptoWallet class
def main():
    try:
        # Create or load a wallet with encryption password
        wallet = MultiAssetCryptoWallet(encryption_password="secure_password")
        
        # Fetch Bitcoin private key
        bitcoin_key = wallet.get_private_key("Bitcoin")
        print("Bitcoin Private Key:", bitcoin_key)

        # Fetch Ethereum private key
        ethereum_key = wallet.get_private_key("Ethereum")
        print("Ethereum Private Key:", ethereum_key)

        # Add a custom cryptocurrency asset
        wallet.add_custom_asset("Litecoin")
        litecoin_key = wallet.get_private_key("Litecoin")
        print("Litecoin Private Key:", litecoin_key)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
