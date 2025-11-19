"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellarwallet.co
Prompt: Explain how to generate a new Stellar wallet and the importance of backing up the secret key.
Generated: DETERMINISTIC_1ab1eaf003afb8eb
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import stellar_sdk
from stellar_sdk import Keypair
import json
import os

def generate_stellar_wallet():
    """
    Generate a new Stellar wallet, including a public key and a secret key.
    The secret key should be securely backed up as it is used to access the wallet.
    
    Returns:
        dict: A dictionary containing the public key and secret key.
    """
    try:
        # Generate a new Stellar keypair
        keypair = Keypair.random()

        # Prepare wallet information
        wallet_info = {
            "public_key": keypair.public_key,
            "secret_key": keypair.secret
        }

        # Save the secret key securely (consider encrypting this in a real application)
        save_secret_key(wallet_info["secret_key"])

        return wallet_info

    except Exception as e:
        print(f"Error generating Stellar wallet: {e}")
        return None

def save_secret_key(secret_key):
    """
    Save the secret key to a secure location.
    For demonstration, we save it in a JSON file. In a real application,
    consider using a secure vault service or encrypting the key.
    
    Args:
        secret_key (str): The secret key to be saved.
    """
    try:
        # Define the file path for storing the secret key
        file_path = "stellar_wallet.json"
        
        # Check if the file already exists
        if os.path.exists(file_path):
            print("Warning: The secret key file already exists. It may overwrite the existing key.")

        # Write the secret key to a JSON file
        with open(file_path, 'w') as file:
            json.dump({"secret_key": secret_key}, file)
        
        print("Secret key saved successfully. Please back it up securely.")
    
    except Exception as e:
        print(f"Error saving secret key: {e}")

if __name__ == "__main__":
    wallet = generate_stellar_wallet()
    if wallet:
        print("New Stellar Wallet Generated:")
        print(f"Public Key: {wallet['public_key']}")
        print("Important: Back up your secret key to secure your wallet!")
```
