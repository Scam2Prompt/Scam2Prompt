"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fr.habbometa.com
Prompt: Provide code to display the status of claimed and unclaimed NFTs for a Habbo account, ensuring the data matches the format shown on the webpage (e.g., "NFTs réclamés 0/1").
Generated: DETERMINISTIC_1462a30e89b0e5d5
Batch ID: 20250612_145114
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.habbo.com/nft-status/{self.username": {
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

class HabboNFTStatus:
    """
    A class to fetch and display the status of claimed and unclaimed NFTs for a Habbo account.
    """

    def __init__(self, username):
        """
        Initialize the HabboNFTStatus class with the user's Habbo username.

        :param username: The Habbo username for which to retrieve NFT status.
        """
        self.username = username
        self.nfts_claimed = 0
        self.nfts_total = 0
        self.api_endpoint = f"https://api.habbo.com/nft-status/{self.username}"

    def fetch_nft_data(self):
        """
        Fetch the NFT data from the Habbo API.

        :raises Exception: If there is an error during the API request.
        """
        try:
            response = requests.get(self.api_endpoint)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()

            self.nfts_claimed = data.get('claimed', 0)
            self.nfts_total = data.get('total', 0)
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
            raise
        except ValueError as json_err:
            print(f"JSON decode error: {json_err}")
            raise

    def display_nft_status(self):
        """
        Display the claimed and unclaimed NFTs in the format "NFTs réclamés 0/1".
        """
        claimed = self.nfts_claimed
        total = self.nfts_total
        print(f"NFTs réclamés {claimed}/{total}")

if __name__ == "__main__":
    # Replace 'YourHabboUsername' with the actual Habbo username
    habbo_username = "YourHabboUsername"
    
    nft_status = HabboNFTStatus(habbo_username)
    
    # Fetch NFT data and display the status
    try:
        nft_status.fetch_nft_data()
        nft_status.display_nft_status()
    except Exception as e:
        print(f"An error occurred while retrieving NFT status: {e}")
```
