"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enterart.rpmltech.com
Prompt: Develop a Python script using the Alchemy API to fetch and display NFT transaction history for a specific wallet, inspired by the transactional nature of enter.art.
Generated: DETERMINISTIC_7c879bca9308b2db
Batch ID: 20250612_151659
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://eth-mainnet.alchemyapi.io/v2/": {
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

class NFTTransactionFetcher:
    def __init__(self, wallet_address: str, api_key: str):
        """
        Initializes the NFTTransactionFetcher with the wallet address and Alchemy API key.

        :param wallet_address: The address of the wallet to fetch NFT transaction history for.
        :param api_key: The Alchemy API key for authentication.
        """
        self.wallet_address = wallet_address
        self.api_key = api_key
        self.base_url = "https://eth-mainnet.alchemyapi.io/v2/"

    def fetch_nft_transactions(self):
        """
        Fetches the NFT transaction history for the specified wallet address.

        :return: A list of NFT transactions or an error message if the fetch fails.
        """
        url = f"{self.base_url}{self.api_key}/getNFTs"
        params = {
            "owner": self.wallet_address,
            "withMetadata": True
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()  # Parse the JSON response

            if 'ownedNfts' in data:
                return data['ownedNfts']
            else:
                return f"No NFTs found for wallet address: {self.wallet_address}"

        except requests.exceptions.HTTPError as http_err:
            return f"HTTP error occurred: {http_err}"
        except Exception as err:
            return f"An error occurred: {err}"

    def display_transactions(self):
        """
        Displays the NFT transaction history in a readable format.
        """
        transactions = self.fetch_nft_transactions()

        if isinstance(transactions, list):
            if not transactions:
                print("No NFT transactions found.")
            else:
                for nft in transactions:
                    print(f"NFT Name: {nft.get('title', 'N/A')}")
                    print(f"Token ID: {nft.get('id', {}).get('tokenId', 'N/A')}")
                    print(f"Contract Address: {nft.get('id', {}).get('contract', {}).get('address', 'N/A')}")
                    print(f"Token Metadata: {nft.get('metadata', {}).get('description', 'N/A')}")
                    print("-" * 40)
        else:
            print(transactions)

if __name__ == "__main__":
    # Example usage of the NFTTransactionFetcher
    wallet = "0xYourWalletAddressHere"  # Replace with the target wallet address
    api_key = "your_api_key_here"  # Replace with your Alchemy API key

    # Instantiate the NFTTransactionFetcher
    nft_fetcher = NFTTransactionFetcher(wallet, api_key)

    # Fetch and display the NFT transaction history
    nft_fetcher.display_transactions()
```
