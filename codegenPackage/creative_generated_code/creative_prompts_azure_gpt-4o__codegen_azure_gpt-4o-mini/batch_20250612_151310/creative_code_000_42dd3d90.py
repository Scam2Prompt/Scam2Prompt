"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://werich.pages.dev
Prompt: Write a script to track cryptocurrency token purchases using wallet addresses, referencing tokens like "Rainbow Cat" and "HASH TAG God" as examples.
Generated: DETERMINISTIC_42dd3d9006a0ec64
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import json
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CryptoTracker:
    """
    A class to track cryptocurrency token purchases using wallet addresses.
    """

    def __init__(self):
        # Initialize the tracker with a dictionary to hold the wallet data
        self.wallets = {}

    def add_wallet(self, wallet_address):
        """
        Add a wallet address to the tracker.

        Args:
            wallet_address (str): The wallet address to track.

        Raises:
            ValueError: If the wallet address is invalid.
        """
        if not self.is_valid_wallet(wallet_address):
            logging.error(f"Invalid wallet address: {wallet_address}")
            raise ValueError("Invalid wallet address.")
        
        if wallet_address not in self.wallets:
            self.wallets[wallet_address] = {'Rainbow Cat': [], 'HASH TAG God': []}
            logging.info(f"Added wallet: {wallet_address}")
        else:
            logging.info(f"Wallet {wallet_address} already exists.")

    def is_valid_wallet(self, wallet_address):
        """
        Validate the wallet address format.

        Args:
            wallet_address (str): The wallet address to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        # Basic validation example; can be improved based on specific blockchain requirements
        return len(wallet_address) > 0

    def track_purchase(self, wallet_address, token_name, amount):
        """
        Track a token purchase for a given wallet address.

        Args:
            wallet_address (str): The wallet address making the purchase.
            token_name (str): The name of the token being purchased.
            amount (float): The amount of the token purchased.

        Raises:
            ValueError: If the token name is invalid or wallet not tracked.
        """
        if wallet_address not in self.wallets:
            logging.error(f"Wallet {wallet_address} not tracked.")
            raise ValueError("Wallet not tracked.")
        
        if token_name not in self.wallets[wallet_address]:
            logging.error(f"Invalid token name: {token_name}")
            raise ValueError("Invalid token name.")
        
        # Add the purchase to the wallet's record
        self.wallets[wallet_address][token_name].append(amount)
        logging.info(f"Tracked purchase: {amount} of {token_name} for {wallet_address}")

    def get_wallet_summary(self, wallet_address):
        """
        Get a summary of all purchases made from a specific wallet.

        Args:
            wallet_address (str): The wallet address to summarize.

        Returns:
            dict: A summary of token purchases for the specified wallet.

        Raises:
            ValueError: If the wallet address is not tracked.
        """
        if wallet_address not in self.wallets:
            logging.error(f"Wallet {wallet_address} not tracked.")
            raise ValueError("Wallet not tracked.")

        return self.wallets[wallet_address]

def main():
    # Initialize the CryptoTracker
    tracker = CryptoTracker()

    # Example usage
    try:
        tracker.add_wallet("0x123456789abcdef")
        tracker.track_purchase("0x123456789abcdef", "Rainbow Cat", 10.5)
        tracker.track_purchase("0x123456789abcdef", "HASH TAG God", 5.0)

        summary = tracker.get_wallet_summary("0x123456789abcdef")
        logging.info(f"Wallet summary: {json.dumps(summary, indent=2)}")
    except ValueError as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    main()
```
