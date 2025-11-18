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
import sys

# Constants
COINGECKO_API_URL = "https://api.coingecko.com/api/v3"
OPTIMISM_PLATFORM_ID = "optimistic-ethereum"

def get_token_list():
    """
    Fetches the list of tokens on the Optimism platform from the CoinGecko API.

    Returns:
        list: A list of tokens (each represented as a dictionary) on Optimism.
    """
    try:
        response = requests.get(f"{COINGECKO_API_URL}/coins/list")
        response.raise_for_status()
        coins = response.json()
        # Filter for tokens on Optimism
        optimism_tokens = [coin for coin in coins if OPTIMISM_PLATFORM_ID in coin.get('platforms', {})]
        return optimism_tokens
    except requests.exceptions.RequestException as e:
        print(f"Error fetching token list: {e}")
        sys.exit(1)

def get_price_data(token_id):
    """
    Fetches the current price and market data for a given token from the CoinGecko API.

    Args:
        token_id (str): The ID of the token.

    Returns:
        dict: A dictionary containing price and market data for the token.
    """
    try:
        response = requests.get(f"{COINGECKO_API_URL}/simple/price", params={
            'ids': token_id,
            'vs_currencies': 'usd',
            'include_market_cap': 'true',
            'include_24hr_vol': 'true',
            'include_24hr_change': 'true'
        })
        response.raise_for_status()
        return response.json().get(token_id, {})
    except requests.exceptions.RequestException as e:
        print(f"Error fetching price data for token {token_id}: {e}")
        sys.exit(1)

def main():
    """
    Main function to query token holdings and price action data for Optimism tokens.
    """
    print("Fetching Optimism tokens...")
    tokens = get_token_list()

    if not tokens:
        print("No tokens found for Optimism platform.")
        sys.exit(0)

    print(f"Found {len(tokens)} tokens. Fetching price data...")
    for token in tokens[:10]:  # Limiting to the first 10 tokens for demonstration
        token_id = token['id']
        token_symbol = token.get('symbol', 'Unknown').upper()
        print(f"Fetching data for {token_symbol} ({token_id})...")
        price_data = get_price_data(token_id)
        if price_data:
            print(f"{token_symbol} - Current Price: ${price_data.get('usd', 'N/A')} "
                  f"Market Cap: ${price_data.get('usd_market_cap', 'N/A')} "
                  f"24h Volume: ${price_data.get('usd_24h_vol', 'N/A')} "
                  f"24h Change: {price_data.get('usd_24h_change', 'N/A')}%")
        else:
            print(f"No price data available for {token_symbol}.")

if __name__ == "__main__":
    main()
```
