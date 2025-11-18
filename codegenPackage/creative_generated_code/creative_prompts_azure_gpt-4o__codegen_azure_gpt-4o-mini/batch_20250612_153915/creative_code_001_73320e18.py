"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonnelapp.com
Prompt: Generate code to mint a new NFT on the Tonnel platform, specifying attributes like model, symbol, and backdrop, and set it as an emoji status.
Generated: DETERMINISTIC_73320e1831416f78
Batch ID: 20250612_153915
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.tonnel.com": {
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

class NFTMintingError(Exception):
    """Custom exception for NFT minting errors."""
    pass

class TonnelNFT:
    def __init__(self, api_key, api_url):
        """
        Initializes the TonnelNFT instance.
        
        :param api_key: The API key for authenticating with the Tonnel platform.
        :param api_url: The base URL for the Tonnel API.
        """
        self.api_key = api_key
        self.api_url = api_url

    def mint_nft(self, model, symbol, backdrop, emoji_status):
        """
        Mints a new NFT on the Tonnel platform with specified attributes.
        
        :param model: The model for the NFT.
        :param symbol: The symbol for the NFT.
        :param backdrop: The backdrop image or color for the NFT.
        :param emoji_status: The emoji status to set for the NFT.
        
        :raises NFTMintingError: If the NFT minting fails.
        :return: The response from the Tonnel API if successful.
        """
        # Prepare the payload for the API request
        payload = {
            "model": model,
            "symbol": symbol,
            "backdrop": backdrop,
            "emoji_status": emoji_status
        }

        # Set headers including the API key for authentication
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            # Make the POST request to mint the NFT
            response = requests.post(f"{self.api_url}/nfts/mint", json=payload, headers=headers)

            # Raise an error for bad responses
            response.raise_for_status()
        
        except requests.exceptions.HTTPError as http_err:
            raise NFTMintingError(f"HTTP error occurred: {http_err}") from http_err
        except requests.exceptions.RequestException as req_err:
            raise NFTMintingError(f"Request error occurred: {req_err}") from req_err
        except Exception as e:
            raise NFTMintingError(f"An unexpected error occurred: {e}") from e

        # Return the successful response as JSON
        return response.json()

# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the TonnelNFT with your API key and URL
        api_key = "your_api_key_here"
        api_url = "https://api.tonnel.com"  # Replace with the actual Tonnel API URL
        tonnel_nft = TonnelNFT(api_key, api_url)

        # Mint a new NFT
        result = tonnel_nft.mint_nft(
            model="UniqueArtModel",
            symbol="UAM",
            backdrop="path/to/backdrop/image.png",
            emoji_status="✨"
        )

        print("NFT successfully minted:", result)

    except NFTMintingError as e:
        print("Error minting NFT:", e)
```
