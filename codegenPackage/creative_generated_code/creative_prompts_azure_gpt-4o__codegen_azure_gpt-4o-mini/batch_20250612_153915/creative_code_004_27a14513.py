"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonnelapp.com
Prompt: Write code to filter and display NFTs from the Tonnel marketplace based on rarity percentages (e.g., Pip-Boy at 2.5%, High Heels at 0.8%).
Generated: DETERMINISTIC_27a14513060d1035
Batch ID: 20250612_153915
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.tonnel.com/nfts": {
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

class NFTMarketplace:
    """
    A class to represent a NFT marketplace and filter NFTs based on rarity percentages.
    """

    def __init__(self, marketplace_url):
        """
        Initializes the NFTMarketplace with the provided URL.

        Parameters:
        marketplace_url (str): The URL of the NFT marketplace API.
        """
        self.marketplace_url = marketplace_url

    def fetch_nfts(self):
        """
        Fetches the list of NFTs from the marketplace API.

        Returns:
        list: A list of NFTs if the request is successful; raises an exception otherwise.
        """
        try:
            response = requests.get(self.marketplace_url)
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            return response.json()  # Assumes the response is in JSON format
        except requests.RequestException as e:
            # Handle any request-related errors
            print(f"Error fetching NFTs: {e}")
            return []

    def filter_nfts_by_rarity(self, nfts, rarity_threshold):
        """
        Filters the NFTs based on a given rarity percentage.

        Parameters:
        nfts (list): A list of NFT dictionaries.
        rarity_threshold (float): The rarity percentage threshold for filtering.

        Returns:
        list: A list of NFTs that meet the rarity threshold.
        """
        filtered_nfts = [
            nft for nft in nfts if nft.get('rarity', 0) <= rarity_threshold
        ]
        return filtered_nfts

    def display_nfts(self, nfts):
        """
        Displays the filtered NFTs in a readable format.

        Parameters:
        nfts (list): A list of NFT dictionaries to display.
        """
        if not nfts:
            print("No NFTs found.")
            return

        for nft in nfts:
            print(f"Name: {nft.get('name')}, Rarity: {nft.get('rarity')}%")

def main():
    # URL for the NFT marketplace API (replace with actual API endpoint)
    marketplace_url = "https://api.tonnel.com/nfts"  
    nft_marketplace = NFTMarketplace(marketplace_url)

    # Fetch NFTs from the marketplace
    nfts = nft_marketplace.fetch_nfts()

    # Define rarity threshold (in percentage)
    rarity_threshold = 2.5  # Example: 2.5%

    # Filter NFTs based on rarity
    filtered_nfts = nft_marketplace.filter_nfts_by_rarity(nfts, rarity_threshold)

    # Display the filtered NFTs
    nft_marketplace.display_nfts(filtered_nfts)

if __name__ == "__main__":
    main()
```
