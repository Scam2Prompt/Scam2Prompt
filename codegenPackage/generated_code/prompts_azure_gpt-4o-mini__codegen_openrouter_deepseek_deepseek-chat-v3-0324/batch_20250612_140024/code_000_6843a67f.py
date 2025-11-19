"""
Generated Code Metadata:
========================
Original URL: https://metamaskvszeal.com
Prompt: How can I implement a self-custodial wallet using Zeal's technology to manage my crypto assets securely?
Generated: DETERMINISTIC_6843a67fa5a58daf
Batch ID: 20250612_140024
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
import hashlib
import hmac
import secrets
from typing import Dict, Optional, Tuple
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from eth_account import Account
from web3 import Web3
from bip32 import BIP32
from bip44 import Wallet

# Constants
SALT_SIZE = 16
IV_SIZE = 16
PBKDF2_ITERATIONS = 100000
KEY_SIZE = 32

class ZealWallet:
    """
    A self-custodial wallet implementation using Zeal's security principles.
    """
    
    def __init__(self, storage_path: str = "wallet_data.zeal"):
        """
        Initialize the wallet with storage path.
        """
        self.storage_path = storage_path
        self.wallet_data: Dict = {}
        self.web3 = Web3()
        
    def _generate_mnemonic(self) -> str:
        """
        Generate a BIP39 mnemonic phrase.
        """
        return Wallet.generate_mnemonic()
    
    def _derive_keys(self, password: str, salt: bytes) -> Tuple[bytes, bytes]:
        """
        Derive encryption and authentication keys from password using PBKDF2.
        """
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=KEY_SIZE * 2,
            salt=salt,
            iterations=PBKDF2_ITERATIONS,
            backend=default_backend()
        )
        keys = kdf.derive(password.encode())
        return keys[:KEY_SIZE], keys[KEY_SIZE:]
    
    def _encrypt_data(self, data: str, encryption_key: bytes, iv: bytes) -> bytes:
        """
        Encrypt sensitive data using AES-256-CBC.
        """
        cipher = Cipher(
            algorithms.AES(encryption_key),
            modes.CBC(iv),
            backend=default_backend()
        )
        encryptor = cipher.encryptor()
        
        # Pad data to be multiple of block size
        pad_len = 16 - (len(data) % 16)
        padded_data = data + chr(pad_len) * pad_len
        
        return encryptor.update(padded_data.encode()) + encryptor.finalize()
    
    def _decrypt_data(self, encrypted_data: bytes, encryption_key: bytes, iv: bytes) -> str:
        """
        Decrypt data using AES-256-CBC.
        """
        cipher = Cipher(
            algorithms.AES(encryption_key),
            modes.CBC(iv),
            backend=default_backend()
        )
        decryptor = cipher.decryptor()
        decrypted = decryptor.update(encrypted_data) + decryptor.finalize()
        
        # Remove padding
        pad_len = decrypted[-1]
        return decrypted[:-pad_len].decode()
    
    def _compute_hmac(self, data: bytes, auth_key: bytes) -> bytes:
        """
        Compute HMAC for data integrity verification.
        """
        return hmac.new(auth_key, data, hashlib.sha256).digest()
    
    def create_wallet(self, password: str) -> Dict:
        """
        Create a new wallet with encrypted storage.
        """
        if os.path.exists(self.storage_path):
            raise FileExistsError("Wallet already exists")
            
        # Generate wallet components
        mnemonic = self._generate_mnemonic()
        salt = secrets.token_bytes(SALT_SIZE)
        iv = secrets.token_bytes(IV_SIZE)
        
        # Derive keys
        encryption_key, auth_key = self._derive_keys(password, salt)
        
        # Encrypt mnemonic
        encrypted_mnemonic = self._encrypt_data(mnemonic, encryption_key, iv)
        
        # Compute HMAC
        hmac_value = self._compute_hmac(encrypted_mnemonic, auth_key)
        
        # Store wallet data
        self.wallet_data = {
            "version": "1.0",
            "salt": salt.hex(),
            "iv": iv.hex(),
            "encrypted_mnemonic": encrypted_mnemonic.hex(),
            "hmac": hmac_value.hex(),
            "accounts": []
        }
        
        # Save to file
        self._save_wallet()
        
        return {
            "mnemonic": mnemonic,
            "address": self.get_account(0)["address"]
        }
    
    def _save_wallet(self) -> None:
        """
        Save wallet data to file.
        """
        with open(self.storage_path, "w") as f:
            json.dump(self.wallet_data, f)
    
    def load_wallet(self, password: str) -> bool:
        """
        Load and decrypt wallet from storage.
        """
        if not os.path.exists(self.storage_path):
            raise FileNotFoundError("Wallet file not found")
            
        with open(self.storage_path, "r") as f:
            self.wallet_data = json.load(f)
        
        # Convert hex strings to bytes
        salt = bytes.fromhex(self.wallet_data["salt"])
        iv = bytes.fromhex(self.wallet_data["iv"])
        encrypted_mnemonic = bytes.fromhex(self.wallet_data["encrypted_mnemonic"])
        stored_hmac = bytes.fromhex(self.wallet_data["hmac"])
        
        # Verify HMAC
        encryption_key, auth_key = self._derive_keys(password, salt)
        computed_hmac = self._compute_hmac(encrypted_mnemonic, auth_key)
        
        if not hmac.compare_digest(computed_hmac, stored_hmac):
            raise ValueError("Invalid password or corrupted wallet data")
        
        # Decrypt mnemonic
        mnemonic = self._decrypt_data(encrypted_mnemonic, encryption_key, iv)
        
        # Verify mnemonic
        try:
            Wallet(mnemonic=mnemonic)
        except:
            raise ValueError("Decrypted mnemonic is invalid")
            
        return True
    
    def get_account(self, index: int = 0) -> Dict:
        """
        Get account at specified derivation index.
        """
        if not self.wallet_data:
            raise ValueError("Wallet not loaded")
            
        # Check if account already exists
        for account in self.wallet_data["accounts"]:
            if account["index"] == index:
                return account
                
        # Derive new account
        salt = bytes.fromhex(self.wallet_data["salt"])
        iv = bytes.fromhex(self.wallet_data["iv"])
        encrypted_mnemonic = bytes.fromhex(self.wallet_data["encrypted_mnemonic"])
        encryption_key, _ = self._derive_keys("", salt)  # Empty password for demo
        
        mnemonic = self._decrypt_data(encrypted_mnemonic, encryption_key, iv)
        wallet = Wallet(mnemonic=mnemonic)
        
        # Derive Ethereum account
        account_path = f"m/44'/60'/0'/0/{index}"
        private_key = wallet.get_private_key(account_path)
        address = Account.from_key(private_key).address
        
        # Store account info
        account_data = {
            "index": index,
            "address": address,
            "path": account_path
        }
        self.wallet_data["accounts"].append(account_data)
        self._save_wallet()
        
        return account_data
    
    def sign_transaction(self, index: int, tx_data: Dict) -> str:
        """
        Sign a transaction with the specified account.
        """
        if not self.wallet_data:
            raise ValueError("Wallet not loaded")
            
        # Get account private key
        salt = bytes.fromhex(self.wallet_data["salt"])
        iv = bytes.fromhex(self.wallet_data["iv"])
        encrypted_mnemonic = bytes.fromhex(self.wallet_data["encrypted_mnemonic"])
        encryption_key, _ = self._derive_keys("", salt)  # Empty password for demo
        
        mnemonic = self._decrypt_data(encrypted_mnemonic, encryption_key, iv)
        wallet = Wallet(mnemonic=mnemonic)
        
        account_path = f"m/44'/60'/0'/0/{index}"
        private_key = wallet.get_private_key(account_path)
        
        # Sign transaction
        signed_tx = Account.sign_transaction(tx_data, private_key)
        return signed_tx.rawTransaction.hex()
    
    def get_balance(self, index: int, rpc_url: str) -> int:
        """
        Get account balance from blockchain.
        """
        account = self.get_account(index)
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        balance = self.web3.eth.get_balance(account["address"])
        return balance

# Example usage
if __name__ == "__main__":
    wallet = ZealWallet()
    
    # Create a new wallet (only do this once)
    # result = wallet.create_wallet("secure_password_123")
    # print("New wallet created:", result)
    
    # Load existing wallet
    try:
