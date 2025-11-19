"""
Generated Code Metadata:
========================
Original URL: https://matrica17.vercel.app
Prompt: Provide an example of querying blockchain stats across Solana, Ethereum, and Polygon networks using a multi-network API integration similar to Matrica17.
Generated: DETERMINISTIC_2c85a2e7a7329e0e
Batch ID: 20250612_153401
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.polygonscan.com/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests

class BlockchainStats:
    """
    A class to query blockchain statistics across multiple networks: Solana, Ethereum, and Polygon.
    """

    def __init__(self):
        # Base URLs for the respective blockchain APIs
        self.api_urls = {
            'solana': 'https://api.solana.com',
            'ethereum': 'https://api.etherscan.io/api',
            'polygon': 'https://api.polygonscan.com/api'
        }

    def get_solana_stats(self):
        """
        Fetches statistics from the Solana blockchain.
        """
        try:
            response = requests.get(f"{self.api_urls['solana']}/stats")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching Solana stats: {e}")
            return None

    def get_ethereum_stats(self):
        """
        Fetches statistics from the Ethereum blockchain.
        """
        params = {
            'module': 'stats',
            'action': 'ethsupply',
            'apikey': 'YourEtherscanAPIKey'  # Replace with your Etherscan API key
        }
        try:
            response = requests.get(self.api_urls['ethereum'], params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching Ethereum stats: {e}")
            return None

    def get_polygon_stats(self):
        """
        Fetches statistics from the Polygon blockchain.
        """
        params = {
            'module': 'stats',
            'action': 'ethsupply',
            'apikey': 'YourPolygonscanAPIKey'  # Replace with your Polygonscan API key
        }
        try:
            response = requests.get(self.api_urls['polygon'], params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching Polygon stats: {e}")
            return None

    def get_all_stats(self):
        """
        Fetches statistics from all supported blockchains.
        """
        stats = {
            'solana': self.get_solana_stats(),
            'ethereum': self.get_ethereum_stats(),
            'polygon': self.get_polygon_stats()
        }
        return stats


if __name__ == "__main__":
    blockchain_stats = BlockchainStats()
    all_stats = blockchain_stats.get_all_stats()
    
    # Print the fetched statistics
    if all_stats:
        print("Blockchain Statistics:")
        for network, stats in all_stats.items():
            print(f"{network.capitalize()}: {stats}")
```

**Note:** Replace `'YourEtherscanAPIKey'` and `'YourPolygonscanAPIKey'` with your actual API keys for Etherscan and Polygonscan respectively.
