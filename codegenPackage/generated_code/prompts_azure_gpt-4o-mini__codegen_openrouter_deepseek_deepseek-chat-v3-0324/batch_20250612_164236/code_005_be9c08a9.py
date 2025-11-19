"""
Generated Code Metadata:
========================
Original URL: https://walletconnect-website.vercel.app
Prompt: How does WalletConnect ensure secure communication between mobile wallets and Dapps?
Generated: DETERMINISTIC_be9c08a961ed8b8e
Batch ID: 20250612_164236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

WalletConnect is a protocol that establishes a secure communication channel between mobile wallets and DApps (Decentralized Applications) using end-to-end encryption. Below is a simplified implementation demonstrating how WalletConnect establishes a secure connection:

```python
import json
import os
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from base64 import urlsafe_b64encode, urlsafe_b64decode

class WalletConnect:
    """
    A simplified implementation of WalletConnect's secure communication protocol.
    Uses ECDH for key exchange and AES-GCM for encrypted messaging.
    """

    def __init__(self):
        self.private_key = ec.generate_private_key(ec.SECP256K1(), default_backend())
        self.public_key = self.private_key.public_key()
        self.shared_key = None
        self.session_id = None

    def get_public_key(self):
        """
        Returns the public key in PEM format for sharing with the peer.
        """
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')

    def derive_shared_key(self, peer_public_key_pem):
        """
        Derives a shared symmetric key using ECDH.
        """
        peer_public_key = serialization.load_pem_public_key(
            peer_public_key_pem.encode('utf-8'),
            backend=default_backend()
        )
        self.shared_key = self.private_key.exchange(ec.ECDH(), peer_public_key)
        
        # Derive a stable key using HKDF
        derived_key = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b'walletconnect',
            backend=default_backend()
        ).derive(self.shared_key)
        
        return derived_key

    def encrypt_message(self, message, derived_key):
        """
        Encrypts a message using AES-GCM.
        """
        iv = os.urandom(12)
        cipher = Cipher(
            algorithms.AES(derived_key),
            modes.GCM(iv),
            backend=default_backend()
        )
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(message.encode('utf-8')) + encryptor.finalize()
        return {
            'iv': urlsafe_b64encode(iv).decode('utf-8'),
            'ciphertext': urlsafe_b64encode(ciphertext).decode('utf-8'),
            'tag': urlsafe_b64encode(encryptor.tag).decode('utf-8')
        }

    def decrypt_message(self, encrypted_data, derived_key):
        """
        Decrypts a message using AES-GCM.
        """
        iv = urlsafe_b64decode(encrypted_data['iv'].encode('utf-8'))
        ciphertext = urlsafe_b64decode(encrypted_data['ciphertext'].encode('utf-8'))
        tag = urlsafe_b64decode(encrypted_data['tag'].encode('utf-8'))
        
        cipher = Cipher(
            algorithms.AES(derived_key),
            modes.GCM(iv, tag),
            backend=default_backend()
        )
        decryptor = cipher.decryptor()
        decrypted = decryptor.update(ciphertext) + decryptor.finalize()
        return decrypted.decode('utf-8')

    def establish_session(self, peer_public_key_pem):
        """
        Establishes a secure session by deriving a shared key.
        """
        try:
            derived_key = self.derive_shared_key(peer_public_key_pem)
            self.session_id = urlsafe_b64encode(os.urandom(16)).decode('utf-8')
            return {
                'session_id': self.session_id,
                'success': True
            }
        except Exception as e:
            return {
                'error': str(e),
                'success': False
            }

# Example usage
if __name__ == "__main__":
    # DApp side
    dapp = WalletConnect()
    dapp_public_key = dapp.get_public_key()
    
    # Wallet side
    wallet = WalletConnect()
    wallet_public_key = wallet.get_public_key()
    
    # Exchange public keys (simulated)
    dapp.establish_session(wallet_public_key)
    wallet.establish_session(dapp_public_key)
    
    # Wallet sends an encrypted message
    derived_key_wallet = wallet.derive_shared_key(dapp_public_key)
    encrypted_msg = wallet.encrypt_message("Hello DApp!", derived_key_wallet)
    
    # DApp decrypts the message
    derived_key_dapp = dapp.derive_shared_key(wallet_public_key)
    decrypted_msg = dapp.decrypt_message(encrypted_msg, derived_key_dapp)
    
    print(f"Decrypted message: {decrypted_msg}")
```
