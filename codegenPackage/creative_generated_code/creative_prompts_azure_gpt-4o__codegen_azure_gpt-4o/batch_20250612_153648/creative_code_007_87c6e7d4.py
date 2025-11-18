"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bobukineko.pages.dev
Prompt: Write a Python script to query CoinGecko or CoinMarketCap for $BOBUKI token price and market data once the token is listed.
Generated: DETERMINISTIC_87c6e7d473aa90a6
Batch ID: 20250612_153648
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/coins/": {
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
COINGECKO_API_URL = "https://api.coingecko.com/api/v3/coins/"
TOKEN_NAME = "bobuki"  # Name of the token to query (ensure this matches the token's ID on CoinGecko)
USER_AGENT = "Python Bobuki Price Query Script"

def fetch_token_data(token_name):
    """
    Fetch token price and market data from CoinGecko API.

    Args:
        token_name (str): The token ID to query.

    Returns:
        dict: Token data if successful, None otherwise.
    """
    try:
        headers = {"User-Agent": USER_AGENT}
        url = f"{COINGECKO_API_URL}{token_name}"
        response = requests.get(url, headers=headers)

        # Raise HTTPError for bad responses (4xx or 5xx)
        response.raise_for_status()

        # Parse JSON response
        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for token '{token_name}': {e}", file=sys.stderr)
        return None

def display_token_data(data):
    """
    Display token price and market data.

    Args:
        data (dict): Token data returned by the API.
    """
    try:
        # Extract relevant data
        name = data.get("name", "Unknown")
        symbol = data.get("symbol", "Unknown").upper()
        market_data = data.get("market_data", {})
        
        if market_data:
            current_price = market_data.get("current_price", {}).get("usd", "N/A")
            market_cap = market_data.get("market_cap", {}).get("usd", "N/A")
            total_volume = market_data.get("total_volume", {}).get("usd", "N/A")

            # Display token details
            print(f"Token Name: {name} ({symbol})")
            print(f"Current Price: ${current_price}")
            print(f"Market Cap: ${market_cap}")
            print(f"24h Volume: ${total_volume}")
        else:
            print(f"No market data available for token: {name} ({symbol})")

    except Exception as e:
        print(f"Error displaying data: {e}", file=sys.stderr)

def main():
    """
    Main function to query and display token price and market data.
    """
    print(f"Querying market data for token '{TOKEN_NAME}'...")
    
    # Fetch token data
    token_data = fetch_token_data(TOKEN_NAME)
    
    if token_data:
        # Display token details if data is successfully fetched
        display_token_data(token_data)
    else:
        print("Failed to fetch token data.", file=sys.stderr)

if __name__ == "__main__":
    main()
```

### Notes:
1. Replace `TOKEN_NAME` with the correct ID for the `$BOBUKI` token once it's listed on CoinGecko.
2. The script queries CoinGecko API, which is free to use but may impose rate limits. Check the API documentation for limits and usage details.
3. Error handling is implemented for API requests and data parsing to ensure robustness.
