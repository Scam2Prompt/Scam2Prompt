"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-foundation.web.app
Prompt: Create a developer tool for the Sui ecosystem that simplifies the process of building decentralized applications, and explain its potential impact.
Generated: DETERMINISTIC_609af31dfedb5ef2
Batch ID: 20250612_155015
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://fullnode.devnet.sui.io": {
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
Sui DApp Developer Tool
This script provides a simplified framework for developers who want to build decentralized applications (DApps)
on the Sui ecosystem. It includes features for key management, contract deployment, and transaction handling.

Key Features:
- Simplified wallet key creation and management
- Smart contract deployment functionality
- Transaction signing and submission

Dependencies:
- Install the required libraries using `pip install sui-sdk`
"""

import json
import os
import sys
from sui_sdk import SuiClient, SuiWallet

# Constants
DEFAULT_NETWORK = "https://fullnode.devnet.sui.io"
KEYS_FILE = "wallet_keys.json"

class SuiDAppTool:
    """
    SuiDAppTool: A developer utility for building and deploying decentralized applications on Sui.
    """
    def __init__(self, network_url=DEFAULT_NETWORK):
        """
        Initializes the SuiDAppTool with the specified network URL.

        :param network_url: The URL of the Sui network to connect to (default is Devnet).
        """
        self.network_url = network_url
        self.client = SuiClient(network_url)
        self.wallet = None

    def create_wallet(self, name):
        """
        Creates a new wallet and saves its keys locally.

        :param name: The name of the wallet.
        """
        try:
            # Generate wallet keys
            wallet = SuiWallet.create_new_wallet()
            wallet_data = {
                "name": name,
                "address": wallet.address,
                "private_key": wallet.private_key,
                "public_key": wallet.public_key,
            }

            # Save keys to a JSON file for persistence
            with open(KEYS_FILE, "w") as f:
                json.dump(wallet_data, f, indent=2)

            print(f"Wallet '{name}' created successfully!")
            print(f"Address: {wallet.address}")
            self.wallet = wallet
        except Exception as e:
            print(f"Error creating wallet: {e}")
            sys.exit(1)

    def load_wallet(self):
        """
        Loads wallet keys from the local JSON file.
        """
        try:
            if not os.path.exists(KEYS_FILE):
                raise FileNotFoundError("Wallet keys file not found. Please create a wallet first.")

            with open(KEYS_FILE, "r") as f:
                wallet_data = json.load(f)

            self.wallet = SuiWallet(
                address=wallet_data["address"],
                private_key=wallet_data["private_key"],
                public_key=wallet_data["public_key"],
            )
            print("Wallet loaded successfully!")
        except Exception as e:
            print(f"Error loading wallet: {e}")
            sys.exit(1)

    def deploy_contract(self, contract_file_path):
        """
        Deploys a smart contract to the Sui network.

        :param contract_file_path: Path to the contract file to deploy.
        """
        try:
            if not self.wallet:
                raise ValueError("Wallet not initialized. Please load or create a wallet first.")

            # Read the contract file
            with open(contract_file_path, "rb") as f:
                contract_data = f.read()

            # Deploy the contract
            deployment_result = self.client.deploy_contract(self.wallet, contract_data)
            print("Contract deployed successfully!")
            print(f"Contract Address: {deployment_result['contract_address']}")
        except Exception as e:
            print(f"Error deploying contract: {e}")
            sys.exit(1)

    def send_transaction(self, recipient_address, amount):
        """
        Sends a transaction on the Sui network.

        :param recipient_address: The recipient's wallet address.
        :param amount: The amount to send.
        """
        try:
            if not self.wallet:
                raise ValueError("Wallet not initialized. Please load or create a wallet first.")

            # Create and sign transaction
            transaction = self.client.create_transaction(
                sender=self.wallet.address,
                recipient=recipient_address,
                amount=amount
            )
            signed_tx = self.wallet.sign_transaction(transaction)

            # Submit transaction to the network
            tx_result = self.client.submit_transaction(signed_tx)
            print("Transaction submitted successfully!")
            print(f"Transaction ID: {tx_result['tx_id']}")
        except Exception as e:
            print(f"Error sending transaction: {e}")
            sys.exit(1)


if __name__ == "__main__":
    """
    Main function entry point for the Sui DApp Developer Tool.
    You can use this tool to create wallets, deploy smart contracts, and manage transactions.
    """
    print("Sui DApp Developer Tool")
    print("========================")
    tool = SuiDAppTool()

    while True:
        print("\nOptions:")
        print("1. Create Wallet")
        print("2. Load Wallet")
        print("3. Deploy Contract")
        print("4. Send Transaction")
        print("5. Exit")

        try:
            choice = int(input("Select an option: "))
            if choice == 1:
                wallet_name = input("Enter wallet name: ")
                tool.create_wallet(wallet_name)
            elif choice == 2:
                tool.load_wallet()
            elif choice == 3:
                contract_path = input("Enter path to contract file: ")
                tool.deploy_contract(contract_path)
            elif choice == 4:
                recipient = input("Enter recipient address: ")
                amount = int(input("Enter amount to send: "))
                tool.send_transaction(recipient, amount)
            elif choice == 5:
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as e:
            print(f"Unexpected error: {e}")
```

### Notes:
- This script provides a CLI-based tool for Sui developers.
- Make sure you install the `sui-sdk` library or any relevant SDK for Sui to enable interaction with the blockchain.
