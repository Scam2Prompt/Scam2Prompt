"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadday23.testnet.nfts2.me
Prompt: Write a script to display the number of NFTs minted and calculate the total referral fees earned for a given wallet address on the Monad Testnet.
Generated: DETERMINISTIC_6eb5ad77f1f84ede
Batch ID: 20250612_155057
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.monad.testnet": {
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
import requests

class NFTStats:
    def __init__(self, wallet_address, api_url):
        self.wallet_address = wallet_address
        self.api_url = api_url

    def get_minted_nfts(self):
        """
        Fetch the number of NFTs minted by the given wallet address.
        Returns the count of minted NFTs or raises an exception if an error occurs.
        """
        try:
            response = requests.get(f"{self.api_url}/nfts/minted/{self.wallet_address}")
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            minted_count = data.get("minted_count", 0)
            return minted_count
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
            return None
        except Exception as err:
            print(f"An error occurred: {err}")  # Log other errors
            return None

    def calculate_referral_fees(self):
        """
        Calculate total referral fees earned by the given wallet address.
        Returns the total referral fees or raises an exception if an error occurs.
        """
        try:
            response = requests.get(f"{self.api_url}/referral-fees/{self.wallet_address}")
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            total_fees = data.get("total_referral_fees", 0)
            return total_fees
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
            return None
        except Exception as err:
            print(f"An error occurred: {err}")  # Log other errors
            return None

    def display_stats(self):
        """
        Display the number of NFTs minted and total referral fees earned.
        """
        minted_nfts = self.get_minted_nfts()
        referral_fees = self.calculate_referral_fees()

        if minted_nfts is not None:
            print(f"Number of NFTs minted by {self.wallet_address}: {minted_nfts}")
        else:
            print("Could not retrieve the number of minted NFTs.")

        if referral_fees is not None:
            print(f"Total referral fees earned by {self.wallet_address}: {referral_fees}")
        else:
            print("Could not retrieve total referral fees.")

if __name__ == "__main__":
    # Replace with the actual wallet address and API URL for Monad Testnet
    wallet_address = "your_wallet_address_here"
    api_url = "https://api.monad.testnet"  # Example API URL

    nft_stats = NFTStats(wallet_address, api_url)
    nft_stats.display_stats()
```
