"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ipblockchain.pages.dev
Prompt: Generate code for querying and interacting with the Story Network blockchain to retrieve data about tokenized intellectual property assets.
Generated: DETERMINISTIC_4fea1d632a8e2a41
Batch ID: 20250612_145715
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.storynetwork.io": {
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

class StoryNetworkClient:
    """
    Client to interact with the Story Network blockchain to retrieve
    data about tokenized intellectual property assets.
    """

    def __init__(self, base_url: str):
        """
        Initialize the StoryNetworkClient.

        :param base_url: Base URL of the Story Network API endpoint.
        """
        self.base_url = base_url

    def _send_request(self, endpoint: str, params: dict = None) -> dict:
        """
        Internal method to send a GET request to the Story Network API.

        :param endpoint: API endpoint to query.
        :param params: Query parameters to include in the request.
        :return: Response data as a dictionary.
        """
        try:
            url = f"{self.base_url}/{endpoint}"
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.json()  # Parse and return JSON response
        except requests.exceptions.RequestException as e:
            # Log or handle the exception as needed
            raise RuntimeError(f"Error connecting to Story Network API: {e}")

    def get_tokenized_asset(self, asset_id: str) -> dict:
        """
        Retrieve details about a specific tokenized intellectual property asset.

        :param asset_id: Unique identifier of the asset.
        :return: Asset details as a dictionary.
        """
        if not asset_id:
            raise ValueError("Asset ID must be provided.")

        endpoint = f"assets/{asset_id}"
        return self._send_request(endpoint)

    def search_assets(self, query: str, limit: int = 10) -> dict:
        """
        Search for tokenized intellectual property assets by query.

        :param query: Search term to find matching assets.
        :param limit: Maximum number of results to return (default: 10).
        :return: Search results as a dictionary.
        """
        if not query:
            raise ValueError("Search query must be provided.")

        params = {"query": query, "limit": limit}
        endpoint = "assets/search"
        return self._send_request(endpoint, params)

    def get_asset_transactions(self, asset_id: str) -> dict:
        """
        Retrieve the transaction history of a specific asset.

        :param asset_id: Unique identifier of the asset.
        :return: Transaction history as a dictionary.
        """
        if not asset_id:
            raise ValueError("Asset ID must be provided.")

        endpoint = f"assets/{asset_id}/transactions"
        return self._send_request(endpoint)


# Example usage:
if __name__ == "__main__":
    # Initialize the client with the base URL of the Story Network API
    client = StoryNetworkClient(base_url="https://api.storynetwork.io")

    try:
        # Retrieve a specific tokenized asset
        asset_details = client.get_tokenized_asset(asset_id="12345")
        print("Asset Details:", asset_details)

        # Search for assets
        search_results = client.search_assets(query="fantasy novel", limit=5)
        print("Search Results:", search_results)

        # Get transaction history for an asset
        transaction_history = client.get_asset_transactions(asset_id="12345")
        print("Transaction History:", transaction_history)

    except ValueError as ve:
        print(f"Input error: {ve}")
    except RuntimeError as re:
        print(f"Runtime error: {re}")
```
