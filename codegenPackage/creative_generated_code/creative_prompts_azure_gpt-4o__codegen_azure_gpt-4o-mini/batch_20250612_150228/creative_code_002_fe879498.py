"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiaoni35loah6mxudvrxltj6qkb5afmoqjqbg2spapid2kltvnqvby.ipfs.dweb.link
Prompt: Recommend libraries or APIs for integrating NAVI Protocol's Oracle Security mechanism to ensure accurate pricing information for collateralized assets.
Generated: DETERMINISTIC_fe87949800cbd5db
Batch ID: 20250612_150228
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.navi-protocol.com/v1/oracle": {
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

class NaviOracleAPI:
    """
    A class to interact with the NAVI Protocol's Oracle Security mechanism
    for retrieving accurate pricing information for collateralized assets.
    """

    BASE_URL = "https://api.navi-protocol.com/v1/oracle"

    def __init__(self, api_key):
        """
        Initializes the NaviOracleAPI with the necessary API key.

        Parameters:
            api_key (str): The API key for authenticating requests.
        """
        self.api_key = api_key

    def get_asset_price(self, asset_symbol):
        """
        Retrieves the current price of the specified asset.

        Parameters:
            asset_symbol (str): The symbol of the asset (e.g., 'ETH', 'BTC').

        Returns:
            float: The current price of the asset.

        Raises:
            ValueError: If the asset symbol is not valid.
            Exception: For any other errors that occur during the API request.
        """
        if not asset_symbol:
            raise ValueError("Asset symbol cannot be empty")

        url = f"{self.BASE_URL}/price/{asset_symbol}"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for HTTP error codes

            data = response.json()
            price = data.get("price")

            if price is None:
                raise Exception(f"Price not found for asset: {asset_symbol}")

            return price

        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}") from http_err
        except requests.exceptions.RequestException as req_err:
            raise Exception(f"Request error occurred: {req_err}") from req_err
        except Exception as general_err:
            raise Exception(f"An error occurred: {general_err}") from general_err

# Example usage
if __name__ == "__main__":
    # Replace with your actual API key
    api_key = "YOUR_API_KEY_HERE"
    oracle_api = NaviOracleAPI(api_key)

    try:
        asset_symbol = "ETH"  # Example asset symbol
        price = oracle_api.get_asset_price(asset_symbol)
        print(f"The current price of {asset_symbol} is: ${price}")
    except Exception as e:
        print(f"Error retrieving asset price: {e}")
```
