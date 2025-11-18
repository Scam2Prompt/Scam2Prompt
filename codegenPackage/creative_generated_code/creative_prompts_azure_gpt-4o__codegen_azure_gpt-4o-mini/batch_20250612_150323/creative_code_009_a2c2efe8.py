"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect.foundation
Prompt: Create a script to fetch and display ecosystem partner data from the WalletConnect Network API, including app and wallet statistics.
Generated: DETERMINISTIC_a2c2efe881f429f6
Batch ID: 20250612_150323
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.walletconnect.org/v1/": {
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

class WalletConnectAPI:
    """Class to interact with the WalletConnect Network API."""

    BASE_URL = "https://api.walletconnect.org/v1/"

    def __init__(self):
        """Initialize the API client."""
        self.session = requests.Session()

    def fetch_partners_data(self):
        """Fetch ecosystem partner data from the WalletConnect API.

        Returns:
            dict: The partner data if the request is successful, else None.
        """
        url = f"{self.BASE_URL}partners"
        try:
            response = self.session.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the parsed JSON data
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
        except Exception as err:
            print(f"An error occurred: {err}")  # Handle other errors
        return None  # Return None if an error occurred

    def display_statistics(self, data):
        """Display app and wallet statistics from the fetched data.

        Args:
            data (dict): The partner data containing app and wallet statistics.
        """
        if not data or 'partners' not in data:
            print("No partner data available to display.")
            return
        
        print(f"{'App Name':<30} {'Wallets':<20} {'Users':<20}")
        print("=" * 70)
        
        for partner in data['partners']:
            app_name = partner.get('name', 'N/A')
            wallets = partner.get('wallets', 'N/A')
            users = partner.get('users', 'N/A')
            print(f"{app_name:<30} {wallets:<20} {users:<20}")

def main():
    """Main function to execute the script."""
    wallet_connect_api = WalletConnectAPI()
    
    # Fetch the partner data from the API
    partner_data = wallet_connect_api.fetch_partners_data()
    
    # Display the fetched statistics
    wallet_connect_api.display_statistics(partner_data)

if __name__ == "__main__":
    main()
```
