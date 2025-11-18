"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zapper-frontend-next-mh2dokjx4-zapper-fi.vercel.app
Prompt: Write code using Zapper's Beta API to track wallet activity, including NFTs, DAOs, and DeFi transactions, for a specific Ethereum address.
Generated: DETERMINISTIC_c3ad12f51810b448
Batch ID: 20250612_151644
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.zapper.fi/v2": {
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

class ZapperAPI:
    """
    A class to interact with Zapper's Beta API for tracking wallet activity.
    """

    BASE_URL = 'https://api.zapper.fi/v2'

    def __init__(self, api_key):
        """
        Initializes the ZapperAPI with the provided API key.

        :param api_key: str - API key for Zapper's Beta API
        """
        self.api_key = api_key

    def get_wallet_activity(self, wallet_address):
        """
        Retrieves wallet activity for a specific Ethereum address, including NFTs, DAOs, and DeFi transactions.

        :param wallet_address: str - The Ethereum address to track
        :return: dict - The wallet activity data
        :raises ValueError: If the wallet address is invalid
        :raises Exception: For any issues during the API request
        """
        if not self.is_valid_ethereum_address(wallet_address):
            raise ValueError("Invalid Ethereum address format.")

        url = f'{self.BASE_URL}/transactions'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}',
        }

        params = {
            'addresses[]': wallet_address,
            'chain': 'ethereum',
            'limit': 50,  # You can adjust this limit as needed
        }

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            print(f"An error occurred: {err}")
            raise

    @staticmethod
    def is_valid_ethereum_address(address):
        """
        Validates the Ethereum address format.

        :param address: str - The Ethereum address to validate
        :return: bool - True if valid, False otherwise
        """
        # Simple checksum validation can be implemented here
        return len(address) == 42 and address.startswith('0x')

# Example usage:
if __name__ == "__main__":
    ZAPPER_API_KEY = 'your_api_key_here'
    wallet_address = '0xYourEthereumAddressHere'

    zapper_api = ZapperAPI(ZAPPER_API_KEY)
    
    try:
        activity = zapper_api.get_wallet_activity(wallet_address)
        print(json.dumps(activity, indent=4))  # Print the activity data in a readable format
    except Exception as e:
        print(f"Failed to fetch wallet activity: {e}")
```

Make sure to replace `'your_api_key_here'` and `'0xYourEthereumAddressHere'` with the actual Zapper API key and the Ethereum address you want to track.
