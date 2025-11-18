"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enterart.rpmltech.com
Prompt: Write a Python script using the OpenSea API to fetch NFT metadata, including the artist's username, price, and type (visual, audio, or video), similar to the structure displayed on enter.art.
Generated: DETERMINISTIC_bd259936232bceea
Batch ID: 20250612_151659
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.opensea.io/api/v1/assets": {
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

class OpenSeaAPI:
    """
    OpenSeaAPI class to interact with the OpenSea API to fetch NFT metadata.
    """

    BASE_URL = "https://api.opensea.io/api/v1/assets"

    def __init__(self, owner: str, asset_contract_address: str = None):
        """
        Initialize the OpenSeaAPI with the owner's address and optional contract address.

        :param owner: The wallet address of the NFT owner.
        :param asset_contract_address: The contract address of the specific NFT.
        """
        self.owner = owner
        self.asset_contract_address = asset_contract_address

    def fetch_nft_metadata(self):
        """
        Fetch NFT metadata from OpenSea API.

        :return: A list of dictionaries containing NFT metadata or an error message if failed.
        """
        params = {
            "owner": self.owner,
            "order_direction": "desc",
            "offset": "0",
            "limit": "20"  # Limit the number of assets fetched
        }
        
        if self.asset_contract_address:
            params["asset_contract_address"] = self.asset_contract_address

        try:
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            assets = response.json().get('assets', [])

            nft_metadata = self._parse_assets(assets)
            return nft_metadata

        except requests.RequestException as e:
            # Handle request exceptions
            return {"error": str(e)}
        except Exception as e:
            # Handle any other exceptions
            return {"error": str(e)}

    def _parse_assets(self, assets):
        """
        Parse the assets to extract relevant NFT metadata.

        :param assets: List of asset dictionaries from the OpenSea API response.
        :return: A list of dictionaries with relevant NFT metadata.
        """
        nft_list = []
        for asset in assets:
            nft_info = {
                "name": asset.get("name"),
                "token_id": asset.get("token_id"),
                "artist_username": asset.get("creator", {}).get("user", {}).get("username", "Unknown"),
                "price": self._get_asset_price(asset),
                "type": self._get_asset_type(asset)
            }
            nft_list.append(nft_info)
        return nft_list

    def _get_asset_price(self, asset):
        """
        Retrieve the price of the NFT asset.

        :param asset: The asset dictionary.
        :return: The price formatted as a string or None if not available.
        """
        if asset.get("sell_orders"):
            return asset["sell_orders"][0]["current_price"]  # Example: Get price of the first sell order
        return None

    def _get_asset_type(self, asset):
        """
        Determine the type of the NFT asset based on its content.

        :param asset: The asset dictionary.
        :return: The type as 'visual', 'audio', or 'video'.
        """
        if asset.get("image_url"):
            return 'visual'
        elif asset.get("animation_url"):
            return 'video'
        elif asset.get("audio_url"):
            return 'audio'
        return 'unknown'


if __name__ == "__main__":
    # Example usage:
    owner_address = "0xYourWalletAddressHere"
    opensea_api = OpenSeaAPI(owner=owner_address)

    nft_data = opensea_api.fetch_nft_metadata()
    print(nft_data)
```
