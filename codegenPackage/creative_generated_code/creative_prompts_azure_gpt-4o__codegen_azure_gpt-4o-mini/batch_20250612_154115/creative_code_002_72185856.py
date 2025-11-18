"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pc.bigwhales.com
Prompt: Generate a script to fetch real-time data for gold and oil prices using an API that aligns with Bigwhales' investment platform capabilities.
Generated: DETERMINISTIC_72185856560c5e44
Batch ID: 20250612_154115
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/v1/prices": {
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
import logging
from datetime import datetime

# Configure logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InvestmentDataFetcher:
    """
    A class to fetch real-time prices for gold and oil using an external API.
    """

    def __init__(self, api_key: str):
        """
        Initializes the InvestmentDataFetcher with the given API key.

        :param api_key: str - The API key for authenticating requests to the price data API.
        """
        self.api_key = api_key
        self.base_url = "https://api.example.com/v1/prices"  # Replace with the actual API URL

    def fetch_prices(self):
        """
        Fetches the latest prices for gold and oil.

        :return: dict - A dictionary containing gold and oil prices, or an error message.
        """
        try:
            response = requests.get(self.base_url, headers={'Authorization': f'Bearer {self.api_key}'})
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

            data = response.json()
            prices = {
                'gold': data.get('gold', {}).get('price'),
                'oil': data.get('oil', {}).get('price'),
                'timestamp': datetime.now().isoformat()
            }
            logging.info("Successfully fetched prices: %s", prices)
            return prices

        except requests.exceptions.HTTPError as http_err:
            logging.error(f'HTTP error occurred: {http_err}')
            return {'error': 'Failed to fetch prices due to HTTP error.'}
        except requests.exceptions.RequestException as req_err:
            logging.error(f'Request error occurred: {req_err}')
            return {'error': 'Failed to fetch prices due to request error.'}
        except Exception as e:
            logging.error(f'An unexpected error occurred: {e}')
            return {'error': 'An unexpected error occurred.'}

if __name__ == "__main__":
    # Replace 'your_api_key_here' with your actual API key
    api_key = 'your_api_key_here'
    
    fetcher = InvestmentDataFetcher(api_key)
    prices = fetcher.fetch_prices()
    
    if 'error' not in prices:
        print(f"Gold Price: {prices['gold']}, Oil Price: {prices['oil']}, Timestamp: {prices['timestamp']}")
    else:
        print(prices['error'])
```
