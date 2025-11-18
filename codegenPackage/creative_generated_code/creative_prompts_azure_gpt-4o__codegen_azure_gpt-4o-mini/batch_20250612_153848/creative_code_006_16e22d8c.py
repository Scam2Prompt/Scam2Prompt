"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-phantomwallet.us
Prompt: Create a script to filter and hide spam NFTs in Phantom Wallet using its blocklist functionality. Include a method to view blocked items if needed.
Generated: DETERMINISTIC_16e22d8c7453dec0
Batch ID: 20250612_153848
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.phantomwallet.com/v1/nfts": {
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
import json
import requests

class PhantomWallet:
    """A class to manage Phantom Wallet and filter spam NFTs using a blocklist."""

    def __init__(self, wallet_address):
        """
        Initializes the PhantomWallet instance.

        Args:
            wallet_address (str): The Phantom wallet address.
        """
        self.wallet_address = wallet_address
        self.blocklist = set()
        self.nft_collection = []
        self.api_url = "https://api.phantomwallet.com/v1/nfts"  # Hypothetical endpoint

    def fetch_nfts(self):
        """Fetches NFTs for the wallet from the Phantom API."""
        try:
            response = requests.get(f"{self.api_url}/{self.wallet_address}")
            response.raise_for_status()  # Raise an error for bad responses
            self.nft_collection = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching NFTs: {e}")
            self.nft_collection = []

    def block_nft(self, nft_id):
        """Blocks an NFT by adding it to the blocklist.

        Args:
            nft_id (str): The ID of the NFT to block.
        """
        self.blocklist.add(nft_id)
        print(f"NFT {nft_id} has been blocked.")

    def is_spam_nft(self, nft):
        """Determines if an NFT is considered spam.

        Args:
            nft (dict): The NFT data to check.

        Returns:
            bool: True if the NFT is in the blocklist, False otherwise.
        """
        return nft['id'] in self.blocklist

    def filter_spam_nfts(self):
        """Filters and returns non-spam NFTs from the wallet's collection."""
        filtered_nfts = [nft for nft in self.nft_collection if not self.is_spam_nft(nft)]
        return filtered_nfts

    def view_blocked_items(self):
        """Returns a list of blocked NFT IDs."""
        return list(self.blocklist)

# Example usage
if __name__ == "__main__":
    # Initialize Phantom Wallet with a given wallet address
    wallet_address = "your_wallet_address_here"  # Replace with a valid wallet address
    wallet = PhantomWallet(wallet_address)

    # Fetch NFTs for the wallet
    wallet.fetch_nfts()

    # Block a spam NFT (example ID)
    wallet.block_nft("spam_nft_id_12345")  # Replace with actual NFT ID to block

    # Get filtered NFTs
    non_spam_nfts = wallet.filter_spam_nfts()
    print("Non-spam NFTs:", non_spam_nfts)

    # View blocked NFT IDs
    blocked_items = wallet.view_blocked_items()
    print("Blocked NFT IDs:", blocked_items)
```
