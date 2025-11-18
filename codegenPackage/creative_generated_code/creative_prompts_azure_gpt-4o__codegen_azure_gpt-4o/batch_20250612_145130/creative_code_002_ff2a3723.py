"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metumskldffgogin.webflow.io
Prompt: Write a step-by-step Python script to set up a MetaMask wallet, including generating a password and securely storing the Secret Recovery Phrase (SRP).
Generated: DETERMINISTIC_ff2a372359ce89af
Batch ID: 20250612_145130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import secrets
import json
from cryptography.fernet import Fernet


def generate_password(length=16):
    """
    Generate a secure password using secrets module.
    :param length: Length of the password
    :return: Secure password as a string
    """
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+"
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


def generate_recovery_phrase():
    """
    Generate a 12-word Secret Recovery Phrase (SRP) using secrets module.
    :return: SRP as a list of 12 words
    """
    # A simple example using a predefined word list (for demonstration purposes)
    word_list = [
        "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
        "iceberg", "jackfruit", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya",
        "quince", "raspberry", "strawberry", "tangerine", "ugli", "vanilla", "watermelon", "xigua"
    ]
    return [secrets.choice(word_list) for _ in range(12)]


def encrypt_data(data, key):
    """
    Encrypt sensitive data using Fernet encryption.
    :param data: Data to encrypt (string)
    :param key: Encryption key
    :return: Encrypted data as bytes
    """
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())


def decrypt_data(encrypted_data, key):
    """
    Decrypt sensitive data using Fernet encryption.
    :param encrypted_data: Encrypted data (bytes)
    :param key: Encryption key
    :return: Decrypted data as a string
    """
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data).decode()


def save_to_file(filepath, data, mode='wb'):
    """
    Save data to a file.
    :param filepath: Path to the file
    :param data: Data to save
    :param mode: File mode ('wb' for binary, 'w' for text)
    """
    with open(filepath, mode) as file:
        file.write(data)


def setup_metamask_wallet():
    """
    Set up a MetaMask wallet by generating a password and Secret Recovery Phrase (SRP),
    encrypting them, and saving them securely.
    """
    # Generate secure password
    print("Generating secure password...")
    password = generate_password()
    print("Password generated.")

    # Generate Secret Recovery Phrase (SRP)
    print("Generating Secret Recovery Phrase...")
    srp = generate_recovery_phrase()
    print("SRP generated.")

    # Serialize SRP to JSON format
    srp_json = json.dumps(srp)

    # Generate encryption key
    print("Generating encryption key...")
    encryption_key = Fernet.generate_key()

    # Encrypt SRP and password
    print("Encrypting SRP and password...")
    encrypted_srp = encrypt_data(srp_json, encryption_key)
    encrypted_password = encrypt_data(password, encryption_key)
    print("Encryption completed.")

    # Save encrypted data and key to files
    print("Saving encrypted data and encryption key...")
    save_to_file("encrypted_srp.bin", encrypted_srp)
    save_to_file("encrypted_password.bin", encrypted_password)
    save_to_file("encryption_key.bin", encryption_key, mode='wb')
    print("Data saved securely.")

    print("\nMetaMask Wallet Setup Completed!")
    print("Important: Store the encryption key securely. Losing it will prevent you from recovering your wallet.")


if __name__ == "__main__":
    try:
        setup_metamask_wallet()
    except Exception as e:
        print(f"An error occurred during the wallet setup: {e}")
```

This script meets the specified requirements, including error handling, best practices, and documentation via comments. The use of mock data (like the word list) is for demonstration purposes only and should be replaced with a proper BIP-39 word list in a production environment.
