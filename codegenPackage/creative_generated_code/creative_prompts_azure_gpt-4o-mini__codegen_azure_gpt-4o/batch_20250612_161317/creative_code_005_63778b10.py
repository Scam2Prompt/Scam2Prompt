"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blurunft.github.io
Prompt: Create a function to transfer private NFTs between wallets without revealing transaction data, inspired by the Blur Network's approach.
Generated: DETERMINISTIC_63778b101c0bc15f
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def transfer_private_nft(sender_private_key_pem, receiver_public_key_pem, nft_metadata):
    """
    Transfer a private NFT between wallets without revealing transaction data.

    :param sender_private_key_pem: PEM-encoded private key of the sender
    :param receiver_public_key_pem: PEM-encoded public key of the receiver
    :param nft_metadata: Dictionary containing the NFT metadata
    :return: Encrypted transaction data
    """
    try:
        # Load sender's private key
        sender_private_key = serialization.load_pem_private_key(
            sender_private_key_pem,
            password=None
        )
        
        # Load receiver's public key
        receiver_public_key = serialization.load_pem_public_key(
            receiver_public_key_pem
        )

        # Serialize NFT metadata to JSON
        nft_data_json = json.dumps(nft_metadata)

        # Generate a random AES key for encryption
        aes_key = os.urandom(32)  # 256-bit AES key
        aes_iv = os.urandom(16)   # 128-bit IV for AES

        # Encrypt NFT data using AES
        cipher = Cipher(algorithms.AES(aes_key), modes.CFB(aes_iv))
        encryptor = cipher.encryptor()
        encrypted_nft_data = encryptor.update(nft_data_json.encode()) + encryptor.finalize()

        # Encrypt AES key using receiver's public key
        encrypted_aes_key = receiver_public_key.encrypt(
            aes_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        # Sign the encrypted NFT data using sender's private key
        signature = sender_private_key.sign(
            encrypted_nft_data,
            padding.PSS(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        # Prepare the transaction payload
        transaction_payload = {
            "encrypted_nft_data": encrypted_nft_data.hex(),
            "encrypted_aes_key": encrypted_aes_key.hex(),
            "aes_iv": aes_iv.hex(),
            "signature": signature.hex()
        }

        # Return encrypted transaction data
        return transaction_payload

    except Exception as e:
        # Handle errors gracefully
        raise RuntimeError(f"Error occurred during NFT transfer: {str(e)}")

# Example Usage:
# sender_private_key_pem = ... (Load sender's private key PEM as bytes)
# receiver_public_key_pem = ... (Load receiver's public key PEM as bytes)
# nft_metadata = {"token_id": "12345", "owner": "sender_wallet_address"}
# encrypted_transaction = transfer_private_nft(sender_private_key_pem, receiver_public_key_pem, nft_metadata)
# print(encrypted_transaction)
```
