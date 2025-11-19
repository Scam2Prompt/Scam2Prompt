"""
Generated Code Metadata:
========================
Original URL: https://appkit-laboratory-96qjy03xf-reown-com.vercel.app
Prompt: Show me how to configure AppKit without email using ethers as the driving library.
Generated: DETERMINISTIC_8a0f106eb3220073
Batch ID: 20250612_155422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from ethers import ethers

# Configuration for AppKit without email
class AppKitConfig:
    def __init__(self, provider_url, private_key):
        """
        Initializes the AppKit configuration.

        :param provider_url: URL of the Ethereum provider (e.g., Infura, Alchemy)
        :param private_key: Private key of the wallet to interact with the Ethereum network
        """
        self.provider_url = provider_url
        self.private_key = private_key
        self.wallet = None
        self.provider = None

    def setup_provider(self):
        """
        Sets up the Ethereum provider using the provided URL.
        """
        try:
            self.provider = ethers.providers.JsonRpcProvider(self.provider_url)
            print("Provider set up successfully.")
        except Exception as e:
            print(f"Error setting up provider: {e}")
            raise

    def setup_wallet(self):
        """
        Sets up the wallet using the provided private key.
        """
        try:
            self.wallet = ethers.Wallet(self.private_key, self.provider)
            print("Wallet set up successfully.")
        except Exception as e:
            print(f"Error setting up wallet: {e}")
            raise

    def get_balance(self):
        """
        Retrieves the balance of the wallet in Ether.

        :return: Balance in Ether
        """
        try:
            balance_wei = self.wallet.get_balance()
            balance_eth = ethers.utils.formatEther(balance_wei)
            return balance_eth
        except Exception as e:
            print(f"Error retrieving balance: {e}")
            raise

    def send_transaction(self, to_address, amount):
        """
        Sends Ether from the wallet to the specified address.

        :param to_address: The recipient's Ethereum address
        :param amount: Amount of Ether to send
        :return: Transaction hash
        """
        try:
            transaction = {
                'to': to_address,
                'value': ethers.utils.parseEther(amount),
                'gas': 21000,
                'gasPrice': await self.provider.getGasPrice(),
                'nonce': await self.provider.getTransactionCount(self.wallet.address),
            }
            tx = await self.wallet.sendTransaction(transaction)
            print(f"Transaction sent: {tx.hash}")
            return tx.hash
        except Exception as e:
            print(f"Error sending transaction: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # Load configuration from environment variables
    PROVIDER_URL = os.getenv("ETH_PROVIDER_URL")
    PRIVATE_KEY = os.getenv("ETH_PRIVATE_KEY")

    if not PROVIDER_URL or not PRIVATE_KEY:
        raise ValueError("Provider URL and Private Key must be set in environment variables.")

    app_kit = AppKitConfig(PROVIDER_URL, PRIVATE_KEY)
    app_kit.setup_provider()
    app_kit.setup_wallet()

    # Get wallet balance
    balance = app_kit.get_balance()
    print(f"Wallet balance: {balance} ETH")

    # Example transaction (uncomment to use)
    # tx_hash = app_kit.send_transaction("0xRecipientAddressHere", "0.01")
    # print(f"Transaction hash: {tx_hash}")
```
