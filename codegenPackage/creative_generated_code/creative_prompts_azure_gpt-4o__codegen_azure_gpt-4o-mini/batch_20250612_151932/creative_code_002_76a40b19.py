"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimismdashboard.xyz
Prompt: Create a Python script to query token holdings and price action data for Optimism tokens using the CoinGecko API.
Generated: DETERMINISTIC_76a40b193884a08f
Batch ID: 20250612_151932
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3": {
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

class CoinGeckoAPI:
    BASE_URL = "https://api.coingecko.com/api/v3"

    @staticmethod
    def get_token_price(token_id: str, vs_currency: str = 'usd') -> dict:
        """
        Fetch the current price of the specified token.

        :param token_id: The ID of the token (e.g., 'optimism')
        :param vs_currency: The currency to compare against (default is 'usd')
        :return: A dictionary containing the price information
        """
        try:
            response = requests.get(f"{CoinGeckoAPI.BASE_URL}/simple/price", 
                                    params={"ids": token_id, "vs_currencies": vs_currency})
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching price for {token_id}: {e}")
            return {}

    @staticmethod
    def get_token_holdings(wallet_address: str) -> dict:
        """
        Fetch the token holdings of a given wallet address using the CoinGecko API.

        :param wallet_address: The blockchain address of the wallet
        :return: A dictionary containing the holdings information
        """
        try:
            response = requests.get(f"{CoinGeckoAPI.BASE_URL}/wallets/{wallet_address}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching holdings for wallet {wallet_address}: {e}")
            return {}

def main():
    # Example usage
    token_id = 'optimism'
    wallet_address = 'your_wallet_address_here'  # Replace with an actual wallet address

    # Get current price of the token
    price_data = CoinGeckoAPI.get_token_price(token_id)
    if price_data:
        print(f"Current price of {token_id}: {price_data.get(token_id, {}).get('usd', 'N/A')} USD")

    # Get token holdings for the specified wallet address
    holdings_data = CoinGeckoAPI.get_token_holdings(wallet_address)
    if holdings_data:
        print(f"Holdings for wallet {wallet_address}: {json.dumps(holdings_data, indent=2)}")

if __name__ == "__main__":
    main()
```
