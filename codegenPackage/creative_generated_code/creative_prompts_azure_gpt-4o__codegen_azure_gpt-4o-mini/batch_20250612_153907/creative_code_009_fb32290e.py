"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blastscan.github.io
Prompt: Write a Python script to compare token performance across multiple blockchains using Blastscan's cross-chain analytics features.
Generated: DETERMINISTIC_fb32290e3d8bc41d
Batch ID: 20250612_153907
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.blastscan.io": {
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

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TokenPerformanceComparer:
    """
    A class to compare token performance across multiple blockchains using Blastscan's analytics features.
    """

    def __init__(self, api_key: str, base_url: str = "https://api.blastscan.io"):
        """
        Initializes the comparer with the API key and base URL.

        Arguments:
        api_key -- The API key for authenticating requests.
        base_url -- The base URL for the Blastscan API (default is set).
        """
        self.api_key = api_key
        self.base_url = base_url

    def fetch_token_data(self, blockchain: str, token: str):
        """
        Fetch token performance data from Blastscan API.

        Arguments:
        blockchain -- The blockchain to query.
        token -- The token to query.

        Returns:
        A dictionary with token performance data.

        Raises:
        Exception if the API request fails.
        """
        url = f"{self.base_url}/analytics/{blockchain}/{token}"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            raise Exception("Failed to fetch token data.")
        except Exception as err:
            logging.error(f"An error occurred: {err}")
            raise Exception("An unexpected error occurred.")

    def compare_tokens(self, blockchains: list, token: str):
        """
        Compare performance data for a specific token across multiple blockchains.

        Arguments:
        blockchains -- A list of blockchains to compare.
        token -- The token to compare.

        Returns:
        A dictionary with performance data from each blockchain.
        """
        performance_data = {}
        
        for blockchain in blockchains:
            logging.info(f"Fetching data for token '{token}' on blockchain '{blockchain}'")
            try:
                data = self.fetch_token_data(blockchain, token)
                performance_data[blockchain] = data
            except Exception as e:
                logging.error(f"Error fetching data for {blockchain}: {str(e)}")
                performance_data[blockchain] = None  # Record failure for that blockchain

        return performance_data

if __name__ == "__main__":
    # Example usage of the TokenPerformanceComparer
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    blockchains = ["Ethereum", "BinanceSmartChain", "Polygon"]
    token = "USDT"

    comparer = TokenPerformanceComparer(API_KEY)
    performance_comparison = comparer.compare_tokens(blockchains, token)

    # Output the performance comparison
    for blockchain, data in performance_comparison.items():
        if data:
            logging.info(f"Performance data for {token} on {blockchain}: {data}")
        else:
            logging.warning(f"No data available for {token} on {blockchain}.")
```
