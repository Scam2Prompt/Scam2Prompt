"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matrica18.vercel.app
Prompt: Generate a script to fetch and display stats for blockchain networks like Solana, Ethereum, and Polygon, inspired by the functionality described on Matrica.
Generated: DETERMINISTIC_2a57071d07b92d4a
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
  "https://api.solana.com": {
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
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import json

class BlockchainStatsFetcher:
    """
    A class to fetch and display stats for various blockchain networks.
    Currently supports Solana, Ethereum, and Polygon.
    """
    
    BASE_URLS = {
        'solana': 'https://api.solana.com',
        'ethereum': 'https://api.etherscan.io/api',
        'polygon': 'https://api.polygonscan.com/api'
    }

    def __init__(self):
        """
        Initializes the BlockchainStatsFetcher instance.
        """
        self.network_data = {}

    def fetch_solana_stats(self):
        """
        Fetches stats from the Solana API.
        """
        try:
            response = requests.post(self.BASE_URLS['solana'], json={"jsonrpc":"2.0","id":1,"method":"getHealth"});
            response.raise_for_status()
            self.network_data['solana'] = response.json()
        except requests.RequestException as e:
            print(f"Error fetching Solana stats: {e}")

    def fetch_ethereum_stats(self):
        """
        Fetches stats from the Ethereum API (Etherscan).
        """
        params = {
            'module': 'stats',
            'action': 'ethsupply',
            'apikey': 'YourEtherscanAPIKey'  # Replace with your Etherscan API key
        }
        try:
            response = requests.get(self.BASE_URLS['ethereum'], params=params)
            response.raise_for_status()
            self.network_data['ethereum'] = response.json()
        except requests.RequestException as e:
            print(f"Error fetching Ethereum stats: {e}")

    def fetch_polygon_stats(self):
        """
        Fetches stats from the Polygon API (Polygonscan).
        """
        params = {
            'module': 'stats',
            'action': 'ethsupply',
            'apikey': 'YourPolygonscanAPIKey'  # Replace with your Polygonscan API key
        }
        try:
            response = requests.get(self.BASE_URLS['polygon'], params=params)
            response.raise_for_status()
            self.network_data['polygon'] = response.json()
        except requests.RequestException as e:
            print(f"Error fetching Polygon stats: {e}")

    def fetch_all_stats(self):
        """
        Fetches stats for all supported blockchains.
        """
        self.fetch_solana_stats()
        self.fetch_ethereum_stats()
        self.fetch_polygon_stats()

    def display_stats(self):
        """
        Displays the fetched stats in a human-readable format.
        """
        for network, data in self.network_data.items():
            print(f"\nStats for {network.capitalize()}:")
            print(json.dumps(data, indent=4))

if __name__ == "__main__":
    stats_fetcher = BlockchainStatsFetcher()
    stats_fetcher.fetch_all_stats()
    stats_fetcher.display_stats()
```

**Note:** Replace `'YourEtherscanAPIKey'` and `'YourPolygonscanAPIKey'` with valid API keys to fetch the data correctly. Ensure you have `requests` library installed in your environment (`pip install requests`).
