"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matrica16.vercel.app
Prompt: Generate code for displaying network statistics for Solana, Ethereum, and Polygon, inspired by the stats section on the Matrica website.
Generated: DETERMINISTIC_8ae7fc768a68ae47
Batch ID: 20250612_153225
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import json
import logging
from typing import Dict, Any

# Set up logging for error handling
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NetworkStatsFetcher:
    """Class to fetch network statistics for Solana, Ethereum, and Polygon."""

    def __init__(self):
        self.base_urls = {
            'solana': 'https://api.mainnet-beta.solana.com',
            'ethereum': 'https://api.etherscan.io/api',
            'polygon': 'https://api.polygonscan.com/api'
        }
        self.api_keys = {
            'ethereum': 'YOUR_ETHERSCAN_API_KEY',
            'polygon': 'YOUR_POLYGONSCAN_API_KEY'
        }

    def fetch_stats(self, network: str) -> Dict[str, Any]:
        """Fetch network statistics for the given network."""
        try:
            if network == 'solana':
                return self._fetch_solana_stats()
            elif network == 'ethereum':
                return self._fetch_ethereum_stats()
            elif network == 'polygon':
                return self._fetch_polygon_stats()
            else:
                raise ValueError("Unsupported network specified.")
        except Exception as e:
            logging.error(f"Error fetching stats for {network}: {e}")
            return {}

    def _fetch_solana_stats(self) -> Dict[str, Any]:
        """Fetch Solana network statistics."""
        # Example RPC request; modify endpoint as needed
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getEpochInfo",
            "params": []
        }
        response = requests.post(self.base_urls['solana'], json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json().get('result', {})

    def _fetch_ethereum_stats(self) -> Dict[str, Any]:
        """Fetch Ethereum network statistics."""
        params = {
            'module': 'stats',
            'action': 'ethsupply',
            'apikey': self.api_keys['ethereum']
        }
        response = requests.get(self.base_urls['ethereum'], params=params)
        response.raise_for_status()
        return response.json().get('result', {})

    def _fetch_polygon_stats(self) -> Dict[str, Any]:
        """Fetch Polygon network statistics."""
        params = {
            'module': 'stats',
            'action': 'ethsupply',
            'apikey': self.api_keys['polygon']
        }
        response = requests.get(self.base_urls['polygon'], params=params)
        response.raise_for_status()
        return response.json().get('result', {})

def main():
    """Main function to display network statistics."""
    fetcher = NetworkStatsFetcher()
    
    networks = ['solana', 'ethereum', 'polygon']
    for network in networks:
        stats = fetcher.fetch_stats(network)
        print(f"{network.capitalize()} Stats: {json.dumps(stats, indent=2)}")

if __name__ == "__main__":
    main()
```
