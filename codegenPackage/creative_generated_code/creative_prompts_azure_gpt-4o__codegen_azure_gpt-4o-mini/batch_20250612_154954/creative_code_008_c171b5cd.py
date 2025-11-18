"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inch-io-landing-production.pages.dev
Prompt: Explain how to use the 1inch Portfolio API to track and display detailed crypto portfolio performance in a Web3 dashboard.
Generated: DETERMINISTIC_c171b5cd52960a7b
Batch ID: 20250612_154954
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.1inch.io/v4.0": {
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

class OneInchPortfolioAPI:
    BASE_URL = "https://api.1inch.io/v4.0"
    
    def __init__(self, network_id):
        """
        Initialize the OneInchPortfolioAPI class.

        Args:
            network_id (str): The ID of the network (e.g., '1' for Ethereum).
        """
        self.network_id = network_id

    def get_portfolio(self, address):
        """
        Retrieve the portfolio details for a given wallet address.

        Args:
            address (str): The wallet address to track.

        Returns:
            dict: The portfolio data returned from the API.
        """
        url = f"{self.BASE_URL}/{self.network_id}/portfolio?address={address}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise HTTPError for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching portfolio data: {e}")
            return None

    def display_portfolio(self, portfolio_data):
        """
        Display the portfolio performance in a user-friendly format.

        Args:
            portfolio_data (dict): The portfolio data to display.
        """
        if not portfolio_data:
            print("No portfolio data to display.")
            return

        print(f"Portfolio for Address: {portfolio_data.get('address')}")
        print("Assets:")
        
        for asset in portfolio_data.get('assets', []):
            print(f" - {asset.get('symbol')}: {asset.get('balance')} (USD Value: {asset.get('usdValue')})")
        
        total_value = sum(asset.get('usdValue', 0) for asset in portfolio_data.get('assets', []))
        print(f"Total Portfolio Value: ${total_value:.2f}")

def main():
    # Example usage of the 1inch Portfolio API
    network_id = '1'  # Ethereum Mainnet
    wallet_address = 'your_wallet_address_here'  # Replace with the actual wallet address

    api = OneInchPortfolioAPI(network_id)
    portfolio_data = api.get_portfolio(wallet_address)
    api.display_portfolio(portfolio_data)

if __name__ == "__main__":
    main()
```

**Note**: Please replace `'your_wallet_address_here'` with an actual wallet address to use the code.
