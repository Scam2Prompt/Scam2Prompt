"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-swiftchain.pages.dev
Prompt: Write a Python script to retrieve supported tokens and chains from the Multichain API and display them in a user-friendly format.
Generated: DETERMINISTIC_69fd291e73ab6578
Batch ID: 20250612_150858
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.multichain.com/v1": {
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

class MultichainAPI:
    """Class to interact with the Multichain API."""

    BASE_URL = "https://api.multichain.com/v1"  # Base URL for the Multichain API

    def __init__(self):
        """Initialize the MultichainAPI instance."""
        self.session = requests.Session()  # Create a session for requests

    def get_supported_tokens(self):
        """Retrieve the list of supported tokens from the Multichain API.

        Returns:
            list: A list of supported tokens.

        Raises:
            Exception: If the API request fails or returns an error.
        """
        try:
            response = self.session.get(f"{self.BASE_URL}/tokens")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to retrieve tokens: {e}")

    def get_supported_chains(self):
        """Retrieve the list of supported chains from the Multichain API.

        Returns:
            list: A list of supported chains.

        Raises:
            Exception: If the API request fails or returns an error.
        """
        try:
            response = self.session.get(f"{self.BASE_URL}/chains")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to retrieve chains: {e}")

    def display_info(self):
        """Retrieve and display supported tokens and chains in a user-friendly format."""
        try:
            tokens = self.get_supported_tokens()  # Get supported tokens
            chains = self.get_supported_chains()  # Get supported chains
            
            print("Supported Tokens:")
            for token in tokens:
                print(f"- {token['name']} (Symbol: {token['symbol']})")

            print("\nSupported Chains:")
            for chain in chains:
                print(f"- {chain['name']} (ID: {chain['id']})")

        except Exception as e:
            print(f"Error: {e}")  # Handle any errors during retrieval

if __name__ == "__main__":
    """Main execution block to run the script."""
    api = MultichainAPI()  # Create an instance of the MultichainAPI
    api.display_info()  # Display supported tokens and chains
```
