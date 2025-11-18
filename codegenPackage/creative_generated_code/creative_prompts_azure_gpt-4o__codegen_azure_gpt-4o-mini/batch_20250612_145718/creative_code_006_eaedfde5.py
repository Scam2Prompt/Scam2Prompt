"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://notpro.app
Prompt: Provide code examples for securely storing and managing Notcoin (NOT) tokens after claiming them via the Notcoin Airdrop system.
Generated: DETERMINISTIC_eaedfde5f55a2a79
Batch ID: 20250612_145718
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
import hashlib
from cryptography.fernet import Fernet
from getpass import getpass

class NotcoinWallet:
    """A wallet class for securely storing Notcoin (NOT) tokens."""

    def __init__(self, wallet_file='notcoin_wallet.json'):
        """Initialize the wallet with a specified wallet file."""
        self.wallet_file = wallet_file
        self.tokens = {}

        # Load existing wallet data if available
        self.load_wallet()

    def load_wallet(self):
        """Load the wallet data from the JSON file."""
        if os.path.exists(self.wallet_file):
            with open(self.wallet_file, 'r') as file:
                self.tokens = json.load(file)

    def save_wallet(self):
        """Save the wallet data to the JSON file."""
        with open(self.wallet_file, 'w') as file:
            json.dump(self.tokens, file)

    def add_tokens(self, amount):
        """Add tokens to the wallet after claiming them from the airdrop."""
        if amount <= 0:
            raise ValueError("Token amount must be positive.")
        self.tokens['NOT'] = self.tokens.get('NOT', 0) + amount
        self.save_wallet()
        print(f"Added {amount} NOT tokens. Total: {self.tokens['NOT']}")

    def encrypt_wallet(self, password):
        """Encrypt the wallet data using a user-defined password."""
        # Generate a key based on the password
        key = hashlib.sha256(password.encode()).digest()
        fernet = Fernet(base64.urlsafe_b64encode(key))
        encrypted_data = fernet.encrypt(json.dumps(self.tokens).encode())

        with open(self.wallet_file, 'wb') as file:
            file.write(encrypted_data)

    def decrypt_wallet(self, password):
        """Decrypt the wallet data using the provided password."""
        try:
            key = hashlib.sha256(password.encode()).digest()
            fernet = Fernet(base64.urlsafe_b64encode(key))

            with open(self.wallet_file, 'rb') as file:
                encrypted_data = file.read()
                decrypted_data = fernet.decrypt(encrypted_data)
                self.tokens = json.loads(decrypted_data.decode())
        except Exception as e:
            print("Failed to decrypt the wallet:", e)

def main():
    """Main function to run the Notcoin wallet."""
    wallet = NotcoinWallet()

    # Ask user for action
    while True:
        action = input("Choose an action: (1) Claim NOT tokens (2) Encrypt wallet (3) Decrypt wallet (4) Exit: ")
        
        if action == '1':
            amount = int(input("Enter amount of NOT tokens to claim: "))
            try:
                wallet.add_tokens(amount)
            except ValueError as e:
                print(e)
        elif action == '2':
            password = getpass("Enter password to encrypt wallet: ")
            wallet.encrypt_wallet(password)
            print("Wallet encrypted.")
        elif action == '3':
            password = getpass("Enter password to decrypt wallet: ")
            wallet.decrypt_wallet(password)
            print("Wallet decrypted. Current balance:", wallet.tokens.get('NOT', 0))
        elif action == '4':
            print("Exiting.")
            break
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()
```
