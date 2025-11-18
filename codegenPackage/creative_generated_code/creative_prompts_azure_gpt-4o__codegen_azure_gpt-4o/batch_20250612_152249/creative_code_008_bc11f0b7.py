"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeie3nw7cyq2q2jw5zaaxhqznmxmr6ano4kkfjked4sebtl2biznzfy.ipfs.dweb.link
Prompt: Generate code to securely store and manage whitelist data for a public pre-sale event, ensuring compatibility with Web3 wallets.
Generated: DETERMINISTIC_bc11f0b7e82501d5
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from web3 import Web3
from eth_account.messages import encode_defunct

# Load environment variables for secure management (e.g., private keys)
from dotenv import load_dotenv
load_dotenv()

# Connect to Ethereum network
INFURA_URL = os.getenv("INFURA_URL")  # Your Infura or equivalent node URL
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum network.")

# Whitelist management class
class WhitelistManager:
    def __init__(self, whitelist_file='whitelist.json'):
        """
        Initialize the WhitelistManager with a given JSON file for storage.
        """
        self.whitelist_file = whitelist_file
        self.whitelist = self._load_whitelist()

    def _load_whitelist(self):
        """
        Load whitelist data from a JSON file. If the file does not exist, initialize with an empty list.
        """
        if os.path.exists(self.whitelist_file):
            with open(self.whitelist_file, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    raise ValueError("Failed to decode JSON from whitelist file.")
        return {}

    def _save_whitelist(self):
        """
        Save the current whitelist to the JSON file.
        """
        with open(self.whitelist_file, 'w') as file:
            json.dump(self.whitelist, file, indent=4)

    def add_to_whitelist(self, wallet_address, signature):
        """
        Add a wallet address to the whitelist after validating the signature.
        """
        if not web3.isAddress(wallet_address):
            raise ValueError("Invalid Ethereum address.")

        # Ensure the wallet address is checksummed
        wallet_address = web3.toChecksumAddress(wallet_address)

        # Message to sign (could be a fixed pre-sale event message)
        message = f"Whitelist for pre-sale: {wallet_address}"
        message_encoded = encode_defunct(text=message)

        # Recover the signer address from the signature
        recovered_address = web3.eth.account.recover_message(message_encoded, signature=signature)
        if recovered_address != wallet_address:
            raise ValueError("Signature validation failed.")

        # Add to whitelist
        if wallet_address in self.whitelist:
            raise ValueError("Wallet address is already whitelisted.")

        self.whitelist[wallet_address] = {"signature": signature}
        self._save_whitelist()

    def remove_from_whitelist(self, wallet_address):
        """
        Remove a wallet address from the whitelist.
        """
        wallet_address = web3.toChecksumAddress(wallet_address)
        if wallet_address not in self.whitelist:
            raise ValueError("Wallet address is not in the whitelist.")

        del self.whitelist[wallet_address]
        self._save_whitelist()

    def is_whitelisted(self, wallet_address):
        """
        Check if a wallet address is in the whitelist.
        """
        wallet_address = web3.toChecksumAddress(wallet_address)
        return wallet_address in self.whitelist

# Example usage
if __name__ == "__main__":
    try:
        manager = WhitelistManager()

        # Example wallet address and signature (replace with real data)
        wallet = "0x1234567890abcdef1234567890abcdef12345678"
        signature = "0x..."

        # Add to whitelist
        manager.add_to_whitelist(wallet, signature)

        # Check whitelist status
        print(f"Is whitelisted: {manager.is_whitelisted(wallet)}")

        # Remove from whitelist
        manager.remove_from_whitelist(wallet)
        print(f"Is whitelisted after removal: {manager.is_whitelisted(wallet)}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
