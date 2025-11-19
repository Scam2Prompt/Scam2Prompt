"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-core.com
Prompt: Explain how to securely store and manage a Bip39 recovery phrase using Wallet-Core tools.
Generated: DETERMINISTIC_dd481a30bbe8a0ef
Batch ID: 20250612_163530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
A Python script demonstrating how to securely store and manage a BIP39 recovery phrase 
using Trust Wallet's Wallet-Core library.

Requirements:
- Install Wallet-Core Python bindings (if available) or compile Wallet-Core for Python.
"""

import os
import wallet_core

# Function to securely store and manage a BIP39 recovery phrase
def securely_manage_bip39_phrase():
    """
    Generates a BIP39 recovery phrase, encrypts it using a user-provided password, and
    demonstrates safe storage and retrieval of the encrypted data.
    """

    try:
        # Generate a new BIP39 recovery phrase (24 words)
        mnemonic = wallet_core.Mnemonic.generate(wallet_core.Mnemonic.Strength.STRONG)
        print("Generated BIP39 Recovery Phrase:", mnemonic)

        # Validate the generated mnemonic
        if not wallet_core.Mnemonic.is_valid(mnemonic):
            raise ValueError("Invalid BIP39 mnemonic phrase generated!")

        # Prompt user for a secure password to encrypt the recovery phrase
        password = input("Enter a strong password to encrypt the recovery phrase: ")

        # Encrypt the mnemonic with the provided password
        encrypted_mnemonic = wallet_core.Encryption.encrypt_data(mnemonic.encode(), password.encode())

        # Save the encrypted recovery phrase securely (e.g., file storage, database, etc.)
        # For this demonstration, we'll save it to a file in the current directory.
        storage_path = "encrypted_bip39_phrase.dat"
        with open(storage_path, "wb") as storage_file:
            storage_file.write(encrypted_mnemonic)
        print(f"Encrypted recovery phrase saved securely to: {storage_path}")

        # Simulate retrieval and decryption
        with open(storage_path, "rb") as storage_file:
            encrypted_data = storage_file.read()

        # Decrypt the mnemonic using the provided password
        decrypted_mnemonic = wallet_core.Encryption.decrypt_data(encrypted_data, password.encode()).decode()

        # Validate the decrypted mnemonic
        if not wallet_core.Mnemonic.is_valid(decrypted_mnemonic):
            raise ValueError("Failed to decrypt a valid BIP39 mnemonic!")

        print("Decrypted BIP39 Recovery Phrase:", decrypted_mnemonic)

    except Exception as e:
        # Handle any exceptions that occur during the process
        print(f"An error occurred: {e}")


# Entry point of the script
if __name__ == "__main__":
    securely_manage_bip39_phrase()
```

**Note**: 
- Replace `wallet_core` with the actual import path of Wallet-Core's Python library if necessary.
- Ensure all dependencies are installed and correctly configured. 
- Password management and encryption should be done using secure libraries and algorithms.
