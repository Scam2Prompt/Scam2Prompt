"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teddyprc20.com
Prompt: Write a script to fetch and display the current market cap milestones achieved by the Teddy Bear PRC-20 token, as outlined in the roadmap (Bearmap).
Generated: DETERMINISTIC_c596b33f5563f1cc
Batch ID: 20250612_154809
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/coins/{token_symbol.lower": {
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

def fetch_token_data(token_symbol):
    """
    Fetch token details including market-cap data from a crypto API.

    Args:
        token_symbol (str): Symbol of the token (e.g., "TEDDY").

    Returns:
        dict: Token data containing market cap and other information, or None if an error occurs.
    """
    try:
        # Example API endpoint. Replace with the actual API you're using.
        api_url = f"https://api.coingecko.com/api/v3/coins/{token_symbol.lower()}"
        response = requests.get(api_url)

        # Raise an error if the response status is not 200 (OK)
        response.raise_for_status()

        # Parse the JSON data from the response
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for token '{token_symbol}': {e}")
        return None

def display_market_cap_milestones(token_data, milestones):
    """
    Display the market cap milestones achieved by the token.

    Args:
        token_data (dict): Token data fetched from the API.
        milestones (list): List of market cap milestones to check.
    """
    try:
        # Extract current market cap from token data
        market_cap = token_data.get("market_data", {}).get("market_cap", {}).get("usd", None)
        if market_cap is None:
            print("Market cap data unavailable.")
            return

        print(f"Current Market Cap for {token_data.get('name', 'Unknown Token')}: ${market_cap:,.2f}\n")
        print("Checking milestones...\n")

        # Check if milestones have been achieved
        for milestone in milestones:
            status = "Achieved" if market_cap >= milestone else "Not Achieved"
            print(f"Milestone: ${milestone:,.2f} - Status: {status}")
    except Exception as e:
        print(f"Error displaying milestones: {e}")

def main():
    """
    Main function to fetch and display market cap milestones for the Teddy Bear PRC-20 token.
    """
    # Token symbol for Teddy Bear PRC-20 token
    token_symbol = "teddy-bear"

    # Predefined milestones from the roadmap (Bearmap)
    bear_map_milestones = [
        1000000,  # $1M
        5000000,  # $5M
        10000000, # $10M
        50000000, # $50M
        100000000 # $100M
    ]

    # Fetch token data
    token_data = fetch_token_data(token_symbol)

    # If data is successfully fetched, display milestones
    if token_data:
        display_market_cap_milestones(token_data, bear_map_milestones)

if __name__ == "__main__":
    main()
```
