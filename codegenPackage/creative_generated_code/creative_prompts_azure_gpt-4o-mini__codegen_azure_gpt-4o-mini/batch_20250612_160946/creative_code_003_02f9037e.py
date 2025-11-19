"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earthmeta-ai.pages.dev
Prompt: Provide an example of how to integrate the EarthMeta AR app with a user's wallet for real-time token tracking.
Generated: DETERMINISTIC_02f9037e9854aa05
Batch ID: 20250612_160946
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com": {
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
import json
import requests

class WalletIntegrationError(Exception):
    """Custom exception for Wallet Integration errors."""
    pass

class EarthMetaWallet:
    def __init__(self, wallet_address, api_url):
        """
        Initialize the EarthMetaWallet with a user's wallet address and API URL.
        
        Args:
            wallet_address (str): The user's wallet address.
            api_url (str): The API URL for token tracking.
        """
        self.wallet_address = wallet_address
        self.api_url = api_url

    def fetch_tokens(self):
        """
        Fetch the tokens associated with the user's wallet address.

        Returns:
            dict: A dictionary containing token information.

        Raises:
            WalletIntegrationError: If the API request fails.
        """
        try:
            response = requests.get(f"{self.api_url}/wallets/{self.wallet_address}/tokens")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Parse the JSON response
        except requests.RequestException as e:
            raise WalletIntegrationError(f"Failed to fetch tokens: {e}")

    def display_tokens(self):
        """
        Display the tokens in a user-friendly format.
        """
        try:
            tokens = self.fetch_tokens()
            print("Tokens in Wallet:")
            for token in tokens.get("tokens", []):
                name = token.get("name", "Unknown Token")
                balance = token.get("balance", 0)
                print(f"{name}: {balance}")
        except WalletIntegrationError as e:
            print(e)

# Example usage
if __name__ == "__main__":
    # Define the wallet address and API URL
    USER_WALLET_ADDRESS = "0x1234567890abcdef1234567890abcdef12345678"
    API_URL = "https://api.example.com"

    # Create an instance of EarthMetaWallet
    wallet_integration = EarthMetaWallet(USER_WALLET_ADDRESS, API_URL)

    # Display the user's tokens
    wallet_integration.display_tokens()
```
