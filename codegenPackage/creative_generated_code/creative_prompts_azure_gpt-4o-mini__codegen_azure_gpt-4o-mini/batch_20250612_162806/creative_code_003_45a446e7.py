"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherscan-explorer.com
Prompt: Generate a code snippet that interacts with the Etherscan API to get the current Ether price and market cap.
Generated: DETERMINISTIC_45a446e759d7096c
Batch ID: 20250612_162806
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api": {
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

class EtherscanAPI:
    """
    A class to interact with the Etherscan API for retrieving Ethereum data.
    """

    BASE_URL = 'https://api.etherscan.io/api'

    def __init__(self, api_key):
        """
        Initializes the EtherscanAPI with the provided API key.

        :param api_key: Your Etherscan API key.
        """
        self.api_key = api_key

    def get_current_ether_data(self):
        """
        Fetches the current Ether price and market cap from the Etherscan API.

        :return: A dictionary containing the price and market cap of Ether.
        :raises ValueError: If the response does not contain valid data.
        :raises Exception: For any other errors related to the API request.
        """
        params = {
            'module': 'stats',
            'action': 'ethprice',
            'apikey': self.api_key
        }

        try:
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()  # Raise an error for bad HTTP response codes.
            data = response.json()  # Parse the JSON response.

            if 'result' not in data:
                raise ValueError("Invalid response format: 'result' key not found.")

            return {
                'eth_price': float(data['result']['ethusd']),
                'market_cap': float(data['result']['ethusd_marketcap'])
            }
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {e}")
        except ValueError as e:
            raise ValueError(f"Error parsing response: {e}")

if __name__ == "__main__":
    # Example usage
    API_KEY = 'YOUR_ETHERSCAN_API_KEY'  # Replace with your Etherscan API key
    etherscan = EtherscanAPI(API_KEY)

    try:
        ether_data = etherscan.get_current_ether_data()
        print(f"Current Ether Price (USD): {ether_data['eth_price']}")
        print(f"Ether Market Cap (USD): {ether_data['market_cap']}")
    except Exception as e:
        print(f"Error: {e}")
```

Make sure to replace `'YOUR_ETHERSCAN_API_KEY'` with your actual Etherscan API key before running the code.
