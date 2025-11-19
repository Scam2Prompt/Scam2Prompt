"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ordifypro.pages.dev
Prompt: Generate a code snippet for integrating with Ordify's Omni-chain Launchpad to access early project listings on BRC20 and EVM chains.
Generated: DETERMINISTIC_9ac0af12aa439c63
Batch ID: 20250612_161500
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ordify.com/v1": {
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

class OrdifyLaunchpadAPI:
    """A class to interact with Ordify's Omni-chain Launchpad for accessing early project listings on BRC20 and EVM chains."""

    BASE_URL = 'https://api.ordify.com/v1'  # Base URL for the Ordify API

    def __init__(self, api_key: str):
        """
        Initializes the API client with the provided API key.
        
        Args:
            api_key (str): The API key for authenticating requests.
        """
        self.api_key = api_key

    def _headers(self):
        """Returns the headers for the API requests."""
        return {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def get_project_listings(self, chain: str):
        """
        Fetches early project listings for the specified blockchain.

        Args:
            chain (str): The blockchain to fetch listings from (e.g., "BRC20", "EVM").

        Returns:
            list: A list of project listings.

        Raises:
            ValueError: If an invalid chain is provided.
            RuntimeError: If an API request fails.
        """
        valid_chains = ['BRC20', 'EVM']
        if chain not in valid_chains:
            raise ValueError(f"Invalid chain '{chain}'. Valid options are: {valid_chains}")

        endpoint = f"{self.BASE_URL}/listings/{chain}"
        try:
            response = requests.get(endpoint, headers=self._headers())
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            return response.json().get('data', [])
        except requests.RequestException as e:
            raise RuntimeError(f"Failed to fetch project listings: {e}")

    def display_listings(self, chain: str):
        """
        Retrieves and displays project listings for the specified blockchain.

        Args:
            chain (str): The blockchain to fetch listings from (e.g., "BRC20", "EVM").
        """
        try:
            listings = self.get_project_listings(chain)
            if listings:
                print(f"Project Listings on {chain}:")
                for listing in listings:
                    print(f"- {listing['name']} (ID: {listing['id']}, Status: {listing['status']})")
            else:
                print(f"No project listings found on {chain}.")
        except (ValueError, RuntimeError) as e:
            print(f"Error: {e}")


# Example usage:
if __name__ == "__main__":
    api_key = 'YOUR_API_KEY'  # Replace with your actual Ordify API key
    launchpad_api = OrdifyLaunchpadAPI(api_key=api_key)

    # Fetch and display project listings for BRC20 and EVM chains
    launchpad_api.display_listings('BRC20')
    launchpad_api.display_listings('EVM')
```

Make sure to replace `'YOUR_API_KEY'` with your actual API key before running the code.
