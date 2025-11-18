"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matrica17.vercel.app
Prompt: Generate code to fetch stats and events from the Ethereum blockchain, ensuring compatibility with APIs that allow switching between networks like Solana, Ethereum, and Polygon.
Generated: DETERMINISTIC_5418d2877baf81cf
Batch ID: 20250612_153401
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.solscan.io/v1.0": {
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

class BlockchainAPIClient:
    """A client to interact with multiple blockchain networks."""

    def __init__(self, network='ethereum'):
        """
        Initialize the API client.

        Args:
            network (str): The blockchain network to connect to. 
                           Options: 'ethereum', 'solana', 'polygon'.
        """
        self.network = network
        self.base_url = self.get_base_url(network)

    def get_base_url(self, network):
        """
        Get the base URL for the specified network.

        Args:
            network (str): The blockchain network.

        Returns:
            str: The base URL for the API.
        """
        network_urls = {
            'ethereum': 'https://api.etherscan.io/api',
            'solana': 'https://api.solscan.io/v1.0',
            'polygon': 'https://api.polygonscan.com/api'
        }
        return network_urls.get(network, 'https://api.etherscan.io/api')

    def fetch_stats(self):
        """Fetch general stats from the current network."""
        try:
            response = requests.get(self.base_url, params={'module': 'stats', 'action': 'ethstats'})
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching stats: {e}")
            return None

    def fetch_events(self, address, event_signature):
        """
        Fetch events from a specified address on the current network.

        Args:
            address (str): The blockchain address to fetch events from.
            event_signature (str): The event signature to filter events.

        Returns:
            dict: The events data, or None if an error occurs.
        """
        try:
            params = {
                'module': 'logs',
                'action': 'getLogs',
                'address': address,
                'topic0': event_signature,
                'apikey': 'YourAPIKeyHere'  # Replace with your actual API key for respective networks
            }
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching events: {e}")
            return None

    def switch_network(self, new_network):
        """
        Switch the blockchain network for the client.

        Args:
            new_network (str): The new blockchain network to connect to.
        """
        if new_network in ['ethereum', 'solana', 'polygon']:
            self.network = new_network
            self.base_url = self.get_base_url(new_network)
        else:
            print(f"Network '{new_network}' is not supported.")

# Example usage
if __name__ == "__main__":
    client = BlockchainAPIClient('ethereum')
    
    # Fetch Ethereum stats
    stats = client.fetch_stats()
    print("Ethereum Stats:", stats)

    # Fetch events for a specific address and event signature
    address = '0xYourAddressHere'
    event_signature = '0xYourEventSignatureHere'
    events = client.fetch_events(address, event_signature)
    print("Fetched Events:", events)

    # Switch to Polygon
    client.switch_network('polygon')
    print("Switched to Polygon network.")
```
