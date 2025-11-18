"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-qr-code.com
Prompt: Suggest a method to securely store and process Ethereum addresses while generating QR codes, similar to the security practices mentioned on the ETH QR Code Generator website.
Generated: DETERMINISTIC_3c0c439a06420257
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
import re
import hashlib
import os
import json
from cryptography.fernet import Fernet

# Constants
SECURE_STORAGE_FILE = "secure_eth_addresses.json"

# Generate a cryptographic key for encrypting the Ethereum addresses
# Ensure you keep this key secure!
def generate_encryption_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)
    print("Encryption key generated and saved to 'encryption_key.key'")
    return key

# Load the encryption key from file
def load_encryption_key():
    if not os.path.exists("encryption_key.key"):
        raise FileNotFoundError("Encryption key file missing. Run generate_encryption_key first.")
    with open("encryption_key.key", "rb") as key_file:
        return key_file.read()

# Validate Ethereum address format
def validate_ethereum_address(address):
    eth_address_pattern = re.compile(r'^0x[a-fA-F0-9]{40}$')
    if eth_address_pattern.match(address):
        return True
    else:
        raise ValueError(f"Invalid Ethereum address: {address}")

# Securely store Ethereum addresses in encrypted storage
def store_ethereum_address(address):
    validate_ethereum_address(address)
    encryption_key = load_encryption_key()
    fernet = Fernet(encryption_key)
    
    # Encrypt the Ethereum address
    encrypted_address = fernet.encrypt(address.encode())
    
    # Hash the address for integrity checks
    hashed_address = hashlib.sha256(address.encode()).hexdigest()
    
    # Store encrypted address and hash securely in a JSON file
    if not os.path.exists(SECURE_STORAGE_FILE):
        with open(SECURE_STORAGE_FILE, "w") as file:
            json.dump({}, file)
    
    with open(SECURE_STORAGE_FILE, "r") as file:
        data = json.load(file)
    
    data[hashed_address] = encrypted_address.decode()
    
    with open(SECURE_STORAGE_FILE, "w") as file:
        json.dump(data, file)
    
    print(f"Ethereum address securely stored. Hash: {hashed_address}")

# Retrieve and decrypt an Ethereum address using its hash
def retrieve_ethereum_address(hashed_address):
    encryption_key = load_encryption_key()
    fernet = Fernet(encryption_key)
    
    if not os.path.exists(SECURE_STORAGE_FILE):
        raise FileNotFoundError("Secure storage file not found.")
    
    with open(SECURE_STORAGE_FILE, "r") as file:
        data = json.load(file)
    
    encrypted_address = data.get(hashed_address)
    if not encrypted_address:
        raise ValueError("Ethereum address not found.")
    
    decrypted_address = fernet.decrypt(encrypted_address.encode()).decode()
    return decrypted_address

# Generate a QR code for an Ethereum address
def generate_qr_code(address):
    validate_ethereum_address(address)
    
    # Use the qrcode library to generate the QR code image
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(address)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    
    # Save QR code to file
    filename = f"{address}.png"
    img.save(filename)
    print(f"QR code generated and saved as '{filename}'")

# Example usage
if __name__ == "__main__":
    try:
        # Generate encryption key once and store securely (uncomment if running for the first time)
        # generate_encryption_key()
        
        # Example Ethereum address
        eth_address = "0x1234567890abcdef1234567890abcdef12345678"
        
        # Store the Ethereum address securely
        store_ethereum_address(eth_address)
        
        # Retrieve the Ethereum address using its hash
        hashed_address = hashlib.sha256(eth_address.encode()).hexdigest()
        retrieved_address = retrieve_ethereum_address(hashed_address)
        print(f"Retrieved Ethereum address: {retrieved_address}")
        
        # Generate QR code for the Ethereum address
        generate_qr_code(retrieved_address)
    
    except Exception as e:
        print(f"Error: {e}")
```
