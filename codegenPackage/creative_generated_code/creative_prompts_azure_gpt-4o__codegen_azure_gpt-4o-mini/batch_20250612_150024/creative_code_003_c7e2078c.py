"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hashpack.co
Prompt: Provide an example of how to bulk modify NFT listings using the SentX API for the Hedera ecosystem.
Generated: DETERMINISTIC_c7e2078c016c6c2a
Batch ID: 20250612_150024
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sentx.io/v1": {
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
from typing import List, Dict

class SentXAPI:
    """
    A class to interact with the SentX API for bulk modifying NFT listings.
    """

    BASE_URL = "https://api.sentx.io/v1"  # Base URL for SentX API

    def __init__(self, api_key: str):
        """
        Initializes the SentXAPI with the provided API key.

        Parameters:
        api_key (str): The API key for authenticating with the SentX API.
        """
        self.api_key = api_key

    def bulk_modify_nft_listings(self, nft_listings: List[Dict]) -> Dict:
        """
        Modifies multiple NFT listings in bulk.

        Parameters:
        nft_listings (List[Dict]): A list of dictionaries containing NFT listing details.

        Returns:
        Dict: The response from the SentX API.
        """
        endpoint = f"{self.BASE_URL}/nft/bulk-modify"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(endpoint, json={"listings": nft_listings}, headers=headers)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()  # Return the JSON response if successful
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")  # Log other request errors
        except Exception as e:
            print(f"An error occurred: {e}")  # Log any other errors

        return {}  # Return an empty dict on error

# Example usage
if __name__ == "__main__":
    # Replace with your actual API key
    API_KEY = "your_api_key_here"

    # Init SentXAPI instance
    sentx_api = SentXAPI(api_key=API_KEY)

    # Sample NFT listings to modify
    listings_to_modify = [
        {"nft_id": "nft1", "price": 150, "is_available": True},
        {"nft_id": "nft2", "price": 200, "is_available": False},
        {"nft_id": "nft3", "price": 300, "is_available": True}
    ]

    # Perform bulk modification
    response = sentx_api.bulk_modify_nft_listings(listings_to_modify)

    # Print the response
    print(response)
```
