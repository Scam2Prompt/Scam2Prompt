"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypto-moments-git-feature-burn-freshdrops.vercel.app
Prompt: Generate a script to query and display NFT collections from "My Collection" using the Crypto Moments API.
Generated: DETERMINISTIC_64916b7eb9035984
Batch ID: 20250612_153648
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.cryptomoments.com": {
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

class CryptoMomentsAPI:
    """
    A class to interact with the Crypto Moments API for retrieving NFT collections.
    """

    BASE_URL = "https://api.cryptomoments.com"

    def __init__(self, user_id):
        """
        Initializes the API client with the user's ID.

        :param user_id: The ID of the user whose NFT collection will be queried.
        """
        self.user_id = user_id

    def get_nft_collections(self):
        """
        Retrieves the NFT collections for the specified user.

        :return: A list of NFT collections or an error message.
        """
        url = f"{self.BASE_URL}/collections/{self.user_id}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises a HTTPError for bad responses
            collections = response.json()  # Parse JSON response
            return collections
        except requests.exceptions.HTTPError as http_err:
            return {'error': f'HTTP error occurred: {http_err}'}
        except requests.exceptions.RequestException as req_err:
            return {'error': f'Request error occurred: {req_err}'}
        except ValueError as json_err:
            return {'error': f'Error parsing JSON response: {json_err}'}

    def display_collections(self):
        """
        Displays the NFT collections in a formatted way.
        """
        collections = self.get_nft_collections()

        if 'error' in collections:
            print(collections['error'])  # Print error message if any
        else:
            print("NFT Collections:")
            for collection in collections:
                print(f" - Name: {collection['name']}, Items: {collection['item_count']}")

def main():
    """
    Main function to run the script.
    """
    user_id = input("Enter your user ID: ")
    api_client = CryptoMomentsAPI(user_id)
    api_client.display_collections()

if __name__ == "__main__":
    main()
```
