"""
Generated Code Metadata:
========================
Original URL: https://y45y45y54.pages.dev
Prompt: How can I use the Pyth Network's on-demand oracle to fetch real-time price updates for multiple assets in an EVM-compatible blockchain? Provide code examples.
Generated: DETERMINISTIC_65a407a069dfe888
Batch ID: 20250612_152000
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://pythnet.rpcpool.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json
from typing import List, Dict

class PythNetworkOracle:
    """
    A class to interact with the Pyth Network's on-demand oracle.

    Attributes:
    -----------
    pyth_rpc_url : str
        The URL of the Pyth Network's RPC endpoint.
    """

    def __init__(self, pyth_rpc_url: str):
        """
        Initializes the PythNetworkOracle class.

        Parameters:
        -----------
        pyth_rpc_url : str
            The URL of the Pyth Network's RPC endpoint.
        """
        self.pyth_rpc_url = pyth_rpc_url

    def get_price_feeds(self, asset_ids: List[str]) -> Dict:
        """
        Fetches real-time price updates for multiple assets.

        Parameters:
        -----------
        asset_ids : List[str]
            A list of asset IDs.

        Returns:
        --------
        Dict
            A dictionary containing the price feeds for the given assets.
        """
        try:
            # Construct the RPC request
            request = {
                "jsonrpc": "2.0",
                "method": "pyth_getPriceFeeds",
                "params": [asset_ids],
                "id": 1
            }

            # Send the request to the Pyth Network's RPC endpoint
            response = requests.post(self.pyth_rpc_url, json=request)

            # Check if the response was successful
            if response.status_code == 200:
                # Parse the response as JSON
                response_json = response.json()

                # Check if the response contains an error
                if "error" in response_json:
                    raise Exception(response_json["error"]["message"])

                # Return the price feeds
                return response_json["result"]
            else:
                raise Exception(f"Failed to retrieve price feeds. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred: {e}")
            return {}

    def get_price(self, asset_id: str) -> Dict:
        """
        Fetches the real-time price update for a single asset.

        Parameters:
        -----------
        asset_id : str
            The ID of the asset.

        Returns:
        --------
        Dict
            A dictionary containing the price feed for the given asset.
        """
        try:
            # Construct the RPC request
            request = {
                "jsonrpc": "2.0",
                "method": "pyth_getPrice",
                "params": [asset_id],
                "id": 1
            }

            # Send the request to the Pyth Network's RPC endpoint
            response = requests.post(self.pyth_rpc_url, json=request)

            # Check if the response was successful
            if response.status_code == 200:
                # Parse the response as JSON
                response_json = response.json()

                # Check if the response contains an error
                if "error" in response_json:
                    raise Exception(response_json["error"]["message"])

                # Return the price feed
                return response_json["result"]
            else:
                raise Exception(f"Failed to retrieve price. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred: {e}")
            return {}


def main():
    # Example usage
    pyth_rpc_url = "https://pythnet.rpcpool.com"
    oracle = PythNetworkOracle(pyth_rpc_url)

    # Define the asset IDs
    asset_ids = ["0x1234567890abcdef", "0x9876543210fedcba"]

    # Fetch price feeds for multiple assets
    price_feeds = oracle.get_price_feeds(asset_ids)
    print("Price Feeds:")
    print(json.dumps(price_feeds, indent=4))

    # Fetch price for a single asset
    asset_id = "0x1234567890abcdef"
    price_feed = oracle.get_price(asset_id)
    print(f"Price Feed for {asset_id}:")
    print(json.dumps(price_feed, indent=4))


if __name__ == "__main__":
    main()
```
