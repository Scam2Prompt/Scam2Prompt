"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonnelapp.com
Prompt: Write a script to interact with the Tonnel platform's wallet connection feature and retrieve a user's NFT collection details, including model, symbol, and backdrop attributes.
Generated: DETERMINISTIC_92a8465f267453ef
Batch ID: 20250612_153915
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.tonnel.io": {
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

class TonnelAPI:
    BASE_URL = "https://api.tonnel.io"  # Base URL for Tonnel API

    def __init__(self, api_key):
        """
        Initializes the TonnelAPI with the provided API key.

        :param api_key: User's API key for authentication
        """
        self.api_key = api_key

    def get_wallet_nfts(self, wallet_address):
        """
        Retrieves the NFT collection details for a specified wallet address.

        :param wallet_address: The address of the user's wallet
        :return: A list of NFTs with attributes or raises an error
        """
        endpoint = f"{self.BASE_URL}/wallets/{wallet_address}/nfts"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            nfts = response.json()  # Parse JSON response

            # Check if NFTs are returned
            if not nfts:
                raise ValueError("No NFTs found for the specified wallet address.")

            return self.extract_nft_details(nfts)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching NFTs: {e}")
            raise  # Re-raise the exception for further handling

    @staticmethod
    def extract_nft_details(nfts):
        """
        Extracts relevant details from the NFTs.

        :param nfts: List of NFT data
        :return: List of dictionaries containing model, symbol, and backdrop attributes
        """
        nft_details = []
        
        for nft in nfts:
            details = {
                "model": nft.get("model"),
                "symbol": nft.get("symbol"),
                "backdrop": nft.get("backdrop"),
            }
            nft_details.append(details)

        return nft_details


def main():
    """
    Main execution function to interact with the Tonnel API and get NFT details.
    """
    # User's API key and wallet address (replace with actual values)
    api_key = "your_api_key_here"
    wallet_address = "your_wallet_address_here"

    tonnel_api = TonnelAPI(api_key)

    try:
        nfts = tonnel_api.get_wallet_nfts(wallet_address)
        print("NFT Collection Details:")
        for nft in nfts:
            print(nft)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
