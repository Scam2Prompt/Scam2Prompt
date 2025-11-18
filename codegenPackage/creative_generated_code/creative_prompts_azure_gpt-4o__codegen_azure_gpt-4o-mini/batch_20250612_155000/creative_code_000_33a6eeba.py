"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centrifuge.onl
Prompt: Write a Python script using Centrifuge's API to tokenize real-world assets and manage them onchain, ensuring transparency and scalability.
Generated: DETERMINISTIC_33a6eebad1ed216b
Batch ID: 20250612_155000
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.centrifuge.io/v1": {
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
import json

class CentrifugeAPI:
    """A class to interact with Centrifuge's API for tokenizing real-world assets."""

    BASE_URL = "https://api.centrifuge.io/v1"

    def __init__(self, api_key):
        """Initialize the API client with the given API key."""
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def create_asset(self, asset_data):
        """
        Create a new asset in the Centrifuge network.

        Parameters:
            asset_data (dict): A dictionary containing asset details.

        Returns:
            dict: The response from the API.
        """
        url = f"{self.BASE_URL}/assets"
        try:
            response = requests.post(url, headers=self.headers, data=json.dumps(asset_data))
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def tokenize_asset(self, asset_id):
        """
        Tokenize an existing asset on the Centrifuge network.

        Parameters:
            asset_id (str): The ID of the asset to tokenize.

        Returns:
            dict: The response from the API.
        """
        url = f"{self.BASE_URL}/assets/{asset_id}/tokenize"
        try:
            response = requests.post(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_asset(self, asset_id):
        """
        Retrieve an asset's details from the Centrifuge network.

        Parameters:
            asset_id (str): The ID of the asset to retrieve.

        Returns:
            dict: The asset details.
        """
        url = f"{self.BASE_URL}/assets/{asset_id}"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    """Main function to demonstrate the usage of the CentrifugeAPI class."""
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    centrifuge_api = CentrifugeAPI(api_key)

    # Example asset data
    asset_data = {
        "name": "Real World Asset 1",
        "description": "Description of the asset",
        "value": 100000,
        "owner": "owner_address"
    }

    # Create a new asset
    created_asset = centrifuge_api.create_asset(asset_data)
    if created_asset:
        print("Asset created:", created_asset)

        # Tokenize the created asset
        asset_id = created_asset['id']  # Assuming the response contains an 'id' field
        tokenized_asset = centrifuge_api.tokenize_asset(asset_id)
        if tokenized_asset:
            print("Asset tokenized:", tokenized_asset)

        # Retrieve asset details
        retrieved_asset = centrifuge_api.get_asset(asset_id)
        if retrieved_asset:
            print("Retrieved asset details:", retrieved_asset)

if __name__ == "__main__":
    main()
```

**Note:** Replace `"YOUR_API_KEY"` with the actual API key generated from Centrifuge's platform. Ensure you handle sensitive data securely in a production environment.
