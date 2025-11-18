"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://data-portability-ui.vercel.vana.com
Prompt: Provide an example of integrating a crypto wallet to secure personal data and enable querying, based on the Vana Network demo.
Generated: DETERMINISTIC_4b11443b1071b615
Batch ID: 20250612_155057
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
"""
Example Python code for integrating a crypto wallet to secure personal data and enable querying, 
based on a conceptual Vana Network demo.

Dependencies:
- `web3` for interacting with blockchain wallets (install with `pip install web3`)
- `cryptography` for encrypting/decrypting personal data (install with `pip install cryptography`)

This code demonstrates:
1. Connecting to a crypto wallet (e.g., MetaMask or a hardware wallet).
2. Encrypting personal data using the wallet's public key.
3. Decrypting data with the wallet's private key.
4. Querying data securely using blockchain transactions.

Note: Customize the Vana Network-specific components and endpoints as necessary.
"""

from web3 import Web3
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key, PublicFormat, Encoding

# Constants
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura Project ID

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check connection to blockchain
if not web3.isConnected():
    raise Exception("Failed to connect to the Ethereum blockchain.")

# Sample personal data to be secured
personal_data = "Sensitive personal information"

# Function to connect to the wallet and get the user's address
def get_wallet_address():
    """
    Prompts the user to connect their wallet and retrieve their Ethereum address.
    """
    try:
        # Example: Retrieving the default account (customize for MetaMask or other wallets)
        wallet_address = web3.eth.accounts[0]
        if not wallet_address:
            raise Exception("No wallet connected or account found.")
        return wallet_address
    except Exception as e:
        raise Exception(f"Error retrieving wallet address: {str(e)}")

# Function to encrypt personal data using the wallet's public key
def encrypt_data_with_wallet_public_key(data, public_key):
    """
    Encrypts personal data using the wallet's public key.
    """
    try:
        encrypted_data = public_key.encrypt(
            data.encode(),  # Convert data to bytes
            OAEP(mgf=MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
        )
        return encrypted_data
    except Exception as e:
        raise Exception(f"Error encrypting data: {str(e)}")

# Function to decrypt personal data using the wallet's private key
def decrypt_data_with_wallet_private_key(encrypted_data, private_key_pem):
    """
    Decrypts encrypted data using the wallet's private key.
    """
    try:
        # Load private key from PEM format (replace with wallet-specific key retrieval)
        private_key = load_pem_private_key(private_key_pem, password=None)
        decrypted_data = private_key.decrypt(
            encrypted_data,
            OAEP(mgf=MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
        )
        return decrypted_data.decode()  # Convert bytes back to string
    except Exception as e:
        raise Exception(f"Error decrypting data: {str(e)}")

# Function to query data securely via blockchain
def query_secure_data(wallet_address, query):
    """
    Sends a query request securely to the Vana Network (or similar service) and retrieves results.
    """
    try:
        # Example: Sending transaction to query data (replace with Vana Network-specific logic)
        tx = {
            "from": wallet_address,
            "to": "0xQueryAddressHere",  # Replace with the querying contract's address
            "data": web3.sha3(text=query),  # Hash the query for security
            "gas": 2000000,
        }
        tx_hash = web3.eth.send_transaction(tx)  # Send transaction
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)  # Wait for receipt
        return receipt
    except Exception as e:
        raise Exception(f"Error querying data securely: {str(e)}")

# Main execution flow
if __name__ == "__main__":
    try:
        # Step 1: Connect wallet and retrieve address
        wallet_address = get_wallet_address()
        print(f"Connected wallet address: {wallet_address}")

        # Step 2: Retrieve wallet public key (example RSA key generation; replace with actual wallet key)
        # NOTE: Wallets like MetaMask or hardware wallets may not expose raw keys directly.
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        public_key = private_key.public_key()

        # Step 3: Encrypt personal data
        encrypted_data = encrypt_data_with_wallet_public_key(personal_data, public_key)
        print(f"Encrypted data: {encrypted_data}")

        # Step 4: Decrypt personal data (example using private key PEM serialization)
        private_key_pem = private_key.private_bytes(
            encoding=Encoding.PEM,
            format=PublicFormat.TraditionalOpenSSL,
            encryption_algorithm=None
        )
        decrypted_data = decrypt_data_with_wallet_private_key(encrypted_data, private_key_pem)
        print(f"Decrypted data: {decrypted_data}")

        # Step 5: Query data securely
        query_result = query_secure_data(wallet_address, "Fetch my sensitive data")
        print(f"Query result: {query_result}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
