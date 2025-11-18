"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect.foundation
Prompt: Provide an example of how to use the WalletGuide API to fetch a list of onchain wallets that meet specific UX and security standards.
Generated: DETERMINISTIC_1989d3c2467ac976
Batch ID: 20250612_150323
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.walletguide.com/v1/wallets": {
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

class WalletGuideAPI:
    """
    A simple client for interacting with the WalletGuide API to fetch
    a list of on-chain wallets that meet specific UX and security standards.
    """

    BASE_URL = "https://api.walletguide.com/v1/wallets"

    def __init__(self, api_key):
        """
        Initializes the WalletGuideAPI client with the provided API key.

        :param api_key: The API key for authenticating requests.
        """
        self.api_key = api_key

    def fetch_wallets(self, ux_rating=None, security_rating=None):
        """
        Fetches a list of on-chain wallets based on UX and security ratings.

        :param ux_rating: Optional; filter wallets based on UX rating.
        :param security_rating: Optional; filter wallets based on security rating.
        :return: A list of wallets that meet the specified criteria.
        :raises ValueError: If invalid parameters are provided.
        :raises requests.HTTPError: If the API request fails.
        """
        # Validate input parameters
        if ux_rating and (ux_rating < 1 or ux_rating > 5):
            raise ValueError("UX rating must be between 1 and 5.")
        if security_rating and (security_rating < 1 or security_rating > 5):
            raise ValueError("Security rating must be between 1 and 5.")

        # Prepare query parameters
        params = {}
        if ux_rating:
            params['ux_rating'] = ux_rating
        if security_rating:
            params['security_rating'] = security_rating

        # Set up headers for authentication
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            # Send GET request to the WalletGuide API
            response = requests.get(self.BASE_URL, headers=headers, params=params)
            # Raise an error for bad responses
            response.raise_for_status()

            # Parse and return JSON response
            return response.json()

        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the error
            raise
        except Exception as err:
            print(f"An error occurred: {err}")  # Log other errors
            raise


if __name__ == "__main__":
    # Example usage of the WalletGuideAPI

    # Replace 'YOUR_API_KEY_HERE' with your actual WalletGuide API key
    api_key = "YOUR_API_KEY_HERE"

    # Create an instance of the WalletGuideAPI
    wallet_guide = WalletGuideAPI(api_key)

    try:
        # Fetch wallets with specific UX and security ratings
        wallets = wallet_guide.fetch_wallets(ux_rating=4, security_rating=5)
        print("Fetched wallets:", wallets)

    except ValueError as ve:
        print(f"Value Error: {ve}")  # Handle invalid input parameters
    except Exception as e:
        print(f"An error occurred while fetching wallets: {e}")  # Handle other exceptions
```
