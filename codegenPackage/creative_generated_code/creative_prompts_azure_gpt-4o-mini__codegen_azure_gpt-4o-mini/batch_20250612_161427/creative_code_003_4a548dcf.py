"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tangocrypto-website.pages.dev
Prompt: Provide an example of using Tangocrypto's API to retrieve data from the Cardano network for a developer project.
Generated: DETERMINISTIC_4a548dcf1077f4f8
Batch ID: 20250612_161427
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.tangocrypto.com/v1/cardano": {
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

class CardanoAPI:
    """
    A class to interact with the Tangocrypto API for retrieving Cardano network data.
    """

    BASE_URL = "https://api.tangocrypto.com/v1/cardano"

    def __init__(self, api_key):
        """
        Initializes the CardanoAPI with the provided API key.

        Args:
            api_key (str): The API key for authenticating requests to the Tangocrypto API.
        """
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def get_block_info(self, block_id):
        """
        Retrieves information about a specific block on the Cardano network.

        Args:
            block_id (str): The ID of the block to retrieve information for.

        Returns:
            dict: The block information if successful, or an error message.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/blocks/{block_id}", headers=self.headers)
            response.raise_for_status()  # Raise an error for HTTP errors
            return response.json()  # Return the block information as a JSON dictionary
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except requests.exceptions.RequestException as req_err:
            return {"error": f"Request error occurred: {req_err}"}

    def get_latest_block(self):
        """
        Retrieves the latest block information from the Cardano network.

        Returns:
            dict: The latest block information if successful, or an error message.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/blocks/latest", headers=self.headers)
            response.raise_for_status()  # Raise an error for HTTP errors
            return response.json()  # Return the latest block information as a JSON dictionary
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except requests.exceptions.RequestException as req_err:
            return {"error": f"Request error occurred: {req_err}"}

# Example usage
if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual Tangocrypto API key
    api_key = 'YOUR_API_KEY'
    cardano_api = CardanoAPI(api_key)

    # Get information about a specific block
    block_id = "some_block_id"  # Replace with a valid block ID
    block_info = cardano_api.get_block_info(block_id)
    print(block_info)

    # Get information about the latest block
    latest_block_info = cardano_api.get_latest_block()
    print(latest_block_info)
```
